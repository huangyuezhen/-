import requests
import re
import datetime
import json
import os
import time
import logging


def get_doctor_list():
    doctor_dict = {}

    def get_doctor_list_by_page(page_no=1, page_count=None):
        url = "http://www.guahao.gov.cn/doctorslist.xhtml?HIS_CD=104501&DEP_ID=218&TOT_REC_NUM=20&PAG_NO={}".format(
            page_no)

        header = {
            "Cookie": "adc-ck=AKMGMCAK; XMEM_ID=mB_vvXwUnYLIS8swqV_srzTO3JE6rX2PsKItraIsn88RH4qFMC9f%21428978414%211567390268436; sid=63dd9a47-10ae-40fa-8b11-d81f121cf32d; UM_distinctid=16cefc066c6267-0fff18d290e701-37c153e-1fa400-16cefc066c8561; CNZZDATA4589427=cnzz_eid%3D1468604796-1567386579-null%26ntime%3D1567386579; JSESSIONID=qvLv6G8tdT5zpo7teh2zYl2EIvqZwLwUTBsIwNxsMAoKcBaz8gT-!428978414",
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'
        }
        doctor_result = requests.get(url,  headers=header)
        doctor_pattern = re.compile(
            r'href="/doc_detail.xhtml\?HIS_CD=(\d+)&DEP_ID=(\d+)&DOC_ID=(\d+)">(\S+)</a></p>\s+<p>(\S+)</p>', re.M)
        for item in doctor_pattern.findall(doctor_result.text):
            doctor_dict[item[2]] = {"name":  item[3],
                                    "title": item[4]}
        if page_count is None:
            page_number_pattern = re.compile(r'尾页&nbsp;&nbsp;</a>&nbsp;共(\d+)页&nbsp;&nbsp;(\d+)条记录')
            page_count = int(page_number_pattern.findall(doctor_result.text)[0][0])
        return page_count

    page_count = get_doctor_list_by_page(page_no=1, page_count=None)
    if page_count > 1:
        for page_no in range(2, page_count+1):
            get_doctor_list_by_page(page_no=page_no, page_count=page_count)
    print(doctor_dict)
    return doctor_dict


def get_number_of_doctor(docktor_id=2042, date='2019-09-03'):
    url = "http://www.guahao.gov.cn/ajx_regtime.xhtml"

    # url = "http://www.guahao.gov.cn/ajx_regtime.xhtml?HIS_CD=104501&DEP_ID=218&DOC_ID=1215&DOC_NM=&REG_DAT=2019-09-04&TM_FLG=1&REG_FEE=0&TRE_FEE=20&BBREG_FEE=0&BBTRE_FEE=26&STA_TM=&END_TM="

    data = {
        "HIS_CD": 104501,
        "DEP_ID": 218,
        "DOC_ID": docktor_id,
        "DOC_NM": '',
        "REG_DAT": date,
        "TM_FLG": 1,
        "REG_FEE": 0,
        "TRE_FEE": 20,
        "BBREG_FEE": 0,
        "BBTRE_FEE": 26,
        "STA_TM": '',
        "END_TM": ''
    }
    header = {
        'Content-Type': 'application/x-www-form-urlencoded',
        # 'Cookie': "adc-ck=AKMGMCAK; XMEM_ID=mB_vvXwUnYLIS8swqV_srzTO3JE6rX2PsKItraIsn88RH4qFMC9f%21428978414%211567390268436; sid=63dd9a47-10ae-40fa-8b11-d81f121cf32d; UM_distinctid=16cefc066c6267-0fff18d290e701-37c153e-1fa400-16cefc066c8561; CNZZDATA4589427=cnzz_eid%3D1468604796-1567386579-null%26ntime%3D1567402785; JSESSIONID=EDnw4fxzDg9lvLm3Eopt3Wwed6KawMeniYwC3kWvUaZBG1ppxLkk!-63878959"
    }

    res = requests.get(url, params=data, headers=header)
    res_html = res.text

    time_pattern = re.compile(r'<td height="40">(\S+)</td>')
    haoyuan_pattern = re.compile(r'<td>(\d+)</td>')
    stop_work_pattern = re.compile(r'停诊')

    # print(res_html)
    if stop_work_pattern.findall(res_html):
        return {}
    haoyaun_res = haoyuan_pattern.findall(res.text)
    time_res = time_pattern.findall(res.text)
    res_ = {}
    if haoyaun_res and time_res:
        for (index_, time_) in enumerate(time_res):
            index_new = 2*index_
            res_[time_] = {
                "总号源": haoyaun_res[index_new],
                "剩余号源": haoyaun_res[index_new+1]
            }
            # print(index_, time_)
            # print(haoyaun_res[index_])

    return res_


if __name__ == "__main__":
    doctor_dict = {}
    if os.path.isfile('doctor_id_dict.json'):
        with open('doctor_id_dict.json', 'r') as fd:
            doctor_dict = json.load(fd)
    else:
        doctor_dict = get_doctor_list()
        with open('doctor_id_dict.json', 'w') as fd:
            json.dump(doctor_dict, fd, ensure_ascii=False, indent=4)
    print(doctor_dict)
    now = datetime.datetime.now()
    # res = get_number_of_doctor(1215, '2019-09-04')
    print("start time :{}".format(now.strftime('%Y-%m-%d %H:%M:S')))
    while True:
        for (_id, item) in doctor_dict.items():
            for i in range(0, 7):
                timedelta = datetime.timedelta(days=i)
                date_ = (now + timedelta).strftime('%Y-%m-%d')

                try:
                    res = get_number_of_doctor(_id, date_)
                    if res:
                        print("========{}=={}====={}===================".format(item['name'], item['title'], date_))
                        for time_, values in res.items():
                            if int(values["剩余号源"]) > 0:
                                print(time_, values['总号源'], values["剩余号源"])
                except Exception:

    time.sleep(30)
    print("end time :{}".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:S')))
