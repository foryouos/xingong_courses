import json
import requests
import re
from lxml import etree
def class_list():
    buildings=[301,302,303,304,305]
    class_list_id=[]
    class_list_name = []
    for building in buildings:
        class_list_url = "http://221.176.153.126:8081/jwweb/ZNPK/Private/List_ROOM.aspx?w=150&id="+str(building)
        req = requests.get(url=class_list_url)
        html = req.text
        # print(html)
        """尝试使用xpath抓取数据"""
        res_ths = r"innerHTML='(.*?)';</script>"
        select_html = re.findall(res_ths, html, re.S | re.M)[0]
        # print(select_html)
        html=etree.HTML(select_html)
        class_id=html.xpath('//*[@id="Sel_ROOM"]/option/@value')[1:]
        class_name=html.xpath('//*[@id="Sel_ROOM"]/option/text()')
        # print(class_id)
        # print(len(class_id))
        # print(class_name)
        # print(len(class_name))
        class_list_id.extend(class_id)
        class_list_name.extend(class_name)
    print(class_list_id)
    print(len(class_list_id))
    print(class_list_name)
    print(len(class_list_name))

    """保存课程名称列表小程序上传文件"""
    class_json = {"lesson": []}
    class_json["lesson"]=class_list_name
    # print(type(lesson_json))
    # lesson_jsondata=json.dumps(class_json,indent=4,ensure_ascii=False,separators=(',',':'))
    lesson_jsondata = json.dumps(class_json,ensure_ascii=False)
    f=open("./上传小程序文件/教室名称列表.json","w",encoding='utf-8')
    f.write(lesson_jsondata)
    print(lesson_jsondata)
    f.close()
    print("教室列表上传微信文件保存成功......")
    # return class_list_name
if __name__ == '__main__':
    class_list=class_list()