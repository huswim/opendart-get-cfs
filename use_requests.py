"""
필요한 패키지(= 라이브러리, 모듈) 가져오기
"""
import pandas as pd
import requests

"""
API 요청 관련 정보를 변수에 저장
"""
url = "https://opendart.fss.or.kr/api/fnlttSinglAcntAll.json"  # API url

params = {
    "crtfc_key": "",  # API 인증키
    "corp_code": "00165680",  # 회사 고유 번호 (호텔신라, 00165680)
    "bsns_year": "",  # 사업 연도
    "reprt_code": "11011",  # 보고서 코드(사업보고서 11011)
    "fs_div": "CFS",  # 개별/연결 구분(연결재무제표: CFS)
}

year_start = 2017
year_end = 2021

"""
API 요청해서 재무제표 가지고 오기
"""
cfs_dict = {}

for year in range(year_start, year_end + 1):
    params["bsns_year"] = str(year)
    response = requests.get(url, params=params)

    if response.status_code == 200:
        cfs_dict[year] = pd.DataFrame(response.json()["list"])
    else:
        print(response.status_code + " : data is not found")

"""
가지고 온 재무제표를 엑셀 파일로 저장
"""
cfs_sum_df = pd.concat(cfs_dict.values(), ignore_index=True)
cfs_sum_df.to_excel(
    "호텔신라" + " 연결재무제표 " + str(year_start) + " - " + str(year_end) + ".xlsx"
)
