import json
def analyse_lesson(search_name,json_all,lesson_detail):
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
    json_all["json_lesson_list"].append({
        search_name: lesson_frame["lesson_name"]
    })
    for lesson in lesson_detail:
        if lesson["class_name"]==search_name:
            # print(lesson["day"])
            week="星期"+lesson["day"][0]
            # print(search_name)
            """上课时间点"""
            day_begin=int(lesson["day"][2])
            day_end=int(lesson["day"][4])
            """课程一天的列表"""
            json_add = json_all["json_lesson_list"][-1][search_name][week_reflect[week]]["lists"]
            """有些课程是四节一起上的"""
            if day_begin+1==day_end:
                # print(lesson["day"])
                # print("这是一大节课")
                """开始通过赋值来修改数据"""
                # print(day_reflect[day_begin])
                json_add[day_reflect[str(day_begin)]]["name"]=search_name
                json_add[day_reflect[str(day_begin)]]["teacher"] =lesson["teacher"]
                json_add[day_reflect[str(day_begin)]]["room"] = lesson["classroom"]
                json_add[day_reflect[str(day_begin)]]["time"] = lesson["week"]
                # print(json_add[day_reflect[str(day_begin)]])

            elif day_begin+3==day_end:
                # print(lesson["day"])
                # print("这是两大节课")
                """开始通过赋值来修改数据"""
                json_add[day_reflect[str(day_begin)]]["name"] = search_name
                json_add[day_reflect[str(day_begin)]]["teacher"] = lesson["teacher"]
                json_add[day_reflect[str(day_begin)]]["room"] = lesson["classroom"]
                json_add[day_reflect[str(day_begin)]]["time"] = lesson["week"]
                # print(json_add[day_reflect[str(day_begin)]])

                json_add[day_reflect[str(day_begin+2)]]["name"] = search_name
                json_add[day_reflect[str(day_begin+2)]]["teacher"] = lesson["teacher"]
                json_add[day_reflect[str(day_begin+2)]]["room"] = lesson["classroom"]
                json_add[day_reflect[str(day_begin+2)]]["time"] = lesson["week"]
                # print(json_add[day_reflect[str(day_begin + 2)]])
    print(search_name+"添加完成")
    #
    return json_all
if __name__ == '__main__':
    #获取所有课程名称;
    with open("./上传小程序文件/课程名称列表.json", "r", encoding='utf-8') as f:
        name_list=json.loads(f.read())
        f.close()
    json_all_01={"introduce":"课程课表",
              "json_lesson_list":[]}
    json_all_02 = {"introduce": "课程课表",
                   "json_lesson_list": []}
    """读取课程具体课表内容"""
    with open('./临时文件/课程根数据.json', 'r', encoding='utf-8') as fp:
        lessonjson=json.load(fp)
    # """保存课表全部内容，保存到一个文件夹"""
    # for name in name_list["lesson"]:
    #     json_all=analyse_lesson(name,json_all,lessonjson["lesson"])
    # data_jsonss = json.dumps(json_all, indent=4, ensure_ascii=False, separators=(',', ':'))
    # with open("./临时文件/课程课表总内容.json", "w", encoding='utf-8') as f:
    #     f.write(data_jsonss)
    #     f.close()
    """由于微信小程序限制，分两个文件保存"""
    print(len(name_list["lesson"]))
    for name in name_list["lesson"][0:int(len(name_list["lesson"])/2)]:
        json_all_01=analyse_lesson(name,json_all_01,lessonjson["lesson"])
    data_jsonss_01 = json.dumps(json_all_01, ensure_ascii=False)
    with open("./上传小程序文件/课程课表分01.json", "w", encoding='utf-8') as f:
        f.write(data_jsonss_01)
        f.close()
    print("\n第一个分文件保存成功\n")
    """第二部分"""
    for name in name_list["lesson"][int(len(name_list["lesson"])/2):]:
        json_all_02=analyse_lesson(name,json_all_02,lessonjson["lesson"])
    data_jsonss_02 = json.dumps(json_all_02, ensure_ascii=False)
    with open("./上传小程序文件/课程课表分02.json", "w", encoding='utf-8') as f:
        f.write(data_jsonss_02)
        f.close()
    print("第二个分文件保存成功")
    print("共保存的课程数"+str(len(name_list["lesson"])))
