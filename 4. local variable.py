class MyClass:
    def __init__(self):
        self.instance_variable = "I am an instance variable"

    def my_method(self):
        # This is a local variable
        local_variable = "I am a local variable"
        print(local_variable)

        # Accessing an instance variable
        print(self.instance_variable)

# Create an instance of MyClass
obj = MyClass()

obj.my_method()

# print(obj.instance_variable)

# print(local_variable)
