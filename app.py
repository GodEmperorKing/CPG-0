print("Hello, World!")

def greet():
    return "Hello, class!"

result = greet()

print(result)

print("Hello, World!")

def greet(name="class"):
    return f"Hello, {name}!"

# Calling the function
result = greet()

# Logic to react to the result
if "class" in result:
    print(f"{result} Time to start the lesson.")
else:
    print(result)
