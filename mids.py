class MyClass:
    def __init__(self):
        print("Object created.")

    def __del__(self):
        print("Object destroyed.")

    def __str__(self) -> str:
        return 'new'

obj = MyClass()
print(obj)
# del obj  # This will trigger the __del__ method and the object will be destroyed
