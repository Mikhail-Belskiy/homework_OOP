class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = [] #пройденые курсы
        self.courses_in_progress = [] #изучаются сейчас
        self.grades = {} #оценки

    def graiding_lecturer(self, lecturer, course, grade):
        if isinstance (lecturer, Lecturer) and course in lecturer.courses_attached and course in self.finished_courses:
            if lecturer.grades.get(course, None):
                    lecturer.grades[course].append(grade)
            else:
                    lecturer.grades[course] = [grade]
        else:
            print('Вы не можете оценить преподавателя')

        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = [] #список курсов которые ведут 
        
    

class Lecturer (Mentor):
    def __init__(self, name, surname, *grades):
        super().__init__(name, surname)
        self.grades= {}
       

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
            return print ('Нелья оценить этого студента')
    


student_1 = Student ('Bonya', 'Belskaya', 'W')
student_1.finished_courses = ['Введение в програмирование']
student_1.courses_in_progress = ['C++', 'Python']

student_2 = Student ('Mikl', 'Petrov', 'M')
student_2.finished_courses = ['Git']
student_2.courses_in_progress = ['Python', 'Основы ОПП']

lector_1 = Lecturer ('Boris', 'Ivanov')
lector_1.courses_attached = ['Python']

lector_2 = Lecturer ('Sergey', 'Kuchenko')
lector_2.courses_attached = ['C++']

reviver_1 = Reviewer ('Sam', 'Kasper')
reviver_1.courses_attached = ['C++', 'Python']

reviver_2 = Reviewer ('Sam', 'Kasper')
reviver_2.courses_attached = ['C++', 'Git']

 
reviver_1.rate_hw(student_1, 'Python', 10)
reviver_1.rate_hw(student_1, 'Python', 10)
reviver_1.rate_hw(student_1, 'Python', 10)

student_1.graiding_lecturer(lector_1, 'Python', 10)

print(student_1.grades)
print(lector_1.grades)