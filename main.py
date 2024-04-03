class Zoo():
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.collaborators = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_collaborator(self, collaborator):
        self.collaborators.append(collaborator)

    def animal_sound(self):
        for animal in self.animals:
            animal.make_sound()

    def animal_eat(self):
        for animal in self.animals:
            animal.eat_animal(animal.eat)


class ZooKeeper():
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f'{self.name} кормит {animal.name}')
        animal.eat_animal(animal.eat)


class Veterinarian():
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f'{self.name} лечит {animal.name}')
        print(f'{animal.name} успешно вылечен!')


class Animal():
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound

    def make_sound(self):
        print(f'{self.name} издает звук {self.sound}')

    def eat_animal(self, food):
        print(f'{self.name} ест {food}')


class Bird(Animal):
    def __init__(self, name, age, sound, eat):
        super().__init__(name, age, sound)
        self.eat = eat


class Mammal(Animal):
    def __init__(self, name, age, sound, eat):
        super().__init__(name, age, sound)
        self.eat = eat


class Reptile(Animal):
    def __init__(self, name, age, sound, eat):
        super().__init__(name, age, sound)
        self.eat = eat


# Создаем экземпляр зоопарка
zoo = Zoo('Зоопарк')

# Создаем экземпляры сотрудников
keeper = ZooKeeper('Иван')
vet = Veterinarian('Мария')

# Добавляем сотрудников в зоопарк
zoo.add_collaborator(keeper)
zoo.add_collaborator(vet)

# Создаем экземпляры животных
raven = Bird('Ворон', 3, 'каркает', 'зерно')
eagle = Bird('Орёл', 5, 'клекот', 'мясо')
wolf = Mammal('Волк', 7, 'рычит', 'мясо')
antelope = Mammal('Антилопа', 4, 'мычит', 'траву')
varan = Reptile('Варан', 2, 'шипит', 'мясо')

# Добавляем животных в зоопарк
zoo.add_animal(raven)
zoo.add_animal(eagle)
zoo.add_animal(wolf)
zoo.add_animal(antelope)
zoo.add_animal(varan)

# Сотрудники кормят животных
zoo.animal_eat()

# Ветеринар лечит животных
for animal in zoo.animals:
    vet.heal_animal(animal)

# Животные издают звуки
zoo.animal_sound()
