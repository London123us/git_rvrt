print("Hello It's my git revert command learning.")

def outerfun():
    print("Outer Func")

    def innerfun():
        print("Inner Func")
    innerfun()

outerfun()

def outerfun2():
    print("Outer fun2")

    # innerfun2()
    # # It will give us error, cannot find out the innerfun2()
    # # because it's below then func call
    def innerfun2():
        print("Inner fun2")
    innerfun2()

outerfun2()
