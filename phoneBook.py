
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
        self.patchFile = 'phone.txt'
        self.readPhoneBook(self.patchFile)
        self.working = True
        self.menuBook()
    def menuBook(self):
        while(self.working):
            self.welcome()
            id = int(input('What you wish?\n'))
            if(id == 0):
                self.printPhoneBook()
            elif(id == 1):
                self.appendContact()
            elif(id == 2):
                request = str(input('Enter contact details\n'))
                human = self.findContact(request)
                if human != None: self.printContact(human)
            elif(id == 3):
                request = str(input('Enter delete contact\n'))
                human = self.findContact(request)
                if human != None: self.deleteContact(human)
            elif(id == 4):
                request = str(input('Enter what contact you want change\n'))
                human = self.findContact(request)
                if human != None: self.changeContact(human)
            elif(id == 9):
                id = str(input('Save book, y/n?\n'))
                if id == 'y': self.saveBook()
                self.working = False

    def appendContact(self):
        h = self.takeInfo()
        self.persona.append(h)

    def takeInfo(self):
        verification = False
        while (verification == False):
            firstName = str(input('Enter first name\n'))
            secondName = str(input('Enter second name\n'))
            phoneNumber = int(input('Enter phone number\n'))
            description = str(input('Enter description\n'))
            if firstName != '' or secondName != '': verification = True
        if verification : return Human(firstName=firstName, secondName=secondName, phone=phoneNumber, description=description)
    
    def printPhoneBook(self):
        for i in self.persona:
            contact = i.firstName + " " + i.secondName + " " +  str(i.phone) + " " +  i.description
            print(f'{contact}')
   
    def findContact(self, searchingRequest):
        str(searchingRequest)
        resultSearching = []
        for i in self.persona:
            if searchingRequest.lower() in i.firstName.lower(): resultSearching.append(i)#return i
            elif searchingRequest.lower() in i.secondName.lower(): resultSearching.append(i)#return i
            elif searchingRequest.lower() in str(i.phone).lower(): resultSearching.append(i)#return i
        if len(resultSearching) == 1: return resultSearching[0]
        elif len(resultSearching) == 0: return Human('-', '-', 0, 'Contact not found')
        choice = False
        while(not choice):
            for c in range (0, len(resultSearching)):
                print(f'id contact {c}')
                self.printContact(resultSearching[c])
            sizeFindContact = len(resultSearching)
            id = int(input(f'Choice contact ID\nPress {sizeFindContact} to exit\n'))
            if id < sizeFindContact: 
                return resultSearching[id]
            elif id == sizeFindContact: return Human('-', '-', 0, 'Contact not selected')
   
    def printContact(self, contact):
        cont = contact.firstName + " " + contact.secondName + " " +  str(contact.phone) + " " +  contact.description
        print(f'{cont}')
    
    def deleteContact(self, contact):
        if(contact in self.persona):
            self.persona.remove(contact)
            print('delete')
        else: print('Not found')
    
    def changeContact(self, contact):
        self.printContact(contact=contact)
        change = False
        while(change == False):
            id = int(input('\nPress 0 to change first name\nPress 1 to change second name\nPress 2 to change phone number\nPress 3 to change description\nPress 9 to exit\n'))
            if (id == 0): 
                contact.firstName = str(input('Enter new name\n'))
                exit = input('Do you like change anything else? y/n\n')
                if(exit == 'n'): change = True
            elif (id == 1): 
                contact.secondName = str(input('Enter new name\n'))
                exit = input('Do you like change anything else? y/n\n')
                if(exit == 'n'): change = True
            elif (id == 2): 
                contact.phone = int(input('Enter new number\n'))
                exit = input('Do you like change anything else? y/n\n')
                if(exit == 'n'): change = True
            elif (id == 3): 
                contact.description = str(input('Enter new description\n'))
                exit = input('Do you like change anything else? y/n\n')
                if(exit == 'n'): change = True
            elif(id == 9): change = True
    
    def welcome(self):
        instruction = '\nWelcome to the phone book\n0 - Print phone book\n1 - Add contact\n2 - Search for a contact\n3 - Delete contact\n4 - Change contact\n9 - Exit'
        print(instruction)
    
    def readPhoneBook(self, patch):
        file = open(patch, 'r', encoding='utf-8')
        for line in file:
            pers = line.split(',')
            if len(pers) >= 4:
                self.persona.append(Human(firstName=pers[0], secondName=pers[1], phone=pers[2], description=pers[3]))
        file.close()

    def saveBook(self):
        file = open(self.patchFile, 'w', encoding='utf-8')
        for i in self.persona:
            data = i.firstName + ', ' + i.secondName + ', ' + str(i.phone) + ', ' + i.description
            file.write(data + '\n')
        file.close()
        print(f'book saved. url = {self.patchFile}')


book = PhoneBook()




