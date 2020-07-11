aString = "My team is a %s" %("dream Team")
otherString = "I'm %s years old, I live in %s" %("25", "Hanoi")
sString = "%s %s"
result = sString %("1", "2")
print(aString)
print(otherString)
print(sString %("6", "8"))
print(result)

#%f
f = "%3f" %(3.99)
name ="Hoang Nam Khanh"
address = "Hanoi"
phoneNumber = "0368782814"
result = f"This is my name: {name}"
info = f"Name: {name}\nAddress: {phoneNumber}\nPhone: {phoneNumber}"
print(f)
print(result)
print(info)
