import os
import shutil

source = '/Users/ericcallaway/Google Drive/School Work/Summer 2022/Artificial Intelligence/Home Work/HW#5/imgs1/'
dest = '/Users/ericcallaway/Google Drive/School Work/Summer 2022/Artificial Intelligence/Home Work/HW#5/class_3/'

# allfiles = os.listdir(source)
dest_files = os.listdir(dest)

source_files = os.listdir(source)
print(dest_files)

for f in sorted(source_files):
    if int(f.strip('.bmp')) > 4086 and int(f.strip('.bmp')) <= 4348:
        # print(f)
        shutil.move(source + f, dest + f)

source_files = sorted(os.listdir(source))
print(sorted(dest_files))

   

# print(allfiles)
# print(dest_files)

# for f in allfiles:
#     shutil.move(source + f, dest + f)

# dest_files = sorted(os.listdir(dest))
# print(dest_files)

# print(dest_files) 