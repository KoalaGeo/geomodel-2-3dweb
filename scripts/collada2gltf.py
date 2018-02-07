# Convert files from collada to GLTF v2
# by calling 'COLLADA2GLTF-bin' which is assumed to be available locally
# See https://github.com/KhronosGroup/COLLADA2GLTF/tree/2.0 for more information
#
import os
import glob

# Path where 'COLLADA2GLTF-bin' is located
COLLADA2GLTF_BIN = os.path.join(os.environ['HOME'], 'github', 'COLLADA2GLTF', 'build')

def convert(src_dir, file_mask):
  wildcard_str = os.path.join(src_dir, file_mask)
  daefile_list = glob.glob(wildcard_str)
  for daefile_str in daefile_list:
    fileName, fileExt = os.path.splitext(daefile_str)
    cmd_str = os.path.join(COLLADA2GLTF_BIN, "COLLADA2GLTF-bin -i "+daefile_str+" -o "+fileName+".gltf")
    print(cmd_str)
    os.system(cmd_str)
