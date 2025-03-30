#4.Write a python GUI program to create a pizza application.(Use checkbox,radiobutton,entry,label,image,button).
from tkinter import *
from tkinter import filedialog,messagebox
import random
import time
window=Tk()

var=IntVar()
var1=IntVar()
var2=IntVar()
var.set(0)
var1.set(0)
var2.set(0)

pizzavar=StringVar()
ssdvar=StringVar()
taxvar=StringVar()
totalvar=StringVar()
pizzavar.set('')
ssdvar.set('')
taxvar.set('')
totalvar.set('')

varT1=IntVar()
varT2=IntVar()
varT3=IntVar()
varT4=IntVar()
varT5=IntVar()
varT6=IntVar()
varT7=IntVar()
varT8=IntVar()
varT9=IntVar()
varT10=IntVar()
varT11=IntVar()
varT12=IntVar()
varT13=IntVar()
varT14=IntVar()
varT14=IntVar()
varT15=IntVar()
varT16=IntVar()
varT17=IntVar()
varT18=IntVar()
varT19=IntVar()
varT20=IntVar()
varT21=IntVar()
varT22=IntVar()
varT23=IntVar()
varT24=IntVar()
varT24=IntVar()
varT25=IntVar()
varT26=IntVar()
varT27=IntVar()
varT28=IntVar()
varT29=IntVar()
varT30=IntVar()
varT31=IntVar()
varT32=IntVar()
varT33=IntVar()
varT34=IntVar()
varT34=IntVar()
varT35=IntVar()
varT36=IntVar()
varT37=IntVar()
varT38=IntVar()
varT1.set(0)
varT2.set(0)
varT3.set(0)
varT4.set(0)
varT5.set(0)
varT6.set(0)
varT7.set(0)
varT8.set(0)
varT9.set(0)
varT10.set(0)
varT11.set(0)
varT12.set(0)
varT13.set(0)
varT14.set(0)
varT14.set(0)
varT15.set(0)
varT16.set(0)
varT17.set(0)
varT18.set(0)
varT19.set(0)
varT20.set(0)
varT21.set(0)
varT22.set(0)
varT23.set(0)
varT24.set(0)
varT24.set(0)
varT25.set(0)
varT26.set(0)
varT27.set(0)
varT28.set(0)
varT29.set(0)
varT30.set(0)
varT31.set(0)
varT32.set(0)
varT33.set(0)
varT34.set(0)
varT34.set(0)
varT35.set(0)
varT36.set(0)
varT37.set(0)
varT38.set(0)

window.title("Pizza App")
window.geometry("1821x900")
window.resizable(0,0)
window.config(bg="#b0b7b8")
options = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]

def getState():
   x=clicked.get()
   print(x)

mode=''
Rs_mode=0
def getMode():
   global mode
   global Rs_mode
   choice=var.get()
   if choice==1:
      mode="PickUp"
   elif choice==2:
      mode="Delivery"
      Rs_mode=100
   else:
      mode="Dine-In"
   return messagebox.showinfo('Pizza App', f'You Selected {mode}.')

size=''
Rs_size=0
def getsize():
   global size
   global Rs_size
   choice=var1.get()
   if choice==1:
      size="Small"
      Rs_size=100
   elif choice==2:
      size="Regular"
      Rs_size=150
   elif choice==3:
      size="Medium"
      Rs_size=300
   elif choice==4:
      size="Large"
      Rs_size=600
   elif choice==5:
      size="Giant Slice"
      Rs_size=150
   elif choice==6:
      size="The Giant"
      Rs_size=1000
   elif choice==7:
      size="Monster"
      Rs_size=1500

   

base=''
Rs_base=0
def getbase():
   global base
   global Rs_base
   choice=var2.get()
   if choice==1:
      base="Thin Crust"
      Rs_base=75
   elif choice==2:
      base="Regular"
      Rs_base=0
   elif choice==3:
      base="Cheese Burst"
      Rs_base=150
   elif choice==4:
      base="Pan Crust"
      Rs_base=50
   if choice==5:
      base="Kebab Crust"
      Rs_base=200
   elif choice==6:
      base="San Francisco Style Crust"
      Rs_base=125
   elif choice==7:
      base="Stuffed Crust"
      Rs_base=175

 
pizza=''
Rs_pizza=0
def getpizza():
   global pizza
   global Rs_pizza
   choice=varp1.get()
   if choice==1:
      pizza="Margherita"
      Rs_pizza=50
   elif choice==2:
      pizza="Double Cheese Margherita"
      Rs_pizza=125
   elif choice==3:
      pizza="Fresh Veggie"
      Rs_pizza=100
   elif choice==4:
      pizza="Mexican Green Wave"
      Rs_pizza=160
   if choice==5:
      pizza="5 Pepper"
      Rs_pizza=160
   elif choice==6:
      pizza="Deluxe Veggie"
      Rs_pizza=150
   elif choice==7:
      pizza="Veg Extravaganza"
      Rs_pizza=300
   elif choice==8:
      pizza="Farmhouse"
      Rs_pizza=125

   
#topping/extras func
t4=''
Rs_t4=0
def e4():
   global t4
   global Rs_t4
   x=varT4.get()
   if x==1:
      t4="Onions"
      Rs_t4=10

t5=''
Rs_t5=0
def e5():
   global t5
   global Rs_t5
   x=varT5.get()
   if x==1:
      t5="Spinach"
      Rs_t5=15

t6=''
Rs_t6=0
def e6():
   global t6
   global Rs_t6
   x=varT6.get()
   if x==1:
      t6="Black Olives"
      Rs_t6=12

t7=''
Rs_t7=0
def e7():
   global t7
   global Rs_t7
   x=varT7.get()
   if x==1:
      t7="Mushrooms"
      Rs_t7=20

t8=''
Rs_t8=0
def e8():
   global t8
   global Rs_t8
   x=varT8.get()
   if x==1:
      t8="Panner"
      Rs_t8=30

t9=''
Rs_t9=0
def e9():
   global t9
   global Rs_t9
   x=varT9.get()
   if x==1:
      t9="Olives"
      Rs_t9=12

t10=''
Rs_t10=0
def e10():
   global t10
   global Rs_t10
   x=varT10.get()
   if x==1:
      t10="Pesto"
      Rs_t10=5

t11=''
Rs_t11=0
def e11():
   global t11
   global Rs_t11
   x=varT11.get()
   if x==1:
      t11="Jalapenoes"
      Rs_t11=8

