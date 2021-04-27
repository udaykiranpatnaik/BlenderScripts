import bpy
import os

NormalizeFactor = 100

# Get Spline Curve Infomation
def GetSplineCurveData(context):
    selected_objects = bpy.context.selected_objects
    result = []
    for ob in selected_objects:
        spline_track = {}
        spline_track["id"] = selected_objects.index(ob)
        spline_track["data"] =[]
        # Determining the type of the selected object
        if ob.type == 'CURVE':
            # Iterating Spline points data
            for spline in ob.data.splines:
                # Determining the length of the program
                if len(spline.bezier_points) > 0:
                    # Iterating through tht bezier points
                    for bezier_point in spline.bezier_points.values():
                        #spline_points = []
                        spline_dict = {}
                        spline_dict["Position"] = {}
                        spline_dict["InTangent"] = {}
                        spline_dict["OutTangent"] = {}

                        # Determing the position in the world
                        co = ob.matrix_world @ bezier_point.co;
                        spline_dict["Position"]["x"] = co.y * NormalizeFactor 
                        spline_dict["Position"]["y"] = co.x * NormalizeFactor
                        spline_dict["Position"]["z"] = co.z * NormalizeFactor
                       
                        # Determinig the handle position of point tangents
                        handle_in = ob.matrix_world @ bezier_point.handle_right;
                        spline_dict["InTangent"]["x"] = handle_in.y * NormalizeFactor
                        spline_dict["InTangent"]["y"] = handle_in.x * NormalizeFactor
                        spline_dict["InTangent"]["z"] = handle_in.z * NormalizeFactor    
                         
                        handle_out = ob.matrix_world @ bezier_point.handle_left;
                        spline_dict["OutTangent"]["x"] = handle_out.y * NormalizeFactor
                        spline_dict["OutTangent"]["y"] = handle_out.x * NormalizeFactor
                        spline_dict["OutTangent"]["z"] = handle_out.z * NormalizeFactor   
                        #spline_points.append(spline_dict)
                        spline_track["data"].append(spline_dict)
        result.append(spline_track)
    return result               

# Generate GPX file from spline data
def GenerateGPX(spline_data):
    xml_header = '<?xml version="1.0" encoding="UTF-8"?>'\
    '\n'+'<gpx version="1.1" creator="VeloViewer with Barometer"'\
    '\n'+'xmlns="http://www.topografix.com/GPX/1/0"'\
    '\n'+'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"'\
    '\n'+'xsi:schemaLocation="http://www.topografix.com/GPX/1/0 http://www.topografix.com/GPX/1/0/gpx.xsd">'
    xml_track_start = '<trk>'
    xml_track_end = '</trk>'
    xml_gpx_end = '</gpx>'
    xml_trackname = '<name>VeloViewer GPX Test</name>'
    xml_tracksegment_start = '<trkseg>'
    xml_tracksegment_end = '</trkseg>'
    #xml_trackpoint = '<trkpt lat="' + + '" lon="' + + '"><ele>'+ +'</ele><time>2021-04-12T00:00:00Z</time></trkpt>'
    
    xml_string = xml_header + '\n' + xml_track_start + '\n\t' + xml_trackname + '\n'
    for seg in spline_data:
        xml_string += '\t\t'+xml_tracksegment_start + '\n'
        track_segments_data = seg.get('data')
        for track_points in track_segments_data:
            latitude = track_points.get('Position')['x']*(0.0000001)
            longitude = track_points.get('Position')['y']*(0.0000001)
            elevation = track_points.get('Position')['z']*(0.01)
            elevation = round(elevation,2)
            xml_string += '\t\t\t'+'<trkpt lat="' +str(latitude) + '" lon="' + str(longitude)+ '"><ele>"'+ str(elevation) +'"</ele><time>2021-04-12T00:00:00Z</time></trkpt>'+'\n'
        xml_string += '\t\t' + xml_tracksegment_end +'\n'
    xml_string += '\t' + xml_track_end +'\n' + xml_gpx_end
    return xml_string
    
        
def WriteToFile(gpx_data):
    
    filepath = "D:\Workspace\Scripts\BlenderScripts\VelowviewerGPXTest.gpx"
    #Opening File in Memory
    file = open(filepath, 'w', encoding='utf-8')
   
    #Writing file contents
    file.write(gpx_data);
    
    #Writing file contents
    file.close()
    
class SplineOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "spline.operator"
    bl_label = "Spline Curve Operator"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        points = GetSplineCurveData(context)
        gpx_data = GenerateGPX(points)
        WriteToFile(gpx_data)
        return {'FINISHED'}


def register():
    bpy.utils.register_class(SplineOperator)


def unregister():
    bpy.utils.unregister_class(SplineOperator)


if __name__ == "__main__":
    register()
