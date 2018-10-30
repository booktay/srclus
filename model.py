class Template(object):
    def __init__(self):
        self.value = "hello"
        self.other_value = "bonjour"
        self.constant_value = 42

        for cls in reversed(self.__class__.mro()):
            if hasattr(cls, 'init'):
                cls.init(self)
