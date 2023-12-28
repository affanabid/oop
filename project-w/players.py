class BattingStats:
    def __init__(self, fours=0, sixes=0, dot_balls=0, balls_faced=0, runs_scored=0):
        self.fours = fours
        self.sixes = sixes
        self.dot_balls = dot_balls
        self.balls_faced = balls_faced
        self.runs_scored = runs_scored

    def display_batting_stats(self):
        print('\n****** Batsman Stats ******')
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


class BowlerStats:
    def __init__(self, maiden_overs=0, fours=0, sixes=0, ones=0, twos=0, threes=0, wide_balls=0, no_balls=0,
                 runs_received=0, total_overs_bowled=0.0, economy=0.0):
        self.maiden_overs = maiden_overs
        self.fours = fours
        self.sixes = sixes
        self.ones = ones
        self.twos = twos
        self.threes = threes
        self.wide_balls = wide_balls
        self.no_balls = no_balls
        self.runs_received = runs_received
        self.total_overs_bowled = total_overs_bowled
        self.economy = economy

    def display_bowling_stats(self):
        print('\n****** Bowler Stats ******')
        print(f"Maiden Overs: {self.maiden_overs}")
        print(f"Fours: {self.fours}")
        print(f"Sixes: {self.sixes}")
        print(f"Ones: {self.ones}")
        print(f"Twos: {self.twos}")
        print(f"Threes: {self.threes}")
        print(f"Wide Balls: {self.wide_balls}")
        print(f"No Balls: {self.no_balls}")
        print(f"Runs Received: {self.runs_received}")
        print(f"Total Overs Bowled: {self.total_overs_bowled}")
        print(f"Economy: {self.economy:.2f}")

    def update_maiden_overs(self, count=1):
        self.maiden_overs += count

    def update_fours(self, count=1):
        self.fours += count

    def update_sixes(self, count=1):
        self.sixes += count

    def update_ones(self, count=1):
        self.ones += count

    def update_twos(self, count=1):
        self.twos += count

    def update_threes(self, count=1):
        self.threes += count

    def update_wide_balls(self, count=1):
        self.wide_balls += count

    def update_no_balls(self, count=1):
        self.no_balls += count

    def update_runs_received(self, runs):
        self.runs_received += runs

    def update_overs_bowled(self, overs):
        self.total_overs_bowled += overs

    def update_economy(self):
        if self.total_overs_bowled > 0:
            self.economy = self.runs_received / self.total_overs_bowled


class Player:
    def __init__(self, name, age, team, role, batting_average=0.0, bowling_average=0.0, batting_stat=(), bowler_stat=()):
        self.name = name
        self.age = age
        self.team = team
        self.role = role
        self.batting_average = batting_average
        self.bowling_average = bowling_average
        self.batsman = BattingStats(*batting_stat)
        self.bowler = BowlerStats(*bowler_stat)

    def display_player_info(self):
        print(f"Player Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Team: {self.team}")
        print(f"Role: {self.role}")
        if self.role.lower() == 'batsman':
            print(f"Batting Average: {self.batting_average}")
            self.batsman.display_batting_stats()
        else:
            print(f"Bowling Average: {self.bowling_average}")
            self.bowler.display_bowling_stats()

    def update_batting_average(self, new_average):
        print("\nUpdating batting average...")
        self.batting_average = new_average

    def update_bowling_average(self, new_average):
        print("\nUpdating bowling average...")
        self.bowling_average = new_average


# Example usage:
batting_stats = (2, 3, 5, 15, 30)
bowler_stats = (1, 3, 2, 10, 5, 2, 2, 1, 42, 6.3, 10)

player1 = Player("Virat Kohli", 33, "India", "Batsman", batting_average=53.41, batting_stat=batting_stats)
player2 = Player("Jasprit Bumrah", 28, "India", "Bowler", bowling_average=21.65, bowler_stat=bowler_stats)

player1.display_player_info()

print("\n")

player2.display_player_info()