t12=''
Rs_t12=0
def e12():
   global t12
   global Rs_t12
   x=varT12.get()
   if x==1:
      t12="Red Paprika"
      Rs_t12=8

t13=''
Rs_t13=0
def e13():
   global t13
   global Rs_t13
   x=varT13.get()
   if x==1:
      t13="Pepproni"
      Rs_t13=75

t14=''
Rs_t14=0
def e14():
   global t14
   global Rs_t14
   x=varT14.get()
   if x==1:
      t14="Sausage"
      Rs_t14=70

t15=''
Rs_t15=0
def e15():
   global t15
   global Rs_t15
   x=varT15.get()
   if x==1:
      t15="Bacon"
      Rs_t15=50

t16=''
Rs_t16=0
def e16():
   global t16
   global Rs_t16
   x=varT16.get()
   if x==1:
      t16="Chicken"
      Rs_t16=70

t17=''
Rs_t17=0
def e17():
   global t17
   global Rs_t17
   x=varT17.get()
   if x==1:
      t17="Ham"
      Rs_t17=85

t18=''
Rs_t18=0
def e18():
   global t18
   global Rs_t18
   x=varT18.get()
   if x==1:
      t18="Thumbs up"
      Rs_t18=40

t19=''
Rs_t19=0
def e19():
   global t19
   global Rs_t19
   x=varT19.get()
   if x==1:
      t19="Coke"
      Rs_t19=40

t20=''
Rs_t20=0
def e20():
   global t20
   global Rs_t20
   x=varT20.get()
   if x==1:
      t20="Fanta"
      Rs_t20=45

t21=''
Rs_t21=0
def e21():
   global t21
   global Rs_t21
   x=varT21.get()
   if x==1:
      t21="Mountain Dew"
      Rs_t21=45

t22=''
Rs_t22=0
def e22():
   global t22
   global Rs_t22
   x=varT22.get()
   if x==1:
      t22="Sprite"
      Rs_t22=40

t23=''
Rs_t23=0
def e23():
   global t23
   global Rs_t23
   x=varT23.get()
   if x==1:
      t23="Maaza"
      Rs_t23=50

t24=''
Rs_t24=0
def e24():
   global t24
   global Rs_t24
   x=varT24.get()
   if x==1:
      t24="7 Up"
      Rs_t24=40

t25=''
Rs_t25=0
def e25():
   global t25
   global Rs_t25
   x=varT25.get()
   if x==1:
      t25="Cheese Dip"
      Rs_t25=20
     
t26=''
Rs_t26=0
def e26():
   global t26
   global Rs_t26
   x=varT26.get()
   if x==1:
      t26="Jalapeño Dip"
      Rs_t26=20

t27=''
Rs_t27=0
def e27():
   global t27
   global Rs_t27
   x=varT27.get()
   if x==1:
      t27="Garlic Dip"
      Rs_t27=20

t28=''
Rs_t28=0
def e28():
   global t28
   global Rs_t28
   x=varT28.get()
   if x==1:
      t28="Sweet Chilli Dip"
      Rs_t28=20

t29=''
Rs_t29=0
def e29():
   global t29
   global Rs_t29
   x=varT29.get()
   if x==1:
      t29="Thousand Island Dip"
      Rs_t29=20

t30=''
Rs_t30=0
def e30():
   global t30
   global Rs_t30
   x=varT30.get()
   if x==1:
      t30="Chilli Sauce"
      Rs_t30=20

t31=''
Rs_t31=0
def e31():
   global t31
   global Rs_t31
   x=varT31.get()
   if x==1:
      t31="Mustard"
      Rs_t31=20

t32=''
Rs_t32=0
def e32():
   global t32
   global Rs_t32
   x=varT32.get()
   if x==1:
      t32="Garlic bread"
      Rs_t32=99

t33=''
Rs_t33=0
def e33():
   global t33
   global Rs_t33
   x=varT33.get()
   if x==1:
      t33="Cheese Garlic bread"
      Rs_t33=149

t34=''
Rs_t34=0
def e34():
   global t34
   global Rs_t34
   x=varT34.get()
   if x==1:
      t34="Stuffed Garlic bread"
      Rs_t34=179

t35=''
Rs_t35=0
def e35():
   global t35
   global Rs_t35
   x=varT35.get()
   if x==1:
      t35="Mac & Cheese"
      Rs_t35=109

t36=''
Rs_t36=0
def e36():
   global t36
   global Rs_t36
   x=varT36.get()
   if x==1:
      t36="Smoke Chili Mac&Chesee"
      Rs_t36=129
t37=''
Rs_t37=0
def e37():
   global t37
   global Rs_t37
   x=varT37.get()
   if x==1:
      t37="Arrabiata Sauce Pasta"
      Rs_t37=159

t38=''
Rs_t38=0
def e38():
   global t38
   global Rs_t38
   x=varT38.get()
   if x==1:
      t38="Mexican Taco"
      Rs_t38=99
tt=''
tr=0
def toma():
   global tt
   global tr
   x=varT1.get()
   if x==1:
      tt="Tomatoes"
      tr=10

tct=''
tcr=0
def pepe():
   global tct
   global tcr
   x=varT2.get()
   if x==1:
      tct="Pepper"
      tcr=9

tcc=''
tccr=0
def caps():
   global tcc
   global tccr
   x=varT3.get()
   if x==1:
      tcc="Capsicum"
      tccr=10


def total():
   textCostofFood.delete(0,END)
   textCostofSDD.delete(0,END)
   textTax.delete(0,END)
   textTotalCost.delete(0,END)  
   pizzavar.set('')
   ssdvar.set('')
   taxvar.set('')
   totalvar.set('')
   global costpizza,costSSD,tax,totalval
   costpizza=Rs_pizza+Rs_base+Rs_size
   pizzavar.set(str(costpizza)+ ' Rs')

   costSSD=tr + tcr + tccr + Rs_t4 + Rs_t5 + Rs_t6 + Rs_t7 + Rs_t8 + Rs_t9 + Rs_t10 + Rs_t11 + Rs_t12 + Rs_t13 + Rs_t14 + Rs_t15 + Rs_t16 + Rs_t17 + Rs_t18 + Rs_t19+ Rs_t20 + Rs_t21 + Rs_t22 + Rs_t23 + Rs_t24 + Rs_t25 + Rs_t26 + Rs_t27 + Rs_t28 + Rs_t29+ Rs_t30 + Rs_t31 + Rs_t32 + Rs_t33 + Rs_t34 + Rs_t35 + Rs_t36 + Rs_t37 + Rs_t38
   ssdvar.set(str(costSSD)+ ' Rs')

   atx=(costpizza+costSSD)*0.18
   tax=round(atx,2)
   taxvar.set(str(tax)+ ' Rs')

   totalval=tax+costSSD+costpizza+Rs_mode
   totalvar.set(str(totalval)+ ' Rs')
 


