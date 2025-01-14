import inspect

class Car:
    def __init__(self):
        self.color = 'blue'
        self.number = 'oe235'
    def get_color(self):
        return self.color

    def get_number(self):
        return self.number

def introspection_info(obj):
    return {'type': type(obj), 'attrs': [i for i in dir(obj) if not inspect.ismethod(i) ], 'methods': [i for i in dir(obj) if inspect.ismethod(i)], 'module': inspect.getmodule(obj)}

car = Car()

print(introspection_info(car))

number_info = introspection_info(42)
print(number_info)