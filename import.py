# list_items = [{1:[x for x in range(1,32)]},{2:[x for x in range(1,29)]},{3:[x for x in range(1,32)]},{4:[x for x in range(1,31)]},{5:[x for x in range(1,32)]},{6:[x for x in range(1,31)]},{7:[x for x in range(1,32)]},{8:[x for x in range(1,32)]},{9:[x for x in range(1,31)]},{10:[x for x in range(1,32)]},{11:[x for x in range(1,31)]},{12:[x for x in range(1,32)]}]

# def date_of_birth(list_item,y,month,day) :
#     if month in list_item.keys() and day in list_item[month] :
#         if month + 9 <= 12 :
#             n_month = month + 9s
#             list_year = y.split("-")
#             year = list_year[1]
#             if day in list_items[n_month-1][n_month] :
#                 if day <= 9 and n_month <= 9 :
#                     print(f"date of birth is {year}-0{n_month}-0{day}")
#                 if n_day <= 9 :
#                     print(f"date of birth is {year}-{n_month}-0{day}")
#                 elif n_month <= 9 :
#                     print(f"date of birth is {year}-0{n_month}-{day}")
#                 else :
#                     print(f"date_of birth is {year}-{n_month}-{day}")
#             else :
#                 n_day = max(list_items[n_month-1][n_month])
#                 if n_day <= 9 and n_month <= 9 :
#                     print(f"date of birth is {year}-0{n_month}-0{n_day}")
#                 if n_day <= 9 :
#                     print(f"date of birth is {year}-{n_month}-0{n_day}")
#                 elif n_month <= 9 :
#                     print(f"date of birth is {year}-0{n_month}-{n_day}")
#                 else :
#                     print(f"date of birth is {year}-{n_month}-{n_day}")
#         elif month + 9 > 12 :
#             int_month = month + 9 
#             mo_month = int_month % 13
#             m_month = mo_month + 1
#             list_year = y.split("-")
#             year = int(list_year[1]) + 1
#             if day in list_items[m_month-1][m_month]:
#                 if day <= 9 and m_month <= 9 :
#                     print(f"date of birth is {year}-0{m_month}-0{day}")
#                 if day <= 9 :
#                     print(f"date of birth is {year}-{m_month}-0{day}")
#                 elif m_month <= 9 :
#                     print(f"date of birth is {year}-0{m_month}-{day}")
#                 else : 
#                     print(f"date of birth is {year}-{m_month}-{day}")
#             else :
#                 n_day = max(list_items[m_month-1][m_month])
#                 if n_day <= 9 and m_month <= 9 :
#                     print(f"date of birth is {year}-0{m_month}-0{n_day}")
#                 if n_day <= 9 :
#                     print(f"date of birth is {year}-{m_month}-0{n_day}")
#                 elif m_month <= 9 :
#                     print(f"date of birth is {year}-0{m_month}-{n_day}")
#                 else :
#                     print(f"date of birth is {year}-{m_month}-{n_day}")
#     else :
#         print(f"invalid date")

            
            
# print(date_of_birth(list_items[4],"20-25",5,30))


def characters(string_1,string_2) :
    same_characters = []
    for i in string_2 :
        for j in string_1 :
            if i==j :
                print(i)
                same_characters.append(i)               
    number = len(same_characters)
    return number

case_1 = characters("camel","nand")
print(case_1)


    


