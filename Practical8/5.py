class Lion:
    def roar(self):
        self.legs = 4
        self._ears = 2 #protected
        self.__mane = "thick" #private
        print(self.__mane)

class Cub(Lion):
    def play(self):
        print(self._ears)

pr = Cub()
pr.roar()
pr.play()
print(pr.legs)
