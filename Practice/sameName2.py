def spam():
    # 告訴 Python 
    # 在這個函示中所用的 eggs 變數是全域變數
    # 不是在這個函示中又建立一個區域變數
    global eggs
    eggs = 'spam'
    
eggs = 'global'
spam()
print(eggs)