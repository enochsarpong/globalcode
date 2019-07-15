num=[10,40,60,15]

def old_age(x):
    return x > 20

filter(old_age,num)

print( list(filter(old_age,num)) )