from mathutils import Quaternion
from collections import OrderedDict

# Face shapekeys
face_shapes = [
    'eyeBlinkLeft',
    'eyeLookDownLeft',
    'eyeLookInLeft',
    'eyeLookOutLeft',
    'eyeLookUpLeft',
    'eyeSquintLeft',
    'eyeWideLeft',
    'eyeBlinkRight',
    'eyeLookDownRight',
    'eyeLookInRight',
    'eyeLookOutRight',
    'eyeLookUpRight',
    'eyeSquintRight',
    'eyeWideRight',
    'jawForward',
    'jawLeft',
    'jawRight',
    'jawOpen',
    'mouthClose',
    'mouthFunnel',
    'mouthPucker',
    'mouthLeft',
    'mouthRight',
    'mouthSmileLeft',
    'mouthSmileRight',
    'mouthFrownLeft',
    'mouthFrownRight',
    'mouthDimpleLeft',
    'mouthDimpleRight',
    'mouthStretchLeft',
    'mouthStretchRight',
    'mouthRollLower',
    'mouthRollUpper',
    'mouthShrugLower',
    'mouthShrugUpper',
    'mouthPressLeft',
    'mouthPressRight',
    'mouthLowerDownLeft',
    'mouthLowerDownRight',
    'mouthUpperUpLeft',
    'mouthUpperUpRight',
    'browDownLeft',
    'browDownRight',
    'browInnerUp',
    'browOuterUpLeft',
    'browOuterUpRight',
    'cheekPuff',
    'cheekSquintLeft',
    'cheekSquintRight',
    'noseSneerLeft',
    'noseSneerRight',
    'tongueOut'
]

# Tpose from Studio live
actor_bones = OrderedDict()
actor_bones['hip'] = Quaternion((-1.0, 0.0, -0.0, 0.0))
actor_bones['spine'] = Quaternion((-0.0, -0.0, 0.0, -1.0))
actor_bones['chest'] = Quaternion((-0.0, -0.0, 0.0, -1.0))
actor_bones['neck'] = Quaternion((-0.0, -0.0, 0.0, -1.0))
actor_bones['head'] = Quaternion((-0.0, -0.0, 0.0, -1.0))

actor_bones['leftShoulder'] = Quaternion((-0.70711, 0.0, 0.0, 0.70711))
actor_bones['leftUpperArm'] = Quaternion((-0.5, -0.5, -0.5, 0.5))
actor_bones['leftLowerArm'] = Quaternion((-0.5, -0.5, -0.5, 0.5))
actor_bones['leftHand'] = Quaternion((-0.5, -0.5, -0.5, 0.5))

actor_bones['rightShoulder'] = Quaternion((0.70711, 0.0, -0.0, 0.70711))
actor_bones['rightUpperArm'] = Quaternion((0.5, 0.5, -0.5, 0.5))
actor_bones['rightLowerArm'] = Quaternion((0.5, 0.5, -0.5, 0.5))
actor_bones['rightHand'] = Quaternion((0.5, 0.5, -0.5, 0.5))

actor_bones['leftUpLeg'] = Quaternion((0.70711, -0.0, 0.70711, -0.0))
actor_bones['leftLeg'] = Quaternion((0.70711, -0.0, 0.70711, 0.0))
actor_bones['leftFoot'] = Quaternion((0.0, -0.0, 0.70711, -0.70711))
actor_bones['leftToe'] = Quaternion((0.0, -0.0, 0.70711, -0.70711))

actor_bones['rightUpLeg'] = Quaternion((0.70711, -0.0, -0.70711, 0.0))
actor_bones['rightLeg'] = Quaternion((0.70711, -0.0, -0.70711, 0.0))
actor_bones['rightFoot'] = Quaternion((0.0, 0.0, -0.70711, 0.70711))
actor_bones['rightToe'] = Quaternion((0.0, 0.0, -0.70711, 0.70711))

glove_bones = OrderedDict()
glove_bones['hip'] = Quaternion((-1.0, 0.0, -0.0, 0.0))
glove_bones['spine'] = Quaternion((-0.0, -0.0, 0.0, -1.0))
glove_bones['chest'] = Quaternion((-0.0, -0.0, 0.0, -1.0))
glove_bones['neck'] = Quaternion((-0.0, -0.0, 0.0, -1.0))
glove_bones['head'] = Quaternion((-0.0, -0.0, 0.0, -1.0))

glove_bones['leftShoulder'] = Quaternion((-0.70711, 0.0, 0.0, 0.70711))
glove_bones['leftUpperArm'] = Quaternion((-0.5, -0.5, -0.5, 0.5))
glove_bones['leftLowerArm'] = Quaternion((-0.5, -0.5, -0.5, 0.5))
glove_bones['leftHand'] = Quaternion((-0.5, -0.5, -0.5, 0.5))

