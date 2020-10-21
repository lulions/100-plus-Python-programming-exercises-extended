def get_power_dict(n):
    dict_out = {}
    for i in range(1, n + 1):
        dict_out[i] = i ** 2
    return dict_out


out = get_power_dict(8)

print(out)
