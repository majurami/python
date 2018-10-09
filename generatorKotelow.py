kotely = "ʕ•ᴥ•ʔ"
print (kotely)

owcaUzytkownik = input('Podaj ile kotelow chcesz wygenerowac :) ')
print(owcaUzytkownik)
try:
    owcaUzytkownik = int(owcaUzytkownik) #zamiana tego co wpisal user 
except ValueError as owcaError:
    #tu podajecie instrukcje ktore maja sie wykonac jesli uzytkownik zle poda dane czyli zdarzy sie error 
    owcaUzytkownik = 1
    print("Program potrzebuje liczby a nie ciagu znak")

print (kotely * owcaUzytkownik)