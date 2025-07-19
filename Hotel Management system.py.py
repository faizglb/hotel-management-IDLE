import os
import platform
import mysql.connector
import datetime
mydb = mysql.connector.connect(user='root', password='12345faiz',
                               host='localhost',
                               database='hotel')
mycursor=mydb.cursor()

def registercust():
    custid=input("enter the customer id to customer(***room no. rented to customer is customer ID***): ")
    name=input("enter name: ")
    phone=input("enter phone number of customer : ")
    addr=input("enter address: ")
    indate=input("enter check in date: ")
    outdate=input("enter check out date: ")
    sql="insert into custdata(custid,custname,phone,addr,indate,outdate)values('{}','{}','{}','{}','{}','{}')".format(custid,name,phone,addr,indate,outdate)
    mycursor.execute(sql)
    mydb.commit()





def roomrent():
    print("Do you want to see room type  : Enter 1 for yes :")
    ch=int(input("enter your choice:"))
    print ("We have the following rooms for you:-")
    print ("room no - 01.  type A---->rs 4000/Per day -:- enter  1 to select")
    print ("room no - 02.  type A---->rs 4000/Per day -:- enter  2 to select")
    print ("room no - 03.  type A---->rs 4000/Per day -:- enter  3 to select")
    print ("room no - 04.  type A---->rs 4000/Per day -:- enter  4 to select")
    print ("room no - 05.  type A---->rs 3000/Per day -:- enter  5 to select")
    print ("room no - 06.  type B---->rs 3000/Per day -:- enter  6 to select")
    print ("room no - 07.  type B---->rs 3000/Per day -:- enter  7 to select")
    print ("room no - 08.  type B---->rs 3000/Per day -:- enter  8 to select")
    print ("room no - 09.  type B---->rs 3000/Per day -:- enter  9 to select")
    print ("room no - 10.  type B---->rs 3000/Per day -:- enter 10 to select")
    print ("room no - 11.  type C---->rs 2000/Per day -:- enter 11 to select")
    print ("room no - 12.  type C---->rs 2000/Per day -:- enter 12 to select")
    print ("room no - 13.  type C---->rs 2000/Per day -:- enter 13 to select")
    print ("room no - 14.  type C---->rs 2000/Per day -:- enter 14 to select")
    
    

    x=int(input("Enter Your Choice Please->"))
    n=int(input("For How Many days You would Stay:"))
    if(x==1):
        print ("you have opted room type A , room no-01")
        s=4000*n
    elif(x==2):
        print ("you have opted room type A , room no-02")
        s=4000*n
    elif(x==3):
        print ("you have opted room type A , room no-03")
        s=4000*n
    elif(x==4):
        print ("you have opted room type A , room no-04")
        s=4000*n
    elif(x==5):
        print ("you have opted room type A , room no-05")
        s=4000*n
    elif (x==6):
        print ("you have opted room type B , room no-06")
        s=3000*n
    elif (x==7):
        print ("you have opted room type B , room no-07")
        s=3000*n
    elif (x==8):
        print ("you have opted room type B , room no-08")
        s=3000*n
    elif (x==9):
        print ("you have opted room type B , room no-09")
        s=3000*n
    elif (x==10):
        print ("you have opted room type B , room no-10")
        s=3000*n 
    elif (x==11):
        print ("you have opted room type C , room no-11")
        s=2000*n
    elif (x==12):
        print ("you have opted room type C , room no-12")
        s=2000*n
    elif (x==13):
        print ("you have opted room type C , room no-13")
        s=2000*n
    elif (x==14):
        print ("you have opted room type C , room no-14")
        s=2000*n
    else:
        print ("please choose a room")
    print ("your room rent is =",s,"\n")


    print("**enter the info for saving data**")
    cust_name=input("enter the name of the customer:")
    payment=input("enter the amount need to be paid:")
    roomno=input("enter roomno assigned to the customer:")
    roomtype=input("enter room type assigned to the customer:")
    sql="insert into room(roomno,roomtype,payment,cust_name)values('{}','{}','{}','{}')".format(roomno,roomtype,payment,cust_name)
    mycursor.execute(sql)
    mydb.commit()

    
    




def orderitem():
    
    print("Do you want to see menu available : Enter 1 for yes :")
    ch=int(input("enter your choice :"))               
    if ch==1 :
        sql="select * from restaurent"
        mycursor.execute(sql)
        rows=mycursor.fetchall()
        for x in rows:
            print(x)
    print("Do you want to purchase from above list  [***you can order one item at a time***]:")
    d=int(input("enter your choice:"))
    if(d==1):
        print("you have ordered tea")
        a=int(input("enter quantity"))
        s=10*a
        print("your amount for tea is :",s,"\n")
    elif (d==2):
        print("you have ordered coffee")
        a=int(input("enter quantity"))
        s=10*a
        print("your amount for coffee is :",s,"\n")
    elif(d==3):
        print("you have ordered cold drink")
        a=int(input("enter quantity"))
        s=20*a
        print("your amount for colddrink is :",s,"\n")
    elif(d==4):
        print("you have ordered dhokla")
        a=int(input("enter quantity"))
        s=30*a
        print("your amount for dhokla is :",s,"\n")
    elif(d==5):
        print("you have ordered pasta")
        a=int(input("enter quantity"))
        s=50*a
        print("your amount for pasta is :",s,"\n")
    elif(d==6):
        print("you have ordered samosa")
        a=int(input("enter quantity"))
        s=10*a
        print("your amount for samosa is :",s,"\n")
    elif(d==7):
        print("you have ordered noodles")
        a=int(input("enter quantity"))
        s=40*a
        print("your amount for noodles is :",s,"\n")
    elif(d==8):
        print("you have ordered ice cream")
        a=int(input("enter quantity"))
        s=20*a
        print("your amount for ice cream is :",s,"\n")
    elif(d==9):
        print("you have ordered kachori")
        a=int(input("enter quantity"))
        s=10*a
        print("your amount for kachori is :",s,"\n")
    elif(d==10):
        print("you have ordered milk")
        a=int(input("enter quantity"))
        s=20*a
        print("your amount for milk is :",s,"\n")
    else:
        print("please enter your choice from the menu")


    print("**enter the info for saving data**")    
    amount=input("enter total amount for ordered items:")
    item=input("enter the name of the item ordered:")
    quantity=input("enter the quntity ordered:")
    C_ID=input("enter the customer id of customer  (***room no. rented to customer is customer ID***): ")
    sql="insert into restaurentbilling(item,quantity,amount,C_ID)values('{}','{}','{}','{}')".format(item,quantity,amount,C_ID)
    mycursor.execute(sql)
    mydb.commit()    


