import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

from player import Player


class Database:
    __instance = None

    def __init__(self):
        if Database.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Database.__instance = self

        self.scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive.file",
            "https://www.googleapis.com/auth/drive"

        ]
        self.creds = ServiceAccountCredentials.from_json_keyfile_name(
                        "creds.json", self.scope)
        self.client = gspread.authorize(self.creds)
        self.sheet = self.client.open("VEX Change Up").sheet1


    @staticmethod
    def get_instance():
        if Database.__instance == None:
            Database()
        return Database.__instance


    def __get_row(self, col, val):
        for row in self.get_all_data():
            if row[col].lower() == val.lower():
                return row


    def __wlt_to_lst(self, wlt):
        return list(map(int, wlt.split("-")))


    def sort(self):
        players = [Player(d) for d in self.get_all_data()]
        players.sort(reverse=True)

        for i in range(len(players)):
            p = players[i]
            p.data["Rank"] = i+1

            sheet_range = f"A{i+2}:G{i+2}"
            new_cell_values = [[v for v in p.data.values()]]
            self.sheet.update(sheet_range, new_cell_values)


    def get_all_data(self):
        return self.sheet.get_all_records()


    def get_player_data(self, ign):
        return self.__get_row("IGN", ign)


    def get_team_data(self, team):
        return self.__get_row("Team", team)


    def get_rank_data(self, rank):
        return self.__get_row("Rank", rank)


    def add_stats(self, team, wlt, wp, ap, sp):
        row = self.__get_row("Team", team)

        wlt_lst = self.__wlt_to_lst(row["W-L-T"])
        add_wlt_lst = self.__wlt_to_lst(wlt)
        for i in range(3):
            wlt_lst[i] += add_wlt_lst[i]
        row["W-L-T"] = f"{wlt_lst[0]}-{wlt_lst[1]}-{wlt_lst[2]}"

        row["WP"] = str(int(row["WP"]) + wp)
        row["AP"] = str(int(row["AP"]) + ap)
        row["SP"] = str(int(row["SP"]) + sp)

        row_num = row["Rank"] + 1
        sheet_range = f"A{row_num}:G{row_num}"
        new_cell_values = [[v for v in row.values()]]
        self.sheet.update(sheet_range, new_cell_values)
