
# Important plugin info for Blender
bl_info = {
    'name': 'Retargeting for Blender',
    'author': 'm00n',
    'category': 'Animation',
    'location': 'View 3D > Tool Shelf > Retarget',
    'description': 'Retarget animations directly in Blender',
    'version': (1, 4, 0),
    'blender': (2, 80, 0),
    'wiki_url': 'https://rokoko.freshdesk.com/support/solutions/folders/47000761699',
}

import os
import sys
import json
import shutil
import pathlib
import pkgutil
import platform
import traceback
import ensurepip
import subprocess

first_startup = "bpy" not in locals()
import bpy


class LibraryManager:
    os_name = platform.system()
    system_info = {
        "operating_system": os_name,
    }

    def __init__(self, libs_main_dir):
        self.libs_main_dir = libs_main_dir
        self.libs_info_file = os.path.join(self.libs_main_dir, ".lib_info")

        python_ver_str = "".join([str(ver) for ver in sys.version_info[:2]])
        self.libs_dir = os.path.join(self.libs_main_dir, "python" + python_ver_str)

        # Set python path on older Blender versions
        try:
            self.python = bpy.app.binary_path_python
        except AttributeError:
            self.python = sys.executable

        self.check_libs_info()
        self._prepare_libraries()

    def _prepare_libraries(self):
        # Create main library directory
        if not os.path.isdir(self.libs_main_dir):
            os.mkdir(self.libs_main_dir)
        # Create python specific library directory
        if not os.path.isdir(self.libs_dir):
            os.mkdir(self.libs_dir)

        # Add the library path to the modules, so they can be loaded from the plugin
        if self.libs_dir not in sys.path:
            sys.path.append(self.libs_dir)

    def install_libraries(self, required):
        missing_after_install = []

        # Install missing libraries
        missing = [mod for mod in required if not pkgutil.find_loader(mod)]
        if missing:
            # Ensure and update pip
            self._update_pip()

            # Install the missing libraries into the library path
            print("Installing missing libraries:", missing)
            try:
                command = [self.python, '-m', 'pip', 'install', f"--target={str(self.libs_dir)}", *missing]
                subprocess.check_call(command, stdout=subprocess.DEVNULL)
            except subprocess.CalledProcessError as e:
                print("PIP Error:", e)
                print("Installing libraries failed.")
                if self.os_name != "Windows":
                    print("Retrying with sudo..")
                    command = ["sudo", self.python, '-m', 'pip', 'install', f"--target={str(self.libs_dir)}", *missing]
                    subprocess.call(command, stdout=subprocess.DEVNULL)
            finally:
                # Reset console color, because it could still be colored after running pip
                print('\033[39m')

            # Check if all library installations were successful
            missing_after_install = [mod for mod in required if not pkgutil.find_loader(mod)]
            installed_libs = [lib for lib in missing if lib not in missing_after_install]
            if missing_after_install:
                print("WARNING: Could not install the following libraries:", missing_after_install)
            if installed_libs:
                print("Successfully installed missing libraries:", installed_libs)

        # Create library info file after all libraries are installed to ensure everything is installed correctly
        self.create_libs_info()

        return missing_after_install

    def check_libs_info(self):
        if not os.path.isdir(self.libs_dir):
            return

        # If the library info file doesn't exist, delete the libs folder
        if not os.path.isfile(self.libs_info_file):
            print("Library info is missing, deleting library folder.")
            shutil.rmtree(self.libs_main_dir)
            return

        # Read data from info file
        current_data = self.system_info
        with open(self.libs_info_file, 'r', encoding="utf8") as file:
            loaded_data = json.load(file)

        # Compare info and delete libs folder if it doesn't match
        for key, val_current in current_data.items():
            val_loaded = loaded_data.get(key)
            if not val_loaded == val_current:
                print("Current info:", current_data)
                print("Loaded info: ", loaded_data)
                print("Library info is not matching, deleting library folder.")
                shutil.rmtree(self.libs_main_dir)
                return

    def create_libs_info(self):
        # If the path doesn't exist or the info file already exists, don't create it
        if not os.path.isdir(self.libs_dir) or os.path.isfile(self.libs_info_file):
            return

        # Write the current data to the info file
        with open(self.libs_info_file, 'w', encoding="utf8") as file:
            json.dump(self.system_info, file)


