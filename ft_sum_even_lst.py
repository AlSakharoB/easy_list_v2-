def ft_len_mass(mass):
    count = 0
    for i in mass:
        count += 1
    return count


def ft_sum_even_lst(lst1):
    sum = 0
    for i in range(ft_len_mass(lst1)):
        if i % 2 == 0:
            sum += float(lst1[i])
    return sum
