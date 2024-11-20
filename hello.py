class Greeter:
    def __init__(self, name="World"):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}!")

# Create an instance of the Greeter class
hello_world = Greeter()

# Call the greet method
hello_world.greet()
