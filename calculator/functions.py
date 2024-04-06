options = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
a_tot_d = ['a', 'b', 'c', 'd']
e_of_f = ['e', 'f']
g_of_h = ['g', 'h']

reken_teken = ''
reken_methode = ''
voorzetsel = ''
zero_division = False

firstRound = True
n1 = False
n2 = False
    
    
    
def addition(n1:float, n2:float):
    result = n1 + n2
    return result
    
def subtraction(n1:float, n2:float):
    result = n1 - n2
    return result

def multiplication(n1:float, n2:float):
    result = n1 * n2	
    return result

def division(n1:float, n2:float):
    try:
        result = n1 / n2
    except ZeroDivisionError:
        print('kan niet delen door 0')
    result = n1 / n2
    return result



def inputFloat(question:str):
    while True:
        try:
            nummer = float(input(question))
            return nummer
        except ValueError:
            print('\033[91mvoer een geldige getal in\033[0m')



def printResultaat(n1:float, n2:float, set_rekenTeken:str, resultaat:float):
    print('++----------------------------++')
    print(f'{n1} {set_rekenTeken} {n2} = {resultaat}')
    print('--------------------------------')
    n1 = resultaat
    print(f'wat wil je doen met de uitkomst ({n1})?')



def resultCalculation(set_rekenTeken:str, choice:str, n1:float, n2:float):
    set_choice = chosen_choice(choice)
    set_rekenTeken = chosen_reken_teken(choice, reken_teken)
    
    resultaat = set_choice(n1, n2)
    printResultaat(n1, n2, set_rekenTeken, resultaat)
    return resultaat
    
    
    
def chosen_choice(choice:str):
    if choice == 'a':
        choice = addition
        return choice
    elif choice == 'b':
        choice = subtraction
        return choice
    elif choice == 'c':
        choice = multiplication
        return choice
    elif choice == 'd':
        choice = division
        return choice
    elif choice == 'e':
        choice = addition
        return choice
    elif choice == 'f':
        choice = subtraction
        return choice
    elif choice == 'g':
        choice = multiplication
        return choice
    elif choice == 'h':
        choice = division
        return choice
    
    
    
def chosen_reken_teken(choice:str, reken_teken:str):
    if choice == 'a':
        reken_teken = '+'
        return reken_teken
    elif choice == 'b':
        reken_teken = '-'
        return reken_teken
    elif choice == 'c':
        reken_teken = 'x'
        return reken_teken
    elif choice == 'd':
        reken_teken = ':'
        return reken_teken
    elif choice == 'e':
        reken_teken = '+'
        return reken_teken
    elif choice == 'f':
        reken_teken = '-'
        return reken_teken
    elif choice == 'g':
        reken_teken = 'x'
        return reken_teken
    elif choice == 'h':
        reken_teken = ':'
        return reken_teken
    
    
    
def chosen_reken_methode(choice:str, reken_methode:str):
    if choice == 'a':
        reken_methode = 'optellen'
        return reken_methode
    elif choice == 'b':
        reken_methode = 'aftrekken'
        return reken_methode
    elif choice == 'c':
        reken_methode = 'vermenigvuldigen'
        return reken_methode
    elif choice == 'd':
        reken_methode = 'delen'
        return reken_methode
    elif choice == 'e':
        reken_methode = 'ophogen'
        return reken_methode
    elif choice == 'f':
        reken_methode = 'verlagen'
        return reken_methode
    elif choice == 'g':
        reken_methode = 'verdubbelen'
        return reken_methode
    elif choice == 'h':
        reken_methode = 'halveren'
        return reken_methode



def chosen_voorzetsel(choice:str, voorzetsel:str):
    if choice == 'a':
        voorzetsel = 'bij'
        return voorzetsel
    elif choice == 'b':
        voorzetsel = 'van'
        return voorzetsel
    elif choice == 'c':
        voorzetsel = 'bij'
        return voorzetsel
    elif choice == 'd':
        voorzetsel = 'door'
        return voorzetsel
    elif choice == 'e':
        voorzetsel = 'ophogen'
        return voorzetsel
    elif choice == 'f':
        voorzetsel = 'verlagen'
        return voorzetsel
    elif choice == 'g':
        voorzetsel = 'verdubbelen'
        return voorzetsel
    elif choice == 'h':
        voorzetsel = 'halveren'
        return voorzetsel



        
        