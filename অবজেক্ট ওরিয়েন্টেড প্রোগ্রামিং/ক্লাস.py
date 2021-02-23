



# class Persion:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def persion(self):
#         return 'Name : ' + self.name, ' Age : ', self.age,  'Gender : ' + self.gender
#
# people1 = Persion('Joy', 20, 'Male')
# people2 = Persion('Ziaur Rahman Joy', 22, 'Male')
#
# print(people1.persion())
# print(people2.name)


# property

# class Country:
#     sentance = 'I love Bangladesh'
#     def __init__(self, name, independence):
#         self.name = name
#         self.independence = independence
#
#     def print_function(self):
#         if self.name == 'Bangladesh':
#             return self.name, self.independence, self.sentance
#         return self.name, self.independence
#
# bangladesh1 = Country('Bangladesh', 1971)
# india = Country('India', 1947)
# print(bangladesh1.print_function())
# print(india.print_function())



# multiple inheritance

class Car:
    def __init__(self, car_name):
        self.car_name = car_name

    # def car(self):
    #     print(self.car_name)

class Driver:
    def __init__(self, driver):
        self.driver_name = driver

    # def driver(self):
    #     print(self.driver_name)

class Child(Car, Driver):
    def __init__(self, car, driver):
        Car.__init__(self, car)
        Driver.__init__(self, driver)

    def Print(self):
        print('Driver name :', self.driver_name, 'Bus Name :', self.car_name)

bus1 = Child('Hanif', 'Joy')
bus1.Print()
