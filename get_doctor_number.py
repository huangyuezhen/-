import requests
import datetime
import re
import time

import traceback


def get_session_id():
    url = "https://open.weixin.qq.com/connect/oauth2/authorize?response_type=code&scope=snsapi_base&state=getOpenId&appid=wx0de227fe13646a00&redirect_uri=http%3A%2F%2Fsp.yx129.cn%2F%2520mobileApp%2Fregister%2Findex%3FappCode%3Dwechat%26appId%3Dwx0de227fe13646a00%26bizCode%3D1%26isParent%3D0%26getOpenIdTime%3D1#wechat_redirect"
    header = {
        "Acceept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Use-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1219.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat",
        "Cookie": "acw_tc=7819730615668903876163731e25e19565d4d5d8130f2d3b8b30d29345f62d; JSESSIONID=528E777532F4DB744BBB00B380CEBE80; Hm_lvt_5d2c204f0385209d909fc75ce81345d1=1566897181,1566897309,1566897364,1566897688; Hm_lpvt_5d2c204f0385209d909fc75ce81345d1=1566898348"
    }
    res = requests.get(url, headers=header)
    print(res.header, res.text)


def cookie_outdate(res):
    if res.status_code == 302:
        location = res.headers['Location']
        set_cookie = res.headers['Set-Cookie']
        print(res.status_code, set_cookie)
        print(location)
        header = {
            "Cookie": "JSESSIONID=2854629C4F679FDCCDD6A198E848B90; Path=/; HttpOnly",
            # "Cookie": cookie,
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1219.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 micromessage/6.5.2.501 NetType/WIFI WindowsWechat"
        }
        data = {
            "openId": "oAFPxs9iFmyT7UGFWyrgDsmkMt-s",
            "showDays": "8",
            "appCode": "wechat",
            "appId": "wx0de227fe13646a00",
            "hospitalId": "441fb80035b2440086507e04afb784ca",
            "hospitalCode": "zsdxdsfsyy",
            "hospitalName": "中山大学附属第三医院",
            "branchHospitalId": "cd63b140c0ee4444a2f8509d806b971b",
            "branchHospitalCode": "2",
            "branchHospitalName": "天河院区",
            "regType": "",
            "deptCode": "218",
            "deptName": "产科门诊",
            "doctorCode": "",
            "selectRegDate": "2019-08-28",
            "category": "",
            "isHasDutyReg": "1",
            "nextDay": "2019-08-28",
            "isSearchDoctor": "",
            "isHasAppointmentReg": "1",
            "doctorPic": "",
            "personalAccountFee": "",
            "overallPlanFee": "",
            "regChannel": ""
        }

        header['Cookie'] = set_cookie
        res = requests.post(location, headers=header, data=data, allow_redirects=False)
        if res.status_code == 301:
            location = res.headers['Location']
            skfrmwrespcookie = res.headers._store['skfrmwrespcookie']
            print('==========301======')
            print(res.status_code,  skfrmwrespcookie)
            print(location)
            header['skfrmwrespcookie'] = skfrmwrespcookie[1]
            res = requests.post(location, headers=header, data=data, allow_redirects=False)
            print('==========200======')
            print(res.status_code, res.headers._store['skfrmwrespcookie'])
            print(res.text)


def generate_order(cookie, data):
    data = data
    url = "http://sp.yx129.cn/mobileApp/register/confirm/generateOrder"
    header = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": cookie
    }
    res = requests.post(url, headers=header, data=data)
    print('generate_order', res.status_code)
    if res.staus_code == 200:
        print('挂号成功,请尽快登录微信公众号完成支付！')


def get_doctor_info():
    url = "http://sp.yx129.cn/%20mobileApp/register/index?appCode=wechat&appId=wx0de227fe13646a00&bizCode=1&isParent=0"

    url_post = "http://sp.yx129.cn//mobileApp/register/doctor/queryDoctorList?timeTemp=15668935176206"
    header = {
        "Cookie": "JSESSIONID=524AACD7BAE82CC21F14B1D188539CFC; Path=/; HttpOnly",
        # "Cookie": cookie,
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1219.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 micromessage/6.5.2.501 NetType/WIFI WindowsWechat"
    }

    data = {
        "openId": "oAFPxs9iFmyT7UGFWyrgDsmkMt-s",
        "showDays": "8",
        "appCode": "wechat",
        "appId": "wx0de227fe13646a00",
        "hospitalId": "441fb80035b2440086507e04afb784ca",
        "hospitalCode": "zsdxdsfsyy",
        "hospitalName": "中山大学附属第三医院",
        "branchHospitalId": "cd63b140c0ee4444a2f8509d806b971b",
        "branchHospitalCode": "2",
        "branchHospitalName": "天河院区",
        "regType": "",
        "deptCode": "218",
        "deptName": "产科门诊",
        "doctorCode": "",
        "selectRegDate": "2019-08-28",
        "category": "",
        "isHasDutyReg": "1",
        "nextDay": "2019-08-28",
        "isSearchDoctor": "",
        "isHasAppointmentReg": "1",
        "doctorPic": "",
        "personalAccountFee": "",
        "overallPlanFee": "",
        "regChannel": ""
    }

    now = datetime.datetime.now()
    count = 0
    print("start time :{}".format(now.strftime('%Y-%m-%d %H:%M:S')))
    try:
        while True:
            count += 1
            print(count)
            for i in range(0, 7):
                timedelta = datetime.timedelta(days=i)
                date_ = (now + timedelta).strftime('%Y-%m-%d')
                data['selectRegDate'] = date_

                res = requests.post(url_post, headers=header, data=data, allow_redirects=False)
                # res = requests.post(url_post, headers=header, data=data, allow_redirects=True)

                if res.status_code == 200:
                    doctor_title = re.compile(r'.*主任|硕士.*')
                    for item in res.json()['message']['doctors']:
                        # print(date_)
                        # print(item['deptName'], item['doctorName'], item['doctorTitle'], item['leftTotalNum'])
                        if item['doctorTitle'] and doctor_title.search(
                                item['doctorTitle']) and int(
                                item['leftTotalNum']) > 0:
                            print(date_)
                            print(item['deptName'], item['doctorName'], item['doctorTitle'], item['leftTotalNum'])
                else:
                    cookie_outdate(res)
                    print(res.status_code, res.text)
                    break
            time.sleep(40)
    except Exception as e:
        print(e)
        print("end time :{}".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:S')))
        print(traceback.format_exc())
        raise Exception('error')


if __name__ == "__main__":
    get_doctor_info()
