def rebuild(list):
    string = ''
    count = len(list)
    for i in range(0, count):
        if i == (count - 1):
            string += ('and ' + list[i])
        else:
            string += (list[i] + ', ')
    return string
    
spam = ['apples', 'bananas', 'tofu', 'cats']
print(rebuild(spam))