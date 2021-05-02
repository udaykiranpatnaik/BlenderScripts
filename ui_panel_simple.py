import bpy
from bpy.types import Panel, PropertyGroup, Scene, WindowManager
from bpy.props import (IntProperty,EnumProperty,StringProperty,PointerProperty,)
from bpy.utils import register_class

class HelloWorldPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Hello World Panel"
    bl_idname = "OBJECT_PT_hello"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "object"

    def draw(self, context):
        layout = self.layout

        obj = context.object
        placeholder = context.scene.placeholder

        row = layout.row()
        row.prop(obj, "name")
        
        col = layout.column()
        col.prop(placeholder, "NormalizeFactor", text="Normalization Factor")
        
        col.prop(placeholder, "file_path", text="Filepath")


        
#        row = layout.row()
#        row.operator("mesh.primitive_cube_add")

class GlobalVariableProperties(PropertyGroup):
    NormalizeFactor : IntProperty(
    name="Normalization Factor",
    min = 1,
    default = 100,
    soft_max = 1000,
    description = "Normalization Factor"
    )
    
    fileproperties : StringProperty(
    name="File",
    default="Hello",
    description="Wanted File",
    maxlen=1024,
    subtype="FILE_PATH",
    )
    
    
def register():
    bpy.utils.register_class(HelloWorldPanel)


def unregister():
    bpy.utils.unregister_class(HelloWorldPanel)


if __name__ == "__main__":
    register()
