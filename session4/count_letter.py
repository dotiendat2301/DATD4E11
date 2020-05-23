sentence = 'asdaasfasaqwe'
# sorted_sentence = sorted(sentence)
count_dictionary = {}
for char in sentence:  # như đếm list
    if char in count_dictionary:
        count_dictionary[char] = count_dictionary[char] + 1
    else:
        count_dictionary[char] = 1

for key in count_dictionary:
print(key,count_dictionary(key))



