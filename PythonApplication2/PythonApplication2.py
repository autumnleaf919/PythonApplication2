import random as rd
import datetime as dt
print("猜猜拳1-->剪刀 2-->石頭 3-->布 ")
you=input()
you=int(you)
d=dt.datetime.now()
rd.seed(d)
m=rd.randint(1,3)
print(m)
if you==m:
    print("平手")
elif you==1 and m==3:
    print("勝利")
elif m==1 and you==3:
    print("敗北")
elif you<m:
    print("敗北")
elif you>m:
    print("勝利")