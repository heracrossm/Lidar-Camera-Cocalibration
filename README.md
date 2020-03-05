# Lidar-Camera-Cocalibration

Installation:

  git clone --recurse-submodules https://github.com/mfxox/ILCC
  
  cd ILCC
  
  python setup.py install

Process Data:
1. Make a folder for example named as DATA and make the image and point cloud folders DATA/img and DATA/pcd respectively.

2. Put panoramic images into DATA/img and point cloud files into DATA/pcd. The files should be named like 00XX.png or 00XX.csv.

3. cd DATA and copy config.yaml to DATA and modify config.yaml according to your situation.

4. Corner detection from images.
