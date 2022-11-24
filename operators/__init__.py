if "bpy" not in locals():
    from . import detector
    from . import actor
    from . import retargeting
else:
    import importlib
    importlib.reload(detector)
    importlib.reload(actor)
    importlib.reload(retargeting)
