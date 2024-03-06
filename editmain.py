# items = {
#     "Items": [
#         {"id": 1, "name": "น้ำเปล่า", "price": 10},
#         {"id": 2, "name": "น้ำลีโอ", "price": 17},
#         {"id": 3, "name": "น้ำสิงห์", "price": 17},
#         {"id": 4, "name": "โค้ก", "price": 15},
#         {"id": 5, "name": "ชาเขียว", "price": 15},
#         {"id": 6, "name": "เบียร์ช้าง", "price": 25},
#         {"id": 7, "name": "สปอร์ตแชมป์", "price": 30},
#         {"id": 8, "name": "เบียร์สิงห์", "price": 20},
#         {"id": 9, "name": "น้ำดื่มมิเนอรัลไลท์", "price": 20},
#         {"id": 10, "name": "น้ำปลา", "price": 25},
#     ]
# }


# class Item:

#     def __init__(self, data):
#         self.data = data

#     def __str__(self):
#         for item in self.data["Items"]:
#             print(
#                 "รหัสสินค้า : {} ชือสินค้า : {} ราคา : {} บาท".format(
#                     item["id"], item["name"], item["price"]
#                 )
#             )

#     def send_ids(self, id):
#         for item in self.data["Items"]:
#             if item["id"] == id:
#                 return item["id"]

#     def send_name(self, id):
#         for item in self.data["Items"]:
#             if item["id"] == id:
#                 return item["name"]

#     def send_price(self, id):
#         for item in self.data["Items"]:
#             if item["id"] == id:
#                 return item["price"]


# class Continue(Item):

#     def __init__(self):
#         pass

#     def _chack_out(self):
#         out = int(input("ต้องการทำรายการต่อกด 1 หยุดการทำรายการกด 2 : ").strip())
#         if out == 1:
#             pass
#         elif out == 2:
#             print("จบการทำรายการ")
#             exit()
#         else:
#             print("รหัสไม่ถูกต้อง")

#     def _chack_money(self):
#         money = int(input("ถ้าต้องการเติมเงินเพิ่มกด 1 หยุดการทำรายการกด 2 : ").split())
#         if money == 1:
#             pass
#         elif money == 2:
#             print("จบการทำรายการ")
#             exit()
#         else:
#             print("รหัสไม่ถูกต้อง")


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


# class Findproducts(Item):

#     def __init__(self):
#         self.items = Item(items)
#         self.calculate = Calculate()
#         self.continues = Continue()
#         super().__init__(items)

#     def findproduct(self, money):
#         while True:
#             super().__str__()
#             item_id = int(input("กรุณากรอกรหัสสินค้า : ").strip())
#             price = super().send_price(item_id)
#             if price is None:
#                 print("ไม่พบสินค้าที่ตรงกับรหัสที่ให้")
#                 exit()
#             money = self.calculate.change(money, price)
#             if money < 0:
#                 print("เงินของคุณไม่เพียงพอ")
#                 return
#             self.continues._chack_out()


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
#             self.continues._chack_money()

#         self.findproducts.findproduct(money)


# inputmoney = InputMoney()
# inputmoney._input_money()


from Dataitem import items
from playsound import playsound


class Item:

    def __init__(self, data):
        self.data = data

    def __str__(self):
        for item in self.data["Items"]:
            print(
                "รหัสสินค้า : {} {} {} บาท".format(item["id"], item["name"], item["price"])
            )

    def send_ids(self, id):
        for item in self.data["Items"]:
            if item["id"] == id:
                return item["id"]

    def send_name(self, id):
        for item in self.data["Items"]:
            if item["id"] == id:
                return item["name"]

    def send_price(self, id):
        for item in self.data["Items"]:
            if item["id"] == id:
                return item["price"]


