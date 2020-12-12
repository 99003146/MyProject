from datetime import datetime
bike_l = {"Pulsar": 20, "Unicorn": 30, "Royal Enfield": 10}


class Display:
    def __init__(self):
        self.bikes = {}

    def display(self, bikes):
        for (bike, no) in zip(bikes.keys(), bikes.values()):
            print("Bike:", bike, "|", "Numbers available: ", no)


class Bike:
    def __init__(self):
        self.bikes = {}
        self.bike_name = ""
        self.number = 0

    def rent(self, bikes, bike_name, number):
        if bike_name in bikes.keys():
            value = bikes.get(bike_name)
            newval = value-number
            if(newval >= 0):
                bikes[bike_name] = newval
                print("You have rented: ", bike_name)
                print("Numbers Rented:", number)
            else:
                print("Required Number of bikes not available")

    def ret_bike(self, bikes, bike_name, number, hours_used):
        if bike_name in bikes.keys():
            cost = hours_used*number*50
            value = bikes.get(bike_name)
            newval = value+number
            bikes[bike_name] = newval
            print("You have returned:", bike_name)
            print("Number Returned:", number)
            print("Amount Payable:", cost)


class Customer(Bike, Display):
    def __init__(self):
        self.user_n = ""
        self.phone_n = ""

    def c_rent(self, user_n, phone_n, bikes, bike_name, number):
        print("***************************")
        print("UserName: ", user_n)
        print("Phone number: ", phone_n)
        Bike.rent(self, bikes, bike_name, number)

    def c_return(self, bike, bike_name, number, hours_used):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        Bike.ret_bike(self, bike, bike_name, number, hours_used)
        print("You have returned the bike at ", current_time)
        print()
        print("Database Updated")
        print("New Count of Bikes")
        print()
        Display.display(self, bike)


def main():
    print("\n 1. Display Bike Details")
    print("\n 2. Rent Bike")
    print("\n 3. Return Bike")
    choice = input("Enter Choice: ")

    if choice == "1":
        dis = Display()
        dis.display(bike_l)
    if choice == "2":
        usrname = input("Enter Name: ")
        phoneno = input("Enter Phone Number: ")
        bike_n = input("Enter Name of Bike to rent: ")
        number = int(input("Enter Number of bikes to rent"))
        ren = Customer()
        ren.c_rent(usrname, phoneno, bike_l, bike_n, number)
    if choice == "3":
        bike_n = input("Enter Name of Bike to return: ")
        number = int(input("Enter Number of bikes to return"))
        hours_used = int(input("Enter Number of hours used"))
        retu = Customer()
        retu.c_return(bike_l, bike_n, number, hours_used)


if __name__ == "__main__":
    main()
