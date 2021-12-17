import requests
from datetime import datetime
from urllib import parse
import pandas as pd
from bs4 import BeautifulSoup
from secret import key

def getHoliday(year: int) -> pd.DataFrame:
    url = 'http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService/getRestDeInfo'
    api_key_utf8 = key
    api_key_decode = parse.unquote(api_key_utf8)

    params ={
        'serviceKey' : api_key_decode,
        'numOfRows' : '50',
        'solYear' : year
    }

    temp = ['월', '화', '수', '목', '금', '토', '일']

    response = requests.get(url, params=params)
    xml = BeautifulSoup(response.text, "lxml")
    items = xml.find('items')
    item_list = []
    for item in items:
        dt = datetime.strptime(item.find("locdate").text.strip(), '%Y%m%d')
        item_dict = {
            "DayName" : item.find("datename").text.strip(),
            "DateTime" : dt,
            "weekday" : temp[dt.weekday()]
        }
        item_list.append(item_dict)

    return pd.DataFrame(item_list)

print(getHoliday(2022))

