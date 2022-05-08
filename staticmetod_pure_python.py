class StaticMethod:

    def __init__(self, f):
        self.f = f

    def __get__(self, obj, objtype=None):
        return self.f

    def __call__(self, *args, **kwds):
        return self.f(*args, **kwds)


class Person:
    def say_hello(self):
        print('Hello')

    # @staticmethod
    def goodbye(StaticMethod):
        print('Goodbye')


p = Person()
p.goodbye()
