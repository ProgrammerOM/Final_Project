from Classitem import Item


class Continue(Item):

    def __init__(self):
        pass

    def _chack_out(self):
        out = int(input("ต้องการทำรายการต่อกด 1 หยุดการทำรายการกด 2 : ").strip())
        if out == 1:
            pass
        elif out == 2:
            print("จบการทำรายการ")
            exit()
        else:
            print("รหัสไม่ถูกต้อง")
