class MyMeta(type):
    def __new__(cls, name, bases, attrs):
        attrs['my_attr'] = "hello world"
        return super().__new__(cls, name, bases, attrs)


class MyClass(metaclass=MyMeta):
    pass


object = MyClass()
print(object.my_attr)
