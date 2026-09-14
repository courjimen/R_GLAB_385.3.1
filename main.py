#R GLAB 385.3.1

#Add contacts
    # define a func called "add_contact"
    # get name, phone from the user

def add_contact():
    print('Add Contact')
    name = input("Enter Name: ")
    phone = input("Enter phone number: ")

    try:
        if len(name) == 0:
            raise ValueError("User must input a valid name.")

        if len(phone) == 0:
                    raise ValueError("User must input a valid number.")

        with open('data/contacts.txt', mode='a') as f:
            f.write(f'{name}: {phone}\n')

        print(f' ✅ {name} has been added to your contacts!')

    except ValueError as e:
        print(f'Value Error: {e}')

    except Exception as e:
            print(f'❌ Error: {e}')

#View contacts
# define the view/contact func
#create the basic try/except block
#use 'with' to open the file with the correct mode to read

def view_contacts():
    try: 
        with open('data/contacts.txt', 'r' ) as f:
            contacts = f.readlines()

        if not contacts:
            print('Your list is empty.')
        else:
            for person in contacts:
                    print(person, end='')


    except FileNotFoundError as e:
         print(f'❌ File not found: your path was not found')
    except Exception as e:
        print(f'❌ Error: {e}' )

#Quit out of applications ✅
# Declare a function called "main" it should contain a while True: loop
def main ():
    while True:
        # logic
        print( '\n==== ☎️ Contact List Application ☎️ ====')
        print('1.   Add Contact')
        print('2.   View Contact')   
        print('3.   Quit')

        choice = input('Enter your choice: ')

# Control flow 'if' statement to ctrl actions program takes
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            print('👋🏾 Goodbye')
            break
        else: 
            print('❌ Invalid choice ❌ Please try again.')

# call the main func
if __name__ == '__main__':
    main()