from Classitem import Item


# class Calculate(Item):

#     def __init__(self):
#         pass

#     def change(self, current_money, price):
#         while True:
#             balance = current_money - price
#             if balance < 0:
#                 print("เงินของคุณไม่เพียงพอ")
#             else:
#                 print("เงินทอน: ", balance)
#                 return balance


class Calculate(Item):

    def __init__(self):
        pass

    def change(self, current_money, price):
        while True:
            balance = current_money - price
            if balance < 0:
                print("\nยอดเงินของคุณมีไม่เพียงพอ กรุณาเติมเงิน")
            else:
                print("\n", "เงินทอน: ", balance, "บาท")
                return balance