def receipt():
   global costpizza,costSSD,tax,totalval
   custName=e1.get()
   email=e2.get()
   phno=e3.get()
   ad1=a1.get()
   ad2=a2.get()
   ad3=a3.get()
   ad4=a4.get()
   ad5=clicked.get()
   global mode
   global Rs_mode
   global base
   global pizza
   global Rs_pizza
   global size
   global Rs_size
   global base
   global Rs_base
   if custName == '' or email == '' or phno=='' or ad1=='' or ad2=='' or ad3=='' or ad4=='' :
      textReceipt.insert(END,"Above Entry is/are empty")
   else:
      textReceipt.insert(END,base)
      textReceipt.delete(1.0,END)
      x=random.randint(100,10000)
      billnumber='BILL'+str(x)
      date=time.strftime('%d/%m/%Y')
      if var.get()==2:
          textReceipt.insert(END,f"Mode:{mode}  {Rs_mode}Rs")
      else:
          textReceipt.insert(END,f"Mode:{mode}")
      textReceipt.insert(END,'\nReceipt Ref:\t'+billnumber+'\t\t\t\t\t   '+date+'\n')
      textReceipt.insert(END,'****************************************************************************************\n')
      textReceipt.insert(END,f"Customer Name: {custName}")
      textReceipt.insert(END,f"\nEmail ID: {email}")
      textReceipt.insert(END,f"\nPhone No.: {phno}")
      textReceipt.insert(END,f"\n***************************************ADDRESS************************************\n{ad1},{ad2},{ad3}-{ad4},{ad5}\n")
      textReceipt.insert(END,'****************************************************************************************\n')
      textReceipt.insert(END,f"Pizza: {pizza}\t\t\t\t{Rs_pizza}Rs")
      textReceipt.insert(END,f"\n{size} Size\t\t\t\t{Rs_size}Rs")
      textReceipt.insert(END,f"\n{base}\t\t\t\t{Rs_base}Rs\n")
      textReceipt.insert(END,'****************************************************************************************\n')
      textReceipt.insert(END,"Extra-Toppings/Sides/Drinks :\n")
      if varT1.get()==1:
          textReceipt.insert(END,f'{tt}\t\t\t\t{tr}Rs\n')
      if varT2.get()==1:
          textReceipt.insert(END,f'{tct}\t\t\t\t{tcr}Rs\n')
      if varT3.get()==1:
          textReceipt.insert(END,f'{tcc}\t\t\t\t{tccr}Rs\n')      
      if varT4.get()==1:
          textReceipt.insert(END,f'{t4}\t\t\t\t{Rs_t4}Rs\n')
      if varT5.get()==1:
          textReceipt.insert(END,f'{t5}\t\t\t\t{Rs_t5}Rs\n')
      if varT6.get()==1:
          textReceipt.insert(END,f'{t6}\t\t\t\t{Rs_t6}Rs\n')
      if varT7.get()==1:
          textReceipt.insert(END,f'{t7}\t\t\t\t{Rs_t7}Rs\n')
      if varT8.get()==1:
          textReceipt.insert(END,f'{t8}\t\t\t\t{Rs_t8}Rs\n')
      if varT9.get()==1:
          textReceipt.insert(END,f'{t9}\t\t\t\t{Rs_t9}Rs\n')
      if varT10.get()==1:
          textReceipt.insert(END,f'{t10}\t\t\t\t{Rs_t10}Rs\n')
      if varT11.get()==1:
          textReceipt.insert(END,f'{t11}\t\t\t\t{Rs_t11}Rs\n')
      if varT12.get()==1:
          textReceipt.insert(END,f'{t12}\t\t\t\t{Rs_t12}Rs\n')
      if varT13.get()==1:
          textReceipt.insert(END,f'{t13}\t\t\t\t{Rs_t13}Rs\n')
      if varT14.get()==1:
          textReceipt.insert(END,f'{t14}\t\t\t\t{Rs_t14}Rs\n')
      if varT15.get()==1:
          textReceipt.insert(END,f'{t15}\t\t\t\t{Rs_t15}Rs\n')
      if varT16.get()==1:
          textReceipt.insert(END,f'{t16}\t\t\t\t{Rs_t16}Rs\n')
      if varT17.get()==1:
          textReceipt.insert(END,f'{t17}\t\t\t\t{Rs_t17}Rs\n')
      if varT18.get()==1:
          textReceipt.insert(END,f'{t18}\t\t\t\t{Rs_t18}Rs\n')
      if varT19.get()==1:
          textReceipt.insert(END,f'{t19}\t\t\t\t{Rs_t19}Rs\n')
      if varT20.get()==1:
          textReceipt.insert(END,f'{t20}\t\t\t\t{Rs_t20}Rs\n')
      if varT21.get()==1:
          textReceipt.insert(END,f'{t21}\t\t\t\t{Rs_t21}Rs\n')
      if varT22.get()==1:
          textReceipt.insert(END,f'{t22}\t\t\t\t{Rs_t22}Rs\n')
      if varT23.get()==1:
          textReceipt.insert(END,f'{t23}\t\t\t\t{Rs_t23}Rs\n')
      if varT24.get()==1:
          textReceipt.insert(END,f'{t24}\t\t\t\t{Rs_t24}Rs\n')
      if varT25.get()==1:
          textReceipt.insert(END,f'{t25}\t\t\t\t{Rs_t25}Rs\n')
      if varT26.get()==1:
          textReceipt.insert(END,f'{t26}\t\t\t\t{Rs_t26}Rs\n')
      if varT27.get()==1:
          textReceipt.insert(END,f'{t27}\t\t\t\t{Rs_t27}Rs\n')
      if varT28.get()==1:
          textReceipt.insert(END,f'{t28}\t\t\t\t{Rs_t28}Rs\n')
      if varT29.get()==1:
          textReceipt.insert(END,f'{t29}\t\t\t\t{Rs_t29}Rs\n')
      if varT30.get()==1:
          textReceipt.insert(END,f'{t30}\t\t\t\t{Rs_t30}Rs\n')
      if varT31.get()==1:
          textReceipt.insert(END,f'{t31}\t\t\t\t{Rs_t31}Rs\n')
      if varT32.get()==1:
          textReceipt.insert(END,f'{t32}\t\t\t\t{Rs_t32}Rs\n')
      if varT33.get()==1:
          textReceipt.insert(END,f'{t33}\t\t\t\t{Rs_t33}Rs\n')
      if varT34.get()==1:
          textReceipt.insert(END,f'{t34}\t\t\t\t{Rs_t34}Rs\n')
      if varT35.get()==1:
          textReceipt.insert(END,f'{t35}\t\t\t\t{Rs_t35}Rs\n')
      if varT36.get()==1:
          textReceipt.insert(END,f'{t36}\t\t\t\t{Rs_t36}Rs\n')
      if varT37.get()==1:
          textReceipt.insert(END,f'{t37}\t\t\t\t{Rs_t37}Rs\n')
      if varT38.get()==1:
          textReceipt.insert(END,f'{t38}\t\t\t\t{Rs_t38}Rs\n')
      textReceipt.insert(END,'\n****************************************************************************************\n')
      textReceipt.insert(END,f"Total Cost of Pizza = {costpizza}Rs\n")
      textReceipt.insert(END,'****************************************************************************************\n')
      textReceipt.insert(END,f"Total Cost of Sides/Toppings/Drinks = {costSSD}Rs\n")
      textReceipt.insert(END,'****************************************************************************************\n')
      textReceipt.insert(END,f"Total Tax = {tax}Rs\n")
      textReceipt.insert(END,'****************************************************************************************\n')
      textReceipt.insert(END,'****************************************************************************************\n')
      textReceipt.insert(END,f"TOTAL COST = {totalval}Rs\n")
      textReceipt.insert(END,'****************************************************************************************\n')
      textReceipt.insert(END,'****************************************************************************************\n')


      
   


