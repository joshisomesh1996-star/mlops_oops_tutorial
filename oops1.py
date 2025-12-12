#initialize class
class employee:
    def __init__(self):
        print("Started initializing employee")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        print("Attributes initialized")

    
    def travel(self, destination):
        print("Traveling method called")
        print(f"{self.id} is traveling to {destination}")

sam = employee()
sam.travel("New York")
print(type(sam))
