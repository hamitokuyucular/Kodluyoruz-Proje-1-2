list1 = [[1, 2], [3, 4], [5, 6, 7]]

def reverse_list(l):
    l.reverse()  # Önce ana listeyi ters çevir
    for sublist in l:  # Sonra her alt liste için:
        if isinstance(sublist, list):  # Eğer alt liste de bir listeyse
            reverse_list(sublist)  # Aynı işlemi recursive olarak uygula

reverse_list(list1)
print(list1)  # [[7, 6, 5], [4, 3], [2, 1]]