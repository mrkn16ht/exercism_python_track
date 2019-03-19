#marked with comment(#) is the original value

#class HighScores(object):
#   def __init__(self, scores):
#        pass

class HighScores(object):
    def __init__(self, scores):
        self.scores = scores

    def latest(self):
        return self.scores[-1]
    
    def personal_best(self):
        return max(self.scores)

    def personal_top_three(self):
        descending_scores = sorted(self.scores, reverse = True)
        return descending_scores[:3]
