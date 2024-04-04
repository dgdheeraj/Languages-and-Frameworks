class Singleton:
    instance = None
    def __init__(self):
        if Singleton.instance:
            raise Exception("Please call the getInstance() method!")
        Singleton.instance = self
    @classmethod
    def getInstance(cls):
        if not cls.instance:
            cls.instance = Singleton()
        return cls.instance

obj = Singleton()
obj2 = Singleton.getInstance()
print(obj==obj2)