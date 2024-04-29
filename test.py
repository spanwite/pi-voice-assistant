class Test:
    value = 1
    def hello_world(self):
        print(self.value)

test = Test()
foo = getattr(Test, 'hello_world')

foo(test)