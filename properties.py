from bpy.types import Scene, Object
from bpy.props import IntProperty, StringProperty, EnumProperty, BoolProperty, CollectionProperty, PointerProperty

from .core import animation_lists, retargeting
from .panels import retargeting as retargeting_ui


def register():
    # Retargeting
    Scene.rsl_retargeting_armature_source = PointerProperty(
        name='Source',
        description='Select the armature with the animation that you want to retarget',
        type=Object,
        poll=retargeting.poll_source_armatures,
        update=retargeting.clear_bone_list
    )
    Scene.rsl_retargeting_armature_target = PointerProperty(
        name='Target',
        description='Select the armature that should receive the animation',
        type=Object,
        poll=retargeting.poll_target_armatures,
        update=retargeting.clear_bone_list
    )
    Scene.rsl_retargeting_auto_scaling = BoolProperty(
        name='Auto Scale',
        description='This will scale the source armature to fit the height of the target armature.'
                    '\nBoth armatures have to be in T-pose for this to work correctly',
        default=True
    )
    Scene.rsl_retargeting_use_pose = EnumProperty(
        name="Use Pose",
        description='Select which pose of the source and target armature to use to retarget the animation.'
                    '\nBoth armatures should be in the same pose before retargeting',
        items=[
            ("REST", "Rest", "Select this to use the rest pose during retargeting."),
            ("CURRENT", "Current", "Select this to use the current pose during retargeting.")
        ]
    )
    Scene.rsl_retargeting_bone_list = CollectionProperty(
        type=retargeting_ui.BoneListItem
    )
    Scene.rsl_retargeting_bone_list_index = IntProperty(
        name="Index for the retargeting bone list",
        default=0
    )

    # Face shapekeys
    for shape in animation_lists.face_shapes:
        setattr(Object, 'rsl_face_' + shape, StringProperty(
            name=shape,
            description='Select the shapekey that should be animated by this shape'
        ))

    # Actor bones
    for bone in animation_lists.get_bones().keys():
        setattr(Object, 'rsl_actor_' + bone, StringProperty(
            name=bone,
            description='Select the bone that corresponds to the actors bone'
        ))
