class One:
    def __init__(self,name):
        self.name=name

class Two:
    def __init__(self,age):
        self.age=age

class Three(One):
    def profession(self):
        print('profession')

class Four(Two):
    def hobby(self):
        print('hobby')

class Five(Four, Three):
    def __init__(self, name, age):
        Three.__init__(self, name)
        Four.__init__(self, age)

    def __str__(self):
        return f'{self.name} {self.age}'

v = Five ('Beka', 20)
v.profession()
v.hobby()
print(v)




