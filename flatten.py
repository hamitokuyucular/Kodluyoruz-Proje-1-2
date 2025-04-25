def flatten_list(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):  # Eğer eleman bir liste ise
            flat_list.extend(flatten_list(item))  # Düzleştir
        else:
            flat_list.append(item)  # Değilse direkt listeye ekle
    return flat_list

# Verilen girdi
nested_list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

# Fonksiyonu çağır ve sonucu yazdır
print(flatten_list(nested_list))