glove_bones['rightShoulder'] = Quaternion((0.70711, 0.0, -0.0, 0.70711))
glove_bones['rightUpperArm'] = Quaternion((0.5, 0.5, -0.5, 0.5))
glove_bones['rightLowerArm'] = Quaternion((0.5, 0.5, -0.5, 0.5))
glove_bones['rightHand'] = Quaternion((0.5, 0.5, -0.5, 0.5))

glove_bones['leftUpLeg'] = Quaternion((0.70711, -0.0, 0.70711, -0.0))
glove_bones['leftLeg'] = Quaternion((0.70711, -0.0, 0.70711, 0.0))
glove_bones['leftFoot'] = Quaternion((0.0, -0.0, 0.70711, -0.70711))
glove_bones['leftToe'] = Quaternion((0.0, -0.0, 0.70711, -0.70711))

glove_bones['rightUpLeg'] = Quaternion((0.70711, -0.0, -0.70711, 0.0))
glove_bones['rightLeg'] = Quaternion((0.70711, -0.0, -0.70711, 0.0))
glove_bones['rightFoot'] = Quaternion((0.0, 0.0, -0.70711, 0.70711))
glove_bones['rightToe'] = Quaternion((0.0, 0.0, -0.70711, 0.70711))

glove_bones['leftThumbProximal'] = Quaternion((-0.0923, -0.56098, -0.70106, 0.43046))
glove_bones['leftThumbMedial'] = Quaternion((-0.2706, -0.65328, -0.65328, 0.2706))
glove_bones['leftThumbDistal'] = Quaternion((-0.2706, -0.65328, -0.65328, 0.2706))

glove_bones['leftIndexProximal'] = Quaternion((-0.5, -0.5, -0.5, 0.5))
glove_bones['leftIndexMedial'] = Quaternion((-0.5, -0.5, -0.5, 0.5))
glove_bones['leftIndexDistal'] = Quaternion((-0.5, -0.5, -0.5, 0.5))

glove_bones['leftMiddleProximal'] = Quaternion((-0.5, -0.5, -0.5, 0.5))
glove_bones['leftMiddleMedial'] = Quaternion((-0.5, -0.5, -0.5, 0.5))
glove_bones['leftMiddleDistal'] = Quaternion((-0.5, -0.5, -0.5, 0.5))

glove_bones['leftRingProximal'] = Quaternion((-0.5, -0.5, -0.5, 0.5))
glove_bones['leftRingMedial'] = Quaternion((-0.5, -0.5, -0.5, 0.5))
glove_bones['leftRingDistal'] = Quaternion((-0.5, -0.5, -0.5, 0.5))

glove_bones['leftLittleProximal'] = Quaternion((-0.5, -0.5, -0.5, 0.5))
glove_bones['leftLittleMedial'] = Quaternion((-0.5, -0.5, -0.5, 0.5))
glove_bones['leftLittleDistal'] = Quaternion((-0.5, -0.5, -0.5, 0.5))

glove_bones['rightThumbProximal'] = Quaternion((0.0923, 0.56099, -0.70106, 0.43046))
glove_bones['rightThumbMedial'] = Quaternion((0.2706, 0.65328, -0.65328, 0.2706))
glove_bones['rightThumbDistal'] = Quaternion((0.2706, 0.65328, -0.65328, 0.2706))

glove_bones['rightIndexProximal'] = Quaternion((0.5, 0.5, -0.5, 0.5))
glove_bones['rightIndexMedial'] = Quaternion((0.5, 0.5, -0.5, 0.5))
glove_bones['rightIndexDistal'] = Quaternion((0.5, 0.5, -0.5, 0.5))

glove_bones['rightMiddleProximal'] = Quaternion((0.5, 0.5, -0.5, 0.5))
glove_bones['rightMiddleMedial'] = Quaternion((0.5, 0.5, -0.5, 0.5))
glove_bones['rightMiddleDistal'] = Quaternion((0.5, 0.5, -0.5, 0.5))

glove_bones['rightRingProximal'] = Quaternion((0.5, 0.5, -0.5, 0.5))
glove_bones['rightRingMedial'] = Quaternion((0.5, 0.5, -0.5, 0.5))
glove_bones['rightRingDistal'] = Quaternion((0.5, 0.5, -0.5, 0.5))

glove_bones['rightLittleProximal'] = Quaternion((0.5, 0.5, -0.5, 0.5))
glove_bones['rightLittleMedial'] = Quaternion((0.5, 0.5, -0.5, 0.5))
glove_bones['rightLittleDistal'] = Quaternion((0.5, 0.5, -0.5, 0.5))

def get_bones(with_gloves=True):
    """
    Return all bones with their default positions. This represents the exact default position of the Studio reference avatar
    :param with_gloves: Determines if the hand bones should be included or not
    :return: dictionary with bone names and default positions
    """
    # TODO: Remove redundant entries and create dicts at the start of the plugin
    return glove_bones if with_gloves else actor_bones