def save():
    if textReceipt.get(1.0,END)=='\n':
        pass
    else:
        url=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
        if url==None:
            pass
        else:

            bill_data=textReceipt.get(1.0,END)
            url.write(bill_data)
            url.close()
            messagebox.showinfo('Information','Your Bill Is Succesfully Saved')


def reset():
   var.set(None)
   var1.set(None)
   var2.set(None)
   varp1.set(None)
   e1.delete(0,END)
   e2.delete(0,END)
   e3.delete(0,END)
   a1.delete(0,END)
   a2.delete(0,END)
   a3.delete(0,END)
   a4.delete(0,END)
   clear()
   varT1.set(0)
   varT2.set(0)
   varT3.set(0)
   varT4.set(0)
   varT5.set(0)
   varT6.set(0)
   varT7.set(0)
   varT8.set(0)
   varT9.set(0)
   varT10.set(0)
   varT11.set(0)
   varT12.set(0)
   varT13.set(0)
   varT14.set(0)
   varT14.set(0)
   varT15.set(0)
   varT16.set(0)
   varT17.set(0)
   varT18.set(0)
   varT19.set(0)
   varT20.set(0)
   varT21.set(0)
   varT22.set(0)
   varT23.set(0)
   varT24.set(0)
   varT24.set(0)
   varT25.set(0)
   varT26.set(0)
   varT27.set(0)
   varT28.set(0)
   varT29.set(0)
   varT30.set(0)
   varT31.set(0)
   varT32.set(0)
   varT33.set(0)
   varT34.set(0)
   varT34.set(0)
   varT35.set(0)
   varT36.set(0)
   varT37.set(0)
   varT38.set(0)
   pizzavar.set('')
   ssdvar.set('')
   taxvar.set('')
   totalvar.set('')
   


TopF=Frame(window,bd=10,relief="ridge")
TopF.pack(side=TOP)
Cinfo=Frame(TopF,bd=10,relief="ridge",bg="#b0b7b8")
Cinfo.pack(side=LEFT)
Pinfo=Frame(TopF,bd=10,relief="ridge",bg="#b0b7b8")
Pinfo.pack(side=LEFT)
Rinfo=Frame(TopF,bd=10,relief="ridge",bg="#b0b7b8")
Rinfo.pack(side=LEFT)
Ainfo=Frame(TopF,bd=10,relief="ridge",bg="#b0b7b8")
Ainfo.pack(side=LEFT)


Plabel_top=Label(Pinfo,text="Customer Details",font=('Arial',23,'bold','italic'),fg="black",bg="#b0b7b8",bd=10)
Plabel_top.grid(row=1,column=1)
Rlabel_top=Label(Rinfo,text="ABC's Pizza Ordering App",font=('Arial',45,'bold','italic'),fg="black",bg="#b0b7b8",bd=20)
Rlabel_top.grid(row=0,column=0,pady=19)


pname = Label(Pinfo, text = "Full Name:",font=('Arial',15,'italic','bold'),fg="black",bg="#b0b7b8")
pemail = Label(Pinfo, text = "Email:",font=('Arial',15,'italic','bold'),fg="black",bg="#b0b7b8")
pmNo = Label(Pinfo, text = "Phone No.:",font=('Arial',15,'italic','bold'),fg="black",bg="#b0b7b8")
pname.grid(row = 2, column = 0)
pemail.grid(row = 3, column = 0)
pmNo.grid(row = 4, column = 0)
e1 = Entry(Pinfo,width=20,font=('Arial',12,'bold'))
e2 = Entry(Pinfo,width=27,font=('Arial',12,'bold'))
e3 = Entry(Pinfo,width=12,font=('Arial',12,'bold'))
e1.grid(row = 2, column = 1, pady = 2)
e2.grid(row = 3, column = 1, pady = 2)
e3.grid(row = 4, column = 1, pady = 2)


add1 = Label(Ainfo, text = " Address Line: ",font=('Arial',15,'italic','bold'),fg="black",bg="#b0b7b8")
add2 = Label(Ainfo, text = " Address Line2: ",font=('Arial',15,'italic','bold'),fg="black",bg="#b0b7b8")
add3 = Label(Ainfo, text = "City:",font=('Arial',15,'italic','bold'),fg="black",bg="#b0b7b8")
add4 = Label(Ainfo, text = "Pincode:",font=('Arial',15,'italic','bold'),fg="black",bg="#b0b7b8")
add1.grid(row = 1, column = 0,pady=5)
add2.grid(row = 2, column = 0,pady=3)
add3.grid(row = 3, column = 0,pady=3)
add4.grid(row = 4, column = 0,pady=3)
a1 = Entry(Ainfo,width=27,font=('Arial',12,'bold'))
a2 = Entry(Ainfo,width=27,font=('Arial',12,'bold'))
a3 = Entry(Ainfo,width=25,font=('Arial',12,'bold'))
a4 = Entry(Ainfo,width=20,font=('Arial',12,'bold'))
a1.grid(row = 1, column = 1, pady = 2)
a2.grid(row = 2, column = 1, pady = 2)
a3.grid(row = 3, column = 1, pady = 2) 
a4.grid(row = 4, column = 1, pady = 2) 

