# TODO Напишите функцию find_common_participants

def find_common_participants(group1_str, group2_str, separator=','):
    participants1 = group1_str.split(separator)
    participants2 = group2_str.split(separator)

    set1 = set(participants1)
    set2 = set(participants2)

    common_participants = set1.intersection(set2)

    return sorted(list(common_participants))

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print("Тест 1: С разделителем по умолчанию (запятая)")
print("Участники первой группы: 'Иванов,Петров,Сидоров' ")
print("Участники второй группы: 'Петров,Сидоров,Смиронов' ")
result1= find_common_participants("Иванов,Петров,Сидоров", "Петров,Сидоров,Смирнов")
print(f"Общие участники: {result1}")
print()
# TODO Провеьте работу функции с разделителем отличным от запятой
