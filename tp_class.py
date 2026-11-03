
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



# votre code

class Classe:
    def __init__(self, classname: str):
        self.classname = classname
        self.classe = defaultdict(list)

    def add_student(self, student: Student):
        self.classe[(student.first_name, student.last_name)] = student

    def __len__(self):
        return len(self.classe)

    def get_student(self, first_name: str, last_name: str):
        if (first_name, last_name) in self.classe:
            return self.classe[(first_name, last_name)]
        else:
            return None
    def load_students_from_file(self, filename: str):
        with open(filename, 'r', encoding='utf-8') as fichier:
            for line in fichier:
                noms = line.strip().split(',')
                student = Student(noms[0], noms[1])
                Classe.add_student(self, student)

    def load_grades_from_file(self, filename: str):
        with open(filename, 'r', encoding='utf-8') as fichier:
            for line in fichier:
                infos = line.strip().split(',')
                student = Student(infos[0], infos[1])
                if Classe.get_student(self, infos[0], infos[1]) is None:
                    print(f"L'élève {infos[0]} {infos[1]} n'est pas dans la classe")
                    continue
                else:
                    course = infos[2]
                    notes = list(map(float, infos[3:]))
                    for i in notes:
                        student.add_grade(course, i)

    def catalog(self):
        catalogue = defaultdict(int)
        for student in self.classe:
            for matiere in Student.followed_topics(student):
                catalogue[matiere] +=1
        return catalogue

    def compute_averages(self):
        dico = defaultdict(int)
        for student in self.classe:
            for matiere in Student.followed_topics(student):
                dico[matiere][0] += Student.compute_average(student, matiere)
                dico[matiere][1] += 1
        for matiere in dico.keys():
            dico[matiere][0] = dico[matiere][0]/dico[matiere][1]
        return dico


    def __repr__(self):
        return f"Class({self.classname}, Students: {self.classe})"




