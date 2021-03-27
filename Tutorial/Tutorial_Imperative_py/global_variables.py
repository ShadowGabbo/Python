x = "awesome"

def myfunc():
  #scope of the function
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#global 
def myfunc():
  global x #rendere gloabale una variabile
  x = "fantastic"

myfunc()

print("Python is " + x)