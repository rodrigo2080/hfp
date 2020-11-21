names = ['John', 'Eric', ['Iker', 'Santi'], 'Peter', ['Clau', 'Pia']]

def print_lol(the_list, indent=False, level=0):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, indent, level+1)
        else:
            if indent:
                for tap_stop in range(level):
                    print("\t", end='')
            print(each_item)

print_lol(names)

print_lol(names, 0)

print_lol(names, True)

print_lol(names, True, 5)

print_lol(names, True, -5)

print_lol(names, True, -1)
