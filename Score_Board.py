import re
from tabulate import tabulate  # type: ignore

# ---------- Helpers ----------
def safe_input(prompt, default=""):
    try:
        return input(prompt)
    except Exception:
        return default

def extract_first_int(s):
    m = re.search(r'-?\d+', s)
    if m:
        try:
            return int(m.group())
        except Exception:
            return None
    return None

# ---------- Number words mapping ----------
number_words = {
    "zero":0, "one":1, "two":2, "three":3, "four":4, "five":5,
    "six":6, "seven":7, "eight":8, "nine":9, "ten":10
}

def parse_overs_input(s):
    s = s.strip().lower()
    # Try numeric
    try:
        return int(s)
    except:
        pass
    # Try word
    return number_words.get(s, None)

# ---------- Models ----------
class Player:
    def __init__(self, name):
        self.name = str(name)
        self.runs = 0
        self.balls = 0
        self.wickets = 0
        self.is_out = False

    def add_runs(self, runs, count_ball=True):
        try:
            runs = int(runs)
        except Exception:
            runs = 0
        self.runs += runs
        if count_ball:
            self.balls += 1

    def take_wicket(self):
        self.wickets += 1

    def get_out(self):
        self.is_out = True

class Team:
    def __init__(self, name, players):
        self.name = str(name)
        self.players = [Player(p) for p in (players if isinstance(players, (list, tuple)) else [])]
        self.score = 0
        self.wickets = 0
        self.overs = 0
        self.balls_in_over = 0
        self.current_batsmen = [
            self.players[0] if len(self.players) > 0 else None,
            self.players[1] if len(self.players) > 1 else None,
        ]
        self.next_batsman_index = 2 if len(self.players) > 2 else len(self.players)

    def update_score(self, runs):
        try:
            self.score += int(runs)
        except Exception:
            pass

    def fall_of_wicket(self, bowler):
        self.wickets += 1
        striker = self.current_batsmen[0]
        if striker:
            striker.get_out()
        if bowler:
            bowler.take_wicket()
        if self.next_batsman_index < len(self.players):
            self.current_batsmen[0] = self.players[self.next_batsman_index]
            self.next_batsman_index += 1
            return True
        else:
            self.current_batsmen[0] = None
            return False

    def swap_strike(self):
        self.current_batsmen[0], self.current_batsmen[1] = self.current_batsmen[1], self.current_batsmen[0]

