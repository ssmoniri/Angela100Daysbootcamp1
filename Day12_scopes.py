#DAY 12 scope, global scope vs local scope


    def a_function(a_parameter):
        a_variable = 15  # this is local variable and just executed within the function that is defined
        return a_parameter


    a_function(10)
    print(a_variable)# this can not be run and giving us a NameError which means this is a local variable which defined
    # within the function



#The print statement is outside the function foo().
# So it can't access the local variable i = 100. It only sees the global i, which is equal to 50.
i = 50
def foo():
    i = 100
    return i
foo()
print(i)


#Remember that in Python there is no block scope.
# Inside a if/else/for/while code block is the same as outside it.
def bar():
    my_variable = 9
    if 16 > 9:
        my_variable = 16
    print(my_variable)

bar()