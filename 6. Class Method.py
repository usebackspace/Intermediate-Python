class Bike:
    price_hiked=0

# When we use instance method changes reflect on current object
    # @classmethod
    def increased_price(self,price):
        self.price_hiked = price*0.2 +price

# When we use class method changes reflect on all object
    # @classmethod
    # def increased_price(cls,price):
    #     cls.price_hiked = price*0.2 +price


apache= Bike()
yamaha= Bike()
ninja= Bike()

apache.increased_price(10000)
yamaha.increased_price(100)


print(f'Hiked price of Apcahe: {apache.price_hiked}')
print(f'Hiked price of Yahama" {yamaha.price_hiked}')
print(f'Hiked price of Ninja: {ninja.price_hiked}')


