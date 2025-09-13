class Player:
    def __init__(self, name):
        self.name = name
        self.runs = 0
        self.balls = 0
        self.wickets = 0
        self.is_out = False

    def add_runs(self, runs, count_ball=True):
        self.runs += runs
        if count_ball:
            self.balls += 1

    def take_wicket(self):
        self.wickets += 1

    def get_out(self):
        self.is_out = True


class Team:
    def __init__(self, name, players):
        self.name = name
        self.players = [Player(p) for p in players]
        self.score = 0
        self.wickets = 0
        self.overs = 0
        self.balls_in_over = 0
        self.current_batsmen = [self.players[0], self.players[1]]
        self.next_batsman_index = 2

    def update_score(self, runs):
        self.score += runs

    def fall_of_wicket(self, bowler):
        self.wickets += 1
        self.current_batsmen[0].get_out()
        bowler.take_wicket()

        if self.next_batsman_index < len(self.players):
            new_batsman = self.players[self.next_batsman_index]
            self.current_batsmen[0] = new_batsman
            self.next_batsman_index += 1
        else:
            print("⚠️ All players are out!")

    def swap_strike(self):
        self.current_batsmen[0], self.current_batsmen[1] = self.current_batsmen[1], self.current_batsmen[0]


class Match:
    def __init__(self, batting_team, bowling_team):
        self.batting_team = batting_team
        self.bowling_team = bowling_team
        self.current_bowler = None
        self.over_number = 0

    def set_bowler(self):
        print(f"\nAvailable Bowlers from {self.bowling_team.name}:")
        for idx, player in enumerate(self.bowling_team.players):
            print(f"{idx+1}. {player.name} (Wickets: {player.wickets})")

        choice = int(input("Select bowler number: ")) - 1
        self.current_bowler = self.bowling_team.players[choice]
        self.over_number += 1
        print(f"\n🎳 Bowler for Over {self.over_number}: {self.current_bowler.name}")

    def play_ball(self):
        batsman = self.batting_team.current_batsmen[0]
        outcome = input(f"\nBall outcome for {batsman.name} (0,1,2,3,4,6,W,Wd): ").strip()

        if outcome.upper() == "W":
            print(f"❌ {batsman.name} is OUT! Bowler: {self.current_bowler.name}")
            self.batting_team.fall_of_wicket(self.current_bowler)

        elif outcome.upper() == "WD":  # wide ball
            print(f"⚠️ Wide ball by {self.current_bowler.name}. +1 run")
            self.batting_team.update_score(1)
            # wide → runs add hote hain but ball count nahi hoti
            self.display_scoreboard()
            return

        else:
            runs = int(outcome)
            batsman.add_runs(runs)
            self.batting_team.update_score(runs)
            print(f"✅ {batsman.name} scored {runs} run(s).")

            # rotate strike if runs are odd
            if runs % 2 != 0:
                self.batting_team.swap_strike()

        # ball count only for legal deliveries
        self.batting_team.balls_in_over += 1

        if self.batting_team.balls_in_over == 6:
            self.batting_team.overs += 1
            self.batting_team.balls_in_over = 0
            self.batting_team.swap_strike()  # swap batsmen at over end
            self.set_bowler()  # new bowler after over

        self.display_scoreboard()

    def display_scoreboard(self):
        print("\n================== SCOREBOARD ==================")
        print(f"Batting: {self.batting_team.name}")
        print(f"Score: {self.batting_team.score}/{self.batting_team.wickets}")
        print(f"Overs: {self.batting_team.overs}.{self.batting_team.balls_in_over}")
        print(f"Striker: {self.batting_team.current_batsmen[0].name} "
              f"({self.batting_team.current_batsmen[0].runs} runs, {self.batting_team.current_batsmen[0].balls} balls)")
        print(f"Non-striker: {self.batting_team.current_batsmen[1].name} "
              f"({self.batting_team.current_batsmen[1].runs} runs, {self.batting_team.current_batsmen[1].balls} balls)")
        if self.current_bowler:
            print(f"Bowler: {self.current_bowler.name} (Wickets: {self.current_bowler.wickets})")

        if self.batting_team.next_batsman_index < len(self.batting_team.players):
            print(f"Next batsman: {self.batting_team.players[self.batting_team.next_batsman_index].name}")
        else:
            print("No batsman left!")

        print("\n--- Team Players Performance ---")
        for player in self.batting_team.players:
            print(f"{player.name}: {player.runs} runs ({player.balls} balls){' OUT' if player.is_out else ''}")

        print("\n--- Bowling Team Performance ---")
        for player in self.bowling_team.players:
            print(f"{player.name}: {player.wickets} wickets")
        print("=============================================\n")


# ---------------- MAIN ----------------
team1 = Team("Team A", ["Ali", "Ahmed", "Hassan", "Usman", "Bilal", "Owais"])
team2 = Team("Team B", ["John", "Smith", "David", "Chris", "Tom", "Andrew"])

match = Match(team1, team2)

# Start Match
match.set_bowler()

# Simulate 2 overs (12 balls or more if wides)
for i in range(12):
    match.play_ball()
