def ft_len_mass(mass):
    count = 0
    for i in mass:
        count += 1
    return count


def ft_rmstrspc(str1):
    str2 = ''
    for i in range(ft_len_mass(str1)):
        if str1[i] == ' ':
            i += 1
        else:
            str2 += str1[i]
            i += 1
    return str2
