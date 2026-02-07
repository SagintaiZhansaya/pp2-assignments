#1
class Student:
    def study(self):
        print("Student studies")

class Athlete:
    def train(self):
        print("Athlete trains")

class StudentAthlete(Student, Athlete):
    pass

sa = StudentAthlete()
sa.study()
sa.train()

#2
class Printer:
    def print_doc(self):
        print("Printing document")

class Scanner:
    def scan_doc(self):
        print("Scanning document")

class AllInOne(Printer, Scanner):
    pass

device = AllInOne()
device.print_doc()
device.scan_doc()

#3
class Flyer:
    def fly(self):
        print("Flying")

class Swimmer:
    def swim(self):
        print("Swimming")

class Duck(Flyer, Swimmer):
    pass

d = Duck()
d.fly()
d.swim()

#4
class Jump:
    def jump(self):
        print("Jumping")

class Shoot:
    def shoot(self):
        print("Shooting")

class Player(Jump, Shoot):
    pass

p = Player()
p.jump()
p.shoot()

#5
class Logger:
    def log(self, message):
        print("LOG:", message)

class Saver:
    def save(self):
        print("Data saved")

class App(Logger, Saver):
    pass

app = App()
app.log("App started")
app.save()
