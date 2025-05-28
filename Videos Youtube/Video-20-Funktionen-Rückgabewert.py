
def say_hello(first_name, last_name):
    print(print("Hallo " + first_name + " " + last_name))
    print("Willkommen zurück")

print(type(say_hello("Nico", "Mustermann")))

def maximum(a, b):
    if a < b:
        return b
    else:
        return a
    
result = maximum(3, 7)
print(result)

def maximum(a, b):
    if a < b:
        return b
    else:
        return a
    
result = maximum(7, 3)
print(result)