#!/usr/bin/env python3
#coding:utf-8

import re,datetime
import codecs
import matplotlib.pyplot as plt
files=["E:/sendcouponlog/error10.191.92.116.log",
       "E:/sendcouponlog/error10.191.92.117.log",
       "E:/sendcouponlog/error10.191.92.115.log",
       "E:/sendcouponlog/error10.191.81.61.log",
       "E:/sendcouponlog/error10.191.62.145.log",
       "E:/sendcouponlog/error10.191.52.161.log",
       "E:/sendcouponlog/error10.191.43.179.log",
       "E:/sendcouponlog/error10.191.43.154.log",
       "E:/sendcouponlog/error10.191.42.105.log",
       "E:/sendcouponlog/error10.191.42.104.log"]
batchkeys_exclude=["FP_t8w7zv",
"FP_8zbs4b",
"FP_t8izts",
"MF_8zc9ue",
"FP_t8w7zv",
"FP_z8ce8v",
"FP_8bszih",
"FP_8bszxw",
"FP_8zbs4b",
"VIP_8zc9uv",
"FP_8ce9zf",
"FP_8c9zw4",
"FP_zt8wmo",
"FP_8bszxw",
"FP_z8djjt",
"FP_8cfzby",
"FP_z8c937",
"FP_8cfzby",
"FP_z8djjt",
"EXCHANGE_8bs1z7",
"FP_t8wznt",
"FP_8dzj10",
"FP_8zbs4b",
"FP_t8jjzu",
"FP_8bsz1g",
"FP_z8c937",
"FP_8bsz6e",
"FP_tz8w75",
"FP_8cz4pb",
"VIP_8c4ztj",
"FP_tz8jhb",
"FP_8bszp1",
"FP_z8djfe",
"FP_8bslzu",
"FP_t8zj4v",
"FP_8bsz6e",
"FP_z8c4qx",
"FP_8bslzu",
"VIP_t8ipzu",
"FP_8bskz0",
"FP_z8djfe"];
re_info = r"没有查询到有效的批次信息或者传入了非法的批次发券"
re_time = "2018-04-18 21:00:00";
def string_toDatetime(string):
    return datetime.datetime.strptime(string, "%Y-%m-%d %H:%M:%S")

def analysis_log():
    data=set() #去重
    for file_name in files:
        print("开始解析",file_name)
        file=open(file_name,'r',encoding='UTF-8')
        for (num,line) in enumerate(file):
            result=re.findall(re_info,line)
            #获取日志中是否包含字符串
            if result != None and len(result) != 0:
                currtime=line[0:19]
                #时间比较
                if string_toDatetime(currtime)>string_toDatetime(re_time):
                    batchKey=re.findall(r"batchKey='(.+?)'", line)[0]
                    if batchKey in batchkeys_exclude:
                        print(batchKey,"已经存在")
                    print(batchKey)
                    data.add(batchKey)
    write_txt(data,"data.txt")
def write_txt(data, path):
    output = open(path, 'w')  # 打开文件
    for txt in data:
        output.write(txt)  #write方法，写入到指定文件中
        output.write("\n")
    output.close()  # close关闭文件
if __name__ == '__main__':
    analysis_log()

