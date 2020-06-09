class Lilies:
    def __init__(self, name, petals, price):
        self.name = str(name)
        self.petals = int(petals)
        self.price = float(price)

    def introduce_self(self):
        return (f"The name of the flower is {self.name} it has {self.petals} and it costs {self.price}")

lily1 = Lilies("Tiger Lily",6,8.4)
lily2 = Lilies("Casablanca Lily",5,6.5)

print(lily1.price)
