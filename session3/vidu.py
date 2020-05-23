# from random import shuffle
# quiz = input("enter your quiz")
# # list_quiz= quiz.split() # chia tách theo dấu phẩy( hoặc dấu gì tùy)
# # print(list_quiz)           # không điền gì tự tách
# list_quiz = list(quiz)
# print(list_quiz)
# shuffle(list_quiz)
# for i in range(len(list_quiz)):
#     print(list_quiz[i],end='')

# ans = input(" your guess?").lower()
# if ans == quiz:
#     print('bingo')
# else:
#     print('T.T')

# BÀI TẬP
# district = ['st', 'bđ', 'btl', 'cg', 'đđ', 'hbt']
# km2 = [111.43, 9224, 43.35, 12.04, 9.96, 10.09]
# population = [150300, 247100, 333300, 266800, 420900, 318000]
# maxpopulation = max(population)
# print('max population : ',maxpopulation)

# print('min population : ', min(population))
# print(population.index(maxpopulation))

# minpopulation = min(population)
# print(minpopulation)
# print(population.index(minpopulation))

# namedmax = district[4]
# print(namedmax)

# namedmin = district[0]
# print(namedmin)

# km2.sort()
# print(km2)

# mdcd= []
# for i in range(len(district)):
#     mdcd.append(int(population[i]//km2[i]))
# print(mdcd)

# total = 0
# for i in mdcd:
#     total = total + i
# print('Mật độ dân cư trung bình =', int(total//len(district)))

#SERIOUS EXERCISES
print('hello my name is dat and these are my sheep sizes')
sheepsize = [5, 7, 300, 90, 24, 50, 75]
# print(sheepsize)

# print('now my biggest sheep has size lets shear it')
# print(max(sheepsize))
# sheepsize[sheepsize.index(max(sheepsize))]= 8
# print('after shearing here is my flock')
# print(sheepsize)
for s in range(1,4):
    print("month",s)
    for i in range(len(sheepsize)):
        sheepsize[i]+=60
    print(sheepsize)





