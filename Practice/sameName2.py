def spam():
    global eggs    # 指全域變數的 eggs ，不是又建立一個區域變數 eggs
    eggs = 'spam'

eggs = 'global'    # 全域變數 eggs
spam()
print(eggs)
