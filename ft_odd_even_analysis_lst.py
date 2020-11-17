def ft_len_mass(mass):
    count = 0
    for i in mass:
        count += 1
    return count


def ft_odd_even_analysis_lst(lst):
    chet = 0
    ne_chet = 0
    chet_sum = 0
    ne_chet_sum = 0
    for i in lst:
        if i % 2 == 0:
            max_chet = min_chet = i
            break
    for i in lst:
        if i % 2 != 0:
            max_ne_chet = min_ne_chet = i
            break
    for i in range(ft_len_mass(lst)):
        if int(lst[i]) % 2 == 0:
            chet += 1
            chet_sum += int(lst[i])
            if int(lst[i]) > max_chet:
                max_chet = int(lst[i])
            if int(lst[i]) < min_chet:
                min_chet = int(lst[i])
        else:
            ne_chet += 1
            ne_chet_sum += int(lst[i])
            if int(lst[i]) > max_ne_chet:
                max_ne_chet = int(lst[i])
            if int(lst[i]) < min_ne_chet:
                min_ne_chet = int(lst[i])
    print("Анализ списка:")
    print("Кол-во четных:", chet, "\t\t", "Кол-во нечетных:", ne_chet)
    print("Макс четное:", max_chet, "\t\t", "Макс нечетное:", max_ne_chet)
    print("Мин четное:", min_chet, "\t\t", "Мин нечетное:", min_ne_chet)
    print("Сумма четных:", chet_sum, "\t\t", "Сумма нечетных:", ne_chet_sum, end="")

