#R GLAB 385.3.1

#Add contacts
#View contacts
#Quit out of applications

# Declare a function called "main" it should contain a while True: loop
def main ():
    while True:
        # logic
        print( '==== ☎️ Contact List Application ☎️ ====')
        print('1.   Add Contact')
        print('2.   View Contact')   
        print('3.   Quit')

        choice = input('Enter your choice: ')

# Control flow 'if' statement to ctrl actions program takes
        if choice == '1':
            print('Add Contact')
        elif choice == '2':
            print('View Contacts')
        elif choice == '3':
            print('👋🏾 Goodbye')
            break
        else: 
            print('❌ Invalid choice ❌ Please try again.')
