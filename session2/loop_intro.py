# for i in range(26):
#     print(i)

# for i in range(0,100,2):
#     print(i)

# for i in range(100,0,-1):
#     print(i)

# for i in ['a','b','c']:  ( gói lại thành 1 dãy các chữ cái-ngoặc [])
#     print(i)

# ex viết 1 biểu thức tính tổng từ 0-n

# n = int(input("nhập số")) 
# Sum=0
# for i in range(n+1):
#     Sum = Sum + i 
# print(Sum) (sum ghi đè giá trị cũ lại cộng thêm 1 giá trị i mới)

# from turtle import *
# edges = int(input("Number of edges"))
# for edge in range(3,edges+1):
#     angle=360/edges
#     for i in range(edge):
#         forward(100)
#         left(angle)

# # mainloop()
# count = 0
# running = True
# while running:
#     if count == 5:
#         running = False
#     # break
#     print("you can stop me") 
#     count = count + 1
 
# # Khi bị chạy liên tục muốn dừng bấm Crtl+C
# #  break dừng lại 

username = "mindx" 
password = "password"
count= 0
while True:             
    # sau wile là True hoặc gán biến
    if count > 7 :
        print("hết lần thử rồi bạn ơi")
        break
    username_input = input("username")
    password_input = input("password")
    if username_input == username and password_input ==password:
        print("Đăng nhập Thành Công")
        break
else:
    count = +1









