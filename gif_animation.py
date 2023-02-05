# open up any gif files in the ./animation/input directory
# and save them as png files in the ./animation/output directory
# with the same name as the gif file

import os
from PIL import Image
import imageio
import shutil

# get the current working directory
cwd = os.getcwd()

# get the input and output directories
input_dir = os.path.join(cwd, 'animation', 'input')
output_dir = os.path.join(cwd, 'animation', 'output')
processed_dir = os.path.join(cwd, 'animation', 'processed')

# get the list of files in the input directory
files = os.listdir(input_dir)

# loop through the files
for file in files:
    print('Processing file: ' + file)
    # get the full path to the file
    file_path = os.path.join(input_dir, file)
    # open the file
    im = Image.open(file_path)
    # save each frame of the gif as a png file
    # get the number of frames in the gif
    num_frames = im.n_frames
    # loop through the frames
    for frame in range(num_frames):
        # set the current frame
        im.seek(frame)
        # get the name of the file without the extension
        file_name = os.path.splitext(file)[0]
        # get the full path to the output file
        output_file = os.path.join(output_dir, file_name + '_' + str(frame) + '.png')
        # save the file
        im.save(output_file)
        print('Saved file: ' + output_file)
    # then move the file to the processed folder
    shutil.copy2(file_path, processed_dir)



# process output files
# open up any png files in the ./animation/output directory
# and save them as gif files in the ./output/anim directory
# with the same name as the png file
# create a list of filenames in the output_dir
filenames = os.listdir(output_dir)
# get full path to file
file_paths = []
filename = os.path.splitext(filenames[0])[0]
for files in filenames:
    file_paths.append(os.path.join(output_dir, files))

# save the files as an animated gif
gif_dir = os.path.join(cwd, 'output', 'animation')
imageio.mimsave(f'{filename}.gif', [imageio.imread(f) for f in file_paths], fps=10)

