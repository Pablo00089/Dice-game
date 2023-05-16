import random

# data uživatel
random_number_user_1 = random.randint(1,6)
random_number_user_2 = random.randint(1,6)
random_number_user_3 = random.randint(1,6)
total_user_number = int(random_number_user_1 + random_number_user_2 + random_number_user_3)
# data pc
random_number_pc_1 = random.randint(1,6)
random_number_pc_2 = random.randint(1,6)
random_number_pc_3 = random.randint(1,6)
total_number = int(random_number_pc_1 + random_number_pc_2 + random_number_pc_3)


def random_pc_fun():
    print("První pokus.")
    print(f"Počítač hodil číslo: {random_number_pc_1}")
    print("Druhý pokus.")
    print(f"Hodil jsi číslo: {random_number_pc_2}")
    print("Třetí pokus.")
    print(f"Hodil jsi číslo: {random_number_pc_3}")
    print(f"Celkově počítač naházel: {total_number}.")


def random_user_fun():
    play_user = input("Napiš 'h' pro hod kostkou. ")
    if play_user == "h":
        print(f"Hodil jsi číslo: {random_number_user_1}")
    play_user = input("Napiš 'h' pro hod kostkou. ")
    if play_user == "h":
        print(f"Hodil jsi číslo: {random_number_user_2}")
    play_user = input("Napiš 'h' pro hod kostkou. ")
    if play_user == "h":
        random_number_user_3 = random.randint(1,6)
        print(f"Hodil jsi číslo: {random_number_user_3}")
    print(f"Celkově jsi naházel: {total_user_number}.")
    
def choise_who_start():
    print("VÍTEJTE VE HŘE'KOSTKY'!")
    print("-----------------------")
    print("Je na čase si hodit mincí a zjistit kdo začne hrát jako první?!")
    random_virgin_eagle = random.randint(0,1)
    print(random_virgin_eagle)
    user_choise = input("Zvolte: panna nebo orel? ")
    print(random_virgin_eagle)
    if user_choise == "panna" and random_virgin_eagle == 0 or user_choise == "orel" and random_virgin_eagle == 1:
        random_user_fun()
        random_pc_fun()
    else:
        random_pc_fun() 
        random_user_fun()   
            
choise_who_start()

def play_again():
    play_again = input("Chceš hrát znovu? ano/ne: ")
    if play_again == "ano":
        choise_who_start()
    
        

def checking_win(a,b):
    if a > b:
        print("-------------")
        print("VYHRÁL JSI!!!")
        print("-------------")
        play_again()

    elif a < b:
        print("-------------")
        print("PROHRÁL JSI!!!")   
        print("-------------") 
        play_again()
    else:
        print("-------------")
        print("JE TO REMÍZA!!!.")  
        print("-------------")  
        play_again()

checking_win(total_user_number,total_number)