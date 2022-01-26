import requests
import re
import easyocr
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
#百度的登录文件
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
    # try:
    with open("./yan.png", 'wb') as f:
        f.write(num.content)
        f.close()
    print("文件保存成功")
    try:
        reader = easyocr.Reader(['en'],model_storage_directory='C:\ProgramData\Anaconda3\Lib\site-packages\easyocr\model')  # this needs to run only once to load the model into memory
        result =  reader.readtext(num.content,detail = 0)[0]
        return result
    except:
        print("验证码验证部分出现报错.....")
        yanzhengma()

def request_detail(lesson_id,text):
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
    data={
        "Sel_XNXQ": "20210",  #时间期限,第几学期对应的代码
        "Sel_KC":lesson_id, #课程名称对应ID
        "gs": "2",  #格式二的形式输出
        "txt_yzm": str(text)  #验证码
    }
    url="http://221.176.153.126:8081/jwweb/ZNPK/KBFB_LessonSel_rpt.aspx"
    req=requests.post(url=url,headers=headers,data=data)
    req.encoding=req.apparent_encoding
    res_th = r"font-size:16pt'>(.*?)</td></tr><tr><td style='text-align"
    try:
        m_th = re.findall(res_th,req.text, re.S | re.M)[0]
        print(m_th+"原始数据抓取成功......")
        print("验证码识别成功")
    except(IndexError):
        print("indexError，验证码验证出错")
        text = yanzhengma()
        print(text)
        request_detail(lesson_id, text)


if __name__ == '__main__':
    # 获取验证码

    text = yanzhengma()
    print(text)

    lesson_id="380484"
    request_detail(lesson_id,text)
