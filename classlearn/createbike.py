class Bike:
    def __init__(self,model,colour,make,price):     #initialize class with given parameter
        self.model = model
        self.colour = colour
        self.make = make
        self.price = price

    def Display_detail(self):               # function 1
        print("Bike model is: ",self.model)
        print("colour is : ",self.colour)
        print("Manufacture Year is : ",self.make)

    def Onroad_price(self):            # function 2
        if self.price < 100000:
            self.price = 40000 + self.price
            print("Onroad price is: ", self.price)
        else:
            self.price = 10000 + self.price
            print("Onroad price is:",self.price)

    def Booking_confirm(self):          #function 3
        print(f"would you like to book {self.colour} colour  {self.model} now ?")
        reply = str(input("Enter yes or No :"))
        if reply=="yes":
            print(f"your {self.colour} colour {self.model} bike is booked")
        elif reply == "no":
            print("Thank You !")
        else:
            print("wrong input")

b1 = Bike("Classic 350 ","black","2025",900000)             # obj 1
b2 = Bike("HD Fatboy ","black","2025",1700000)              # obj 2

b1.Display_detail()                                         # call function for obj 1
b1.Onroad_price()
b1.Booking_confirm()

b2.Display_detail()                                         # call function for obj 2
b2.Onroad_price()
b2.Booking_confirm()






