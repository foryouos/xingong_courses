import requests
import re
import time
import pandas as pd
from lxml import etree
from aip import AipOcr
import chardet
import json


def lesson_name_list(): #获取所有课程数量列表
    lesson_name_json={"lesson":[]}
    lesson_id_json = {"lesson": []}
    class_list_url = "http://221.176.153.126:8081/jwweb/ZNPK/Private/List_XNXQKC.aspx?xnxq=20210"
    req = requests.get(url=class_list_url)
    html = req.text
    #获取课程ID
    res_th = r"<option value=(.*?)>"
    lesson_id = re.findall(res_th, html, re.S | re.M)
    # print("共有的课程ID数量：" + str(len(lesson_id)))
    # print(lesson_id)
    #用正则表达式获取具体名字
    res_th = r"\|(.*?)</option>"
    lesson_name=re.findall(res_th, html, re.S | re.M)
    # print("共有的课程数量：" + str(len(lesson_name)))
    # print(lesson_name)
    lesson_name_list=[]
    lesson_id_list=[]
    print(len(lesson_name))
    for i in range(len(lesson_name)):
        lesson_name_list.append(lesson_name[i])
        lesson_id_list.append(lesson_id[i])
    lesson_name_json["lesson"]=lesson_name_list
    lesson_id_json["lesson"] = lesson_id_list
    # print(type(lesson_json))
    lesson_jsondata=json.dumps(lesson_name_json,indent=4,ensure_ascii=False,separators=(',',':'))
    # lesson_jsondata = json.dumps(lesson_name_json, ensure_ascii=False)
    f=open("./上传小程序文件/课程名称列表.json","w",encoding='utf-8')
    f.write(lesson_jsondata)
    f.close()
    print("课程名称以及对应ID已经保存到本地文件夹.....")
    return lesson_name_json
if __name__ == '__main__':
    #获取课程名称列表
    print("正在获取课程课表以及对应的ID。。。。。。。")
    lesson_name_json = lesson_name_list()
    print(lesson_name_json)