# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 17:34:38 2019

@author: cms
"""

# 执行pip install baidu-aip
from aip import AipFace
# 参数image：图像base64编码 以及top_num参数
import base64
import pprint

""" 你的 APPID AK SK """
APP_ID = '16705847'
API_KEY = 'SdxVqk8FA96vlznb9yxCCAAs'
SECRET_KEY = '7m5G4tyoEFRmdzpygagT7hE62jWvEHSG'

client = AipFace(APP_ID, API_KEY, SECRET_KEY)

def check(input_img):


    f = open(input_img, 'rb')


    img = base64.b64encode(f.read())

    # img参数进行一下str转换
    # "取决于image_type参数，传入BASE64字符串或URL字符串或FACE_TOKEN字符串"
    image = str(img, 'utf-8')

    imageType = "BASE64"

    """ 调用人脸检测 """
    client.detect(image, imageType)

    """ 如果有可选参数 """
    options = {}
    options["face_field"] = "age"
    options["max_face_num"] = 2
    options["face_type"] = "LIVE"
    options["liveness_control"] = "LOW"

    """ 带参数调用人脸检测 """
    result = client.detect(image, imageType, options)
    return result

