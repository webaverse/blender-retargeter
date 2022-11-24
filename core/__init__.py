if "bpy" not in locals():
    import bpy
    from . import animation_lists
    from . import utils
    from . import detection_manager
    from . import custom_schemes_manager
    from . import fbx_patcher
else:
    import importlib
    importlib.reload(animation_lists)
    importlib.reload(utils)
    importlib.reload(detection_manager)
    importlib.reload(custom_schemes_manager)
    importlib.reload(fbx_patcher)