class India():
    def capital(self):
        print("india capital is  new delhi")

    def language(self):
        print("india language is india ")

    def type(self):
        print("type is kos sher")


class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is a developed country.")



objectIndia= India()
objectUsa =USA()

for country in (objectIndia, objectUsa):
    country.capital()
    country.language()
    country.type()