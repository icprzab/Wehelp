from msilib.schema import Condition
import pandas as pd
import numpy as np
import requests
res = requests.get(
    "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json")
event = res.json()
clist = event["result"]["results"]

df = pd.DataFrame(clist)
df_loc = df.loc[:, ["xpostDate", "stitle", "address",
                    "longitude", "latitude", "file"]]
date = []
for i in df_loc["xpostDate"]:
    ts = i.split("20")
    ts2 = ts[1].split("/")
    date.append(int(ts2[0]))
df_loc["year"] = date

condition = df_loc["year"] >= 15
year_filter = df_loc[condition]
df_loc2 = year_filter.loc[:, ["stitle", "address",
                              "longitude", "latitude", "file"]]

region = []
for i in df_loc2["address"]:
    ts = i.split("市  ")
    ts2 = ts[1].split("區")
    region.append(ts2[0]+"區")
df_loc2["區域"] = region

link = []
for i in df_loc2["file"]:
    ts = i.split("jpg")
    link.append(ts[0])
df_loc2["link"] = link

link2 = []
for i in df_loc2["link"]:
    ts = i.split("JPG")
    link2.append(ts[0]+"jpg")
df_loc2["第一張圖檔網址"] = link2

df_loc3 = df_loc2.loc[:, ["stitle", "區域",
                          "longitude", "latitude", "第一張圖檔網址"]]

df_loc3_rename1 = df_loc3.rename(columns={"stitle": "景點名稱"})
df_loc3_rename2 = df_loc3_rename1.rename(columns={"longitude": "經度"})
df_loc3_rename3 = df_loc3_rename2.rename(columns={"latitude": "緯度"})

mid_term_marks_df = pd.DataFrame(df_loc3_rename3)
mid_term_marks_df.to_csv("week-3.csv", index=False)
