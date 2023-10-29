from random import randint
class Batsman:

    def __init__(self, name, country, score_list=[], matches=0):
        self.__name = name
        self.__country = country
        self.scores = score_list
        if matches == 0:
            self.matches = randint(1, 95)
        else:
            self.matches = matches
        self.scores = self._randomScores(matches)
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def country(self):
        return self.__country
    
    @country.setter
    def country(self, new_country):
        self.__country = new_country

    def no_of_matches(self):
        return self.matches
    
    def _randomScores(self, no_of_matches):
        prob = randint(0, 10)
        for i in range(no_of_matches):
            if prob <= 6:
                random_score = randint(0, 180)
            elif prob <= 8:
                random_score = randint(180, 350)
            else:
                random_score = randint(350, 500)
            self.scores.append(random_score)
            print(random_score, end=' ')
        print()
        return self.scores
    
    def calcTotal(self):
        total = 0
        for score in self.scores:
            total += score
        return total
    
    def calcAverage(self):
        total = self.calcTotal()
        average = total // self.matches
        return average
    
    def findMaxScore(self):
        max_score = 0
        for score in self.scores:
            if score > max_score:
                max_score = score
        return max_score
    
    def count50s(self):
        count_50 = 0
        for score in self.scores:
            if score >= 50:
                count_50 += 1
        return count_50

    def count100s(self):
        count_100 = 0
        for score in self.scores:
            if score >= 100:
                count_100 += 1
        return count_100
    
    def show(self):
        print('Player: \t',self.name)
        print('Scores: \t', end=' ')
        self._randomScores(self.matches)
        print('Total: \t\t',self.calcTotal())
        print('Average: \t',self.calcAverage())
        print('Maximum Score: \t',self.findMaxScore())
        print('Fifties: \t',self.count50s())
        print('Hundreds: \t',self.count100s())

def main():
    batsmen = []
    batsmen.append(Batsman('Asim', 'pak', [], 5))
    batsmen.append(Batsman('Ali', 'pak', [], 5))
    batsmen.append(Batsman('Amir', 'pak'))
    for batsman in batsmen:
        batsman.show()
        print()
main()