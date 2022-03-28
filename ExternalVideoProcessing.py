import os
import glob 
from shutil import copyfile
import hashlib
import json
import sys
import subprocess
import logging
from multiprocessing import Pool
import pdb
import time
import pickle
import numpy as np
import pandas as pd
import pydicom as dicom 
import png
# pydicom imports needed to handle data errors
from pydicom import config
from pydicom import datadict
from pydicom import values 
from utils import video_save
import argparse


# Instantiate the parser
parser = argparse.ArgumentParser()
parser.add_argument('--ifolder', type=str,
                    default="/media/Datacenter_storage/James_ECHO_LVH/External_Validation/Echo AI- Dr. Oh files/", 
                    help='path for input video')
parser.add_argument('--ofolder', type=str, default='../temp/',
                    help='path to the image folder after processing')

def main():
    folder = args.ifolder
    ofolder = args.ofolder    
    arr = glob.glob(folder)
    for i in range(len(arr)):
        if 'NL' in arr[i]:
        #ds = dicom.dcmread(folder+'Echo AI- Dr. Oh files/'+arr[i], force=True)
            orig_img = itk.imread(folder+arr[i])
            acc = arr[i].split('_')
            if len(acc)<2:
                acc = arr[i].split(' ')
            path = ofolder+'NL_NP/'+acc[1]+'/'
            Check_folder = os.path.isdir(path)
            if not os.path.exists(path):
                os.makedirs(path)
                print("created folder : ", folder+'NL_NP/'+acc[1]+'/')
            video_save(orig_img, path, acc[1])

if __name__ == "__main__":
    main()