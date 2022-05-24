
# Title: CDInventory.py
# Desc: CDInventory using 2d lists

# Declare variables
user_choice = ''  # User input
list_of_table = []  # list of lists to hold data
# TODO replace list of lists with list of dicts
list_of_row = []  # list of data row
while True:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    print('Please choose your option from the menu')
    user_choice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if user_choice == 'x':
        # 5. Exit the program if the user chooses so
        break
    if user_choice == 'l':
        # loading existing data
        read_file = open('CDInventory.txt', 'r')
        for row in read_file:
            print(row)
        read_file.close()
    elif user_choice == 'a':
        # 2. Add data to the table (2d-list) each time the user wants to add data
        string_of_ID = input('Enter an ID: ')
        CD_title = input('Enter the CD\'s Title: ')
        artist_name = input('Enter the Artist\'s Name: ')
        int_of_ID = int(string_of_ID)
        list_of_row = [int_of_ID, CD_title, artist_name]
        list_of_table.append(list_of_row)
    elif user_choice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID, CDTitle, Artist')
        for row in list_of_table:
            print(*row, sep=', ')
    elif user_choice == 'd':
        # deleting an entry
        del list_of_row[:-1]
    elif user_choice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        with open('CDInventory.txt', 'a') as file:
            for row in list_of_table:
                list_of_row = ''
                for item in row:
                    list_of_row += str(item) + ', '
                list_of_row = list_of_row[:-1] + '\n'
                file.write(list_of_row)
    else:
        print('Please choose either l, a, i, d, s or x!')