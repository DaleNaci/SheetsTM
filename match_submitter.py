from match import Match
from database import Database


class MatchSubmitter:
    __instance = None

    def __init__(self):
        if MatchSubmitter.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            MatchSubmitter.__instance = self


    @staticmethod
    def get_instance():
        if MatchSubmitter.__instance == None:
            MatchSubmitter()
        return MatchSubmitter.__instance


    def add_match(self, m):
        db = Database.get_instance()

        for team in m.no_shows:
            db.add_stats(team, "0-1-0", 0, 0, 0)

        sp = min(m.red_score, m.blue_score)

        alliances = [m.red_alliance, m.blue_alliance]
        colors = ["red", "blue"]
        for alliance, color in zip(alliances, colors):
            if m.game_winner == "tie":
                wp = 1
            else:
                wp = 2 * (m.game_winner == color)

            if m.auton_winner == "tie":
                ap = 3
            else:
                ap = 6 * (m.auton_winner == color)

            if m.game_winner == color:
                wlt = "1-0-0"
            elif m.game_winner == "tie":
                wlt = "0-0-1"
            else:
                wlt = "0-1-0"

            for team in alliance:
                if not team in m.no_shows:
                    db.add_stats(team, wlt, wp, ap, sp)

        db.sort()
