if "bpy" not in locals():
    from . import retargeting
else:
    import importlib
    importlib.reload(retargeting)