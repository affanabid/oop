class Player:
    def __init__(self, name, age, team, role, batting_average=0.0, bowling_average=0.0):
        self.name = name
        self.age = age
        self.team = team
        self.role = role
        self.batting_average = batting_average
        self.bowling_average = bowling_average

    def display_player_info(self):
        print(f"Player Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Team: {self.team}")
        print(f"Role: {self.role}")
        if self.role == 'Batsman' or self.role == 'batsman':
            print(f"Batting Average: {self.batting_average}")
        else:
            print(f"Bowling Average: {self.bowling_average}")

    def update_batting_average(self, new_average):
        print("\nUpdating batting average...")
        self.batting_average = new_average

    def update_bowling_average(self, new_average):
        print("\nUpdating bowling average...")
        self.bowling_average = new_average

# player1 = Player("Virat Kohli", 33, "India", "Batsman", batting_average=53.41)
# player2 = Player("Jasprit Bumrah", 28, "India", "Bowler", bowling_average=21.65)

# player1.display_player_info()
# player1.update_batting_average(56.23)0
# player1.display_player_info()

# print("\n")
# player2.display_player_info()
# player2.update_bowling_average(20.15)
# player2.display_player_info()

class BattingStats:
    def __init__(self, fours=0, sixes=0, dot_balls=0, balls_faced=0, runs_scored=0):
        self.fours = fours
        self.sixes = sixes
        self.dot_balls = dot_balls
        self.balls_faced = balls_faced
        self.runs_scored = runs_scored

    def display_batting_stats(self):
        print(f"Fours: {self.fours}")
        print(f"Sixes: {self.sixes}")
        print(f"Dot Balls: {self.dot_balls}")
        print(f"Balls Faced: {self.balls_faced}")
        print(f"Runs Scored: {self.runs_scored}")

    def update_fours(self, count=1):
        self.fours += count

    def update_sixes(self, count=1):
        self.sixes += count

    def update_dot_balls(self, count=1):
        self.dot_balls += count

    def update_balls_faced(self, count=1):
        self.balls_faced += count

    def update_runs_scored(self, runs):
        self.runs_scored += runs


# batting_stats = BattingStats()

# batting_stats.update_fours(2)
# batting_stats.update_sixes(1)
# batting_stats.update_dot_balls(5)
# batting_stats.update_balls_faced(15)
# batting_stats.update_runs_scored(30)

# batting_stats.display_batting_stats()
