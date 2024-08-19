class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = [] #пройденые курсы
        self.courses_in_progress = [] #изучаются сейчас
        self.grades = {} #оценки

    def graiding_lecturer(self, lecturer, course, grade):
        if isinstance (lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if lecturer.grades.get(course, None):
                    lecturer.grades[course].append(grade)
            else:
                    lecturer.grades[course] = [grade]
        else:
            print('Вы не можете оценить преподавателя')

    

    def __str__(self) -> str:
        conclusion = self.get_score()
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашнее задание: {round(conclusion,1)} \nКурсы в процессе обучения: {", ".join(self.courses_in_progress)} \nЗавершённые курсы:{", ".join(self.finished_courses)}'
    
    def get_score(self):
        conclusion = float(0)
        if self.grades:
            for value in self.grades.values():
                conclusion += sum(value)
            conclusion = conclusion/len(self.grades)
        return conclusion

    def __le__(self, other):
        return self.get_score() <= other.get_score()
    def __ge__(self, other):
        return self.get_score() >= other.get_score()
    def __ne__(self, other):
        return self.get_score() != other.get_score()


        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = [] #список курсов которые ведут 
        
    

class Lecturer (Mentor):
    def __init__(self, name, surname, *grades):
        super().__init__(name, surname)
        self.grades= {}

    def __str__(self) -> str:
        conclusion = self.get_score()
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {round(conclusion,1)}'
    
    def get_score(self):
        conclusion = float(0)
        if self.grades:
            for value in self.grades.values():
                conclusion += sum(value)
            conclusion = conclusion/len(self.grades)
        return conclusion    

    def __le__(self, other):
        return self.get_score() <= other.get_score()
    def __ge__(self, other):
        return self.get_score() >= other.get_score()
    def __ne__(self, other):
        return self.get_score() != other.get_score()
       

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)   
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print ('Нелья оценить этого студента')
        
    def __str__(self) -> str:
        return f'Имя: {self.name} \nФамилия: {self.surname}'
   
   

student_1 = Student ('Bonya', 'Belskaya', 'W')
student_1.finished_courses = ['Введение в програмирование']
student_1.courses_in_progress = ['C++', 'Python']

student_2 = Student ('Mikl', 'Petrov', 'M')
student_2.finished_courses = ['Git']
student_2.courses_in_progress = ['Python', 'Основы ОПП']

lector_1 = Lecturer ('Boris', 'Ivanov')
lector_1.courses_attached = ['Python', 'C++', 'Введение в програмирование' ]

lector_2 = Lecturer ('Sergey', 'Kuchenko')
lector_2.courses_attached = ['C++', 'Python', 'Основы ОПП']

reviver_1 = Reviewer ('Sam', 'Kasper')
reviver_1.courses_attached = ['C++', 'Python']

reviver_2 = Reviewer ('Sam', 'Kasper')
reviver_2.courses_attached = ['C++', 'Git']

 
reviver_1.rate_hw(student_1, 'Python', 10)
reviver_1.rate_hw(student_1, 'C++', 8)
reviver_1.rate_hw(student_2, 'Python', 10)

student_1.graiding_lecturer(lector_1, 'Python', 9)
student_1.graiding_lecturer(lector_2, 'Python', 5)


#print(student_1.grades)
#print(lector_1.grades)
print(student_1)
print(lector_1)
print(reviver_1)

def average_rating_students (Students: list, course: str):
    rating, count = 0, 0
    for student in Students:
        if student.grades.get(course, None):
            rating += sum(student.grades[course])
            count +=1
            if count !=0:
                return rating/count
            else:
                return 'нет оценок'
    
print (average_rating_students ([student_1, student_2], 'Python'))


def average_rating_lector (lectors: list, course: str):
    rating, count = 0, 0
    for lector in lectors:
        if lector.grades.get(course, None):
            rating += sum(lector.grades[course])
            count +=1
            if count !=0:
                return rating/count
            else:
                return 'нет оценок'
            
print (average_rating_students ([lector_1, lector_2], 'Python'))
