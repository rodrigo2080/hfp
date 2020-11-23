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
    with open('man_data_sin.txt', 'w') as man_file:
        print(man, file=man_file)
    with open('other_data_sin.txt', 'w') as other_file:
        print(other, file=other_file)

except IOError as err:
    print('File Error ' + str(err))
