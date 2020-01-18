# python global variable
def function_local():
        global a
        print('a is -> ',a)
        a = 50
        print('After new value within the function a is -> ',a)
a = 100
function_local()
print('Value of a is ->',a)
