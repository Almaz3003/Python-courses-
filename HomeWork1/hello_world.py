##### variant with Class and entry point #####

class Hello:
    def __init__(self):
        self.hi_message = "Hello World!"


greeting = Hello()
print(greeting.hi_message)


##### variant with return function #####

def hi():
    n = "Hello World!"
    return n


print(hi())

##### just print() variant #####

print("Hello World!")
