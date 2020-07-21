# Một set được giới hạn bởi một dấu cặp ngoặc nhọn({}),
# Tất cả những gì nằm trong đó đều là phần tử của set
# Các phần tử của set được ngăn cách nhau bởi dấu phẩy(,)
# Set không chứa nhiều hơn một phần tử trùng lặp 
# Set chỉ có thể chứa các hashtable object 
# nhưng chính nó không phải là một hashtable object 
# do đó không thể chứa set trong một set

set_1 = {1, 9, 5, 2}
print(set_1)
print(type(set_1))

set_2 = {"Hoang", "Nam", "Khanh", "Hoang"}
print(set_2)

set_3 = {value for value in range(10, 20, 2)}
print(set_3)

# Khởi tạo set sử dụng constructor
# Chỉ có thể khởi tạo một set rỗng bằng cách sử dụng constructor
set_4 = set((1,9,2))
print(set_4)

#Venn
#Các toán tử của set
print(1 in {1, 3, 2})
# print({1, 3, 2, 4} - {2, 1})
# print({1, 3, 2, 4} & {2, 1})
# print({1, 3, 2, 4} | {2, 1, 3})
print({1, 3, 2, 4} ^ {2, 1, 3})
# print({1, 3, 2, 4} != {2, 1})