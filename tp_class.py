
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def norm(self):
        return (self.x**2 + self.y**2)**0.5

    def __repr__(self):
        return f"Point({self.x}, {self.y})" 


p = Point(3, 4)
print(p.norm())
print(Point.norm(p)) #Cela renvoie la même chose
#2. Si on enlève self des arguments de norm(), on obtient le message d'erreur "TypeError: norm() takes 0 positional arguments but 1 was given" lorsque qu'on appelle p.norm()
print(p) #3. On a <__main__.Point object at 0x107c5bfd0> si on enlève le repr

class Bad:

    def __init__(self, items):
        self.items = []
    

    def add(self, x):
        self.items.append(x)

a, b = Bad([]), Bad([])
a.add(1)
print(b.items)
print(a.items)

# On voit que b = [1], a et b sont modifiés en même temps même si on n'appelle que a. On a ceci car les deux instances partagent 
# On ajoute un init pour définir items comme une instance non commune


class Tirelire:

    def __init__(self):
        self.pieces = []

    def deposit(self, value: float):
        if value <= 0:
            raise ValueError
        else:
            self.pieces.append(value)

    def total(self):
        t = 0
        for x in self.pieces:
            t += x
        return t

    def __len__(self):
        l = 0
        for x in self.pieces:
            l += 1
        return l

    def __repr__(self):
        return f"Tirelire({self.__len__()} coins, total={self.total()})"



