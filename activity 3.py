class India():
    def Capital(self):
        print("New Delhi is the capital of India.")
    def Language(self):
        print("Hindi is the language of India.")
    def Type(self):
        print("India is a developing country.")
class USA():
    def Capital(self):
        print("Washington DC is the capital of USA.")
    def Language(self):
        print("English is the language of USA.")
    def Type(self):
        print("USA is a developed country.")
obj_ind = India()
obj_usa = USA()
for country in (obj_ind,obj_usa):
    country.Capital()
    country.Language()
    country.Type()