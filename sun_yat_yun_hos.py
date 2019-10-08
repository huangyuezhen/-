import requests

header = {
    "Accept": "text/html, application/xhtml+xml, application/xml",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1219.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat"
}

url = "http://sp.yx129.cn/%20mobileApp/register/index?appCode=wechat&appId=wx0de227fe13646a00&bizCode=1&isParent=0"

res = requests.get(url, headers=header)
print(res.headers())
