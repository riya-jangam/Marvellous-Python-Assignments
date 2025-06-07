class vehicle:

    def __init__(self, a):
        self.name = a

    def start(self):
        print("name of vehicle: "+self.name)

class car(vehicle):
    def __init__(self,b):
        super().__init__(b)
        
    def start(self):
        print("Car is a vehicle")
        
def main():
    obj1=car("Fortuner")
    obj1.start()

if __name__ == "__main__":
    main()