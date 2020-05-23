# monan1 = 'phở'
# monan2 = ' bún'
# monan3 = ' trứng rán'
# monan4 = 'thịt chó'
# monan5 = 'cơm'


# list 
# monan = [ 'phở', 'bún', 'trứng rán', 'thịt chó', 'cơm']
# print(monan[-1]) 
# I : initialize
# C: creat
# R: read
# U: update
# D: delete
# Inteam/ Value và lưu index"thứ tự của các values"- độ dài list
#     ['a', 'b', 'c']===> độ dài là 3
#     [  1, 2, 3]
#  dấu = - thay đổi chiều đếm

#  tính độ dài list dùng len
# item = monan[0] bóc tách phần tử
# a = input()
# monan.append(a)  # ==> CREAT mặc định thêm vào cuối
# for i in range(len(monan)):
#  print(monan[i])

# U: update - sửa phần tử thứ mấy và sửa thành gì
# monan[0]='cơm'
# print(monan)
#  lấy vị trí 

# print(monan.index('trứng'))
# print(monan)
# print('trứng'in monan) ==> có thể sử dụng để đưa vào bài điều kiện
# CHỮA BÀI

# monan = [ 'phở', 'bún', 'trứng rán', 'thịt chó', 'cơm']
# for i in range(len(monan)):
#  print(i+1,monan[i])
# if update_value in monan:
#     update_value = input('nhập tên món ăn muốn đổi')
#     index = monan.index(update_value)
#     monan[index] = input('nhập tên món ăn mới')
#     print(monan)
# else:
#     print(' không tìm thấy đâu')

# DELETE
# monan = [ 'phở', 'bún', 'trứng rán', 'thịt chó', 'cơm']
#     print(monan[i])
# for i in range(len(monan)):
# monan.pop() # delete
# monan.remove('bún') # delete by value
# print(monan)


# đề bài- điền chữ vào xong cho trộn- xong điền chữ đúng vào 
import random
0
print("Nhập Vào Đê")
input_word = input()
value_list = list(input_word)
print(value_list)

random.shuffle(value_list)
print(value_list)

try = input()

makeitastring = ''.join(map(str,value_list))

