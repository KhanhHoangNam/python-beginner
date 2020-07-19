# được giới hạn bởi cặp dấu ngoặc tròn ()
# Các phần tử tuple được phân cách nhau bởi dấu phẩy (,)
# tuple có khả năng chứa mọi giá trị
# tuple truy xuất nhanh hơn list
# dung lượng chiếm dung lượng trong bộ nhớ nhỏ hơn list
# bảo vệ dữ liệu không bị thay đổi
# có thể dùng làm key của dictionary

tup = (1,3,2,9,6, ("Hoang", "Nam", "Khanh"))
aTuple = tuple("Hoang Nam Khanh")
anotherTuple = tuple(i for i in range(10) if i % 2 != 0)
print(tup)
print(aTuple)
print(tuple(anotherTuple))
print(aTuple + anotherTuple)
print(len(anotherTuple))
print(anotherTuple[::-1])
print(anotherTuple[:-1])

# a functions example
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

print(quicksort([3,6,8,0,11,100,1]))