# Parent Class : User
# Hold details of the user -- DONE
# Create a Function to show the user details  -- DONE
# Child Class : Bank
# Store the details about the bank balance
# Store the details about amount
# Allows for deposits, withdrawal, view balance
### Parent Class
class User():
    def __init__(self, name, age, gender):
        self.u_name = name
        self.u_age = age
        self.gender = gender

    def user_details(self):
        print("User Details :-> ")
        print(" ")
        print("User Name --> " + self.u_name)
        print("User Age --> " + str(self.u_age))
        print("User Gender --> " + self.gender)


## Child Class
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Account Balance --> ", self.balance)


user = Bank("Jayateerth Dambal", 20, 'Male')
user.deposit(200)

