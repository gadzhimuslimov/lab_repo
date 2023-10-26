# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, spliter=","):
    group1, group2 = group1.split(spliter), group2.split(spliter)  # Распаковка кортежа по переменным
    return sorted(set(group1).intersection(group2))


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, spliter='|'))
