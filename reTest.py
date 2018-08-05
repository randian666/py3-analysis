#!/usr/bin/env python3

import re

s="文件上传成功！"

res1 = re.search("上传成功".encode('gbk'), s.encode('gbk')) # 匹配出'上传成功'

if res1 is not None:
    print("匹配成功")
    print(res1.group().decode('gbk'))
else:
    print("匹配失败")