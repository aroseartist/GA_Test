def k_animals(animals):
    k_list = []
    for item in animals:
        if item[0] == 'k':
            k_list.append(item)
    print k_list
    return k_animals

k_animals(['panda cake', 'koala cub', 'squid adoodle', 'swedish fishies', 'kandy crane', 'hammertime shark'])
