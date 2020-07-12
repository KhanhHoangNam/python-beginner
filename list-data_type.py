print("List data type Lesson")
# Một list được giới hạn bởi các cặp ngoặc vuông
# Các phần tử của list được ngăn cách nhau bởi dấu phẩy(,)
# List có khả năng lưu trữ mọi đối tượng của python.
# vào bao gồm cả chính nó.

aList = [1,2,3, ["Hoang", "Nam", "Khanh", [10, 100]]]
aList += ["Nothing", "Everthing"]
aList *= 3
aSubList = "Nothing"
anotherList = [i for i in range(10)]
multipleList = [[n, n*1, n*2] for n in range(0,3)]
aStringList = list("Hoang Nam Khanh")
print(aList)
print(anotherList)
print(multipleList)
print(aStringList)
print(aSubList in aList)
print(aList[3][0])