def laundarybill():
    
    
    print("Do you want to see rate for laundary : Enter 1 for yes :")       
    ch=int(input("enter your choice:"))
    if ch==1:
        sql="select * from laundary"
        mycursor.execute(sql)
        rows=mycursor.fetchall()
        for x in rows:
             print(x)
    print("Do you want to choose from above list  [***you can choose one item at a time***]:")
    e=int(input("enter your choice:"))
    if(e==1):
        print("you have chosen pant")
        b=int(input("enter quantity"))
        f=50*b
        print("your amount for pants is :",f,"\n")
    elif (e==2):
        print("you have chosen shirts")
        b=int(input("enter quantity"))
        f=70*b
        print("your amount for shirt is :",f,"\n")
    elif(e==3):
        print("you have chosen suit")
        b=int(input("enter quantity"))
        f=90*b
        print("your amount for suit is :",f,"\n")
    elif(e==4):
        print("you have chosen sari")
        b=int(input("enter quantity"))
        f=110*b
        print("your amount for sari is :",f,"\n")
    elif(e==5):
        print("you have chosen others [others include undergarments and jeans]")
        b=int(input("enter quantity"))
        f=150*b
        print("your amount for others is :",f,"\n")
    else:
        print("please enter your choice from the menu")
        

    print("**enter the info for saving data**")
    cname=input("enter the name of the cloth:")     #CLOTH NAME
    quantity=input("enter the quantity of the clothes:")
    price=input("enter the amount for the laundary:")
    C_ID=input("enter the customer id of customer  (***room no. rented to customer is customer ID***): ")
    sql="insert into laundarybill(cname,quantity,price,C_ID)values('{}','{}','{}','{}')".format(cname,quantity,price,C_ID)
    mycursor.execute(sql)
    mydb.commit()


def gaming():

    print("Do you want to see games available : Enter 1 for yes :")       
    ch=int(input("enter your choice:"))
    print(" Sno, Game , No. of players , Price")
    if ch==1:
        sql="select * from gaming"
        mycursor.execute(sql)
        rows=mycursor.fetchall()
        for x in rows:
             print(x)
    print("Do you want to choose from above list  [***you can choose one item at a time***]:")
    z=int(input("enter your choice:"))
    if(z==1):
        print("you have chosen Bowling")
        g=int(input("enter no. of players:"))
        h=700*g
        print("your amount for bowling is :",h,"\n")
    elif (z==2):
        print("you have chosen snooker")
        g=int(input("enter no. of players"))
        h=450*g
        print("your amount for snooker is :",h,"\n")
    elif(z==3):
        print("you have chosen table tennis")
        g=int(input("enter no. of players"))
        h=150*g
        print("your amount for table tennis is :",h,"\n")
    elif(z==4):
        print("you have chosen video games")
        g=int(input("enter no. of players"))
        h=500*g
        print("your amount for video games is :",h,"\n")
    elif(z==5):
        print("you have chosen VR games")
        g=int(input("enter the no. of players"))
        h=1000*g
        print("your amount for VR games is :",h,"\n")
    else:
        print("please enter your choice from the menu")
        

    print("**enter the info for saving data**")
    cname=input("enter the name of the customer:")
    gname=input("enter the name of the game chosen:")
    players=input("enter the no. of players:")
    amount=input("enter the amount for playing games:")
    sql="insert into gamebill(cname,gname,players,amount)values('{}','{}','{}','{}')".format(cname,gname,players,amount)
    mycursor.execute(sql)
    mydb.commit()
             
    


def Menuset():
    print("enter 1 : to select room  and calculating room bill ")
    print("enter 2 : to enter customer data                        [*****select room type and calculate room bill before entering customer data*****]")
    print("enter 3 : for restaurent ")
    print("enter 4 : for laundary ")
    print("enter 5 : for gaming section ")
    
    print("enter 6 : for exit:")
    try:
        userinput=int(input("please select an above option:"))
    except ValueError:
        exit("\n hi thats not a number")

    
    if(userinput==2):
        registercust()
    elif(userinput==1):
        roomrent()
    elif(userinput==3):
        orderitem()
    elif(userinput==4):
        laundarybill()
    elif(userinput==5):
        gaming()
    elif(userinput==6):
        print('                                 *********THANKYOU FOR VISITING**********                                 ')
        quit()
    else:
        print("enter correct choice")
Menuset()


def runagain():
    runagn=input("\n want to run again y/n:")
    while(runagn.lower()=='y'):
        if(platform.system()=="windows"):
            p=0
            
        else:
            li=0
        Menuset()
        runagn=input("\n want to run again y/n:")
runagain()
