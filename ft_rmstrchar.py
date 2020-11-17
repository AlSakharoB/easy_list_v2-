def ft_len_mass(mass):
    count = 0
    for i in mass:
        count += 1
    return count


def ft_rmstrchar(str2, less):
    str1 = ""
    for i in range(ft_len_mass(str2)):
        if str2[i] not in less:
            str1 += str2[i]
    return str1
