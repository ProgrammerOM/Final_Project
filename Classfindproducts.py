from Dataitem import items
from Classitem import Item
from Classcontinue import Continue
from Classcalculate import Calculate


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
