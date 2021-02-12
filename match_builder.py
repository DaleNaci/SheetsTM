from match import Match


class MatchBuilder:
    def __init__(self):
        # Lists of team names
        self.red_alliance = []
        self.blue_alliance = []
        self.no_shows = []
        # Ints
        self.red_score = None
        self.blue_score = None
        # Values "red" "blue" "tie"
        self.auton_winner = None
        self.game_winner = None


    def with_teams(self, red_teams, blue_teams):
        self.red_alliance = red_teams
        self.blue_alliance = blue_teams
        return self


    def with_scores(self, red_points, blue_points):
        self.red_score = red_points
        self.blue_score = blue_points
        return self


    def with_auton_winner(self, winner):
        self.auton_winner = winner
        return self


    def with_game_winner(self, winner):
        self.game_winner = winner
        return self


    def with_no_shows(self, teams):
        self.no_shows = teams
        return self


    def build(self):
        return Match(
            self.red_alliance,
            self.blue_alliance,
            self.red_score,
            self.blue_score,
            self.auton_winner,
            self.game_winner,
            self.no_shows
        )
