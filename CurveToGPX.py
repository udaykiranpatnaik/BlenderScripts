import bpy

class ProcessSpline(bpy.types.operator):
    bl_idname = "spline.get_data"
    bl_label = "Get Spline Data" 

    def execute(self, context):
        for ob in bpy.context.selected_objects:
        # Determining the type of the selected object
        if ob.type == 'CURVE':
            # Iterating Spline points data
            for spline in ob.data.splines:
                # Determining the length of the program
                if len(spline.bezier_points) > 0:
                    # Iterating through tht bezier points
                    for bezier_point in spline.bezier_points.values():
                        # Writing the file with beziers
                        file.write('%s,' % str(counter));
                        # Determing the position in the world
                        co = ob.matrix_world @ bezier_point.co;
                        # Determinig the handle position of point tangents
                        handle_in = ob.matrix_world @ bezier_point.handle_right;
                        handle_out = ob.matrix_world @ bezier_point.handle_left;
                        # writing the Handles data
                        print(f'%s',co)

        return {'FINISHED'}


def register():
    bpy.utils.register_class(ProcessSpline)

def unregister():
    bpy.utils.unregister_class(ProcessSpline)