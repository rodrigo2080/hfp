from nester import print_lol

man=[]
other=[]

try:
    data = open('sketch.txt')

    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass

    data.close()
except IOError:
    print('No se encuentra el archivo con la información a separar')

try:
    with open('man_data.txt', 'w') as man_file:
        print_lol(man, fh=man_file)
    with open('other_data.txt', 'w') as other_file:
        print_lol(other, fh=other_file)

except IOError as err:
    print('File Error ' + str(err))
