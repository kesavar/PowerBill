#!/usr/bin/python

Units=[0,0,0,0,0]		
		
Fixed_charges=337.50

Units_Bill=float(input("Enter Energy Charges: "))
Total_Bill=float(input("Enter Total_bill: "))

Vary_charges=Total_Bill-Units_Bill-Fixed_charges

print ("Variable Charges:",Vary_charges)
print ("fixed charges:",Fixed_charges)


#################### READ FROM FILE PRVIOUS MONTH METER READINGS ##################
#cur_month=now.month()
#print(cur_month)

fp=open("C:\\Users\\kesava\\python_ex\\Bill_History.txt","r+")
#fp=open("/media/ubuntu/SASI/kesava/power/Bill_History","r+")
last_Before= fp.readlines()[-2]
print(last_Before)
before=[x.split() for x in last_Before.split()]
fp.seek(0,0) 
last_line = fp.readlines()[-1]
print(last_line)
last=[x.split() for x in last_line.split()]
fp.close()	 

k=1
for k in range(1,5):
	var=last[k]
	var1=var[0]

	temp=before[k]
	var2=temp[0]
	
	#val=k-1
	Units[k-1]=int(var1)-int(var2)

#print(Units[0],Units[1],Units[2],Units[3])
Total_Units=Units[0]	
Online_charge=(1.15*Total_Bill)/100
unit_price=(Units_Bill/Units[0])

Grnd_flr_units=Units[1]
first_flr_units=Units[2]
second_flr_units=Units[3]

Motor_units=Total_Units-(Grnd_flr_units+first_flr_units+second_flr_units)

Motor_portion=Motor_units/3.0

print ("Average Unit price: ",unit_price)
print ("Total units: ",Total_Units)
print("motor units, share ",Motor_units,Motor_portion)
print("GrndFloor_units: ",Grnd_flr_units)
print("1stFloor_units: ",first_flr_units)
print("2ndFloor_units: ",second_flr_units)

#print ("sum of individual units + motor: ",Grnd_flr_units+first_flr_units+second_flr_units+Motor_units)


Grnd_Used_ratio=((Grnd_flr_units+Motor_portion)/Total_Units)
First_Used_ratio=((first_flr_units+Motor_portion)/Total_Units)
second_Used_ratio=((second_flr_units+Motor_portion)/Total_Units)

print("Ground used ratio :: variable charges:",Grnd_Used_ratio,Grnd_Used_ratio*Vary_charges)
print("First_Used_ratio :: variable charges:",First_Used_ratio,First_Used_ratio*Vary_charges)
print("second_Used_ratio :: variable charges:",second_Used_ratio,second_Used_ratio*Vary_charges)

GrndFlr_bill=(Grnd_Used_ratio*Vary_charges)+(unit_price*(Grnd_flr_units+Motor_portion)+(Fixed_charges/3.0)+Online_charge*Grnd_Used_ratio)
FirstFlr_bill=(First_Used_ratio*Vary_charges)+(unit_price*(first_flr_units+Motor_portion)+(Fixed_charges/3.0)+Online_charge*First_Used_ratio)
SecndFlr_bill=(second_Used_ratio*Vary_charges)+(unit_price*(second_flr_units+Motor_portion)+(Fixed_charges/3.0)+Online_charge*second_Used_ratio)
Total_Bill=GrndFlr_bill+FirstFlr_bill+SecndFlr_bill-Online_charge

print ("GrndFlr_bill+online_charge: ",GrndFlr_bill)
print ("FirstFlr_bill+online_charge: ",FirstFlr_bill)
print ("SecndFlr_bill+online_charge: ",SecndFlr_bill)
print("Total_Bill+OnllinePayment_charges: ",Total_Bill,Online_charge,(Total_Bill+Online_charge))

#############  writing Bills to file ####################
fo=open("Bill_History.txt","a")
str1=str(GrndFlr_bill)
fo.write(str1[:6]+'\t')
str1=str(FirstFlr_bill)
fo.write(str1[:6]+'\t')
str1=str(SecndFlr_bill)
fo.write(str1[:6]+'\t')


str1=str(Total_Bill)
fo.write(str1[:6]+'\t')

fo.close()	 
