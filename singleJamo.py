import os
import shutil

source_dir = "./images"
target_dir = "./combinations"

if not os.path.exists(target_dir):
    os.makedirs(target_dir)

for i in range(1, 41):
    source_file = os.path.join(source_dir, f"{i}.PNG")
    fileNum = str(i).zfill(2)
    target_file = os.path.join(target_dir, f"{fileNum}.PNG")

    shutil.copy(source_file, target_file)

