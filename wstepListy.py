#jest pusta lista
pustaOwca = []
#lista z elementami
pelnaOwca = [67, "Tak owce są fajne", True, 67.4, [], [1,2,3]]
#wyciąganie elementów. indeksujemy od 0
pelnaOwca[2] #wyciagnie 3 element
#wyciaganie kawalkow listy
pelnaOwca[0:4] #obie instrukcje wyciagna elementy 1 2 3 4
pelnaOwca[:4] 
#wyciaganie kawalka nie od zera
print (pelnaOwca[1:3]) #wyciagam elementy od indeksu 1 do indeksu 3-1
#zwracanie ostatniego elementu
print(pelnaOwca[-1])
#odwracanie listy
pelnaOwca[::-1] 
# łączenie list
[1,2,3] + [4,5,6]
#dodawanie elementu do listy
pelnaOwca.append(7)