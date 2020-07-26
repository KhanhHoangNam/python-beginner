# Kiểu dữ liệu dict trong python
dic = {"name":"Nam Khanh", "domain":"khanhhn.com.vn"}
print(dic)
print(type(dic))

# Khởi tạo dict 
class Map_Class:
            def keys(self):
                return [1, 2, 3] 
            def __getitem__(self, key):
                return key * 2
map_obj = Map_Class()
dic = dict(map_obj)
print(dic)