data = []

def register():
    login = (input("Введи свой логин:\n"))
    password = (input("Введи свой пароль:\n"))
    if (login == "ibrahimchik" and password == "xgpz0138" or (login == "egor_zenov" and password == "00000000") or (
        login == "serix_666" and password == "ebuchiynexy666") or (
            login == "GeneralGrievous" and password == "Fraersdalnazad_3") or (
                login == "huy" and password == "penis") or (login == "Jane956" and password == "969013") or (
                    login == "aliya.nur28" and password == "Sezalo1410") or (
                        login == "ar2sha" and password == "qwerty1982ar2sha") or (
                            login == "lina_cherry" and password == "75dhvDark07#$L") or (
                                login == "ivanovao15478" and password == "#4507_rs06") or (
                                    login == "Ben26" and password == "2yT6!hD5sZ")):
        print("\n\nО, кайф!")
        data.append(login)
        data.append(password)
        menu()
    else:
        print("\nКажется, я тебя не знаю ;(\nПопробуй ещё раз\n")
        register()

def quit_all():
    input()

def menu():
    menu_input = input(
        "Чем займёмся сегодня?)\nНажимай соответствующую клавишу, указанную после двоеточия\n\nПроверим ДЗ: "
        "t\nПосмотрим расписание: r\nСделаем дз: d\nОбо мне: i\nВыйти: q\n\n")
    if menu_input == "t":
        task()
    elif menu_input == "r":
        if data[0] == 'ibrahimchik':
            print("\n\nИбрахим, вот твоё расписание:\nСреда: 17:10 - 18:40\n\n")
        elif data[0] == 'egor_zenov':
            print("\n\nЕгор, вот твоё расписание:\nПятница: 17:25 - 18:55\n\n")
        elif data[0] == 'serix_666':
            print("\n\nМаксим, вот твоё расписание:\nСуббота: 21:00 - 22:30\nВоскресенье: 19:55 - 21:25\n\n")
        elif data[0] == 'GeneralGrievous':
            print("\nМаксим, вот твоё расписание:\nСреда: 19:00 - 20:30\nСуббота: 19:15 - 20:45\n")
        elif data[0] == 'huy':
            print("\n\nЕгор, вот твоё расписание:\nСуббота: 21:00 - 22:30\nВоскресенье: 19:55 - 21:25\n\n")
        elif data[0] == 'Jane956':
            print("\n\nЖанна, вот твоё расписание:\nВоскресенье: 11:35 - 13:05\n\n")
        elif data[0] == 'aliya.nur28':
            print("\n\nАлия, вот твоё расписание:\nСреда: 15:35 - 17:05\nПятница: 15:50 - 17:20\n\n")
        elif data[0] == 'ar2sha':
            print("\n\nАртур, вот твоё расписание:\nПонедельник: 22:00 - 23:30\nПятница: 20:55 - 22:25\n\n")
        elif data[0] == 'lina_cherry':
            print(
                "\n\nАлина, вот твоё расписание:\nЧетверг: 19:00 - 20:30 (информатика)\nПятница: 19:20 - 20:50 (русский язык)\nВоскресенье: 16:30 - 18:00\n\n")
        elif data[0] == 'ivanovao15478':
            print("\n\nСаша, вот твоё расписание:\nПонедельник: 20:55 - 22:25\nЧетверг: 20:35 - 22:05\n\n")
        elif data[0] == "Ben26":
            print("\n\nОлег, вот твоё расписание:\nЧетверг: 17:00 - 18:30\nВоскресенье: 14:55 - 16:25\n\n")

        menu()
    elif menu_input == "d":
        print(
            "\nВот твоя ссылка на Яндекс Диск: https://disk.yandex.ru/d/Rs4vuNIHnlB5CA\nТам ты сможешь найти все задания, пробники и конспекты к ним!\n")
        menu()
    elif menu_input == "i":
        print(
            "\nПривет!\nМеня зовут Егор, и я преподаю информатику)\nОкончил одну из лучших школ РФ (Центр Педагогического мастерства), ныне учусь в МГТУ им. Н. Э. Баумана.\n\nВ чем моё ключевое отличие от всех остыльных?\n\n· Всё очень просто - я не придумываю тех заданий, которых не будет на экзамене.\n· Объясняю сложный материал простым языком, чтобы даже 5-ти классник смог понять)\n· На моих уроках нет ни единого правила, ведь моя цель - не вызывать отвращение к информатике, а показать, что сдать инфу на 90+ - легче простого!\n· Моя цель - лишь твои баллы и хорошее настроение, ничего более)\n\nЯ в социальных сетях:\nTelegram: https://t.me/epustovit\nКанал: https://t.me/egepusto\nVK: https://vk.com/pustovitegor\n\n\nВерю в тебя, удачи!\n\n\n")
        menu()
    elif menu_input == "q":
        print("\nПонял)\nХорошего дня!\n")
        quit_all()
    else:
        print("\nК сожалению, не смог распознать введенную команду ;(\nДавай попробуем снова)\n")
        menu()


