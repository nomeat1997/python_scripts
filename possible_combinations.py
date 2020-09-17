def combos(input_list):
    all_combos = []
    for mask in range(pow(2,len(input_list))):
        new_list = []
        mask_str = bin(mask)[2:]
        for bit_no in range(-1,-len(mask_str)-1,-1):
            if mask_str[bit_no] == "1":
                new_list = [input_list[bit_no]] + new_list
        all_combos.append(new_list)
    return all_combos
print(combos("A B C D E".split()))
