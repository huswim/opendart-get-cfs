import OpenDartReader
import pandas as pd

API_KEY = ""  # API 인증키
dart = OpenDartReader(API_KEY)

corp_name = "호텔신라"
year_start = 2017
year_end = 2021

cfs_dict = {}

for year in range(year_start, year_end + 1):
    cfs_dict[year] = dart.finstate_all(corp_name, year)

cfs_sum_df = pd.concat(cfs_dict.values(), ignore_index=True)
cfs_sum_df.to_excel(
    corp_name + " 연결재무제표 " + str(year_start) + " - " + str(year_end) + ".xlsx"
)