q1 = ['15', '25', '12', '15', '67', '22', '15', '35', '46', '14', '24', '22', '14', '17', 'БЖКИДАЕГВ']
q2 = ['ywzx', 'wzyx', 'yxzw', 'yxwz', 'zyxw', 'xzwy', 'xwzy', 'zywx', 'wyzx', 'ywzx', 'yzwx', 'yxwz', 'ywzx', 'yzxw', 'zwyx']
q3 = ['680', '820', '966', '24', '48', '268.5', '63140', '251560', '129000', '620', '620', '355', 'М35', 'М20', '1354070']
q4 = ['20', '5', '110', '111', '1100', '23', '18', '19', '22', '24', '26', '35', '10', '00000111', '11111000']
q5 = ['296', '187', '2949', '9878', '1067', '50979', '29', '102', '1009', '23', '61', '180', '7', '103', '9']
q6 = ['64', '40', '40', '18', '66', '60', '73', '13', '145', '18', '174', '15', '195', '237', '15']
q7 = ['200', '64', '1081', '64', '12', '10', '198', '120', '8', '1', '10', '1080', '150', '43200', '24']
q8 = ['РРРОК', 'РКРКО', '82', '3073', '2711', '720', '8880', '126', '160', '1863219', '405', '150', '6075', '192', '293601280']
q9 = ['2453', '1074', '2', '1842', '2640', '2241', '303', '445', '61', '83', '24', '10', '36', '6840', '1483']
q10 = ['2', '1', '2', '1', '5', '6', '42', '271', '32', '20', '8', '7', '7', '20', '10']
q11 = ['200', '60', '100', '4992', '4736', '2500', '160', '700', '43', '14', '5', '750', '9', '26', '22']
q12 = ['28', '339', '888', '388', '28', '6', '2', '16', '156', '40', '12', '138', '110', '5', '98']
q13 = ['ГБВА', 'ВБГА', 'ВГАБ', 'ЕЗБГДВЖА', 'egadbfc', 'ГВЖЕДБА', 'HBEA', 'ECFA', 'HBFA', '248', '19', '20', '7235', '29', '674']
q14 = ['8767', '1597', '9', '26789', '7', '27', '14', '5310266', '194', '229', '224', '2715', '41428', '18754', '224']
q15 = ['23', '99', '81', '27', '23', '94', '90', '30', '44', '38', '0', '12', '24', '12', '5']
q16 = ['120', '3194', '4090506', '34602572', '49', '142', '5', '38', '18', '32', '89', '134', '720', '259060409', '880']
q17 = ['2802 1990', '635 19730', '170 18662', '1061 14847', '205 99520570', '212587 9972', '4999742 19990', '9082691 19995', '13510315 19999', '29278 19860', '1175 29451', '299 196183', '1684', '2453 -176846', '78 115709']
q18 = ['1212 392', '1496 782', '1372 648', '1322 594', '1439 681', '721 640', '2656 1665', '2226  902', '2167 718', '1102 1029', '1911 178', '1825 236', '321', '358', '69']
q19_21 = ['3 9 12 8', '11 10 17 19 16', '11 10 18 19 17', '9 8 22 23 21', '28 25 26 23', '118 113 117 112', '29 25 28 24', '29 25 28 24', '70 27 29 52', '4 12 14 13', '18 31 34 30', '7 16 19 18', '13 20 25 24', '43 27 42 38', '55 31 54 50', '28 20 29 9']
q22 = ['24', '34', '25', '34', '25', '47', '2', '6', '5', '1', '9', '6', '7', '73', '65']
q23 = ['22', '89', '23', '38', '50', '45', '1232', '13', '26', '37', '21', '45', '40', '372', '170']
# q24 = []
q25 = ['1072461 1272460371 1772469231', '1076020 10760200 107602000 1076020000 1576026930', '1271361 4657 12633621 46277 12663651 46387 12693681 46497', '321657 159 34105757 16859 35117257 17359 36128757 17859 37140257 18359 38151757 18859 39163257 19359', '154698 59 11468628 4374 12425658 4739 15401628 5874 16476648 6284 17433678 6649 19452618 7419', '3 58153 7 24923 59 2957 13 13421 149 1171 5 34897 211 827 2 87251', '2 4 52561 105122 2 4 52567 105134 2 4 52571 105142', '1 2 4 78157 156314 312628 1 3 9 34739 104217 312651', '2 4 55102 110204 2 14 15746 110222 2 6 36742 110226 2 22 10022 110242', '144 568260', '1728 21632 1260 1152 4127787', '6876 6374 6924 8024 8358', '17 1119403 151 16666667 27272728', '700005 233338 700007 100008 700012 350008 700015 140008 700031 24168', '500002 178 500004 18 500016 48 500018 58 500020 4348']
# q26 = []
# q27 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '']


