#default value
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function() # when вызываещь без аргумента
my_function("Brazil")