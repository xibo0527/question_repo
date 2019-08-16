import urllib.request
import urllib
import json
import logging

logger = logging.getLogger('apis')

def send_sms(mobile,captcha):
    flag = True
    url = 'https://open.ucpaas.com/ol/sms/sendsms'
    headers = {
        "Content-Type": "application/json; charset=utf-8"
    }
    values = {
        "sid": "ff485ff7a8c88a5f5d14e394f334c780",
        "token": "f3d5d4da3f9bc6e03f5aad48996fd3a0",
        "appid": "28e04774ff6341d0a14a4a0592ac8768",
        "templateid": "489059",
        "param": str(captcha),
        "mobile": mobile,

    }
    try:
        # 将字典格式化成bytes格式
        data = json.dumps(values).encode('utf-8')
        logger.info(f"即将发送短信: {data}")
        # 创建一个request,放入我们的地址、数据、头
        request = urllib.request.Request(url, data, headers)
        html = urllib.request.urlopen(request).read().decode('utf-8')
        # html = '{"code":"000000","count":"1","create_date":"2018-07-23 13:34:06","mobile":"15811564298","msg":"OK","smsid":"852579cbb829c08c917f162b267efce6","uid":""}'
        code = json.loads(html)["code"]
        if code == "000000":
            logger.info(f"短信发送成功：{html}")
            flag = True
        else:
            logger.info(f"短信发送失败：{html}")
            flag = False
    except Exception as ex:
        logger.info(f"出错了,错误原因：{ex}")
        flag = False
    return flag

if __name__ == "__main__":
        # 测试短信接口是否是管用
    send_sms("18973426581", "123456")