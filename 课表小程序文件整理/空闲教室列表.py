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
        html=etree.HTML(select_html)
        class_name=html.xpath('//*[@id="Sel_ROOM"]/option/text()')
        class_list_name.extend(class_name)
    print(len(class_list_name))
    return class_list_name
def vacant_class(class_name,vacant_class_json,class_data):
    week_reflect = {"星期一": 0, "星期二": 1, "星期三": 2, "星期四": 3, "星期五": 4, "星期六": 5, "星期日": 6}
    day_reflect = {"上午一": 0, "上午二": 1, "下午一": 2, "下午二": 3, "晚自习": 4}
    print("正在增加此数据...."+class_name)
    for namedict in class_data:
        name=list(namedict.keys())[0]
        if name==class_name:
            # print(vacant_class_json)
            # print(namedict[class_name])
            for i in namedict[class_name]:
                # print(i["name"])
                for j in i["lists"]:
                    # print(j)
                    if j["name"]=="":
                        # vacant_class_json["vacant_class"][i["name"]][j["typeName"]].append(class_name)
                        # print(i["name"]+"的"+j["typeName"]+class_name+"是空教室")
                        vacant_class_json["vacant_class"][week_reflect[i["name"]]][i["name"]][day_reflect[j["typeName"]]][j["typeName"]].append(class_name)

    return vacant_class_json
if __name__ == '__main__':
    #读取所有课程列表
    class_list=class_list()
    vacant_class_json={"vacant_class":[
                                    {"星期一":[
                                                {"上午一":[]},
                                               {"上午二":[]},
                                               {"下午一":[]},
                                               {"下午二":[]},
                                               {"晚自习":[]},
                                               ]},
                                       {"星期二": [{"上午一":[]},
                                               {"上午二":[]},
                                               {"下午一":[]},
                                               {"下午二":[]},
                                               {"晚自习":[]},]},
                                       {"星期三": [{"上午一":[]},
                                               {"上午二":[]},
                                               {"下午一":[]},
                                               {"下午二":[]},
                                               {"晚自习":[]},]},
                                       {"星期四": [{"上午一":[]},
                                               {"上午二":[]},
                                               {"下午一":[]},
                                               {"下午二":[]},
                                               {"晚自习":[]},]},
                                       {"星期五": [{"上午一":[]},
                                               {"上午二":[]},
                                               {"下午一":[]},
                                               {"下午二":[]},
                                               {"晚自习":[]},]},
                                       {"星期六": [{"上午一":[]},
                                               {"上午二":[]},
                                               {"下午一":[]},
                                               {"下午二":[]},
                                               {"晚自习":[]},]},
                                       {"星期日": [{"上午一":[]},
                                               {"上午二":[]},
                                               {"下午一":[]},
                                               {"下午二":[]},
                                               {"晚自习":[]},]},
                                       ]}
    """生成空闲教室列表"""
    with open('./上传小程序文件/教室课程课表.json', 'r', encoding='utf-8') as fp:
        lesson_detail=json.load(fp)
    print(len(class_list))
    """所有的空闲教室列表"""
    # for class_name in class_list:
    #     # print(class_name[1])
    #     """传递参数为，检索的教室名称，数据保存文件，教室课表数据集"""
    #     vacant_class_json=vacant_class(class_name,vacant_class_json,lesson_detail["json_class_list"])
    # # print(vacant_class_json)
    # vacant_data_jsons = json.dumps(vacant_class_json, indent=4, ensure_ascii=False, separators=(',', ':'))
    # """优化空间设计"""
    # # data_jsonss = json.dumps(json_all,ensure_ascii=False)
    # with open("./上传小程序文件/空闲教室.json", "w", encoding='utf-8') as f:
    #     f.write(vacant_data_jsons)
    #     print(vacant_data_jsons)
    #     f.close()
    """仅有教学楼1,和学院楼的空闲教室"""
    class_list_simple=class_list[56:108]
    class_list_simple.extend(class_list[153:-11])
    print(class_list_simple)
    for class_name in class_list_simple:
        # print(class_name[1])
        """传递参数为，检索的教室名称，数据保存文件，教室课表数据集"""
        vacant_class_json=vacant_class(class_name,vacant_class_json,lesson_detail["json_class_list"])
    # print(vacant_class_json)
    vacant_data_jsons = json.dumps(vacant_class_json, indent=4, ensure_ascii=False, separators=(',', ':'))

    """优化空间设计"""
    # vacant_data_jsons = json.dumps(vacant_class_json, ensure_ascii=False)
    with open("./上传小程序文件/空闲教室简约版.json", "w", encoding='utf-8') as f:
        f.write(vacant_data_jsons)
        print(vacant_data_jsons)
        f.close()