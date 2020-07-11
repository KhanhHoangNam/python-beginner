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

# format method
r = "Name: {}, Address: {}".format("Khanh", "Hanoi")
print(f)
print(result)
print(info)
print(r)

#String-Lesson 4
a = ".Hoang Nam Khanh."
b = a.capitalize()
c = a.upper()
d = a.swapcase()
e = a.title()
f = a.center(30, "*")
g = a.ljust(30, "*")
h = a.rjust(30, "*")
j = a.encode(encoding="utf-8", errors="strict")
k = a.join(["Hello ", " Hi ", " Welcome "])
l = a.replace("a", "*")
z = a.strip(".")
# print(int(a))
print(type(a))
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(j)
print(k)
print(l)
print(z)

#String -Lesson5
color = "green,red,purple,gold"
colorList = color.split(",", 1)
partitionColorList = color.partition(",")
print(colorList)
print(partitionColorList)
print(color.startswith("green"))
print(color.endswith("HiHi"))
print(color.find("e"))
print(color.rfind("e"))