class Continue(Item):

    def __init__(self):
        pass

    def _chack_out(self):
        out = int(
            input("\nต้องการทำรายการต่อกด [1] หากไม่ต้องการทำรายการต่อกด [2]: ").strip()
        )
        if out == 1:
            pass
        elif out == 2:
            print("\nจบการทำรายการ")
            exit()


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

            if item_id == 0:
                self._top_up_money(money)
            else:
                price = super().send_price(item_id)
                if price is None:
                    print("ไม่พบสินค้าที่ตรงกับรหัสที่ให้")
                    exit()
                money = self.calculate.change(money, price)
                if money < 0:
                    print("เงินของคุณไม่เพียงพอ")
                    self._input_money()  # เรียกใช้งาน _input_money หากเงินไม่เพียงพอ
                self.continues._chack_out()

    def add_money(self, current_money):
        amount = int(input("\nกรุณาเติมเงินเพิ่ม: ").strip())
        current_money += amount
        print("\nยอดเงินของคุณมี", current_money, "บาท", "\n")


# class InputMoney(Item):

#     def __init__(self):
#         self.items = Item(items)
#         self.calculate = Calculate()
#         self.continues = Continue()
#         self.findproducts = Findproducts()
#         super().__init__(items)

#     def _input_money(self):
#         # playsound ('doorbell1.mp3')
#         money = int(input("\nกรุณาเติมเงินของคุณเพื่อทำการซื้อสินค้า : ").strip())
#         self.continues._chack_out()

#         # เรียกเมธอดใหม่สำหรับเติมเงินเพิ่มหากต้องการ
#         self._top_up_money(money)

#     def _top_up_money(self, money):
#         top_up_option = int(
#             input(
#                 "\nต้องการเติมเงินเพิ่มหรือไม่? (กด [1] เพื่อเติมเงินเพิ่ม, กด [2] เพื่อไม่เติมเงินเพิ่ม): "
#             ).strip()
#         )
#         if top_up_option == 1:
#             amount = int(input("\nกรุณาเติมเงินเพิ่ม: ").strip())
#             money += amount
#             print("\nยอดเงินของคุณมี", money, "บาท", "\n")
#         elif top_up_option == 2:
#             print("\nยอดเงินของคุณไม่มีการเปลี่ยนแปลง")
#         else:
#             print("\nตัวเลือกไม่ถูกต้อง")
#             self._top_up_money(money)  # เรียกเมธอดอีกครั้งถ้าผู้ใช้ป้อนตัวเลือกที่ไม่ถูกต้อง
#         self.findproducts.findproduct(money)


class InputMoney(Item):

    def __init__(self):
        self.items = Item(items)
        self.calculate = Calculate()
        self.continues = Continue()
        self.findproducts = Findproducts()
        super().__init__(items)

    def _input_money(self):
        # playsound ('doorbell1.mp3')
        money = int(input("\nกรุณาเติมเงินของคุณเพื่อทำการซื้อสินค้า : ").strip())
        self.continues._chack_out()

        # เรียกเมธอดใหม่สำหรับเติมเงินเพิ่มหากต้องการ
        self._top_up_money(money)

    def _top_up_money(self, money):
        top_up_option = int(
            input(
                "\nต้องการเติมเงินเพิ่มหรือไม่? (กด [1] เพื่อเติมเงินเพิ่ม, กด [2] เพื่อไม่เติมเงินเพิ่ม): "
            ).strip()
        )
        if top_up_option == 1:
            amount = int(input("\nกรุณาเติมเงินเพิ่ม: ").strip())
            money += amount
            print("\nยอดเงินของคุณมี", money, "บาท", "\n")
        elif top_up_option == 2:
            print("\nยอดเงินของคุณไม่มีการเปลี่ยนแปลง")
        else:
            print("\nตัวเลือกไม่ถูกต้อง")
            self._top_up_money(money)  # เรียกเมธอดอีกครั้งถ้าผู้ใช้ป้อนตัวเลือกที่ไม่ถูกต้อง
        self.findproducts.findproduct(money)


inputmoney = InputMoney()
inputmoney._input_money()


inputmoney = InputMoney()
inputmoney._input_money()
