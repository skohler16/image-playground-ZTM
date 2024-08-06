import sys
import os
from PIL import Image


JPG_folder = sys.argv[1]
PNG_folder = sys.argv[2]

if not os.path.exists(PNG_folder):
    os.makedirs(PNG_folder)

for filename in os.listdir(JPG_folder):
    try:
        img = Image.open(f'{JPG_folder}{filename}')
        clean_name = os.path.splitext(filename)[0]
        img.save(f'{PNG_folder}{clean_name}.png','png')
        print('all done')
    except OSError:
        print('cannot convert those files')