from Classitem import Item


class Calculate(Item):

    def __init__(self):
        pass

    def change(self, current_money, price):
        while True:
            balance = current_money - price
            if balance < 0:
                print("เงินของคุณไม่เพียงพอ")
            else:
                print("เงินทอน: ", balance)
                return balance
