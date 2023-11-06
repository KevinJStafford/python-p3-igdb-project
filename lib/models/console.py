import ipdb 

class Console:

    def __init__ (self, console_name):
        self.name = console_name

    def console_type (self):
        print(f"I love this {self.name} so much!!")


ipdb.self_trace()