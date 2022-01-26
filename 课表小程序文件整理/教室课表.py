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
def analyse_class(search_name,json_all,lesson_detail):
    lesson_frame = {
        "lesson_name":
            [
                {
                    "name": "星期一",
                    "lists": [
                        {
                            "typeName": "上午一",
                            "name": "",
                            "teacher": "",
                            "room": "",
                            "time": ""
                        },
                        {
                            "typeName": "上午二",
                            "name": "",
                            "teacher": "",
                            "room": "",
                            "time": ""
                        },
                        {
                            "typeName": "下午一",
                            "name": "",
                            "teacher": "",
                            "room": "",
                            "time": ""
                        },
                        {
                            "typeName": "下午二",
                            "name": "",
                            "teacher": "",
                            "room": "",
                            "time": ""
                        },
                        {
                            "typeName": "晚自习",
                            "name": "",
                            "teacher": "",
                            "room": "",
                            "time": ""
                        },
                    ]
                },
                {
                    "name": "星期二",
                    "lists": [
                        {
                            "typeName": "上午一",
                            "name": "",
                            "teacher": "",
                            "room": "",
                            "time": ""
                        },
                        {
                            "typeName": "上午二",
                            "name": "",
                            "teacher": "",
                            "room": "",
                            "time": ""
                        },
                        {
                            "typeName": "下午一",
                            "name": "",
                            "teacher": "",
                            "room": "",
                            "time": ""
                        },
                        {
                            "typeName": "下午二",
                            "name": "",
                            "teacher": "",
                            "room": "",
                            "time": ""
                        },
                        {
                            "typeName": "晚自习",
                            "name": "",
                            "teacher": "",
                            "room": "",
                            "time": ""
                        },
                    ]
                },
                {
                    "name": "星期三",
                    "lists": [
                        {
                            "typeName": "上午一",
                            "name": "",
                            "teacher": "",
                            "room": "",
                            "time": ""
                        },
                        {
                            "typeName": "上午二",
                            "name": "",
                            "teacher": "",
                            "room": "",
                            "time": ""
                        },
                        {
                            "typeName": "下午一",
                            "name": "",
                            "teacher": "",
                            "room": "",
                            "time": ""
                        },
                        {
                            "typeName": "下午二",
                            "name": "",
                            "teacher": "",
                            "room": "",
                            "time": ""
                        },
                        {
                            "typeName": "晚自习",
                            "name": "",
                            "teacher": "",
                            "room": "",
                            "time": ""
                        },
                    ]
                },
                {
                    "name": "星期四",
                    "lists": [
                        {
                            "typeName": "上午一",
                            "name": "",
                            "teacher": "",
                            "room": "",
                            "time": ""
                        },
                        {
                            "typeName": "上午二",
                            "name": "",
                            "teacher": "",
                            "room": "",
                            "time": ""
                        },
                        {
                            "typeName": "下午一",
                            "name": "",
                            "teacher": "",
                            "room": "",
                            "time": ""
                        },
                        {
                            "typeName": "下午二",
                            "name": "",
                            "teacher": "",
                            "room": "",
                            "time": ""
                        },
                        {
                            "typeName": "晚自习",
                            "name": "",
                            "teacher": "",
                            "room": "",
                            "time": ""
                        },
                    ]
                },
                {
                    "name": "星期五",
                    "lists": [
                        {
                            "typeName": "上午一",
                            "name": "",
                            "teacher": "",
                            "room": "",
                            "time": ""
                        },
                        {
                            "typeName": "上午二",
                            "name": "",
                            "teacher": "",
                            "room": "",
                            "time": ""
                        },
                        {
                            "typeName": "下午一",
                            "name": "",
                            "teacher": "",
                            "room": "",
                            "time": ""
                        },
                        {
                            "typeName": "下午二",
                            "name": "",
                            "teacher": "",
                            "room": "",
                            "time": ""
                        },
                        {
                            "typeName": "晚自习",
                            "name": "",
                            "teacher": "",
                            "room": "",
                            "time": ""
                        },
                    ]
                },
                {
                    "name": "星期六",
                    "lists": [
                        {
                            "typeName": "上午一",
                            "name": "",
                            "teacher": "",
                            "room": "",
                            "time": ""
                        },
                        {
                            "typeName": "上午二",
                            "name": "",
                            "teacher": "",
                            "room": "",
                            "time": ""
                        },
                        {
                            "typeName": "下午一",
                            "name": "",
                            "teacher": "",
                            "room": "",
                            "time": ""
                        },
                        {
                            "typeName": "下午二",
                            "name": "",
                            "teacher": "",
                            "room": "",
                            "time": ""
                        },
                        {
                            "typeName": "晚自习",
                            "name": "",
                            "teacher": "",
                            "room": "",
                            "time": ""
                        },
                    ]
                },
                {
                    "name": "星期日",
                    "lists": [
                        {
                            "typeName": "上午一",
                            "name": "",
                            "teacher": "",
                            "room": "",
                            "time": ""
                        },
                        {
                            "typeName": "上午二",
                            "name": "",
                            "teacher": "",
                            "room": "",
                            "time": ""
                        },
                        {
                            "typeName": "下午一",
                            "name": "",
                            "teacher": "",
                            "room": "",
                            "time": ""
                        },
                        {
                            "typeName": "下午二",
                            "name": "",
                            "teacher": "",
                            "room": "",
                            "time": ""
                        },
                        {
                            "typeName": "晚自习",
                            "name": "",
                            "teacher": "",
                            "room": "",
                            "time": ""
                        },
                    ]
                },
            ]
    }
    week_reflect={"星期一":0,"星期二":1,"星期三":2,"星期四":3,"星期五":4,"星期六":5,"星期日":6}
    day_reflect = {"1": 0, "3": 1, "5": 2, "7": 3, "9": 4}
    # print(search_name)
    json_all["json_class_list"].append({
        search_name: lesson_frame["lesson_name"]
    })
    for lesson in lesson_detail:
        if lesson["classroom"]==search_name:
            # print(lesson)
            week="星期"+lesson["day"][0]
            # print(week)
    #         """上课时间点"""
            day_begin=int(lesson["day"][2])
            day_end=int(lesson["day"][4])
            # print(day_begin)
    #         """课程一天的列表"""
            json_add = json_all["json_class_list"][-1][search_name][week_reflect[week]]["lists"]
            # print(json_add)
    #         """有些课程是四节一起上的"""
            if day_begin+1==day_end:
                json_add[day_reflect[str(day_begin)]]["name"]=lesson["class_name"]
                json_add[day_reflect[str(day_begin)]]["teacher"] =lesson["teacher"]
                json_add[day_reflect[str(day_begin)]]["room"] = lesson["classroom"]
                json_add[day_reflect[str(day_begin)]]["time"] = lesson["week"]

            elif day_begin+3==day_end:
                """开始通过赋值来修改数据"""
                json_add[day_reflect[str(day_begin)]]["name"] = lesson["class_name"]
                json_add[day_reflect[str(day_begin)]]["teacher"] = lesson["teacher"]
                json_add[day_reflect[str(day_begin)]]["room"] = lesson["classroom"]
                json_add[day_reflect[str(day_begin)]]["time"] = lesson["week"]
                # print(json_add[day_reflect[str(day_begin)]])

                json_add[day_reflect[str(day_begin+2)]]["name"] = lesson["class_name"]
                json_add[day_reflect[str(day_begin+2)]]["teacher"] = lesson["teacher"]
                json_add[day_reflect[str(day_begin+2)]]["room"] = lesson["classroom"]
                json_add[day_reflect[str(day_begin+2)]]["time"] = lesson["week"]
                # print(json_add[day_reflect[str(day_begin + 2)]])
    #
    print(search_name+"添加完成")
    # #
    return json_all
if __name__ == '__main__':
    #读取所有课程列表
    with open('./临时文件/课程根数据.json', 'r', encoding='utf-8') as fp:
        lesson_detail=json.load(fp)
    #读取教室列表
    json_all = {"introduce": "教室课表",
                "json_class_list": []}
    class_list=class_list()
    print(class_list)
    for class_name in class_list:
        json_all=analyse_class(class_name,json_all,lesson_detail["lesson"])
    # data_jsonss = json.dumps(json_all, indent=4, ensure_ascii=False, separators=(',', ':'))
    """优化空间设计"""
    data_jsonss = json.dumps(json_all,ensure_ascii=False)
    with open("上传小程序文件/教室课程课表.json", "w", encoding='utf-8') as f:
        f.write(data_jsonss)
        # print(data_jsonss)
        f.close()
