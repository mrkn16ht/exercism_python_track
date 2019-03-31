#marked with comment(#) is the original value

# class School(object):
#     def __init__(self):
#         pass

#     def add_student(self, name, grade):
#         pass

#     def roster(self):
#         pass

#     def grade(self, grade_number):
#         pass
from operator import itemgetter
class School(object):
    def __init__(self):
        self.students_list=[]

    def add_student(self, name, grade):
        students=(name, grade)
        self.students_list.append(students)
        self.students_list=sorted(self.students_list, key=itemgetter(1,0))

    def roster(self):
        return [(roster[0]) for roster in self.students_list]

    def grade(self, grade_number):
        return [(roster[0]) for roster in self.students_list if roster[1]==grade_number]