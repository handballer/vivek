
list = ['GUVI'] 
def foo(x,n):
     print x * n

 
def my_map_simple(fun, list):
     for item in list:
         fun(item)

 
my_map_simple(foo, list)
