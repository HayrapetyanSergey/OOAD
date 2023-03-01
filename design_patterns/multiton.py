class Multiton:
    instances = {}
    limit = 0

    def __new__(cls, key):
        if key in cls.instances:
            return cls.instances[key]
        if len(cls.instances) >= cls.limit:
            raise ValueError(f"Can't create more than {cls.limit} instances")
        instance = super().__new__(cls)
        cls.instances[key] = instance
        return instance

Multiton.limit = 3
instance1 = Multiton("key1")
instance2 = Multiton("key2")
instance3 = Multiton("key3")
# Raises ValueError:
instance4 = Multiton("key4")
# Returns the same instance as instance1:
instance1_again = Multiton("key1")