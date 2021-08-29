class Reptile:
    def crawl(self):
        pass

    def sting(self):
        pass

class Python(Reptile):
    def crawl(self):
        print("crawling...")

class Snake(Reptile):
    def sting(self):
        print("sting...")

print(issubclass(Python, Reptile))
print(isinstance(Snake(), Reptile))
