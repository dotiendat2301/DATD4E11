# CÁCH TRUY CẬP
# person = ['Đạt', 96, 'Viettel', 1, False, True]
#dictionary, object,map..v.v
# person = {
#     'name': 'Đạt', 
#     'yob':{ 
#         'year': 1996, 
#         'month': 1,
#         'day': 1
#      },
#     'company': ['Viettel', 'Vinaphone'],
#     'key': None
# }
# print(person['name'])# in công ty các thứ ..,lấy có thể án biến
# name = person['name']#list cho 1 key cũng được
# print(name)
# print(len(person['company']))

# for key in person:
#     print(key,person[key]) # xem key


# TẠO THÊM KEY VÀ VALUES
# person['relationship'] = True

# for key in person:
#     print(key,person[key])

# UPDATE # mọi giá trị key đều là duy nhất UNIQUE
 
# person['yob']['month'] = 4

#DELETE
# del person['key']
# print(key,person[key])


#EX:
tc = {
    'hc': 'học',
    'ng': 'người',
    'pt': 'party',
    'ns': 'năm sinh',
    'lm': 'làm',
    'stt': 'status'
}
while True:
    print(tc)
    search = input('Yourcode: ')
    if search in tc :
        print('trans = ',tc[search])

    else:
        ask = input('not found, do you want to conntribute this word?(Y/N)').lower()
        if ask in['y','yes']:
            mearning = input('enter your trans :')
            tc[search] = mearning
            print('update')
            




