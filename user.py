class User:
    def __init__(self, name,):
        self.name = name
        self.account_balance = 0

    def deposit(self, amount):
        self.account_balance += amount

    def withdrawal(self, amount):
        self.account_balance -= amount

    def display_balance(self):
        print("User: ", self.name, "Balance: ", self.account_balance)

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        # other_user. += amount 

user = User("Mr.x")
# print(user.__dict__)
user.deposit(300)
user.deposit(300)
user.deposit(400)
user.withdrawal(200)
print(user.display_balance())

user2 = User("Mr.y")

user2.deposit(1000)
user2.deposit(1000)
user2.withdrawal(500)
user2.withdrawal(500)
print(user2.display_balance())

user3 = User("Mr.z")

user3.deposit(10000)
user3.withdrawal(1000)
user3.withdrawal(1000)
user3.withdrawal(1000)
user3.transfer_money(user2,1000)
print(user3.display_balance())

