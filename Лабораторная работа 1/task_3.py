list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
equally = len(list_players) // 2
team1 = list_players[:equally]
team2 = list_players[equally:]

print(team1)
print(team2)
