def spam():
    global eggs
    eggs = 'spam'    # this is the global

def bacon():
    eggs = 'bacon'   # this is a local, because 'eggs' is assigned in function

def ham():
    print(eggs)      # this is the global, bacause there is no 'eggs' defined in function

eggs = 42            # this is the global
spam()
print(eggs)
