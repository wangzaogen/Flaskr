

def str_add(s1, s2):
    s1_list  = list(s1)
    s2_list  = list(s2)
    s1_index = len(s1_list)-1
    s2_index = len(s2_list)-1

    w = 0
    array = []

    while s1_index >= 0 or s2_index >=0:
        s2_r = 0
        if s2_index < 0 :
            s2_r = 0
        else:
            s2_r = int(s2_list[s2_index])

        s1_r = 0
        if s1_index < 0 :
            s1_r = 0
        else:
            s1_r = int(s1_list[s1_index])

        r = s1_r + s2_r

        if(r >= 10):
            r = r -10 + w
            w = 1
        else:
            r = r + w
            w = 0
        array.append(str(r))
        s1_index -= 1
        s2_index -= 1
        array_s  = array.sort()
    return ''.join(array[::-1])

if __name__ == '__main__':
    s1 = "124"
    s2 = "368"
    print(str_add(s1,s2))