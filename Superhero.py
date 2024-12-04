class Superhero:
    def __init__(self, name, power, city, secret_identity):
        self.name = name
        self.power = power
        self.city = city
        self.secret_identity = secret_identity

    def use_power(self):
        return f"{self.name} uses their power: {self.power}!"

    def save_the_day(self):
        return f"{self.name} saves the day in {self.city}!"

    def reveal_identity(self):
        return f"My true identity is {self.secret_identity}."
      class FlyingSuperhero(Superhero):
    def __init__(self, name, power, city, secret_identity, flight_speed):
        super().__init__(name, power, city, secret_identity)
        self.flight_speed = flight_speed  # Speed in km/h

    def fly(self):
        return f"{self.name} is flying at {self.flight_speed} km/h!"

    def save_from_fall(self):
        return f"{self.name} swoops down to save someone from falling!"
      
# Creating an instance of Superhero
batman = Superhero("Batman", "Intelligence and gadgets", "Gotham", "Bruce Wayne")
print(batman.use_power())  # Batman uses their power: Intelligence and gadgets!
print(batman.save_the_day())  # Batman saves the day in Gotham!
print(batman.reveal_identity())  # My true identity is Bruce Wayne.

# Creating an instance of FlyingSuperhero
superman = FlyingSuperhero("Superman", "Super strength", "Metropolis", "Clark Kent", 1000)
print(superman.use_power())  # Superman uses their power: Super strength!
print(superman.fly())  # Superman is flying at 1000 km/h!
print(superman.save_from_fall())  # Superman swoops down to save someone from falling!


