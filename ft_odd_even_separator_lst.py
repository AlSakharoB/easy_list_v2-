def ft_len_mass(mass):
    count = 0
    for i in mass:
        count += 1
    return count


def ft_odd_even_separator_lst(lst):
    lst_even = []
    lst_n_even = []
    for i in range(ft_len_mass(lst)):
        if lst[i] % 2 == 0:
            lst_even.append(lst[i])
        else:
            lst_n_even.append(lst[i])
    return [lst_even, lst_n_even]
