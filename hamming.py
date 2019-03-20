#marked with comment(#) is the original value

#def distance(strand_a, strand_b):
#    pass

def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('The sequences of two strands should have the same length.')
    
    hamming_distance = 0
    for index in range(0, len(strand_a)):
        if strand_a[index] != strand_b[index]:
            hamming_distance +=1
    return hamming_distance
