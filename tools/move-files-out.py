import os
import shutil

#store the path to your root directory
base='.'

# traverse root directory, and list directories as dirs and files as files
for root, dirs, files in os.walk(base):
    path = root.split(os.sep)

    for file in files:
        if not os.path.isdir(file):

            # move file from nested folder into the base folder
            shutil.move(os.path.join(root,file),os.path.join(base,file))
