# -*- coding: UTF-8 -*-


# Decorator function for Singleton using decorator
def singleton(cls):
    instances = {}

    def get_instance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return get_instance


# Singleton using decorator
@singleton
class SingletonDecorator:
    # Class implementation here
    pass


# Singleton using __new__ in parent class
class SingletonParent(object):
    __instance = None

    def __new__(cls, *more):
        if not cls.__instance:
            cls.__instance = super(SingletonParent, cls).__new__(cls, *more)
        return cls.__instance
    # Class implementation here

if __name__ == '__main__':
    s1 = SingletonDecorator()
    s2 = SingletonDecorator()
    print("Singleton using decorator (see addresses):")
    print(s1)
    print(s2)

    s3 = SingletonParent()
    s4 = SingletonParent()
    print("\nSingleton using __new__ in parent class (see addresses):")
    print(s3)
    print(s4)
