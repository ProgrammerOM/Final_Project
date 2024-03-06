from Dataitem import items
from Classitem import Item
from Classcalculate import Calculate
from Classcontinue import Continue
from Classfindproducts import Findproducts


# class InputMoney(Item):

#     def __init__(self):
#         self.items = Item(items)
#         self.calculate = Calculate()
#         self.continues = Continue()
#         self.findproducts = Findproducts()
#         super().__init__(items)

#     def _input_money(self):
#         money = int(input("เติมเงิน : ").strip())
#         self.continues._chack_out()
#         if money < 10:
#             print("เงินของคุณไม่เพียงพอ")
#             exit()
#         self.findproducts.findproduct(money)


class InputMoney(Item):

    def __init__(self):
        self.items = Item(items)
        self.calculate = Calculate()
        self.continues = Continue()
        self.findproducts = Findproducts()
        super().__init__(items)

    def _input_money(self):
        money = int(input("\nกรุณาเติมเงินของคุณเพื่อทำการซื้อสินค้า : ").strip())
        if money < 10:
            print("\nยอดเงินของคุณมีไม่เพียงพอ กรุณาเติมเงิน")
            amount = int(input("\nกรุณาเติมเงินของคุณเพื่อทำการซื้อสินค้า : ").strip())
            money += amount
            print("\nยอดเงินของคุณมี", money, "บาท", "\n")
        self.findproducts.findproduct(money)