c1=Radiobutton(Cinfo, text="Pickup",value=1,variable=var,command=getMode,bg="#b0b7b8",font=('Arial',14,'italic','bold'))
c1.pack( anchor = W )
c2=Radiobutton(Cinfo, text="Delivery",value=2,variable=var,command=getMode,bg="#b0b7b8",font=('Arial',14,'italic','bold'))
c2.pack( anchor = W )
c3=Radiobutton(Cinfo, text="Dine-In",value=3,variable=var,command=getMode,bg="#b0b7b8",font=('Arial',14,'italic','bold'))
c3.pack( anchor = W )


state = Label(Cinfo, text = "State  ",font=('Arial',13,'bold'),fg="black",bg="#b0b7b8",height=2)
state.pack(side=LEFT)
clicked = StringVar()
clicked.set( "Gujarat" )
drop = OptionMenu( Cinfo ,clicked, *options)
drop.pack(side=LEFT)

#RIGHTFrame
rightFrame=Frame(window,bd=15,relief=RIDGE,bg='white')
rightFrame.pack(side=RIGHT)

recieptFrame=Frame(rightFrame,bd=4,relief=RIDGE,bg='black')
recieptFrame.pack(padx=1)
textReceipt=Text(recieptFrame,font=('arial',12,'bold'),bd=2,width=59,height=32)
textReceipt.grid(row=0,column=0)

buttonFrame=Frame(rightFrame,bd=3,relief=RIDGE,bg='black')
buttonFrame.pack(pady=8)
buttonTotal=Button(buttonFrame,text='Total',font=('arial',14,'bold'),fg='white',bg='blue',bd=3,padx=5,command=total)
buttonTotal.grid(row=0,column=1)
buttonReceipt=Button(buttonFrame,text='Receipt',font=('arial',14,'bold'),fg='white',bg='blue',bd=3,padx=5,command=receipt)
buttonReceipt.grid(row=0,column=2)
buttonSave=Button(buttonFrame,text='Save',font=('arial',14,'bold'),fg='white',bg='blue',bd=3,padx=5,command=save)
buttonSave.grid(row=0,column=3)
buttonReset=Button(buttonFrame,text='Reset',font=('arial',14,'bold'),fg='white',bg='blue',bd=3,padx=5,command=reset)
buttonReset.grid(row=0,column=4)



#Main Frame

Main=Frame(window,bd=10,relief="ridge",bg="white")
Main.pack(side=TOP)
varp1=IntVar()
pizza=LabelFrame(Main,text="Pizzas",relief="ridge",bg="#32a8a2",font=('Arial',20,'italic','bold'),fg='white')
pizza.pack(side=LEFT)
p1=Radiobutton(pizza, text="Margherita",value=1,variable=varp1,bg="#32a8a2",font=('Arial',14,'italic','bold'),fg='blue',command=getpizza)
p1.pack( anchor = W )
p2=Radiobutton(pizza, text="Double Cheese Margherita",value=2,variable=varp1,bg="#32a8a2",font=('Arial',14,'italic','bold'),fg='blue',command=getpizza)
p2.pack( anchor = W )
p3=Radiobutton(pizza, text="Fresh Veggie",value=3,variable=varp1,bg="#32a8a2",font=('Arial',14,'italic','bold'),fg='blue',command=getpizza)
p3.pack( anchor = W )
p4=Radiobutton(pizza, text="Mexican Green Wave",value=4,variable=varp1,bg="#32a8a2",font=('Arial',14,'italic','bold'),fg='blue',command=getpizza)
p4.pack( anchor = W )
p5=Radiobutton(pizza, text="5 Pepper",value=5,variable=varp1,bg="#32a8a2",font=('Arial',14,'italic','bold'),fg='blue',command=getpizza)
p5.pack( anchor = W )
p6=Radiobutton(pizza, text="Deluxe Veggie",value=6,variable=varp1,bg="#32a8a2",font=('Arial',14,'italic','bold'),fg='blue',command=getpizza)
p6.pack( anchor = W )
p7=Radiobutton(pizza, text="Veg Extravaganza",value=7,variable=varp1,bg="#32a8a2",font=('Arial',14,'italic','bold'),fg='blue',command=getpizza)
p7.pack( anchor = W )
p8=Radiobutton(pizza, text="Farmhouse",value=8,variable=varp1,bg="#32a8a2",font=('Arial',14,'italic','bold'),fg='blue',command=getpizza)
p8.pack( anchor = W )

customize=LabelFrame(Main,text="Customize",relief="ridge",bg="#32a8a2",font=('Arial',20,'italic','bold'),fg='white')
customize.pack()

size=LabelFrame(customize,bd=9,relief="ridge",bg="#32a8a2",fg='white',text="Size",font=('Arial',15,'italic','bold'))
size.pack(side=LEFT)
s1=Radiobutton(size, text="Small",value=1,variable=var1,bg="#32a8a2",font=('Arial',14,'italic','bold'),fg='blue',command=getsize)
s1.pack( anchor = W )
s2=Radiobutton(size, text="Regular",value=2,variable=var1,bg="#32a8a2",font=('Arial',14,'italic','bold'),fg='blue',command=getsize)
s2.pack( anchor = W )
s3=Radiobutton(size, text="Medium",value=3,variable=var1,bg="#32a8a2",font=('Arial',14,'italic','bold'),fg='blue',command=getsize)
s3.pack( anchor = W )
s4=Radiobutton(size, text="Large",value=4,variable=var1,bg="#32a8a2",font=('Arial',14,'italic','bold'),fg='blue',command=getsize)
s4.pack( anchor = W )
s5=Radiobutton(size, text="Giant Slice",value=5,variable=var1,bg="#32a8a2",font=('Arial',14,'italic','bold'),fg='blue',command=getsize)
s5.pack( anchor = W )
s6=Radiobutton(size, text="The Giant",value=6,variable=var1,bg="#32a8a2",font=('Arial',14,'italic','bold'),fg='blue',command=getsize)
s6.pack( anchor = W )
s7=Radiobutton(size, text="Monster",value=7,variable=var1,bg="#32a8a2",font=('Arial',14,'italic','bold'),fg='blue',command=getsize)
s7.pack( anchor = W )

