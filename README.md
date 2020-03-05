# Lidar-Camera-Cocalibration


# Installation:

    git clone --recurse-submodules https://github.com/mfxox/ILCC
  
    cd ILCC
  
    python setup.py install

# Process Data:
1. Make a folder for example named as DATA and make the image and point cloud folders DATA/img and DATA/pcd respectively.

2. Put panoramic images into DATA/img and point cloud files into DATA/pcd. The files should be named like 00XX.png or 00XX.csv.

3. cd DATA and copy config.yaml to DATA and modify config.yaml according to your situation.

4. Corner detection from images.


# Reference

        @Article{WANG2017Lidar_camera_cali,
        AUTHOR = {Wang, Weimin and Sakurada, Ken and Kawaguchi, Nobuo},
        TITLE = {Reflectance Intensity Assisted Automatic and Accurate Extrinsic Calibration of 3D LiDAR and Panoramic Camera Using a Printed Chessboard},
        JOURNAL = {Remote Sensing},
        VOLUME = {9},
        YEAR = {2017},
        NUMBER = {8},
        ARTICLE-NUMBER = {851},
        ISSN = {2072-4292},
        DOI = {10.3390/rs9080851}
        }
