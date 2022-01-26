import requests
from lxml import etree
import json
def class_name_list():
    class_name_json = {"class_name": []}
    class_list_url = "http://221.176.153.126:8081/jwweb/ZNPK/KBFB_ClassSel.aspx"
    req = requests.get(url=class_list_url)
    # print(req.text)
    html = req.text
    res_th = etree.HTML(html)
    class_name_list = res_th.xpath('//*[@id="theXZBJ"]/select/option/text()')
    class_name_json["class_name"]=class_name_list
    return class_name_json
if __name__ == '__main__':
    """获取班级名称列表"""
    class_name_json=class_name_list()
    print(class_name_json)
    print(len(class_name_json["class_name"]))
    # lesson_jsondata = json.dumps(class_name_json, indent=4, ensure_ascii=False, separators=(',', ':'))
    lesson_jsondata = json.dumps(class_name_json, ensure_ascii=False)
    f = open("./上传小程序文件/班级名称列表.json", "w", encoding='utf-8')
    f.write(lesson_jsondata)
    f.close()
    print("班级名称获取成功，并保存到本地问价夹，课程共计"+str(len(class_name_json["class_name"])))