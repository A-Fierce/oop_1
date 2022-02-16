class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    def add_courses(self, course_name):
        self.finished_course.append(course_name)

    def rate_lc(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __avg_grade(self):
        grades = self.grades
        grade_list = []
        for grade_dict in grades.values():
            for grade_values in grade_dict:
                grade_list.append(grade_values)
        avg_l = sum(grade_list) / len(grade_list)
        return round (avg_l, 2)

    def __courses_in_progress_str(self):
        return ', '.join(self.courses_in_progress)

    def __finished_courses_str(self):
        return ', '.join(self.finished_courses)

    def __str__(self):
        some_student = f'Имя: {self.name}\nФамилия: {self.surname},\nСредняя оценка за домашние задания: {self.__avg_grade()}\n' \
                       f'Курсы в процессе изучения: {self.__courses_in_progress_str()}\nЗавершенные курсы: {self.__finished_courses_str()}'
        return some_student

    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Not a Student!'
        return self.avg_grade() < other.avg_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __avg_grade(self):
        grades = self.grades
        grade_list = []
        for grade_dict in grades.values():
            for grade_values in grade_dict:
                grade_list.append(grade_values)
        avg_l = sum(grade_list) / len(grade_list)
        return round(avg_l, 2)


    def __str__(self):
        some_lecturer = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.__avg_grade()}'
        return some_lecturer

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Not a Lecturer!'
        return self.avg_grade() < other.avg_grade()

class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


    def __str__(self):
        some_reviewer = f'Имя: {self.name}\nФамилия: {self.surname}'
        return some_reviewer



best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['C++']
best_student.finished_courses += ['Java']

best_student2 = Student('Ruoy2', 'Eman2', 'your_gender2')
best_student2.courses_in_progress += ['Python']
best_student2.courses_in_progress += ['C++']
best_student2.finished_courses += ['Java']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer2 = Reviewer('Some2', 'Buddy2')
cool_reviewer2.courses_attached += ['Python']
cool_reviewer2.courses_attached += ['C++']

cool_lecturer = Lecturer('Some1', 'Buddy1')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['C++']
cool_lecturer2 = Lecturer('Some2', 'Buddy2')
cool_lecturer2.courses_attached += ['Python']
cool_lecturer2.courses_attached += ['Java']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'Python', 10)

cool_reviewer2.rate_hw(best_student2, 'C++', 5)
cool_reviewer2.rate_hw(best_student2, 'C++', 8)
cool_reviewer2.rate_hw(best_student2, 'C++', 1)
cool_reviewer2.rate_hw(best_student2, 'Python', 4)
cool_reviewer2.rate_hw(best_student2, 'Python', 8)

best_student.rate_lc(cool_lecturer, 'Python', 1)
best_student.rate_lc(cool_lecturer, 'Python', 5)
best_student.rate_lc(cool_lecturer, 'C++', 5)
best_student.rate_lc(cool_lecturer, 'C++', 2)
best_student.rate_lc(cool_lecturer2, 'Python', 1)
best_student.rate_lc(cool_lecturer2, 'Python', 2)

st_list = [best_student, best_student2]

def avg_students(students_list, students_course):
    key_list = []
    for student in students_list:
        if student.grades.get(students_course) != None:
            grades_one_course = student.grades.get(students_course)
            for grade_list_one in grades_one_course:
                key_list.append(grade_list_one)
    key_avg = sum(key_list) / len(key_list)
    print(f'Средняя оценка за дз на курсе {students_course} - {round(key_avg, 2)}')

avg_students(st_list, 'Python')

lc_list = [cool_lecturer, cool_lecturer2]

def avg_lectures(lect_list, lect_course):
    key_list = []
    for student in lect_list:
        if student.grades.get(lect_course) != None:
            grades_one_course = student.grades.get(lect_course)
            for grade_list_one in grades_one_course:
                key_list.append(grade_list_one)
    key_avg = sum(key_list) / len(key_list)
    print(f'Средняя оценка за лекции на курсе {lect_course} - {round(key_avg, 2)}')

avg_lectures(lc_list, 'Python')






