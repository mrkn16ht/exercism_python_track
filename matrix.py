
#marked with comment(#) is the original value

#class Matrix(object):
#    def __init__(self, matrix_string):
#        pass

#    def row(self, index):
#        pass

#    def column(self, index):
#        pass


#marked with comment(#) for reminder
class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix = matrix_string.split('\n')
        #split('\n') for delete newlines

    def row(self, index):
        return [int(a) for a in self.matrix[index-1].split(' ')]
        #use index, split, comprehensive list
        #1. [index-1] for select index , split(' ') for delete space 
        #2. [int(a) for a in.. ] for convert str to int

    def column(self, index):
        return [int(a.split(' ')[index-1]) for a in self.matrix]
        #use split, index, comprehensive list
        #1. split(' ') for delete space between string
        #2. [index-1] for select index        
        #3. [int(a...for a in...] for convert str to int