def show_error(message="", title="Unable to load plugin!"):
    def draw(self, context):
        layout = self.layout
        msg_list = message.split("\n")

        for i, msg in enumerate(msg_list):
            row = layout.row(align=True)
            row.scale_y = 0.85
            row.label(text=msg)

    # Only show popup if the preferences window is open
    if len(bpy.context.window_manager.windows) > 1:
        bpy.context.window_manager.popup_menu(draw, title=title, icon="ERROR")


classes = []


# register and unregister all classes
def register():
    # Now that the updater is loaded, do the rest of the registration safely
    try:
        register_late()
    except Exception:
        print("\nERROR: plugin failed to load:")
        trace = traceback.format_exc()
        print(trace)
        show_error("Expand the plugin module to access the updater to check for a newer version.\n\n" + trace)
        return


def register_late():
    # Library path
    main_dir = pathlib.Path(os.path.dirname(__file__)).resolve()
    resources_dir = os.path.join(main_dir, "resources")
    libs_dir = os.path.join(resources_dir, "libraries")

    # Install the missing libraries
    # Throw error when a login library is missing, but not when the LZ4 module is missing
    lib_manager = LibraryManager(libs_dir)
    missing = lib_manager.install_libraries(["websockets", "gql", "cryptography", "boto3"])
    if missing:
        raise ImportError("The following libraries could not be installed: " + str(missing))
    lib_manager.install_libraries(["lz4"])

    # If first startup of this plugin, load all modules normally
    # If reloading the plugin, use importlib to reload modules
    # This lets you do adjustments to the plugin on the fly without having to restart Blender
    from . import core
    from . import panels
    from . import operators
    from . import properties
    if first_startup:
        pass
        # print("\nFirst STARTUP!")
    else:
        # print("\nRELOAD!")
        import importlib
        importlib.reload(core)
        importlib.reload(panels)
        importlib.reload(operators)
        importlib.reload(properties)

    global classes, classes_login, classes_always_enable

    # List of all buttons and panels
    classes = [  # These panels will only be loaded when the user is logged in
        panels.retargeting.RetargetingPanel,
        operators.detector.DetectFaceShapes,
        operators.detector.DetectActorBones,
        operators.detector.SaveCustomShapes,
        operators.detector.SaveCustomBonesRetargeting,
        operators.detector.ImportCustomBones,
        operators.detector.ExportCustomBones,
        operators.detector.ClearCustomBones,
        operators.actor.InitTPose,
        operators.actor.ResetTPose,
        operators.actor.PrintCurrentPose,
        operators.retargeting.BuildBoneList,
        operators.retargeting.AddBoneListItem,
        operators.retargeting.ClearBoneList,
        operators.retargeting.RetargetAnimation,
        panels.retargeting.RSL_UL_BoneList,
        panels.retargeting.BoneListItem
    ]

    # Register classes
    # The classes need to be assigned as list() to create a duplicate
    classes_to_register = list(classes)

    register_count = 0
    for cls in classes_to_register:
        try:
            bpy.utils.register_class(cls)
            register_count += 1
        except ValueError:
            print("Error: Failed to register class", cls)
            pass
    if register_count < len(classes_to_register):
        print('Skipped', len(classes_to_register) - register_count, 'ROKOKO classes.')

    # Register all custom properties
    properties.register()

    # Load bone detection list
    core.detection_manager.load_detection_lists()

    # Init fbx patcher
    core.fbx_patcher.start_fbx_patch_timer()

    print("### Loaded plugin successfully!\n")


def unregister():
    from . import operators
    
    # Unregister all classes
    for cls in reversed(classes):
        try:
            bpy.utils.unregister_class(cls)
        except RuntimeError:
            pass

if __name__ == '__main__':
    register()