base=LabelFrame(customize,text="Base",bd=9,relief="ridge",bg="#32a8a2",font=('Arial',15,'italic','bold'),fg='white')
base.pack(side=LEFT)
b1=Radiobutton(base, text="Thin Crust",value=1,variable=var2,bg="#32a8a2",font=('Arial',14,'italic','bold'),fg='blue',command=getbase)
b1.pack( anchor = W )
b2=Radiobutton(base, text="Regular",value=2,variable=var2,bg="#32a8a2",font=('Arial',14,'italic','bold'),fg='blue',command=getbase)
b2.pack( anchor = W )
b3=Radiobutton(base, text="Cheese Burst",value=3,variable=var2,bg="#32a8a2",font=('Arial',14,'italic','bold'),fg='blue',command=getbase)
b3.pack( anchor = W )
b4=Radiobutton(base, text="Pan Crust",value=4,variable=var2,bg="#32a8a2",font=('Arial',14,'italic','bold'),fg='blue',command=getbase)
b4.pack( anchor = W )
b5=Radiobutton(base, text="Kebab Crust",value=5,variable=var2,bg="#32a8a2",font=('Arial',14,'italic','bold'),fg='blue',command=getbase)
b5.pack( anchor = W )
b6=Radiobutton(base, text="San Francisco Style Crust",value=6,variable=var2,bg="#32a8a2",font=('Arial',14,'italic','bold'),fg='blue',command=getbase)
b6.pack( anchor = W )
b7=Radiobutton(base, text="Stuffed Crust",value=7,variable=var2,bg="#32a8a2",font=('Arial',14,'italic','bold'),fg='blue',command=getbase)
b7.pack( anchor = W )


topping=LabelFrame(customize,text="Extra Toppings",bd=10,relief="ridge",bg="#32a8a2",font=('Arial',15,'italic','bold'),fg='white')
topping.pack(side=RIGHT)


#veg-nonveg label
veg=Label(topping,text="Veg Toppings",font=('Arial',14,'bold'),fg='white',bg="#32a8a2")
veg.grid(row=0,column=0,columnspan=2,pady=6)
nveg=Label(topping,text="Non-Veg Toppings",font=('Arial',14,'bold'),fg='white',bg="#32a8a2")
nveg.grid(row=0,column=2,columnspan=2)
#veg
tomato=Checkbutton(topping,text="Tomatoes",font=('Arial',14,'bold'),fg='blue',variable=varT1,bg="#32a8a2",command=toma)
tomato.grid(row=1,column=0,sticky=W)
pepper=Checkbutton(topping,text="Peppers",font=('Arial',14,'bold'),fg='blue',variable=varT2,bg="#32a8a2",command=pepe)
pepper.grid(row=1,column=1,sticky=W)
capsicum=Checkbutton(topping,text="Capsicum",font=('Arial',14,'bold'),fg='blue',variable=varT3,bg="#32a8a2",command=caps)
capsicum.grid(row=2,column=0,sticky=W)
onion=Checkbutton(topping,text="Onions",font=('Arial',14,'bold'),fg='blue',onvalue=1,offvalue=0,variable=varT4,bg="#32a8a2",command=e4)
onion.grid(row=2,column=1,sticky=W)
Spinach=Checkbutton(topping,text="Spinach",font=('Arial',14,'bold'),fg='blue',onvalue=1,offvalue=0,variable=varT5,bg="#32a8a2",command=e5)
Spinach.grid(row=3,column=0,sticky=W)
black_olive=Checkbutton(topping,text="Black Olives",font=('Arial',14,'bold'),fg='blue',onvalue=1,offvalue=0,variable=varT6,bg="#32a8a2",command=e6)
black_olive.grid(row=3,column=1,sticky=W)
Mushrooms=Checkbutton(topping,text="Mushrooms",font=('Arial',14,'bold'),fg='blue',onvalue=1,offvalue=0,variable=varT7,bg="#32a8a2",command=e7)
Mushrooms.grid(row=4,column=0,sticky=W)
panner=Checkbutton(topping,text="Panner",font=('Arial',14,'bold'),fg='blue',onvalue=1,offvalue=0,variable=varT8,bg="#32a8a2",command=e8)
panner.grid(row=4,column=1,sticky=W)
Olives=Checkbutton(topping,text="Olives",font=('Arial',14,'bold'),fg='blue',onvalue=1,offvalue=0,variable=varT9,bg="#32a8a2",command=e9)
Olives.grid(row=5,column=0,sticky=W)
pesto=Checkbutton(topping,text="Pesto",font=('Arial',14,'bold'),fg='blue',onvalue=1,offvalue=0,variable=varT10,bg="#32a8a2",command=e10)
pesto.grid(row=5,column=1,sticky=W)
jalapeño=Checkbutton(topping,text="Jalapeño",font=('Arial',14,'bold'),fg='blue',onvalue=1,offvalue=0,variable=varT11,bg="#32a8a2",command=e11)
jalapeño.grid(row=6,column=0,sticky=W)
paprika=Checkbutton(topping,text="Red Paprika",font=('Arial',14,'bold'),fg='blue',onvalue=1,offvalue=0,variable=varT12,bg="#32a8a2",command=e12)
paprika.grid(row=6,column=1,sticky=W)

#non-veg
Pepperoni=Checkbutton(topping,text="Pepperoni ",font=('Arial',14,'bold'),fg='blue',onvalue=1,offvalue=0,variable=varT13,bg="#32a8a2",command=e13)
Pepperoni.grid(row=1,column=3,sticky=W)
sausage=Checkbutton(topping,text="Sausage",font=('Arial',14,'bold'),fg='blue',onvalue=1,offvalue=0,variable=varT14,bg="#32a8a2",command=e14)
sausage.grid(row=2,column=3,sticky=W)
Bacon=Checkbutton(topping,text="Bacon",font=('Arial',14,'bold'),fg='blue',onvalue=1,offvalue=0,variable=varT15,bg="#32a8a2",command=e15)
Bacon.grid(row=3,column=3,sticky=W)
chicken=Checkbutton(topping,text="Chicken",font=('Arial',14,'bold'),fg='blue',onvalue=1,offvalue=0,variable=varT16,bg="#32a8a2",command=e16)
chicken.grid(row=4,column=3,sticky=W)
ham=Checkbutton(topping,text="Ham",font=('Arial',14,'bold'),fg='blue',onvalue=1,offvalue=0,variable=varT17,bg="#32a8a2",command=e17)
ham.grid(row=5,column=3,sticky=W)
#at start toppings are unselected
tomato.deselect()
pepper.deselect()
capsicum.deselect()
onion.deselect()
Spinach.deselect()
black_olive.deselect()
Mushrooms.deselect()
panner.deselect()
Olives.deselect()
pesto.deselect()
jalapeño.deselect()
paprika.deselect()
Pepperoni.deselect()
sausage.deselect()
Bacon.deselect()
chicken.deselect()
ham.deselect()



