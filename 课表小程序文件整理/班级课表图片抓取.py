import requests
import re
import time
import pandas as pd
from lxml import etree
from aip import AipOcr
import chardet
import json
APP_ID = '24053287'
API_KEY = 'HZbSPqr014lGtvgcOjlB9Y2B'
SECRET_KEY = 'S5Zq0MHV4Tks2g0l4kvkSsw1K3IyW7oZ'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
def orient():
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Cookie": "myCookie=; ASP.NET_SessionId=4vuei0pc3tseivnjimq0go1z",
        "DNT": "1",
        "Host": "221.176.153.126:8081",
        "Origin": "http://221.176.153.126:8081",
        "Referer": "http://221.176.153.126:8081/jwweb/ZNPK/KBFB_RoomSel.aspx",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.72 Safari/537.36"
    }
    url = "http://221.176.153.126:8081/jwweb/sys/ValidateCode.aspx"
    num = requests.get(url=url, headers=headers)
    text = client.basicAccurate(num.content)["words_result"][0]["words"]
    # print("中间测试直接输出%s",text)
    return text
def class_num_list():
    class_list_url = "http://221.176.153.126:8081/jwweb/ZNPK/KBFB_ClassSel.aspx"
    req = requests.get(url=class_list_url)
    # print(req.text)
    html = req.text
    res_th = r"<option value='(.*?)'>"
    m_th = re.findall(res_th, html, re.S | re.M)  # 辅助删除旁边没用的数字，好像可以抽取年份，带抓取
    res_th = r"<option value=(.*?)>"
    class_num_list = re.findall(res_th, html, re.S | re.M)[len(m_th):]
    return class_num_list
def get_class_lesson(class_num_list):
    # print("班级名称")
    # 获取初始验证码
    numlist = class_num_list
    headers = {
        "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Cookie": "myCookie=; ASP.NET_SessionId=4vuei0pc3tseivnjimq0go1z",
        "DNT": "1",
        "Host": "221.176.153.126:8081",
        "Referer": "http://221.176.153.126:8081/jwweb/ZNPK/KBFB_ClassSel.aspx",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.72 Safari/537.36"
    }
    url = "http://221.176.153.126:8081/jwweb/sys/ValidateCode.aspx"
    num = requests.get(url=url, headers=headers)
    text = client.basicAccurate(num.content)["words_result"][0]["words"]
    # 获取课表
    url = "http://221.176.153.126:8081/jwweb/ZNPK/KBFB_ClassSel_rpt.aspx"
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Content-Length": "63",
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": "myCookie=; ASP.NET_SessionId=4vuei0pc3tseivnjimq0go1z",
        "DNT": "1",
        "Host": "221.176.153.126:8081",
        "Origin": "http://221.176.153.126:8081",
        "Referer": "http://221.176.153.126:8081/jwweb/ZNPK/KBFB_ClassSel.aspx",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.72 Safari/537.36"
    }
    data = {
        "Sel_XNXQ": "20210",
        "txtxzbj": "",
        "Sel_XZBJ": numlist,  # 班级名称
        "type": "1",
        "txt_yzm": text,
    }
    # print(text)

    req = requests.post(url=url, data=data, headers=headers)
    html = req.text
    # print(html)
    res_th = r"src='(.*?)'></div></div>"
    m_th = re.findall(res_th, html, re.S | re.M)[0]
    get_url = "http://221.176.153.126:8081/jwweb/ZNPK/" + str(m_th)
    # print(get_url)
    res_th = r"行政班级：(.*?)</td></tr></table><div"
    m_th = re.findall(res_th, html, re.S | re.M)[0]
    class_name = m_th + ".png"
    reqs = requests.get(url=get_url)
    # print(reqs.text)
    print("正在保存图片。。。。。")
    with open("./上传小程序文件/课程图片/" + class_name, 'wb') as f:
        f.write(reqs.content)
        f.close()
        print(class_name + "图片保存成功......")
if __name__ == '__main__':
    # 获取所有班级ID
    class_num_list=class_num_list()
    # # 获取班级课表图片,并保存到班级可变内部
    error_list=[]
    get_class_lesson(class_num_list[0])
    for class_num in class_num_list:
        try:
            print(class_num)
            get_class_lesson(class_num)
        except:
            try:
                print("第二次验证.....")
                get_class_lesson(class_num)
            except:
                try:
                    print("第三次验证.....")
                    get_class_lesson(class_num)
                except:
                    print("已经将验证失败的id放入错误ID中")
                    error_list.append(class_num)

    print(error_list)
    # 错误重新检索：
    error=[]
    for class_num in error_list:
        try:
            get_class_lesson(class_num)
        except:
            try:
                print("第二次验证.....")
                get_class_lesson(class_num)
            except:
                try:
                    print("第三次验证.....")
                    get_class_lesson(class_num)
                except:
                    print("已经将验证失败的id放入错误ID中")
                    error.append(class_num)
    print(error)






