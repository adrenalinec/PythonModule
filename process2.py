a = 'fa'

def func1():
    try:
        print( a + 2)
    except NameError:
        print('fuck')

# print( func1() )
func1()
