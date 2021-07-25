from datetime import datetime, date
import random
# khoảng thời gian chênh lệch giữa 2 ngày tháng
fullnamnay = datetime.now()
namnay = int(fullnamnay.strftime ("%Y"))
namtieptheo = datetime(year = namnay+1, month = 4, day = 27)
sn= namtieptheo-fullnamnay
sinhnhat= str(sn)
songay= sinhnhat[None:3]

"""t4 = datetime(year = 2018, month = 7, day = 12, hour = 7, minute = 9, second = 33)
t5 = datetime(year = 2019, month = 6, day = 10, hour = 5, minute = 55, second = 13)
t6 = t4 - t5
print("t6 =", t6)"""
strA="hello minh la truong"
strB = strA[5:None]
print(strB)
strC =["vjisdjf", "sdfhjdicvh"," ifudsifusidv"]
strD= str(random.choice(strC))
print(strD)