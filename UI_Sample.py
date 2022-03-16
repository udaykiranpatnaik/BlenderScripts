import bpy
from bpy.types import Panel, PropertyGroup, Scene, WindowManager
from bpy.props import (
    IntProperty,
    EnumProperty,
    StringProperty,
    PointerProperty,
)
from bpy.utils import register_class

class MYWHOOSH_PT_Panel(Panel):
    bl_idname = "MYWHOOSH_PT_Panel"
    bl_label = "MY WHOOSH TOOLS"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MY WHOOSH"
    #bl_options = {'DEFAULT_EXPAND'}

    def draw(self, context):
        layout = self.layout
        placeholder = context.scene.placeholder
        col = layout.column()
        col.prop(placeholder, "NormalizeFactor", text="Normalization Factor")
        col.prop(placeholder, "dropdown_box", text="Dropdown")
        col.prop(placeholder, "file_path", text="Filepath")


class PlaceholderProperties(PropertyGroup):
    NormalizeFactor: IntProperty(
        name="Incr-Dec", 
        min=1,
        soft_max = 1000, 
        default=100, 
        description="Tooltip for Incr-Decr"
    )

    file_path: StringProperty(
        name="File",
        default="",
        description="Wanted File",
        maxlen=1024,
        subtype="FILE_PATH",
    )

classes = (
    PlaceholderProperties,
    MYWHOOSH_PT_Panel,
)

def register():
    for cls in classes:
        register_class(cls)

    Scene.placeholder = PointerProperty(type=PlaceholderProperties)

def unregister():
    #the usual unregistration in reverse order ...

    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)

    del Scene.placeholder

if __name__ == "__main__":
    register()