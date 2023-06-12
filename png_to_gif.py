'''
input the path of the pngs' folder, and output the gif file in the same folder.
'''
import os
import imageio

def png_to_gif(path):
    images = []

    # iterate through the names of contents based on the order of file names
    for filename in sorted(os.listdir(path)):
        print(filename)
        if filename.endswith('.png'):
            images.append(imageio.imread(os.path.join(path, filename)))
    
    # and save as gif which will loop forever
    imageio.mimsave(os.path.join(path, 'output.gif'), images, duration=0.3)




if __name__ == '__main__':
    path = '/home/zehua/Downloads/trial_27_output'
    png_to_gif(path)