# A class is like a cookie cutter - it's the template
class Cookie:
    def __init__(self, flavor, size):
        self.flavor = flavor  # Every cookie has a flavor
        self.size = size  # Every cookie has a size
        self.is_baked = False  # New cookies start unbaked

    def bake(self):
        self.is_baked = True
        print(f"The {self.flavor} cookie is baked!")


# Making actual cookies is like creating objects
chocolate_cookie = Cookie("chocolate", "large")
vanilla_cookie = Cookie("vanilla", "small")

# Each cookie is independent
chocolate_cookie.bake()  # Only this cookie gets baked