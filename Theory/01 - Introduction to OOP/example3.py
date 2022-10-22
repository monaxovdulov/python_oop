
class Cat:

    def meow(self):
        print("MEOOOAW!!!")
        print(self)


cat1 = Cat()
print(cat1)
print(cat1.__dict__)
cat1.name = "Murzik"

# print(cat1.__dict__)
# print(dir(cat1))

cat2 = Cat()
cat2.meow()

 