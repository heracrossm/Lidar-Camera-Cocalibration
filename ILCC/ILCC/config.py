# coding=utf-8
'''
Created on 4/26/2017 2:08 28PM Wang Weimin

@author: wangwm
'''
import yaml
import os


# 'file_name_digits': 4 #The number of digits of the filename


def default_params():
    '''Return default configuration
    '''
    default_params_yaml = open("/home/hpec1231/DATA/config.yaml", "r")
    if(yaml.__version__[0]>=5):
        params = yaml.safe_load(default_params_yaml)
    else:
        params = yaml.load(default_params_yaml)

    params['image_format'] = get_img_format(params['base_dir'])
    return params


def get_img_format(base_dir):
    file_ls = os.listdir(os.path.join(base_dir, "img"))
    for file in file_ls:
        ext = file.split(".")[-1]
        if ext in ["png", "PNG", "jpg", "JPG"]:
            return ext

# print default_params()
