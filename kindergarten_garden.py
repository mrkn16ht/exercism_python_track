#marked with comment(#) is the original value

#class Garden(object):
#    def __init__(self, diagram, students):
#        pass

class Garden(object):
    students_def = ['Alice', 'Bob', 'Charlie', 
                    'David', 'Eve', 'Fred', 
                    'Ginny', 'Harriet', 'Ileana', 
                    'Joseph', 'Kincaid', 'Larry']

    def __init__(self, diagram, students=students_def):
        self.diagram = diagram.splitlines()
        self.students = sorted(students)
    
    def plants(self, student):
        plants = {'G': 'Grass', 'C': 'Clover', 'R': 'Radishes', 'V': 'Violets'}
        student_idx = self.students.index(student)
        row1a = plants[self.diagram[0][(student_idx*2)]]
        row1b = plants[self.diagram[0][(student_idx*2+1)]]
        row2a = plants[self.diagram[1][(student_idx*2)]]
        row2b = plants[self.diagram[1][(student_idx*2+1)]]
        return [row1a, row1b, row2a, row2b]