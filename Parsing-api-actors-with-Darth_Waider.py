import requests
import json

base_url = "https://swapi.dev/api/"  # Базовая url
get_actor = "people/4/"     # запрос где видно в каких фильмах снимался актёо


class Parsing_actors_from_films_with_DW():
    """Парсинг актёров кто снимался в в фильмах вместе в Darth Waider"""

    def __init__(self):
        pass

    def get_list_of_films_where_DW_presented(self):
        """Получение списка всех фильмов где есть Darth Waider"""


        url = base_url + get_actor
        print(url)
        result = requests.get(url)
        print("статус код :" + str(result.status_code))
        assert 200 == result.status_code
        if result.status_code == 200:
            print("Успешно!!! Мы получили список всех данных по Darth Vader")
        else:
            print("Провал!!! Запрос ошибочный")
        result.encoding = "utf-8"
        print(result.text)
        check = result.json()
        check_info_value = []
        check_info_value = check.get("films")
        print(check_info_value)
        i = len(check_info_value)


        for k in range(i):                                   # Получение всех имён Киногероев
            result_2 = requests.get(check_info_value[k])
            print("статус код :" + str(result_2.status_code))
            assert 200 == result_2.status_code
            if result_2.status_code == 200:
                print("Успешно!!! Мы получили список фильмов где снимался Darth Vader")
            else:
                print("Провал!!! Запрос ошибочный")
            result_2.encoding = "utf-8"
            print(result_2.text)
            check_2 = result_2.json()
            check_info_value_2 = []
            check_info_value_2 = check_2.get("characters")
            print(check_info_value_2)
            c = len(check_info_value_2)
            print("Всего итераций ", c)


            for a in range(c):                                                # Получение имён всех актёров
                result_3 = result_3 = requests.get(check_info_value_2[a])
                print("статус код :" + str(result_3.status_code))
                assert 200 == result_3.status_code
                if result_3.status_code == 200:
                    print("Успешно!!! Мы получили список всех актёров кто снимался в фильмах вместе с Darth Vader")
                else:
                    print("Провал!!! Запрос ошибочный")
                result_3.encoding = "utf-8"
                print(result_3.text)
                check_3 = result_3.json()
                check_info_value_3 = []
                check_info_value_3 = check_3.get("name")
                print(check_info_value_3)


                my_file = open("Darth_Vader_info.txt", "a+", encoding='utf-8')
                name = check_info_value_3
                my_file.write(check_info_value_3 + "\n")
                my_file.close()


    """Удаление дублей и сохранение файлов в текстовый документ"""

    def remove_dubl(self):
        my_file = open("Darth_Vader_info.txt", "r+")
        file_contents = my_file.read()
        print(file_contents)
        list = []
        for line in file_contents.split("\n"):
            if not line.strip():
                continue
            list.append(line.lstrip())
        print(list)
        li = []
        [li.append(x) for x in list if x not in li]
        print(li)

        with open("Uniques.txt", "w") as file:
            print(*li, file=file, sep="\n")


dw_films = Parsing_actors_from_films_with_DW()
dw_films.get_list_of_films_where_DW_presented()
dw_films.remove_dubl()

print("Парсинг всех актёров кто снимался вместе с Darth Waider завершён")




