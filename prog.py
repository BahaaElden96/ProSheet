from datetime import datetime 
from datetime import timedelta
from datetime import date 
print("Enter num of lec ")
lec=int(input())
date1=[]
date2=[]
date3=[]
tw=int(input("Enter  2 if the doctor come every  2 weeks other 1 "))

for k in range(0,lec,1):
    date1.append(date(2019, 9,int(input("Enter lec day "))))
sec=int(input("Enter num of sec "))
for k in range(0,sec,1):
    date2.append(date(2019, 9,int(input("Enter Sec day "))))
print("Enter num of lab ")
lab=int(input())
for k in range(0,lab,1):
    date3.append(date(2019, 9,int(input("Enter lab day "))))    

lecweek = timedelta(weeks=tw)
secweek= timedelta(weeks=1)

for b in range(0,16,1):
         print("------------Week ",b+1,"----------------------")        
         a=0 
         for d in date1:
             if tw ==2:
               print("Lec ",a+1," ",date1[a].strftime("%d/%m/20%y"))
               print("Lec ",a+1," ",date1[a].strftime("%d/%m/20%y"))
             else:
                print("Lec ",a+1," ",date1[a].strftime("%d/%m/20%y"))
             date1[a]+=lecweek
             a+=1
        
         a=0 
         for d in date2:
           # print("Sec ",a+1," ",date2[a].strftime("%d/%m/20%y"))
            date2[a]+=secweek
            a+=1

