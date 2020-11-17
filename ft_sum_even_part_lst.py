def ft_len_mass(mass):
    count = 0
    for i in mass:
        count += 1
    return count


def ft_sum_even_part_lst(lst1):
    sum = 0
    for i in range(ft_len_mass(lst1)):
        if int(lst1[i]) % 2 == 0:
            sum += int(lst1[i])
    return sum
