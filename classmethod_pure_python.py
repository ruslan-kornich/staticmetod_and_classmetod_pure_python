class ClassMethod(object):

    def __init__(self, f):
        self.f = f

    def __get__(self, obj, cls=None):
        if cls is None:
            cls = type(obj)

        def new_function(*args):
            return self.f(cls, *args)

        return new_function


name = 'Ivan'


class Person:
    name = 'Dima'

    @ClassMethod
    #@classmethod
    def change_name(cls, name):
        cls.name = name


p = Person()
print(p.__dict__)
p.change_name('Boris')

print('Instance dict:', p.__dict__)
print('Person.name:', Person.name)