# ---------- Match ----------
class Match:
    def __init__(self, batting_team, bowling_team, max_overs=None):
        self.batting_team = batting_team
        self.bowling_team = bowling_team
        self.current_bowler = None
        self.over_number = 0
        self.innings_over = False
        self.max_overs = max_overs  # overs limit

    def set_bowler(self):
        if not self.bowling_team.players:
            print("[Info] No bowlers available.")
            self.current_bowler = None
            return

        while True:
            print(f"\nAvailable Bowlers from {self.bowling_team.name}:")
            for idx, player in enumerate(self.bowling_team.players):
                print(f"{idx+1}. {player.name} (Wickets: {player.wickets})")
            choice = safe_input("Select bowler number or name: ").strip()
            if choice.isdigit():
                idx = int(choice) - 1
                if 0 <= idx < len(self.bowling_team.players):
                    self.current_bowler = self.bowling_team.players[idx]
                    break
            else:
                found = None
                for p in self.bowling_team.players:
                    if choice.lower() in p.name.lower():
                        found = p
                        break
                if found:
                    self.current_bowler = found
                    break
            print("❌ Invalid input. Try again.")

        self.over_number += 1
        print(f"🎳 Bowler for Over {self.over_number}: {self.current_bowler.name}")

    def parse_outcome(self, raw):
        s = (raw or "").strip().upper()
        if not s:
            return {"bat_runs": 0, "team_runs": 0, "legal": True, "wicket": False, "note": "Dot ball"}
        if "WD" in s or "WIDE" in s:
            return {"bat_runs": 0, "team_runs": 1, "legal": False, "wicket": False, "note": "Wide"}
        if "NB" in s or "NO BALL" in s:
            return {"bat_runs": 0, "team_runs": 1, "legal": False, "wicket": False, "note": "No-ball"}
        if s in ["W", "OUT", "WICKET"]:
            return {"bat_runs": 0, "team_runs": 0, "legal": True, "wicket": True, "note": "Wicket"}
        first_int = extract_first_int(s)
        if first_int is not None:
            return {"bat_runs": first_int, "team_runs": first_int, "legal": True, "wicket": False, "note": f"{first_int} run(s)"}
        return {"bat_runs": 0, "team_runs": 0, "legal": True, "wicket": False, "note": "Unrecognized -> Dot ball"}

    def play_ball(self):
        if self.innings_over:
            return

        striker = self.batting_team.current_batsmen[0]
        striker_name = striker.name if striker else "No striker"
        raw = safe_input(f"\nBall outcome for {striker_name}: ", "")
        parsed = self.parse_outcome(raw)

        # Wicket
        if parsed["wicket"]:
            if striker:
                print(f"❌ {striker.name} OUT! by {self.current_bowler.name if self.current_bowler else 'Unknown'}")
                if not self.batting_team.fall_of_wicket(self.current_bowler):
                    self.innings_over = True
        else:
            if striker:
                striker.add_runs(parsed["bat_runs"], count_ball=parsed["legal"])
            self.batting_team.update_score(parsed["team_runs"])
            if parsed["bat_runs"] % 2 == 1:
                self.batting_team.swap_strike()
            if parsed["legal"]:
                self.batting_team.balls_in_over += 1

        # Over complete
        if self.batting_team.balls_in_over >= 6:
            self.batting_team.overs += 1
            self.batting_team.balls_in_over = 0
            self.batting_team.swap_strike()
            if not self.innings_over and (self.max_overs is None or self.batting_team.overs < self.max_overs):
                self.set_bowler()

        # Overs limit check
        if self.max_overs is not None and self.batting_team.overs >= self.max_overs:
            print(f"🏁 Overs limit ({self.max_overs}) reached! Innings finished.")
            self.innings_over = True

        self.display_scoreboard()

    def display_scoreboard(self):
        print("\n================== SCOREBOARD ==================")
        print(f"{self.batting_team.name} {self.batting_team.score}/{self.batting_team.wickets}  Overs: {self.batting_team.overs}.{self.batting_team.balls_in_over}")
        table = []
        for p in self.batting_team.players:
            status = "OUT" if p.is_out else "NOT OUT"
            table.append([p.name, p.runs, p.balls, status])
        print(tabulate(table, headers=["Batsman", "Runs", "Balls", "Status"], tablefmt="fancy_grid"))
        bowl_table = [[p.name, p.wickets] for p in self.bowling_team.players]
        print(tabulate(bowl_table, headers=["Bowler", "Wickets"], tablefmt="fancy_grid"))
        print("===============================================\n")

# ---------------- MAIN ----------------
if __name__ == "__main__":
    # Example teams
    team1 = Team("Team A", ["Ali", "Ahmed", "Abdullah", "Usman", "Bilal", "Zain"])
    team2 = Team("Team B", ["John", "Smith", "David", "Chris", "Tom", "Andrew"])

    print("=== Cricket Simulator ===")
    
    # Ask for overs (numbers or words)
    while True:
        overs_input = safe_input("How many overs do you want for the match? (number or word): ", "2")
        overs_limit = parse_overs_input(overs_input)
        if overs_limit and overs_limit > 0:
            break
        print("❌ Invalid input. Enter a number (e.g., 5) or word (e.g., five).")

    match = Match(team1, team2, max_overs=overs_limit)

    # First bowler
    match.set_bowler()

    # Automatically play balls until innings ends
    while not match.innings_over:
        match.play_ball()
        # Check if over is complete and innings not over
        if match.batting_team.balls_in_over == 0 and not match.innings_over:
            print("\n⚡ Over completed! Time to change the bowler.")
            match.set_bowler()

    print("Match finished. Thanks for watching / playing")

