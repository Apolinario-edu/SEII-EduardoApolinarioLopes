import os
from datetime import datetime

os.chdir("C:")

#print(dir(os))

print(os.getcwd())
# print(dir(os))
# print(os.getcwd())
# os.makedir("created_dir/Sub-Dir-1")
# os.makedirs("created_dir/Sub-Dir-1")
# os.removedirs("created_dir/Sub-Dir-1")
# os.rename('READ.ME', 'LEIA.ME')
# print(os.stat('LEIA.ME').st_size)
# mod_time = os.stat('LEIA.ME').st_mtime
# print(datetime.fromtimestamp(mod_time)) 
# print(os.listdir())

# for dirpath, dirnames, filenames in os.walk('C:'):
#     print('Current Path: ', dirpath)
#     print('Directories: ', dirnames)
#     print('Files: ', filenames)
#     print()

# os.environ.get('prog09')
# file_path = os.path.join(os.environ.get('Teste'), 'test.txt')
# print(file_path)

# print(os.path.basename('prog03.py'))
# print(os.path.dir('prog03.py'))
# print(os.path.split('prog03.py'))
# print(os.path.exits('prog03.py'))
# print(os.path.splitext('prog03.py'))
