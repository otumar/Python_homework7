# Вывод данных

def print_data(data):
    if len(data) > 0:
        print("Last name".center(20), "First name".center(20),
              "Phone number".center(15), "Description".center(30))
        print("-"*85)
        for elem in data:
            print(elem[0].center(20), elem[1].center(20),
                  elem[2].center(15), elem[3].center(30))
    else:
        print("No data")