#Bottom Frame
bottomframe=Frame(window,bd=5,relief=RIDGE)
bottomframe.pack(side=BOTTOM)
btframe=Frame(bottomframe,bd=1)
btframe.pack(side=TOP,padx=30,pady=16)
bbframe=Frame(bottomframe,bd=1)
bbframe.pack(side=TOP,padx=46)

drink=LabelFrame(btframe,text="Drinks",bd=10,relief=RIDGE,fg="blue",font=('arial',16,'bold'))
drink.pack(side=RIGHT,padx=2)
thumbsup=Checkbutton(drink,text="Thumbs Up",font=('Arial',14,'bold'),fg='blue',onvalue=1,offvalue=0,variable=varT18,command=e18)
thumbsup.grid(row=0,column=0,sticky=W)
coke=Checkbutton(drink,text="Coke",font=('Arial',14,'bold'),fg='blue',onvalue=1,offvalue=0,variable=varT19,command=e19)
coke.grid(row=1,column=0,sticky=W)
fanta=Checkbutton(drink,text="Fanta",font=('Arial',14,'bold'),fg='blue',onvalue=1,offvalue=0,variable=varT20,command=e20)
fanta.grid(row=2,column=0,sticky=W)
mountaindew=Checkbutton(drink,text="Mountain Dew",font=('Arial',14,'bold'),fg='blue',onvalue=1,offvalue=0,variable=varT21,command=e21)
mountaindew.grid(row=3,column=0,sticky=W)
sprite=Checkbutton(drink,text="Sprite",font=('Arial',14,'bold'),fg='blue',onvalue=1,offvalue=0,variable=varT22,command=e22)
sprite.grid(row=4,column=0,sticky=W)
maaza=Checkbutton(drink,text="Maaza",font=('Arial',14,'bold'),fg='blue',onvalue=1,offvalue=0,variable=varT23,command=e23)
maaza.grid(row=5,column=0,sticky=W)
up7=Checkbutton(drink,text="7 Up",font=('Arial',14,'bold'),fg='blue',onvalue=1,offvalue=0,variable=varT24,command=e24)
up7.grid(row=6,column=0,sticky=W)

dip=LabelFrame(btframe,text="Dips",bd=10,relief=RIDGE,fg="blue",font=('arial',16,'bold'))
dip.pack(side=RIGHT,padx=2)
cheseed=Checkbutton(dip,text="Chesee Dip",font=('Arial',14,'bold'),fg='blue',onvalue=1,offvalue=0,variable=varT25,command=e25)
cheseed.grid(row=0,column=0,sticky=W)
jalapeñod=Checkbutton(dip,text="Jalapeño Dip",font=('Arial',14,'bold'),fg='blue',onvalue=1,offvalue=0,variable=varT26,command=e26)
jalapeñod.grid(row=1,column=0,sticky=W)
garlicd=Checkbutton(dip,text="Garlic Dip",font=('Arial',14,'bold'),fg='blue',onvalue=1,offvalue=0,variable=varT27,command=e27)
garlicd.grid(row=2,column=0,sticky=W)
sweetchillid=Checkbutton(dip,text="Sweet Chilli Dip",font=('Arial',14,'bold'),fg='blue',onvalue=1,offvalue=0,variable=varT28,command=e28)
sweetchillid.grid(row=4,column=0,sticky=W)
thousandislandd=Checkbutton(dip,text="Thousand Island Dip",font=('Arial',14,'bold'),fg='blue',onvalue=1,offvalue=0,variable=varT29,command=e29)
thousandislandd.grid(row=5,column=0,sticky=W)
chillis=Checkbutton(dip,text="Chilli Sauce",font=('Arial',14,'bold'),fg='blue',onvalue=1,offvalue=0,variable=varT30,command=e30)
chillis.grid(row=6,column=0,sticky=W)
mustard=Checkbutton(dip,text="Mustard",font=('Arial',14,'bold'),fg='blue',onvalue=1,offvalue=0,variable=varT31,command=e31)
mustard.grid(row=3,column=0,sticky=W)


side=LabelFrame(btframe,text="Sides",bd=10,relief=RIDGE,fg="blue",font=('arial',16,'bold'))
side.pack(side=RIGHT,padx=2)
garlic_bread=Checkbutton(side,text="Garlic bread",font=('Arial',14,'bold'),fg='blue',onvalue=1,offvalue=0,variable=varT32,command=e32)
garlic_bread.grid(row=0,column=0,sticky=W)
cgarlic_bread=Checkbutton(side,text="Cheese Garlic bread",font=('Arial',14,'bold'),fg='blue',onvalue=1,offvalue=0,variable=varT33,command=e33)
cgarlic_bread.grid(row=1,column=0,sticky=W)
sgarlic_bread=Checkbutton(side,text="Stuffed Garlic bread",font=('Arial',14,'bold'),fg='blue',onvalue=1,offvalue=0,variable=varT34,command=e34)
sgarlic_bread.grid(row=2,column=0,sticky=W)
pasta=Checkbutton(side,text="Mac & Cheese",font=('Arial',14,'bold'),fg='blue',onvalue=1,offvalue=0,variable=varT35,command=e35)
pasta.grid(row=3,column=0,sticky=W)
cpasta=Checkbutton(side,text="Smoke Chili Mac&Chesee",font=('Arial',14,'bold'),fg='blue',onvalue=1,offvalue=0,variable=varT36,command=e36)
cpasta.grid(row=4,column=0,sticky=W)
spasta=Checkbutton(side,text="Arrabiata Sauce Pasta",font=('Arial',14,'bold'),fg='blue',onvalue=1,offvalue=0,variable=varT37,command=e37)
spasta.grid(row=5,column=0,sticky=W)
Taco=Checkbutton(side,text="Mexican Taco",font=('Arial',14,'bold'),fg='blue',onvalue=1,offvalue=0,variable=varT38,command=e38)
Taco.grid(row=6,column=0,sticky=W)

