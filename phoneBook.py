
class Human():
    def __init__(self, firstName, secondName, phone, description) -> None:
        self.firstName = str(firstName)
        self.secondName = str(secondName)
        self.phone = int(phone)
        self.description = str(description)
        self.index = int(0)

class PhoneBook():
    def __init__(self) -> None:
        self.persona = []
        self.readPhoneBook('phone.txt')
    
    def appendContact(self):
        self.persona.append(self.takeInfo())

    def takeInfo():
        verification = False
        while (verification == False):
            firstName = str(input('Enter first name'))
            secondName = str(input('Enter second name'))
            phoneNumber = int(input('Enter phone number'))
            description = str(input('Enter description'))
            if firstName != '' or secondName != '': verification = True
        if verification : return Human(firstName=firstName, secondName=secondName, phone=phoneNumber, description=description)
    
    def printPhoneBook(self):
        for i in self.persona:
            print(f'{i.firstName, i.secondName, i.phone, i.description}')
   
    def findContact(self, searchingRequest):
        str(searchingRequest)
        for i in self.persona:
            if searchingRequest in i.firstName: return i
            elif searchingRequest in i.secondName: return i
            elif searchingRequest in str(i.phone): return i
   
    def printContact(self, contact):
        print(f'{contact.firstName, contact.secondName, contact.phone, contact.description}')
    
    def deleteContact(self, contact):
        self.persona.remove(contact)
        print('delete')

    def welcome(self):
        instruction = 'Welcome to the phone book\n0 - Read phonebook\n1 - Add contact\n2 - Search for a contact\n3 - Delete contact\n9 - Exit'
        print(instruction)
    
    def readPhoneBook(self, patch):
        file = open(patch, 'r', encoding='utf-8')
        for line in file:
            pers = line.split(',')
            if len(pers) >= 4:
                self.persona.append(Human(firstName=pers[0], secondName=pers[1], phone=pers[2], description=pers[3]))
        file.close()


    def workOnPhoneBook(self):
        work = True
        while(work):
            self.welcome()
            task = int(input())
            if(task == 0):
                printPhoneBook(contact)
            elif(task == 1):
                addContact = verifcateContact()
                addToPhoneBook(addContact, patch=url)
            elif(task == 2):
                findContact = input()
                searchInPhoneBook(findContact, patch=url)
            elif(task == 3):
                deleteContact()
            elif(task == 9):
                print('end work')
                work = False

            


def addToPhoneBook(contact, patch = 'phone.txt'):
        file = open(patch, 'a+', encoding='utf-8')
        contact = {}
        oldContact = False
        for k, v in contact.items():
            if oldContact == False and k not in file:
                newContact = '[' + str(k) + ' Phone: ' + str(v) + ']'
                file.write(newContact + '\n')
                break
            else:
                oldContact = True
                for person in file:
                    if person in str(k):
                        start = person.find(str(k))
                        end = person.find(' Phone: ', start)
                        c = person[start:]
        file.close()

def printPhoneBook(contact):
    for i in contact:
        i
        

def searchInPhoneBook(find, patch = 'phone.txt'):
    file = open(patch, 'r', encoding='utf-8')
    for line in file:
        if find in line:
            print(line)
            file.close()
            break
    if(not file.closed()): file.close()



def deleteContact(patch = 'phone.txt'):
    file = open(patch, 'r', encoding='utf-8')
    file.close()




