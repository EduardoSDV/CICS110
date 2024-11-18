x = 10
def most_mysterious_function(a):
    try:
        x = x+a
    except:
        global x
        x =22
    finally:
        global x
        x = 44
most_mysterious_function(5)
print(x)