import bpy
import os


def main(in_path, out_path):
    # iterate over all files in the folder
    file_queue = []
    for file in os.listdir(in_path):
        if file.endswith(".mpd"):
            file_queue.append(file)
    
    for path in file_queue:
        print("Processing file: ", path)
        bpy.ops.import_scene.importldraw(filepath=os.path.join(in_path, path),  addEnvironment=True, positionCamera=True)
        # bpy.ops.import_scene.importldraw(filepath=os.path.join(in_path, path), addEnvironment=True)
    
        bpy.context.scene.cycles.device = 'GPU'
        bpy.context.scene.cycles.samples = 500
        bpy.context.scene.render.engine = 'CYCLES'

        # set camera location and rotation
        bpy.context.object.location[0] = 2.50333
        bpy.context.object.location[1] = -2.64595
        bpy.context.object.location[2] = 2.2224

        bpy.context.object.rotation_euler[0] = 1.0472
        bpy.context.object.rotation_euler[1] = 0
        bpy.context.object.rotation_euler[2] = 1.0472

        bpy.context.scene.render.threads_mode = 'AUTO' # make the light better

        # # set the light source
        bpy.context.object.location[0] = 4.07625
        bpy.context.object.location[1] = 1.00545
        bpy.context.object.location[2] = 5.90386
        bpy.context.object.rotation_euler[0] = 0.650327
        bpy.context.object.rotation_euler[1] = 0.0552172
        bpy.context.object.rotation_euler[2] = 1.86639

        # bpy.context.scene.view_layers["ViewLayer"].use = True # enable the view layer, useless

        # # set the default background color
        # bpy.context.scene.world.use_nodes = True
        # bpy.data.worlds["World"].node_tree.nodes["Background"].inputs[0].default_value = (1, 1, 1, 1) # useless
        # # bpy.data.worlds["World"].node_tree.nodes["Background"].inputs[0].default_value = (0.0508761, 0.0508761, 0.0508761, 1)
        # bpy.data.worlds["World"].node_tree.nodes["Background"].inputs[1].default_value = 1 # useless



        bpy.context.scene.render.filepath = os.path.join(out_path, path[:-4] + ".png")
        bpy.ops.render.render(write_still=True)
        # show render progress
        # bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)

        # select all objects except the camera and the lamp (light source)
        bpy.ops.object.select_all(action='DESELECT')
        print(bpy.data.objects)
        for obj in bpy.data.objects:
#            print(obj.type)
            if obj.type != 'CAMERA' and obj.type != 'LIGHT':
                obj.select_set(True)
            else:
                obj.select_set(False)

        # delete all selected objects
        bpy.ops.object.delete(use_global=False)




if __name__ == '__main__':
    # datafolder = "/home/zehua/Downloads/trial_111"
    # outputfolder = "/home/zehua/Downloads/trial_11_output"
    datafolder = "/Users/zehuajiang/Downloads/trial_32"
    outputfolder = "/Users/zehuajiang/Downloads/trial_32_output"
    main(datafolder, outputfolder)