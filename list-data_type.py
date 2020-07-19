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

#Ma trận
aMatrix = [[1,2,3],[4,5,6]]
print(aMatrix[0])
print(aMatrix[1])

#List continue
a = [1,2,3,9,87,4,5,6]
#count(arg) Trả về số lần xuất hiện của phần tử trong list
print(a.count(1))


#index(arg) Trả về vị trí xuất hiện đầu tiên của phần tử trong list 
# => throw exception nếu trong list không xuất hiện phần tử
print(a.index(9))

#copy() Trả về một bản sao của list
b = a.copy()
b[1] = "khanhhn"
print(a)
print(b)
print(b[-1])

#clear() Xoá mọi phần tử trong list
a.clear()
print(a)

