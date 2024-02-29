from dataclasses import dataclass
from re import M


@dataclass
class adress:
    city: str
    country: str
    pincode: int


""" green i love green \n """


@dataclass
class person:
    name: str
    age: int
    address: adress
    weight: float
    hight: float
    married: bool

    def bmi(self) -> int:
        bmi = self.weight / self.hight**2
        return int(bmi)


matt = person("Matt", 30, adress("London", "UK", 12345), 68.5, 1.75, True)

# ------------main-function-after-this


def main():
    {
        print(matt)  # raw output
    }
    # formatted output
    print(f"{matt.name} is {matt.age} years old")
    print(f"{matt.address.city} is in {matt.address.country}")
    print(f"{matt.weight} kg and {matt.hight} m bmi is {
          matt.bmi()}")
    if matt.married:
        print(f"{matt.name} is married")
        pass
    pass


main()


# ------------nothing-below-this
