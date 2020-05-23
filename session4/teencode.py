teencode = {
    'hc': 'học',
    'nc': 'nói chuyện',
    'vk': 'vũ khí',
    'ck': 'chuyển khoản'
}
while True:
    for key in teencode:
        print(key,end='\t')

    print('*'*30)

    input_key = input('enter the word you want to search:')
    if input_key in teencode:
        print('is mean:',input_key)
    else:
        prompt = input('word not found, would u like to con tribute it meanging?')
        if prompt == 'y':
        teencode[input_key]= input('entermeaning')
        else:
            print(bye)
            break