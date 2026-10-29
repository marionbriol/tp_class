
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




from collections import defaultdict

class Student:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        self.Grades = defaultdict(list)

    def add_grade(self, course: str, grade: float):
        if (0 <= grade <= 20):
            self.Grades[course].append(grade)
        else:
            raise ValueError

    def followed_topics(self):
        topics = []
        for key in self.Grades.keys():
            topics.append(key)
        return topics

    def compute_average(self, course: str):
        moy = 0
        if course in self.Grades:
            moy = sum(self.Grades[course])/len(self.Grades[course])
        else:
            raise ValueError
        return moy

    def report(self):
        L = []

        L.append(f"Report for student {self.first_name} {self.last_name}")
        L.append("+===============+===============+")
        L.append("|     Topic     |    Average    |")
        L.append("+===============+===============+")

        for topic in self.followed_topics():
            L.append(f"|{topic:^15}|{self.compute_average(topic):^15.2f}|")
            L.append("+---------------+---------------+")

        return "\n".join(L)

    def __repr__(self):
        return f"Student({self.first_name} {self.last_name}, Grades: self.Grades)"



# pour tester

try:
    reference_lines = ['Report for student Albert Einstein',
                       '+===============+===============+',
                       '|     Topic     |    Average    |',
                       '+===============+===============+',
                       '|  Mathematics  |     12.80     |',
                       '+---------------+---------------+',
                       '|  Scubadiving  |     12.50     |',
                       '+---------------+---------------+']

    student = Student("Albert", "Einstein")
    student.add_grade("Mathematics", 12.80)
    student.add_grade("Scubadiving", 12.50)
    report = student.report()
    report_lines = report.strip().split('\n')
    assert len(report_lines) == len(reference_lines), \
        f"expected {len(reference_lines)} lines, got {len(report_lines)}"
    for i, (lineref, linestudent) in enumerate(zip(reference_lines, report_lines), start=1):
        assert lineref == linestudent, f"Ligne {i} : \n attendu = {lineref}\n  obtenu = {linestudent}"
except AssertionError as e:
    print("Les deux chaines sont différentes")
    print(e)
except Exception as e:
    print("OOPS - Something's wrong")
    print(f"Error message : {e}")
else:
    print('Congrats ! Your implementation works !')






