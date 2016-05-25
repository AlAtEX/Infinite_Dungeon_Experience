def num(mi,ma):
    while True:
        inp = input("Please enter a number between {a}  and {b}, both are inclusive:  ".format(a = mi,b = ma))
        try:
            inp =  int(inp)
            if mi <= inp <= ma:
                return inp
            else:
                print("That is not between {a} and {b}".format(a = mi, b = ma))
        except:
            print("That is not a number")
