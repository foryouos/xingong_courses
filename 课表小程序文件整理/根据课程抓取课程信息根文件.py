import requests
import re
import time
import pandas as pd
from lxml import etree
from aip import AipOcr
import chardet
import json
#百度的登录文件
APP_ID = '24053287'
API_KEY = 'HZbSPqr014lGtvgcOjlB9Y2B'
SECRET_KEY = 'S5Zq0MHV4Tks2g0l4kvkSsw1K3IyW7oZ'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
class_detail_count=0
text=0
text_count=0
error_list=[]
def lesson_name_list(): #获取所有课程数量列表
    lesson_json={"lesson":[]}
    class_list_url = "http://221.176.153.126:8081/jwweb/ZNPK/Private/List_XNXQKC.aspx?xnxq=20210"
    req = requests.get(url=class_list_url)
    html = req.text
    #获取课程ID
    res_th = r"<option value=(.*?)>"
    lesson_id = re.findall(res_th, html, re.S | re.M)
    res_th = r"\|(.*?)</option>"
    lesson_name=re.findall(res_th, html, re.S | re.M)
    for i in range(len(lesson_id)):
        lesson_json["lesson"].append({"num":i,
                                      "lesson_id":lesson_id[i],
                                      "lesson_name":lesson_name[i]
                                      })
    print("读取课程名称列表成功...")
    return lesson_json
def yanzhengma():
    headers = {
        "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Cookie": "myCookie=; ASP.NET_SessionId=4vuei0pc3tseivnjimq0go1z",
        "DNT": "1",
        "Host": "221.176.153.126:8081",
        "Referer": "http://221.176.153.126:8081/jwweb/ZNPK/KBFB_LessonSel.aspx",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.72 Safari/537.36"
    }
    url = "http://221.176.153.126:8081/jwweb/sys/ValidateCode.aspx"
    num = requests.get(url=url,headers=headers)
    try:
        text = client.basicAccurate(num.content)["words_result"][0]["words"]
        # print("中间测试直接输出%s",text)
        return text
    except:
        print("请检查百度验证码调用是否超过500次,已经将图片保存到本地，需要手动输入....")
        with open("./临时文件/根数据无法识别的验证码.png",'wb') as f:
            f.write(num.content)
            f.close()
def request_detail(lesson_id):
    headers={
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Content-Length": "46",
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": "myCookie=; ASP.NET_SessionId=4vuei0pc3tseivnjimq0go1z",
        "DNT": "1",
        "Host": "221.176.153.126:8081",
        "Origin": "http://221.176.153.126:8081",
        "Referer": "http://221.176.153.126:8081/jwweb/ZNPK/KBFB_LessonSel.aspx",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.72 Safari/537.36"
    }
    global text
    # print(text)
    # text = yanzhengma()
    global text_count
    global error_list
    data={
        "Sel_XNXQ": "20210",  #时间期限,第几学期对应的代码
        "Sel_KC":lesson_id, #课程名称对应ID
        "gs": "2",  #格式二的形式输出
        "txt_yzm": str(text)  #验证码
    }
    url="http://221.176.153.126:8081/jwweb/ZNPK/KBFB_LessonSel_rpt.aspx"
    req=requests.post(url=url,headers=headers,data=data)
    req.encoding=req.apparent_encoding
    # print(req.text)
    try:
        res_th = r"font-size:16pt'>(.*?)</td></tr><tr><td style='text-align"
        m_th = re.findall(res_th,req.text, re.S | re.M)[0]
        #print(m_th+"原始数据抓取成功......")
        with open("./临时文件/根文件依赖.html", 'w',encoding="utf-8") as f:
            f.write(req.text)
            f.close()
        text_count=0
    except:
        try:
            print("验证码数据错误，原始网页没爬取,正在重新验证验证码。。。。。")
            text_count = text_count + 1
            text = yanzhengma()
            if text_count % 5 == 0:
                request_detail(lesson_id)
                # return "continue"
            else:
                request_detail(lesson_id)
            # print(req.text)
        except:
            print(req.text)
def json_clean_lesson(html,data_json):
    # print(html)
    #获取课程名称
    # print(data_json)
    res_th = r"课程：\[(.*?)\](.*?)&ensp;&ensp;总学时"
    l_name = re.findall(res_th,html, re.S | re.M)
    # print(l_name)
    l_name=l_name[0][1]
    print(l_name+"抓取数据成功.....")
    #获取列表全部信息
    res_th = r"<td align='left'>(.*?)<br></td>"
    lists = re.findall(res_th, html, re.S | re.M)
    # print(lists)
    global class_detail_count
    class_detail_count=class_detail_count+len(lists)
    print("已经抓取的课数为"+str(class_detail_count))
    for i in range(0,len(lists),6):
        #对class就行才分
        lists[i+2]=lists[i+2].split(" ")
        if lists[i]!="":
            data_json["lesson"].append({
                                        "class_name": l_name,
                                        "teacher":lists[i],
                                        "class":lists[i+2],
                                        "week":lists[i+3],
                                        "day": lists[i+4],
                                        "classroom":lists[i+5]
                                        })
        else:

            for j in range(3):
                # print(lists[q])
                q = i + j
                lists[q]=lists[q-6]
                # print(lists[q])
            # print(lists[i:i+6])
            data_json["lesson"].append({
                "class_name": l_name,
                "teacher": lists[i],
                "class": lists[i + 2],
                "week": lists[i + 3],
                "day": lists[i + 4],
                "classroom": lists[i + 5]
            })
    return data_json
if __name__ == '__main__':
    #获取课程列表
    #计数
    class_count=0
    #读取本地json文件
    lesson_datail_json = {"lesson": []}
    #抓取课程html并保存,需要传入参数
    print("正在获取课程课表以及对应的ID。。。。。。。")
    lesson_json = lesson_name_list()
    # print(lesson_json)
    #频繁在某一个砍出现验证码验证失败
    #增加错误记录，后期增加
    lesson_lists = lesson_json["lesson"]
    for lesson_name in lesson_lists:
        lesson_id=lesson_name["lesson_id"]
        print("正在抓取第"+str(class_count)+"节课的课程信息")
        #获取html并保存到本地
        request_detail(lesson_id)
        def get_file_content(filePath):
            with open(filePath, 'rb') as fp:
                current_encoding=chardet.detect(fp.read())["encoding"]
                return open(filePath,"r",encoding=current_encoding).read()
        html = get_file_content('./临时文件/根文件依赖.html')
        lesson_datail_json=json_clean_lesson(html,lesson_datail_json)
        class_count=class_count+1
    data_jsons = json.dumps(lesson_datail_json, indent=4, ensure_ascii=False, separators=(',', ':'))
    f = open("./临时文件/课程根数据.json", "w", encoding='utf-8')
    f.write(data_jsons)
    f.close()
    print(data_jsons)
    """获取课程名称列表，到本地lesson_name_list.json,根据课程列表获取课程具体信息保存到本地lesson_data.json"""
