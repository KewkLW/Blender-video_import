bl_info = {
    "name": "Change to Video Size",
    "author": "Kewk",
    "version": (1, 0, 0),
    "blender": (3, 4, 0),
    "category": "Sequencer",
    "location": "Sequencer > Add",
    "description": "Set output properties to match the video or image sequence dimensions",
}

import bpy
from bpy.types import Operator
from bpy.props import EnumProperty

class SEQUENCER_OT_change_to_video_size(Operator):
    bl_idname = "sequencer.change_to_video_size"
    bl_label = "Change to Video Size"
    bl_description = "Set output properties to match the video dimensions"
    bl_options = {'REGISTER', 'UNDO'}

    fit_methods_items = [
        ('FIT', "Fit", ""),
        ('FILL', "Fill", ""),
        ('STRETCH', "Stretch", ""),
        ('CHANGE_TO_VIDEO_SIZE', "Change to Video Size", ""),
    ]
    fit_method: EnumProperty(
        name="Fit Method",
        description="Fit the video to the output resolution",
        items=fit_methods_items,
        default='FIT',
    )

    filepath: bpy.props.StringProperty(
        name="File Path",
        description="File path used for importing the movie file",
        maxlen=1024,
        subtype='FILE_PATH',
    )

    def execute(self, context):
        scene = context.scene
        sequencer = scene.sequence_editor

        # Load movie strip
        movie_strip = sequencer.sequences.new_movie(
            name="Movie",
            filepath=self.filepath,
            channel=1,
            frame_start=1,
        )

        # Change output properties to match video size
        if self.fit_method == 'CHANGE_TO_VIDEO_SIZE':
            element = movie_strip.elements[0]
            scene.render.resolution_x = element.orig_width
            scene.render.resolution_y = element.orig_height

            # Use default square pixel aspect ratio (1:1)
            scene.render.pixel_aspect_x = 1
            scene.render.pixel_aspect_y = 1

        return {'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

def menu_func(self, context):
    layout = self.layout
    layout.operator(SEQUENCER_OT_change_to_video_size.bl_idname)

def register():
    bpy.utils.register_class(SEQUENCER_OT_change_to_video_size)
    bpy.types.SEQUENCER_MT_add.prepend(menu_func)

def unregister():
    bpy.utils.unregister_class(SEQUENCER_OT_change_to_video_size)
    bpy.types.SEQUENCER_MT_add.remove(menu_func)

if __name__ == "__main__":
    register()
