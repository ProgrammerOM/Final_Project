from Dataitem import items
from Classitem import Item
from Classcontinue import Continue
from Classcalculate import Calculate
from Classinputmoney import InputMoney


class Findproducts(Item):

    def __init__(self):
        self.items = Item(items)
        self.calculate = Calculate()
        self.continues = Continue()
        super().__init__(items)

    def findproduct(self, money):
        while True:
            super().__str__()
            item_id = int(input("กรุณากรอกรหัสสินค้า : ").strip())
            price = super().send_price(item_id)
            if price is None:
                print("ไม่พบสินค้าที่ตรงกับรหัสที่ให้")
                exit()
            money = self.calculate.change(money, price)
            if money < 0:
                print("เงินของคุณไม่เพียงพอ")
                return
            self.continues._chack_out()


# class Findproducts(Item):

#     def __init__(self):
#         self.items = Item(items)
#         self.calculate = Calculate()
#         self.continues = Continue()
#         self.input_money = InputMoney()
#         super().__init__(items)

#     def findproduct(self, money):
#         while True:
#             super().__str__()
#             item_id = int(
#                 input("\nกด [รหัสสินค้า] ที่ท่านต้องการซืื้อ หากต้องการเติมเงินเพิ่มกด 0: ").strip()
#             )
#             if item_id == 0:
#                 self.input_money._input_money()
#             else:
#                 pass
#             price = super().send_price(item_id)
#             if price is None:
#                 print("\nไม่พบรหัสสินค้านี้")
#                 exit()
#             money = self.calculate.change(money, price)
#             self.continues._chack_out()


class Findproducts(Item):

    def __init__(self):
        self.items = Item(items)
        self.calculate = Calculate()
        self.continues = Continue()
        self.input_money = InputMoney()
        super().__init__(items)

    def findproduct(self, money):
        while True:
            super().__str__()
            item_id = int(
                input("\nกด [รหัสสินค้า] ที่ท่านต้องการซืื้อ หากต้องการเติมเงินเพิ่มกด 0: ").strip()
            )
            if item_id == 0:
                self.input_money._input_money()
            else:
                price = super().send_price(item_id)
                if price is None:
                    print("\nไม่พบรหัสสินค้านี้")
                    exit()
                money = self.calculate.change(money, price)
                self.continues._chack_out()
