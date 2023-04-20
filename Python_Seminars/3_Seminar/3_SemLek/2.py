# # Напишите программу для печати всех уникальных значений в словаре.
# list_dict = [{"V": "S001"}, {"V": "S002"},
#              {"VI": "S001"}, {"VI": "S005"},
#              {"VII": " S005 "}, {"V": " S009 "},
#              {"VIII": " S007 "}]

list_dict = [{"V": "S001"}, {"V": "S002"},
             {"VI": "S001"}, {"VI": "S005"},
             {"VII": " S005 "}, {"V": " S009 "},
             {"VIII": " S007 "}]


n_list = []
for i in list_dict:
    w_list = list(i.values())
    word = w_list[0]
    word_clear = word.strip()
    n_list.append(word_clear)
print(set(n_list))

# dict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
# result_set = set()

# for i in dict:
#     for j in i:
#         result_set.add(i[j])


# list_dict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, 
#              {"VI": "S005"}, {"VII": " S005 "}, 
#              {" V ":" S009 "}, {" VIII ":" S007 "}]
# unique_dict_items = set()
# for i in list_dict:
#     for j in i.keys():
#         unique_dict_items.add(i[j])
# # print(unique_dict_items)
