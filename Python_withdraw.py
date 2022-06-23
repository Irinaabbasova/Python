vendor = {
    1: 14,
    5: 6,
    10: 7,
    20: 3,
    50: 10,
    100: 2,
    200: 1,
    500: 1
}
withdraw_amount = float(input("How much many do you want to withdraw? "))
wa = withdraw_amount
total = {}
done = False
a = int(vendor[500])*500
b = int(vendor[200])*200
c = int(vendor[100])*100
d = int(vendor[50])*50
e = int(vendor[20])*20
f = int(vendor[10])*10
h = int(vendor[5])*5
i = int(vendor[1])*1
zz = list(vendor.keys())


if wa >= 500: 
        if a >= wa:
                print(zz[-1],a)
        elif   (a+b) >= wa:
                print(zz[-2:],a+b)
        elif   (a+b+c) >= wa:
                print(zz[-3:],a+b+c)
        elif   (a+b+c+d) >= wa:
                print(zz[-4:],a+b+c+d)
        elif   (a+b+c+d+e) >= wa:
                print(zz[-5:],a+b+c+d+e)
        elif   (a+b+c+d+e+f) >= wa:
                print(zz[-6:],a+b+c+d+e+f)
        elif   (a+b+c+d+e+f+h) >= wa:
                print(zz[-7:],a+b+c+d+e+f+h)
        elif   (a+b+c+d+e+f+h+i) >= wa:
                print(zz[-8:],a+b+c+d+e+f+h+i)
        print ('''Sorry, we don't have enough money!''')
# 200
elif   wa >= 200 and wa < 500: 
        if wa == 200:
                print(zz[-2:-1],b)
        elif   (b+c) >= wa:
                print(zz[-3:-1],b+c)
        elif   (b+c+d) >= wa:
                print(zz[-4:-1],b+c+d)
        elif   (b+c+d+e) >= wa:
                print(zz[-5:-1],b+c+d+e)
        elif   (b+c+d+e+f) >= wa:
                print(zz[-6:-1],b+c+d+e+f)
        elif   (b+c+d+e+f+h) >= wa:
                print(zz[-7:-1],b+c+d+e+f+h)
        elif   (b+c+d+e+f+h+i) >= wa:
                print(zz[-8:-1],b+c+d+e+f+h+i)
# 100
elif   wa >= 100 and wa < 200: 
        if wa == 100:
                print(zz[-3:-2],c)
        elif   (c+d) >= wa:
                print(zz[-4:-2],c+d)
        elif   (c+d+e) >= wa:
                print(zz[-5:-2],c+d+e)
        elif   (c+d+e+f) >= wa:
                print(zz[-6:-2],c+d+e+f)
        elif   (c+d+e+f+h) >= wa:
                print(zz[-7:-2],c+d+e+f+h)
        elif   (c+d+e+f+h+i) >= wa:
                print(zz[-8:-2],c+d+e+f+h+i)
#50
elif   wa >= 50 and wa < 100: 
        if wa == 50:
                print(zz[-4:-3],d)
        elif   (d+e) >= wa:
                print(zz[-5:-3],d+e)
        elif   (d+e+f) >= wa:
                print(zz[-6:-3],d+e+f)
        elif   (d+e+f+h) >= wa:
                print(zz[-7:-3],d+e+f+h)
        elif   (d+e+f+h+i) >= wa:
                print(zz[-8:-3],d+e+f+h+i)
#20
elif   wa >= 20 and wa < 50: 
        if wa == 20:
                print(zz[-5:-4],e)
        elif   (e+f) >= wa:
                print(zz[-6:-4],e+f)
        elif   (e+f+h) >= wa:
                print(zz[-7:-4],e+f+h)
        elif   (e+f+h+i) >= wa:
                print(zz[-8:-4],e+f+h+i)
#10
elif   wa >= 10 and wa < 20: 
        if wa == 10:
                print(zz[-6:-5],f)
        elif   (f+h) >= wa:
                print(zz[-7:-5],f+h)
        elif   (f+h+i) >= wa:
                print(zz[-8:-5],f+h+i)
#5
elif   wa >= 5 and wa < 10: 
        if wa == 5:
                print(zz[-7:-6],h)
        elif   (h+i) >= wa:
                print(zz[-8:-6],h+i)
#1
elif   wa >= 1 and wa < 5: 
        if wa == 1:
                print(zz[-8:-7],i)
        
if not wa:
    done = True