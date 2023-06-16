def lyrics(inputs) -> int:
    init_low = 0
    key_horn = 'saramago'
    for xy in inputs:
        if xy == key_horn[0]: key_horn = key_horn[1:]
        if len(key_horn) == 0: init_low, key_horn = init_low+1, 'saramago'
    return init_low
with open('cameos.txt', 'r') as fichero: 
    for inputs in fichero: print(lyrics(inputs.lower()))