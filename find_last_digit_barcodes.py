#Python code to find Last Digit of barcode of Register / Speed Articles

n = str(input("Please enter first 8 numerical digits of Barcode : "))
a = (11-((int((n)[0])*8)+(int((n)[1])*6)+(int((n)[2])*4)+(int((n)[3])*2)+(int((n)[4])*3)+(int((n)[5])*5)+(int((n)[6])*9)+(int((n)[7])*7))%11)
if a == 10:
    a = 0
elif a == 11:
    a = 5
print(str(n)+str(a))
