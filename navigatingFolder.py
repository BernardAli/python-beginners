import os

# d = os.getcwd()
# print(f'{d}')
#
# os.chdir('/home/allgift/Documents')
# print(os.getcwd())
# os.chdir('..')
# print(os.getcwd())
#
# for f in os.listdir():
#     # print(f)
#     print(f'Path: {os.path.abspath(f)}')
#     if os.path.isdir(f): print(f'Dir: {f}')
#     if os.path.isfile(f): print(f'File: {f}')
#     if os.path.islink(f): print(f'Link: {f}')
#
#
# for e in os.scandir():
#     print(e)
#     print(f'Name: {e.name}')
#     print(f'Path: {e.path}')
#     if e.is_dir(): print(f'Dir: {e.name}')
#     if e.is_file(): print(f'File: {e.name}')
#     if e.is_symlink(): print(f'Link: {e.name}')


# Recursive scan
import glob
os.chdir('..')
dir = os.getcwd()
print(dir)
for filename in glob.glob(pathname=dir + '**/**', recursive=True):
    print(f'glob: {filename}')


for currentpath, folders, files in os.walk("."):
    for file in files:
        print(f'walk: {os.path.join(currentpath, file)}')