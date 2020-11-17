def ft_len_mass(mass):
    count = 0
    for i in mass:
        count += 1
    return count


def ft_join(lst, sep1=" "):
    str1 = ""
    for i in range(ft_len_mass(lst) - 1):
        str1 += str(lst[i]) + str(sep1)
    return str1 + str(lst[ft_len_mass(lst) - 1])
