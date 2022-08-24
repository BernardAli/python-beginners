class Vehicle:
    speed = 0

    def drive(self, speed):
        self.speed = speed
        print('Driving')
    
    def stop(self):
        self.spee
        print('Stopped')

    def display(self):
        print(f'Driving at {self.speed} speed')



class Freezer:
    temp = 0
    def freeze(self, temp):
        self.temp = temp
        print('Freezing')
    
    def display(self):
        print(f'Freezing at {self.temp} temp')


class FreezerTruck(Vehicle, Freezer):
    def display(self):
        print(f'Is a freezer: {issubclass(FreezerTruck, Freezer)}')
        print(f'Is a vehicle: {issubclass(FreezerTruck, Vehicle)}')

        # super(Freezer, self).display()
        # super(Vehicle, self).display()

        Freezer.display(self)
        Vehicle.display(self)

t = FreezerTruck()
t.drive(50)
t.freeze(-30)
print('--'*20)
t.display()