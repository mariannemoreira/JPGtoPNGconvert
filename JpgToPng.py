# python3 JpgToPng.py pokedex/ new/ (first argument pokedex - second argument new(new folder we created)
import sys
import os
from PIL import Image

#grab first and second argument
img_folder = sys.argv[1]
output_folder = sys.argv[2]

#test
##print(img_folder, output_folder)
#output will be: pokedex new/

#check if the folder exist and will be created (new folder) if already exist will not create anther one
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

#loop trough pokedex, convert images to png and save to the new folder
for filename in os.listdir(img_folder):
    img = Image.open(f'{img_folder}{filename}')
    clean_name = os.path.splitext(filename[0]) #change name to get first letter of image.png
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('all done!')











