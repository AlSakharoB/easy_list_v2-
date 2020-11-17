def ft_len_mass(mass):
    count = 0
    for i in mass:
        count += 1
    return count


def ft_pos_neg_separator_lst(lst1):
    pos_lst = []
    neg_lst = []
    zero = []
    x = []
    for i in range(ft_len_mass(lst1)):
        if lst1[i] > 0:
            pos_lst.append(lst1[i])
        elif lst1[i] < 0:
            neg_lst.append(lst1[i])
        else:
            zero.append(lst1[i])
    x = [pos_lst, zero, neg_lst]
    return x
