import mymodule

def average(list):
    sum = 0

    for x in list:
        sum = mymodule.add(sum, x)
    return sum/len(list)  
