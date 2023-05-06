import os 
import shutil ##copy utilities

# source file to be copied
source_file = 'C:/Users/trish/Desktop/Git/aws_git/scripts/project.yml'

directory = 'mnt/efs_dummy/abinitio/appconf_root/ss/dev/config'

#if not os.path.exists(directory):
#    os.makedirs(directory)
#    print(f"Directory '{directory}' created successfully!")
#else:
#    print(f"Directory '{directory}' already exists.")
# copy the file to the destination directory
shutil.copy(source_file,directory)

os.chdir(directory)  # change the current working directory to 'example_directory'
print(f"Changed current directory to: {os.getcwd()}")  # print the current working directory



