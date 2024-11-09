from CLASS_19.main import num_list


def add(*args):
    return sum(args)

if __name__ == "__main__":
    import sys
    num_to_add = sys.argv[1:]

    #convert from string to int
    num_to_add = [int(num) for num in num_to_add]


    sum_num = add(*num_to_add)
    print(sum_num)
