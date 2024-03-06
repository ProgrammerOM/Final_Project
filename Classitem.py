class Item:

    def __init__(self, data):
        self.data = data

    def __str__(self):
        for item in self.data["Items"]:
            print(
                "รหัสสินค้า : {} ชือสินค้า : {} ราคา : {} บาท".format(
                    item["id"], item["name"], item["price"]
                )
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
