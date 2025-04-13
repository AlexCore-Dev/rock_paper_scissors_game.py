import random

valasztas = ['kő', 'papír', 'olló']
sanyi_win = 0
kriszti_win = 0

print('Induljon a kő, papír, olló GAME! Gyozzon a jobb!')

while True:
    Kriszti = random.choice(valasztas)
    
    if sanyi_win == 3:
        print(f'Sanyi nyerte a jatekot! Vegeredmeny: {sanyi_win} / {kriszti_win}')
        break

    elif kriszti_win == 3:
        print(f'Kriszti nyerte a jatekot! Vegeredmeny: {sanyi_win} / {kriszti_win}')
        break  
    
    sanyi = input(f'Sanyi valasztasa: ').strip().lower()

    if sanyi not in ['kő', 'papír', 'olló']:
        print('Csak a kő, papír, olló elfogadott!')
        continue 

    elif sanyi == Kriszti:
        print(f'Sanyi valasztasa {sanyi}, Kriszti valasztasa {Kriszti}, Dontetlen! Az allas jelenleg: Sanyi {sanyi_win} / Kriszti {kriszti_win}')
        
    elif sanyi == 'kő' and Kriszti == 'papír':
        kriszti_win += 1
        print(f'Sanyi valasztasa {sanyi}, Kriszti valasztasa {Kriszti}, Kriszti nyert! Az allas jelenleg: Sanyi {sanyi_win} / Kriszti {kriszti_win}')
        
    elif sanyi == 'kő' and Kriszti == 'olló':
        sanyi_win += 1
        print(f'Sanyi valasztasa {sanyi}, Kriszti valasztasa {Kriszti}, Sanyi nyert! Az allas jelenleg: Sanyi {sanyi_win} / Kriszti {kriszti_win}')
        
    elif sanyi == 'papír' and Kriszti == 'kő':
        sanyi_win += 1
        print(f'Sanyi valasztasa {sanyi}, Kriszti valasztasa {Kriszti}, Sanyi nyert! Az allas jelenleg: Sanyi {sanyi_win} / Kriszti {kriszti_win}')

    elif sanyi == 'papír' and Kriszti == 'olló':
        kriszti_win += 1
        print(f'Sanyi valasztasa {sanyi}, Kriszti valasztasa {Kriszti}, Kriszti nyert! Az allas jelenleg: Sanyi {sanyi_win} / Kriszti {kriszti_win}')

    elif sanyi == 'olló' and Kriszti == 'kő':
        kriszti_win += 1
        print(f'Sanyi valasztasa {sanyi}, Kriszti valasztasa {Kriszti}, Kriszti nyert! Az allas jelenleg: Sanyi {sanyi_win} / Kriszti {kriszti_win}')

    elif sanyi == 'olló' and Kriszti == 'papír':
        sanyi_win += 1
        print(f'Sanyi valasztasa {sanyi}, Kriszti valasztasa {Kriszti}, Sanyi nyert! Az allas jelenleg: Sanyi {sanyi_win} / Kriszti {kriszti_win}')