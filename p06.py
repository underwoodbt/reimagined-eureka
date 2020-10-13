class Animal:
    def __init__(self, name=None):
        self._name = name
        self._hunger_level = 0

    def set_hunger_level(self, hunger_level):
        if hunger_level < 0:
            self._hunger_level = 0

        if hunger_level > 10:
            self._hunger_level = 10
        
        else:
            self._hunger_level = hunger_level

    def get_hunger_level(self):
        return self._hunger_level

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def sleep(self):
        print('sleeping...')
        self.set_hunger_level(10)

    def roam(self):
        print('moving around...')
        self.set_hunger_level(self.get_hunger_level() + 1)
        
    def make_noise(self):
        raise NotImplementedError('make_noise not implemented')

    def eat(self):
        raise NotImplementedError('eat not implemented')


class Pet:
    def play(self):
        raise NotImplementedError('make_noise not implemented')
    
    def be_friendly(self):
        raise NotImplementedError('make_noise not implemented')


class Canine(Animal):
    def roam(self):
        print('canines like to roam in packs...')
        # TODO: update hunger level


class Feline(Animal):
    def roam(self):
        print('felines like to roam alone...')
        # TODO: update hunger level


class Wolf(Canine):
    def make_noise(self):
        print('growl...')

    def eat(self):
        print('rip with teeth...')
        
class Cat(Feline, Pet):
    def make_noise(self):
        print('meow...')

    def eat(self):
        print('pick...')
    
    def play(self):
        print('scracth...')

class Dog(Canine, Pet):
    def make_noise(self):
        print('bark...')

    def eat():
        print('rip with teeth')

class Lion(Feline):
    def make_noise(self):
        print('roar...')
    
    def eat():
        print('rip with teeth...')

class Hippo(Animal):
    def make_noise(self):
        print('blub...')

    def eat(self):
        print('slurp...')


class Zoo:
    def __init__(self, name=None):
        self._name = name
        self._zoo_animals = []

    # TODO: add the "add animal" method

    # TODO: "test animals" method


# TODO: main function
def main():
    pass


if __name__ == '__main__':
    main()