class Bracelet:
    def __init__(self, material, color, size):
        self.material = material
        self.color = color
        self.size = size

    def describe(self):
        return f"A {self.color} bracelet made of {self.material}, size {self.size}."

    def resize(self, new_size):
        self.size = new_size
        return f"The bracelet has been resized to {self.size}."


# Derived class (special type of bracelet)
class SmartBracelet(Bracelet):
    def __init__(self, material, color, size, battery_life, features):
        super().__init__(material, color, size) 
        self.battery_life = battery_life
        self.features = features

    def describe(self):
        return (
            f"A smart {self.color} bracelet made of {self.material}, size {self.size}. "
            f"It has {self.battery_life} hours of battery life and features like {', '.join(self.features)}."
        )

    def track_steps(self, steps):
        return f"You walked {steps} steps today!"

    def charge(self):
        self.battery_life = 100
        return "The smart bracelet is now fully charged!"


class LuxuryBracelet(Bracelet):
    def __init__(self, material, color, size, price):
        super().__init__(material, color, size)
        self.__price = price

    def get_price(self):
        return f"This luxury bracelet costs KSh {self.__price}."

    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
            return f"Price updated to KSh {self.__price}."
        return "Invalid price."


if __name__ == "__main__":
    bracelet1 = Bracelet("silver", "blue", "M")
    print(bracelet1.describe())
    print(bracelet1.resize("L"))

    print("-" * 40)

    smart_bracelet = SmartBracelet("plastic", "black", "M", 48, ["heart-rate monitor", "step counter"])
    print(smart_bracelet.describe())
    print(smart_bracelet.track_steps(5432))
    print(smart_bracelet.charge())

    print("-" * 40)

    lux_bracelet = LuxuryBracelet("gold", "red", "S", 5000)
    print(lux_bracelet.describe())
    print(lux_bracelet.get_price())
    print(lux_bracelet.set_price(6000))