#at start all are deselected
thumbsup.deselect()
coke.deselect()
fanta.deselect()
mountaindew.deselect()
sprite.deselect()
maaza.deselect()
up7.deselect()
cheseed.deselect()
jalapeñod.deselect()
garlicd.deselect()
mustard.deselect()
sweetchillid.deselect()
thousandislandd.deselect()
chillis.deselect()
garlic_bread.deselect()
cgarlic_bread.deselect()
sgarlic_bread.deselect()
pasta.deselect()
cpasta.deselect()
spasta.deselect()
Taco.deselect()
#calc
calcframemain=LabelFrame(btframe,text="Calculator",bd=13,relief=RIDGE,fg="blue",font=('arial',16,'bold'))
calcframemain.pack(side=RIGHT,padx=2)
calculatorFrame=Frame(calcframemain,bd=1,relief=RIDGE)
calculatorFrame.pack()
operator=''
def buttonClick(numbers): 
    global operator
    operator=operator+numbers
    calculatorField.delete(0,END)
    calculatorField.insert(END,operator)
def clear():
    global operator
    operator=''
    calculatorField.delete(0,END)
def answer():
    global operator
    result=str(eval(operator))
    calculatorField.delete(0,END)
    calculatorField.insert(0,result)
    operator=''




calculatorField=Entry(calculatorFrame,font=('arial',16,'bold'),width=32,bd=4)
calculatorField.grid(row=0,column=0,columnspan=4)
button7=Button(calculatorFrame,text='7',font=('arial',16,'bold'),fg='yellow',bg='blue',bd=6,width=6,command=lambda:buttonClick('7'))
button7.grid(row=1,column=0)
button8=Button(calculatorFrame,text='8',font=('arial',16,'bold'),fg='yellow',bg='blue',bd=6,width=6,command=lambda:buttonClick('8'))
button8.grid(row=1,column=1)
button9=Button(calculatorFrame,text='9',font=('arial',16,'bold'),fg='yellow',bg='blue',bd=6,width=6,command=lambda:buttonClick('9'))
button9.grid(row=1,column=2)
buttonPlus=Button(calculatorFrame,text='+',font=('arial',16,'bold'),fg='yellow',bg='blue',bd=6,width=6,command=lambda:buttonClick('+'))
buttonPlus.grid(row=1,column=3)
button4=Button(calculatorFrame,text='4',font=('arial',16,'bold'),fg='yellow',bg='blue',bd=6,width=6,command=lambda:buttonClick('4'))
button4.grid(row=2,column=0)
button5=Button(calculatorFrame,text='5',font=('arial',16,'bold'),fg='yellow',bg='blue',bd=6,width=6,command=lambda:buttonClick('5'))
button5.grid(row=2,column=1)
button6=Button(calculatorFrame,text='6',font=('arial',16,'bold'),fg='yellow',bg='blue',bd=6,width=6,command=lambda:buttonClick('6'))
button6.grid(row=2,column=2)
buttonMinus=Button(calculatorFrame,text='-',font=('arial',16,'bold'),fg='yellow',bg='blue',bd=6,width=6,command=lambda:buttonClick('-'))
buttonMinus.grid(row=2,column=3)
button1=Button(calculatorFrame,text='1',font=('arial',16,'bold'),fg='yellow',bg='blue',bd=6,width=6,command=lambda:buttonClick('1'))
button1.grid(row=3,column=0)
button2=Button(calculatorFrame,text='2',font=('arial',16,'bold'),fg='yellow',bg='blue',bd=6,width=6,command=lambda:buttonClick('2'))
button2.grid(row=3,column=1)
button3=Button(calculatorFrame,text='3',font=('arial',16,'bold'),fg='yellow',bg='blue',bd=6,width=6,command=lambda:buttonClick('3'))
button3.grid(row=3,column=2)
buttonMult=Button(calculatorFrame,text='*',font=('arial',16,'bold'),fg='yellow',bg='blue',bd=6,width=6,command=lambda:buttonClick('*'))
buttonMult.grid(row=3,column=3)
buttonAns=Button(calculatorFrame,text='Ans',font=('arial',16,'bold'),fg='yellow',bg='blue',bd=6,width=6,command=answer)
buttonAns.grid(row=4,column=0)
buttonClear=Button(calculatorFrame,text='Clear',font=('arial',16,'bold'),fg='yellow',bg='blue',bd=6,width=6,command=clear)
buttonClear.grid(row=4,column=1)
button0=Button(calculatorFrame,text='0',font=('arial',16,'bold'),fg='yellow',bg='blue',bd=6,width=6,command=lambda:buttonClick('0'))
button0.grid(row=4,column=2)
buttonDiv=Button(calculatorFrame,text='/',font=('arial',16,'bold'),fg='yellow',bg='blue',bd=6,width=6,command=lambda:buttonClick('/'))
buttonDiv.grid(row=4,column=3)



costFrame=Frame(bbframe,bd=4,relief=RIDGE)
costFrame.pack(side=BOTTOM,pady=5)

labelCostofFood=Label(costFrame,text='Cost of Pizza',font=('arial',14,'bold'),fg='black')
labelCostofFood.grid(row=1,column=0,padx=2)
textCostofFood=Entry(costFrame,font=('arial',14,'bold'),bd=6,width=12,state='readonly',textvariable=pizzavar)
textCostofFood.grid(row=1,column=1,padx=2)

labelCostofSDD=Label(costFrame,text='Cost of Sides/Dips/Drinks',font=('arial',14,'bold'),fg='black')
labelCostofSDD.grid(row=1,column=2,padx=2)
textCostofSDD=Entry(costFrame,font=('arial',14,'bold'),bd=6,width=12,state='readonly',textvariable=ssdvar)
textCostofSDD.grid(row=1,column=3,padx=2)

labelTax=Label(costFrame,text='Tax',font=('arial',14,'bold'),fg='black')
labelTax.grid(row=1,column=4,padx=2)
textTax=Entry(costFrame,font=('arial',14,'bold'),bd=6,width=10,state='readonly',textvariable=taxvar)
textTax.grid(row=1,column=5,padx=2)

labelTotalCost=Label(costFrame,text='Total Cost',font=('arial',14,'bold'),fg='black')
labelTotalCost.grid(row=1,column=6,padx=2)
textTotalCost=Entry(costFrame,font=('arial',14,'bold'),bd=6,width=15,state='readonly',textvariable=totalvar)
textTotalCost.grid(row=1,column=7,padx=2)

window.mainloop()
