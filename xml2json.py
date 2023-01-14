#!/usr/bin/python
# -*- coding: utf-8 -*-
#Function:Xml_To_Json
#version 1.1
#Author: Herman
#Date: 2018-06-01
#Usage: python Xml_To_Json.py xmlfile_dir >> tar_dir

import xmltodict
import json
import sys
import os

def pythonXmlToJson(path):
    for filename in os.listdir(path):

        with  open(path+filename, 'r') as f:
            xmlStr = f.read()

        convertedDict = xmltodict.parse(xmlStr)
        jsonStr = json.dumps(convertedDict, indent=1)
        print(jsonStr)

        with open(path+filename+'.json', 'w') as f:
            f.write(jsonStr)

if __name__=="__main__":
    path = r'F:\\Python_learning\\YOLOV5\\Face_Mask\\de\\'
    pythonXmlToJson(path)