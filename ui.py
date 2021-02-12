from match_builder import MatchBuilder
from match_submitter import MatchSubmitter

while True:
    red_team1 = input("Red Team 1: ")
    red_team2 = input("Red Team 2: ")
    blue_team1 = input("Blue Team 1: ")
    blue_team2 = input("Blue Team 2: ")
    red_score = int(input("Red Score: "))
    blue_score = int(input("Blue Score: "))
    auton_winner = input("Auton winner: ")

    if red_score > blue_score:
        game_winner = "red"
    elif red_score < blue_score:
        game_winner = "blue"
    else:
        game_winner = "tie"

    m = MatchBuilder().with_teams(
            [red_team1, red_team2],
            [blue_team1, blue_team2]
        ).with_scores(
            red_score, blue_score
        ).with_auton_winner(
            auton_winner
        ).with_game_winner(
            game_winner
        ).build()

    MatchSubmitter.get_instance().add_match(m)