def task():
    task_input = input("\nВведи номер задания:\n")
    if task_input == "1":
        q_input = []
        for i in range(1, 16):
            q_input.append(input(f"Введи ответ на задание №{i}:""\nЕсли число не является целым, то отделяй точкой целую часть от дробной)\nЕсли в ответе требуется указать 2 ответа, то вписывай их через пробел\n"))
        if q_input == q1:
            print("\nПоздравляю! Слово номер 1:\nНе")
            quit_middle()
        else:
            print("\n")
            for i in range(len(q1)):
                if q1[i] != q_input[i]:
                    print(f"Кажется, я нашел ошибку в №{i + 1}." + "\n" + f"Правильный ответ: {q1[i]}" + "\n")

                else:
                    continue
            print("\nПопробуешь переделать задание?)")
            quit_middle()

    elif task_input == "2":
        q_input = []
        for i in range(1, 16):
            q_input.append(input(f"Введи ответ на задание №{i}:""\nЕсли число не является целым, то отделяй точкой целую часть от дробной)\nЕсли в ответе требуется указать 2 ответа, то вписывай их через пробел\n"))
        if q_input == q2:
            print("\nПоздравляю! Слово номер 2:\nбывает")
            quit_middle()
        else:
            print("\n")
            for i in range(len(q2)):
                if q2[i] != q_input[i]:
                    print(f"Кажется, я нашел ошибку в №{i + 1}." + "\n" + f"Правильный ответ: {q2[i]}" + "\n")

                else:
                    continue
            print("\nПопробуешь переделать задание?)")
            quit_middle()

    elif task_input == "3":
        q_input = []
        for i in range(1, 16):
            q_input.append(input(f"Введи ответ на задание №{i}:""\nЕсли число не является целым, то отделяй точкой целую часть от дробной)\nЕсли в ответе требуется указать 2 ответа, то вписывай их через пробел\n"))
        if q_input == q3:
            print("\nПоздравляю! Слово номер 3:\nсложных")
            quit_middle()
        else:
            print("\n")
            for i in range(len(q3)):
                if q3[i] != q_input[i]:
                    print(f"Кажется, я нашел ошибку в №{i + 1}." + "\n" + f"Правильный ответ: {q3[i]}" + "\n")

                else:
                    continue
            print("\nПопробуешь переделать задание?)")
            quit_middle()

    elif task_input == "4":
        q_input = []
        for i in range(1, 16):
            q_input.append(input(f"Введи ответ на задание №{i}:""\nЕсли число не является целым, то отделяй точкой целую часть от дробной)\nЕсли в ответе требуется указать 2 ответа, то вписывай их через пробел\n"))
        if q_input == q4:
            print("\nПоздравляю! Слово номер 4:\nзаданий. ")
            quit_middle()
        else:
            print("\n")
            for i in range(len(q4)):
                if q4[i] != q_input[i]:
                    print(f"Кажется, я нашел ошибку в №{i + 1}." + "\n" + f"Правильный ответ: {q4[i]}" + "\n")

                else:
                    continue
            print("\nПопробуешь переделать задание?)")
            quit_middle()

    elif task_input == "5":
        q_input = []
        for i in range(1, 16):
            q_input.append(input(f"Введи ответ на задание №{i}:""\nЕсли число не является целым, то отделяй точкой целую часть от дробной)\nЕсли в ответе требуется указать 2 ответа, то вписывай их через пробел\n"))
        if q_input == q5:
            print("\nПоздравляю! Слово номер 5:\nСуществуют")
            quit_middle()
        else:
            print("\n")
            for i in range(len(q5)):
                if q5[i] != q_input[i]:
                    print(f"Кажется, я нашел ошибку в №{i + 1}." + "\n" + f"Правильный ответ: {q5[i]}" + "\n")

                else:
                    continue
            print("\nПопробуешь переделать задание?)")
            quit_middle()

    elif task_input == "6":
        q_input = []
        for i in range(1, 16):
            q_input.append(input(f"Введи ответ на задание №{i}:""\nЕсли число не является целым, то отделяй точкой целую часть от дробной)\nЕсли в ответе требуется указать 2 ответа, то вписывай их через пробел\n"))
        if q_input == q6:
            print("\nПоздравляю! Слово номер 6:\nлишь")
            quit_middle()
        else:
            print("\n")
            for i in range(len(q6)):
                if q6[i] != q_input[i]:
                    print(f"Кажется, я нашел ошибку в №{i + 1}." + "\n" + f"Правильный ответ: {q6[i]}" + "\n")

                else:
                    continue
            print("\nПопробуешь переделать задание?)")
            quit_middle()

    elif task_input == "7":
        q_input = []
        for i in range(1, 16):
            q_input.append(input(f"Введи ответ на задание №{i}:""\nЕсли число не является целым, то отделяй точкой целую часть от дробной)\nЕсли в ответе требуется указать 2 ответа, то вписывай их через пробел\n"))
        if q_input == q7:
            print("\nПоздравляю! Слово номер 7:\nте,")
            quit_middle()
        else:
            print("\n")
            for i in range(len(q7)):
                if q7[i] != q_input[i]:
                    print(f"Кажется, я нашел ошибку в №{i + 1}." + "\n" + f"Правильный ответ: {q7[i]}" + "\n")

                else:
                    continue
            print("\nПопробуешь переделать задание?)")
            quit_middle()

    elif task_input == "8":
        q_input = []
        for i in range(1, 16):
            q_input.append(input(f"Введи ответ на задание №{i}:""\nЕсли число не является целым, то отделяй точкой целую часть от дробной)\nЕсли в ответе требуется указать 2 ответа, то вписывай их через пробел\n"))
        if q_input == q8:
            print("\nПоздравляю! Слово номер 8:\nрешения")
            quit_middle()
        else:
            print("\n")
            for i in range(len(q8)):
                if q8[i] != q_input[i]:
                    print(f"Кажется, я нашел ошибку в №{i + 1}." + "\n" + f"Правильный ответ: {q8[i]}" + "\n")

                else:
                    continue
            print("\nПопробуешь переделать задание?)")
            quit_middle()

    elif task_input == "9":
        q_input = []
        for i in range(1, 16):
            q_input.append(input(f"Введи ответ на задание №{i}:""\nЕсли число не является целым, то отделяй точкой целую часть от дробной)\nЕсли в ответе требуется указать 2 ответа, то вписывай их через пробел\n"))
        if q_input == q9:
            print("\nПоздравляю! Слово номер 9:\nкоторых")
            quit_middle()
        else:
            print("\n")
            for i in range(len(q9)):
                if q9[i] != q_input[i]:
                    print(f"Кажется, я нашел ошибку в №{i + 1}." + "\n" + f"Правильный ответ: {q9[i]}" + "\n")

                else:
                    continue
            print("\nПопробуешь переделать задание?)")
            quit_middle()

    elif task_input == "10":
        q_input = []
        for i in range(1, 16):
            q_input.append(input(f"Введи ответ на задание №{i}:""\nЕсли число не является целым, то отделяй точкой целую часть от дробной)\nЕсли в ответе требуется указать 2 ответа, то вписывай их через пробел\n"))
        if q_input == q10:
            print("\nПоздравляю! Слово номер 10:\nты")
            quit_middle()
        else:
            print("\n")
            for i in range(len(q10)):
                if q10[i] != q_input[i]:
                    print(f"Кажется, я нашел ошибку в №{i + 1}." + "\n" + f"Правильный ответ: {q10[i]}" + "\n")

                else:
                    continue
            print("\nПопробуешь переделать задание?)")
            quit_middle()

    elif task_input == "11":
        q_input = []
        for i in range(1, 16):
            q_input.append(input(f"Введи ответ на задание №{i}:""\nЕсли число не является целым, то отделяй точкой целую часть от дробной)\nЕсли в ответе требуется указать 2 ответа, то вписывай их через пробел\n"))
        if q_input == q11:
            print("\nПоздравляю! Слово номер 11:\nплохо")
            quit_middle()
        else:
            print("\n")
            for i in range(len(q11)):
                if q11[i] != q_input[i]:
                    print(f"Кажется, я нашел ошибку в №{i + 1}." + "\n" + f"Правильный ответ: {q11[i]}" + "\n")

                else:
                    continue
            print("\nПопробуешь переделать задание?)")
            quit_middle()

    elif task_input == "12":
        q_input = []
        for i in range(1, 16):
            q_input.append(input(f"Введи ответ на задание №{i}:""\nЕсли число не является целым, то отделяй точкой целую часть от дробной)\nЕсли в ответе требуется указать 2 ответа, то вписывай их через пробел\n"))
        if q_input == q12:
            print("\nПоздравляю! Слово номер 12:\nпомнишь. ")
            quit_middle()
        else:
            print("\n")
            for i in range(len(q12)):
                if q12[i] != q_input[i]:
                    print(f"Кажется, я нашел ошибку в №{i + 1}." + "\n" + f"Правильный ответ: {q12[i]}" + "\n")

                else:
                    continue
            print("\nПопробуешь переделать задание?)")
            quit_middle()

    elif task_input == "13":
        q_input = []
        for i in range(1, 16):
            q_input.append(input(f"Введи ответ на задание №{i}:""\nЕсли число не является целым, то отделяй точкой целую часть от дробной)\nЕсли в ответе требуется указать 2 ответа, то вписывай их через пробел\n"))
        if q_input == q13:
            print("\nПоздравляю! Слово номер 13:\nПомни - ")
            quit_middle()
        else:
            print("\n")
            for i in range(len(q13)):
                if q13[i] != q_input[i]:
                    print(f"Кажется, я нашел ошибку в №{i + 1}." + "\n" + f"Правильный ответ: {q13[i]}" + "\n")

                else:
                    continue
            print("\nПопробуешь переделать задание?)")
            quit_middle()

    elif task_input == "14":
        q_input = []
        for i in range(1, 16):
            q_input.append(input(f"Введи ответ на задание №{i}:""\nЕсли число не является целым, то отделяй точкой целую часть от дробной)\nЕсли в ответе требуется указать 2 ответа, то вписывай их через пробел\n"))
        if q_input == q14:
            print("\nПоздравляю! Слово номер 14:\nты")
            quit_middle()
        else:
            print("\n")
            for i in range(len(q14)):
                if q14[i] != q_input[i]:
                    print(f"Кажется, я нашел ошибку в №{i + 1}." + "\n" + f"Правильный ответ: {q14[i]}" + "\n")

                else:
                    continue
            print("\nПопробуешь переделать задание?)")
            quit_middle()

    elif task_input == "15":
        q_input = []
        for i in range(1, 16):
            q_input.append(input(f"Введи ответ на задание №{i}:""\nЕсли число не является целым, то отделяй точкой целую часть от дробной)\nЕсли в ответе требуется указать 2 ответа, то вписывай их через пробел\n"))
        if q_input == q15:
            print("\nПоздравляю! Слово номер 15:\nвсё")
            quit_middle()
        else:
            print("\n")
            for i in range(len(q15)):
                if q15[i] != q_input[i]:
                    print(f"Кажется, я нашел ошибку в №{i + 1}." + "\n" + f"Правильный ответ: {q15[i]}" + "\n")

                else:
                    continue
            print("\nПопробуешь переделать задание?)")
            quit_middle()

    elif task_input == "16":
        q_input = []
        for i in range(1, 16):
            q_input.append(input(f"Введи ответ на задание №{i}:""\nЕсли число не является целым, то отделяй точкой целую часть от дробной)\nЕсли в ответе требуется указать 2 ответа, то вписывай их через пробел\n"))
        if q_input == q16:
            print("\nПоздравляю! Слово номер 16:\nможешь! ")
            quit_middle()
        else:
            print("\n")
            for i in range(len(q16)):
                if q16[i] != q_input[i]:
                    print(f"Кажется, я нашел ошибку в №{i + 1}." + "\n" + f"Правильный ответ: {q16[i]}" + "\n")

                else:
                    continue
            print("\nПопробуешь переделать задание?)")
            quit_middle()

    elif task_input == "17":
        q_input = []
        for i in range(1, 16):
            q_input.append(input(f"Введи ответ на задание №{i}:""\nЕсли число не является целым, то отделяй точкой целую часть от дробной)\nЕсли в ответе требуется указать 2 ответа, то вписывай их через пробел\n"))
        if q_input == q17:
            print("\nПоздравляю! Слово номер 17:\nМы")
            quit_middle()
        else:
            print("\n")
            for i in range(len(q17)):
                if q17[i] != q_input[i]:
                    print(f"Кажется, я нашел ошибку в №{i + 1}." + "\n" + f"Правильный ответ: {q17[i]}" + "\n")

                else:
                    continue
            print("\nПопробуешь переделать задание?)")
            quit_middle()

    elif task_input == "18":
        q_input = []
        for i in range(1, 16):
            q_input.append(input(f"Введи ответ на задание №{i}:""\nЕсли число не является целым, то отделяй точкой целую часть от дробной)\nЕсли в ответе требуется указать 2 ответа, то вписывай их через пробел\n"))
        if q_input == q18:
            print("\nПоздравляю! Слово номер 18:\nвсё")
            quit_middle()
        else:
            print("\n")
            for i in range(len(q18)):
                if q18[i] != q_input[i]:
                    print(f"Кажется, я нашел ошибку в №{i + 1}." + "\n" + f"Правильный ответ: {q18[i]}" + "\n")

                else:
                    continue
            print("\nПопробуешь переделать задание?)")
            quit_middle()

    elif task_input == "19":
        print("\nВесь блок теории игр собран в этом задании)\nСледующее доступное задание для выполнения - №22\nЖелаю удачи!")
        q_input = []
        for i in range(1, 16):
            q_input.append(input(f"Введи ответ на задание №{i}:""\nЕсли число не является целым, то отделяй точкой целую часть от дробной)\nЕсли в ответе требуется указать нескольков ответов, то вписывай их через пробел\nНа каждое из 3 заданий блока теории игр (№19-21), вписывай ответы через пробел\n"))
        if q_input == q19_21:
            print("\nПоздравляю! Фраза номер 19:\nразбирали) Желаю удачи")
            quit_middle()
        else:
            print("\n")
            for i in range(len(q19_21)):
                if q19_21[i] != q_input[i]:
                    print(f"Кажется, я нашел ошибку в №{i + 1}." + "\n" + f"Правильный ответ: {q19_21[i]}" + "\n")

                else:
                    continue
            print("\nПопробуешь переделать задание?)")
            quit_middle()


    elif task_input == "22":
        q_input = []
        for i in range(1, 16):
            q_input.append(input(f"Введи ответ на задание №{i}:""\nЕсли число не является целым, то отделяй точкой целую часть от дробной)\nЕсли в ответе требуется указать 2 ответа, то вписывай их через пробел\n"))
        if q_input == q22:
            print("\nПоздравляю! Слово номер 22:\nна")
            quit_middle()
        else:
            print("\n")
            for i in range(len(q22)):
                if q22[i] != q_input[i]:
                    print(f"Кажется, я нашел ошибку в №{i + 1}." + "\n" + f"Правильный ответ: {q22[i]}" + "\n")

                else:
                    continue
            print("\nПопробуешь переделать задание?)")
            quit_middle()

    elif task_input == "23":
        q_input = []
        for i in range(1, 16):
            q_input.append(input(f"Введи ответ на задание №{i}:""\nЕсли число не является целым, то отделяй точкой целую часть от дробной)\nЕсли в ответе требуется указать 2 ответа, то вписывай их через пробел\n"))
        if q_input == q23:
            print("\nПоздравляю! Слово номер 23:\nэкзамене")
            quit_middle()
        else:
            print("\n")
            for i in range(len(q23)):
                if q23[i] != q_input[i]:
                    print(f"Кажется, я нашел ошибку в №{i + 1}." + "\n" + f"Правильный ответ: {q23[i]}" + "\n")

                else:
                    continue
            print("\nПопробуешь переделать задание?)")
            quit_middle()

    # elif task_input == "24":
    #     q_input = []
    #     for i in range(1, 16):
    #         q_input.append(input(f"Введи ответ на задание №{i}:""\nЕсли число не является целым, то отделяй точкой целую часть от дробной)\nЕсли в ответе требуется указать 2 ответа, то вписывай их через пробел\n"))
    #     if q_input == q24:
    #         print("\nПоздравляю! Слово номер 24:\nС")
    #         quit_middle()
    #     else:
    #         print("\n")
    #         for i in range(len(q24)):
    #             if q24[i] != q_input[i]:
    #                 print(f"Кажется, я нашел ошибку в №{i + 1}." + "\n" + f"Правильный ответ: {q24[i]}" + "\n")
    # 
    #             else:
    #                 continue
    #         print("\nПопробуешь переделать задание?)")
    #         quit_middle()
    # 
    elif task_input == "25":
        q_input = []
        for i in range(1, 16):
            q_input.append(input(f"Введи ответ на задание №{i}:""\nЕсли число не является целым, то отделяй точкой целую часть от дробной)\nЕсли в ответе требуется указать нескольков ответов, то вписывай их через пробел\n"))
        if q_input == q25:
            print("\nПоздравляю! Слово номер 25:\nнаилучшими")
            quit_middle()
        else:
            print("\n")
            for i in range(len(q25)):
                if q25[i] != q_input[i]:
                    print(f"Кажется, я нашел ошибку в №{i + 1}." + "\n" + f"Правильный ответ: {q25[i]}" + "\n")

                else:
                    continue
            print("\nПопробуешь переделать задание?)")
            quit_middle()

            # elif task_input == "26":
            #     q_input = []
            #     for i in range(1, 16):
            #         q_input.append(input(f"Введи ответ на задание №{i}:""\nЕсли число не является целым, то отделяй точкой целую часть от дробной)\nЕсли в ответе требуется указать 2 ответа, то вписывай их через пробел\n"))
            #     if q_input == q26:
            #         print("\nПоздравляю! Слово номер 26:\nпожеланиями, ")
            #         quit_middle()
            #     else:
            #         print("\n")
            #         for i in range(len(q26)):
            #             if q26[i] != q_input[i]:
            #                 print(f"Кажется, я нашел ошибку в №{i + 1}." + "\n" + f"Правильный ответ: {q26[i]}" + "\n")
            # 
            #             else:
            #                 continue
            #         print("\nПопробуешь переделать задание?)")
            #         quit_middle()
            # 
            # elif task_input == "27":
            #     q_input = []
            #     for i in range(1, 16):
            #         q_input.append(input(f"Введи ответ на задание №{i}:""\nЕсли число не является целым, то отделяй точкой целую часть от дробной)\nЕсли в ответе требуется указать 2 ответа, то вписывай их через пробел\n"))
            #     if q_input == q27:
            #         print("\nПоздравляю! Слово номер 27:\nЕгор)")
            #         quit_middle()
            #     else:
            #         print("\n")
            #         for i in range(len(q27)):
            #             if q27[i] != q_input[i]:
            #                 print(f"Кажется, я нашел ошибку в №{i + 1}." + "\n" + f"Правильный ответ: {q27[i]}" + "\n")
            # 
            #             else:
            #                 continue
            print("\nПопробуешь переделать задание?)")
            quit_middle()

    else:
        print("\nКажется, номер твоего задания вышел за пределы адекватности)\nПопробуй еще раз) ")
        task()





def quit_middle():
    quit_middle_input = input("\nЕсли хочешь выйти - нажми q, иначе - любую другую клавишу):\n\n")
    if quit_middle_input == "q":
        print("\nОкс")
        menu()
    else:
        print("\nОкей, погнали дальше!")
        task()


print("\nПривет! Это - моё приложение, которое позволяет выполнять ДЗ, автоматически проверять их, смотреть расписание и многое другое")
print("Отныне, тебе не придётся ждать по 100 лет, чтобы получить обратную связь по всем вопросам)")
print("\n\nНа протяжении всей программы заложен квест. Его суть заключается в следующем:\nРешая задачи, ты будешь находить слова. Твоя задача: собрать предложение из этих слов и написать его мне ;)\nЧтобы не потерять слово, советую сразу же после выполнения задания писать его мне)")
print("\nЧто ж, приступим!\n")

register()
