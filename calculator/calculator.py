from functions import *



print('wat wilt u doen?')
while True:
    choice = input('\n A) getallen optellen\n B) getallen aftrekken\n C) vermenigvuldigen\n D) getallen delen\n E) getallen ophogen\n F) getallen verlagen\n G) getallen verdubbelen\n H) getallen halveren\n I) niets\n Kies:  ').lower()
    if choice not in options:
        print()
        print('\033[91mkies uit een van de mogelijk opties\033[0m')
        print()
        continue
    elif choice == 'i':
        if firstRound:
            print()
            print('\033[91mje moet minimaal een berekening maken voordat je mag stoppen\033[0m')
            continue
        else:
            break
    else:
        firstRound = False
        if choice in e_of_f:
            n2 = 1
        elif choice in g_of_h:
            n2 = 2
        set_choice = chosen_choice(choice)
        set_rekenTeken = chosen_reken_teken(choice, reken_teken)
        set_rekenMethode = chosen_reken_methode(choice, reken_methode)
        set_voorzetsel = chosen_voorzetsel(choice, voorzetsel)
        if not n1:
            print('--------------------------------')
            print(f'Getallen {set_rekenMethode}')
            print('--------------------------------')
            n1 = inputFloat('geef de eerste nummer: ')
            if not n2:
                n2 = inputFloat(f'welk getal wil je {set_rekenMethode} {set_voorzetsel} {n1}:  ')
                n1 = resultCalculation(set_rekenTeken, choice, n1, n2)
                n2 = False
                continue 
            elif n2:
                n2 = inputFloat(f'welk getal wil je {set_rekenMethode} {set_voorzetsel} {n1}:  ')
                n1 = resultCalculation(set_rekenTeken, firstRound, choice, n1, n2)
                n2 = False
                continue 
        else:
            if not n2:
                n2 = inputFloat(f'welk getal wil je {set_rekenMethode} {set_voorzetsel} {n1}:  ')
                n1 = resultCalculation(set_rekenTeken, firstRound, choice, n1, n2)
                n2 = False
                continue 
            elif n2:
                n1 = resultCalculation(set_rekenTeken, firstRound, choice, n1, n2)
                n2 = False
                continue