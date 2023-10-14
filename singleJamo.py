import os
import shutil

source_dir = "./images"
target_dir = "./combinations"

if not os.path.exists(target_dir):
    os.makedirs(target_dir)

for i in range(1, 41):
    source_file = os.path.join(source_dir, f"{i}.PNG")
    target_file = os.path.join(target_dir, f"{i}.PNG")

    shutil.copy(source_file, target_file)

