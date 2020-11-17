def ft_len_mass(mass):
    count = 0
    for i in mass:
        count += 1
    return count


def ft_sumlst(lst):
    sum = 0
    for i in range(ft_len_mass(lst)):
        sum += float(lst[i])
    return sum
