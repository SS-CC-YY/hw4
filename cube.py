def cube(num):
    try:
        return num ** 3
    except TypeError:
        return None

#number = 9
#result = cube(number)
#print("result: ", result)