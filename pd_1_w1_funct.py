def addnum(x,y,z=None, flag="False"):
    if (flag):
        print("It's true flag")
    if (z==None):
        return x + y
    else :
        return x+y+z


print(addnum(3,2,flag="True"))