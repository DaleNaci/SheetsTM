class Match:
    def __init__(self, ra, ba, rs, bs, aw, gw, ns):
        # Lists of team names
        self.red_alliance = ra
        self.blue_alliance = ba
        self.no_shows = ns
        # Ints
        self.red_score = rs
        self.blue_score = bs
        # Values "red" "blue" "tie"
        self.auton_winner = aw
        self.game_winner = gw
