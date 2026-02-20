print("=======students information==========")

full_name= input("Enter your full name: ")
birth_year= input("Enter your birth year:")

name_upper=full_name.upper()
first3=full_name[0:3]
last2=birth_year[-2:]

correct_password= first3 + last2

attempts=0
while attempts <3:
    password=input("Enter password the first three letter should be capital and last two should last digit on brith year:")
    
    if password ==correct_password:
        print("correct password")
        break
    else:
        print("wrong password!")
        attempts=+1
        print("Wrong password! Attempts left:", 3 - attempts)
    if attempts==3:
        print("account locked for a while!")



        #partB
maths=int(input("Enter your math marks :"))
economics=int(input("Enter your economics marks :"))
geog= int(input("Enter your geography mark: "))

total_mark= maths+economics+geog
avarage= total_mark/3
print(avarage)

#grading system
if avarage>=75:
    print("grade=A")
elif avarage>=65:
    print("grade=B")
elif avarage>=45:
    print("grade=C")
elif avarage>=30:
    print("grade= D")
else:
    print("grade= F")


#remark
if avarage>=50:
    print("pass")
else:
 print("supplimentary exam")



        



    

 



