def ft_len_mass(mass):
    count = 0
    for i in mass:
        count += 1
    return count


def ft_pos_neg_separator_lst(lst1):
    pos = []
    neg = []
    zero = []
    x = []
    for i in range(ft_len_mass(lst1)):
        if lst1[i] > 0:
            pos.append(lst1[i])
        elif lst1[i] < 0:
            neg.append(lst1[i])
        else:
            zero.append(lst1[i])
    x = [neg, zero, pos]
    return x
