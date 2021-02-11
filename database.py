import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint


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


    def sort(self):
        all_data = self.get_all_data()

        # for row in all_data:



    def get_all_data(self):
        return self.sheet.get_all_records()


    def get_player_data(self, ign):
        return self.__get_row("IGN", ign)


    def get_team_data(self, team):
        return self.__get_row("Team", team)


    def get_rank_data(self, rank):
        return self.__get_row("Rank", rank)
