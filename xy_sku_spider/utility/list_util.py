

def split_list(big_list , max_split: int):
    for i in range(0, len(big_list), max_split):
        yield big_list[i: i+max_split]



