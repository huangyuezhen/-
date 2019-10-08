import requests


def findAllCards():
    url = "http://sp.yx129.cn/mobileApp/common/findAllCardsToRemark?timeTemp=1566957451220"
    header = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Cookie": "acw_tc=7819730615668903876163731e25e19565d4d5d8130f2d3b8b30d29345f62d; wx0de227fe13646a00_oAFPxs9iFmyT7UGFWyrgDsmkMt-s_defaultCard=3187b0d005644596ba7f75a6ef5929d4; JSESSIONID=03E3E6F97C1DF3DFABA840F44240BFA5; Hm_lvt_5d2c204f0385209d909fc75ce81345d1=1566897309,1566897364,1566897688,1566901151; Hm_lpvt_5d2c204f0385209d909fc75ce81345d1=1566957449"
    }
    data = {
        "branchId": "cd63b140c0ee4444a2f8509d806b971b",
        "openId": "oAFPxs9iFmyT7UGFWyrgDsmkMt-s",
        "hospitalCode": "zsdxdsfsyy",
        "branchCode": "2",
        "hospitalId": "441fb80035b2440086507e04afb784ca",
        "platform": "1",
        "appCode": "wechat",
        "appId": "wx0de227fe13646a00"
    }


def generate_order():
    data = {
        "token": "",
        "openId": "oAFPxs9iFmyT7UGFWyrgDsmkMt-s",
        "orderNo": "",
        "showDays": "",
        "appCode": "wechat",
        "appId": "wx0de227fe13646a00",
        "hospitalId": "441fb80035b2440086507e04afb784ca",
        "hospitalCode": "zsdxdsfsyy",
        "hospitalName": "中山大学附属第三医院",
        "branchHospitalId": "cd63b140c0ee4444a2f8509d806b971b",
        "branchHospitalCode": "2",
        "branchHospitalName": "天河院区",
        "deptCode": "218",
        "doctorCode": "3462",
        "selectRegDate": "2019-09-04 星期三",
        "category": "0",
        "deptName": "产科门诊",
        "doctorName": "产科普通号",
        "doctorTitle": "",
        "doctorBeginTime": "14:30",
        "doctorEndTime": "17:00",
        "hisOrdNo": "",
        "regFee": "0",
        "treatFee": "1000",
        "childRegFee": "0",
        "regType": "1",
        "workId": "5371||6513",
        "timeFlag": "",
        "isViewDiseaseDesc": "0",
        "onlinePaymentControl": "1",
        "personalAccountFee": "null",
        "overallPlanFee": "null",
        "teddyId": "049e2a4542cbd3f0800544d42f7d3132",
        "regSourceFeeTemplateCode": "",
        "yuYueNo": "",
        "cardNo": "5000552882",
        "cardType": "1",
        "regPersonType": "1",
        "patientName": "黄月珍",
        "patientSex": "2",
        "patientMobile": "18825052321",
        "idType": "1",
        "idNo": "440823199205295684",
        "isPay": "0",
        "isMedicarePay": "0",
        "diseaseDesc": "",
        "forward": "",
        "bindCardType": "",
        "populationType": "",
        "appointmentType": "",
        "age": "27",
        "guardIdNo": "null",
        "guardName": "null",
        "guardMobile": "null",
        "isQueryPatientType": "0",
        "mediCareType": "",
        "patientTypeId": "",
        "isScanRegister": "",
        "regChannel": "",
        "isLockRegByFaceVerify": "",
        "verifyResultAndToken": "",
        "isBasedOnMedicalInsuranceWay": ""
    }
    url = "http://sp.yx129.cn/mobileApp/register/confirm/generateOrder"
    header = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "JSESSIONID=4F2E9D781FCA210B86B739BF8E6E01D6"
    }
    res = requests.post(url, headers=header, data=data)
    print(res.status_code)


if __name__ == "__main__":
    generate_order()
