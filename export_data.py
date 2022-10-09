# Экспорт данных

def export_data():
    with open('phone.csv', 'r') as file:
        data = []
        tnum = []
        for line in file:
            if ',' in line:
                temp = line.strip().split(',')
                data.append(temp)
            elif ';' in line:
                temp = line.strip().split(';')
                data.append(temp)
            elif ':' in line:
                temp = line.strip().split(':')
                data.append(temp)
            elif line != '':
                if line != '\n':
                    tnum.append(line.strip())
                else:
                    data.append(tnum)
                    tnum = []
    return data
