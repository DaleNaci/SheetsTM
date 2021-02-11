class Player:
    def __init__(self, d):
        self.data = d
        self.tiebreakers = self.get_tiebreakers()


    def __wlt_to_games(self):
        return sum(map(int, self.data["W-L-T"].split("-")))


    def get_tiebreakers(self):
        games_played = self.__wlt_to_games()

        return {
            "avg_WP": self.data["WP"] / games_played,
            "avg_AP": self.data["AP"] / games_played,
            "avg_SP": self.data["SP"] / games_played
        }


    def __lt__(self, other):
        if self.tiebreakers["avg_WP"] != other.tiebreakers["avg_WP"]:
            return self.tiebreakers["avg_WP"] < other.tiebreakers["avg_WP"]
        elif self.tiebreakers["avg_AP"] != other.tiebreakers["avg_AP"]:
            return self.tiebreakers["avg_AP"] < other.tiebreakers["avg_AP"]
        elif self.tiebreakers["avg_SP"] != other.tiebreakers["avg_SP"]:
            return self.tiebreakers["avg_SP"] < other.tiebreakers["avg_SP"]

        return False


    def __eq__(self, other):
        checks = [
            self.tiebreakers["avg_WP"] == other.tiebreakers["avg_WP"],
            self.tiebreakers["avg_AP"] == other.tiebreakers["avg_AP"],
            self.tiebreakers["avg_SP"] == other.tiebreakers["avg_SP"]
        ]

        return all(checks)
