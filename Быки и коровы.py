import random
import tkinter

# Настройки игры
bgcolor = '#F0F8FF'  # Цвет фона
digits_will_be_repeated = 'No'  # Будут ли повторения в загаданной последовательности цветов
number_of_attempts = 10  # Количество попыток, которое дается игроку
size_of_sequence = 4  # Длина последовательности
size_of_alphabet = 10  # Количество возможных цветов
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'brown', 'magenta', 'cyan']


def make_number_without_repeats(size, size_of_alphabet):
    """Генерит случайную последовательность цветов длины size без повторений"""
    global colors
    result = []
    while len(result) != size:
        next_digit = random.randint(0, size_of_alphabet - 1)
        if colors[next_digit] not in result:
            result.append(colors[next_digit])
    return result


def make_number_with_repeats(size, size_of_alphabet):
    """Генерит случайную последовательность из size цветов с возможными повторениями"""
    global colors
    result = []
    while len(result) != size:
        next_digit = random.randint(0, size_of_alphabet - 1)
        result.append(colors[next_digit])
    return result


def make_sequence(repeats_or_not, size, size_of_alphabet):
    """Генери последовательность из size цветов, беря их их первых size_of_alphabet цветов colors"""
    if repeats_or_not == 'Yes':
        return make_number_with_repeats(size, size_of_alphabet)
    return make_number_without_repeats(size, size_of_alphabet)


def back_to_main(*args):
    """Удаляет все переданные окна и возвращает в главное меню"""
    for x_window in args:
        x_window.destroy()
    main_window.deiconify()


def rules():
    """Делает окошно, где объясняются правила игры"""
    main_window.withdraw()
    rules_window = tkinter.Tk()
    rules_window["bg"] = bgcolor
    rules_window.geometry('400x500')
    rules_window.title('Правила игры')
    text = tkinter.Text(rules_window,
                        bg=bgcolor,
                        fg='black',
                        font='arial 12')
    text.insert('insert', " Быки и коровы — логическая игра, в ходе которой за\n"
                          "несколько попыток нужно отгадать загаданную \n"
                          "последовательность цветов.\n"
                          "После каждой попытки выставляется «оценка»,\n"
                          "указывая тем самым на количество\n"
                          "угаданного без совпадения с их позициями\n"
                          "(количество «коров») и полных совпадений\n"
                          "(количество «быков»).\n"
                          "На сером фоне - количество коров\n"
                          "На черном - быков")
    text.config(state='disabled')
    text.pack()
    back_button = tkinter.Button(rules_window,  # Кнопка, возвращающая в главное меню
                                 text='Назад',
                                 bg='#E32636',
                                 fg='white',
                                 font='arial 15',
                                 command=lambda: back_to_main(rules_window))
    back_button.place(anchor='center',
                      relx=0.5, rely=0.50,
                      relwidth=0.4,
                      relheight=0.1)
    rules_window.mainloop()


def repetitions(will_be):
    """Запоминает, будут ли повторения (если 'Yes') или нет (Если 'No')"""
    global digits_will_be_repeated
    digits_will_be_repeated = will_be


def remember_size(val):
    """Запоминает длину загадонной последовательности цветов"""
    global size_of_sequence
    size_of_sequence = int(val)


def remember_attempts(val):
    """Запоминает максимальное количество попыток"""
    global number_of_attempts
    number_of_attempts = int(val)


def remember_alphabet(val):
    """Запоминает количество доступных цветов"""
    global size_of_alphabet
    size_of_alphabet = int(val)


def settings():
    """Делает окно, где можно поменять настройки"""
    main_window.withdraw()
    settings_window = tkinter.Tk()
    settings_window["bg"] = bgcolor
    settings_window.geometry('400x500')
    settings_window.title('Настройки')
    global number_of_attempts
    global size_of_sequence
    global size_of_alphabet

    text_num_of_attempts = tkinter.Label(settings_window,
                                         text='Количество попыток',
                                         bg=bgcolor,
                                         font='Times 15')
    text_num_of_attempts.place(anchor='center',
                               relx=0.5, rely=0.05,
                               relwidth=1,
                               relheight=0.1)

    scale_attempts = tkinter.Scale(settings_window, bg=bgcolor,
                                   from_=4, to=20, orient='horizontal', command=remember_attempts)
    scale_attempts.place(anchor='center',
                         relx=0.5, rely=0.13,
                         relwidth=1,
                         relheight=0.08)
    scale_attempts.set(number_of_attempts)  # Устанавливает либо последнее, либо дефолтное значение

    text_size_of_guessed = tkinter.Label(settings_window,
                                         text='Размер загадонной последовательности',
                                         bg=bgcolor,
                                         font='Times 15')
    text_size_of_guessed.place(anchor='center',
                               relx=0.5, rely=0.25,
                               relwidth=1,
                               relheight=0.1)

    scale_size_of_sequence = tkinter.Scale(settings_window,  # Шкала для выбора длины последовательности
                                           bg=bgcolor,
                                           from_=1, to=10,
                                           orient='horizontal',
                                           command=remember_size)
    scale_size_of_sequence.place(anchor='center',
                                 relx=0.5, rely=0.33,
                                 relwidth=1,
                                 relheight=0.08)
    scale_size_of_sequence.set(size_of_sequence)  # Устанавливает либо последнее, либо дефолтное значение

    text_alphabet = tkinter.Label(settings_window,
                                  text='Сколько цветов всего',
                                  bg=bgcolor,
                                  font='Times 15')
    text_alphabet.place(anchor='center',
                        relx=0.5, rely=0.45,
                        relwidth=1,
                        relheight=0.1)

    scale_alphabet = tkinter.Scale(settings_window,  # Шкала для выбора размера алфавита (кол-ва доступных цветов)
                                   bg=bgcolor,
                                   from_=1, to=10,
                                   orient='horizontal',
                                   command=remember_alphabet)
    scale_alphabet.place(anchor='center',
                         relx=0.5, rely=0.53,
                         relwidth=1,
                         relheight=0.08)
    scale_alphabet.set(size_of_alphabet)

    text_repetitions = tkinter.Label(settings_window,
                                     text='Будут ли повторения',
                                     bg=bgcolor,
                                     font='Times 15')
    text_repetitions.place(anchor='center',
                           relx=0.5, rely=0.65,
                           relwidth=1,
                           relheight=0.1)

    # Далее - две кнопки, отвечающие за то, будут ли повторения или нет
    b_repetitions_yes = tkinter.Button(settings_window,
                                       text='Да',
                                       bg='#E32636',
                                       fg='white',
                                       font='arial 15',
                                       command=lambda: repetitions('Yes'))
    b_repetitions_yes.place(anchor='center',
                            relx=0.25, rely=0.75,
                            relwidth=0.35,
                            relheight=0.1)

    b_repetitions_no = tkinter.Button(settings_window,
                                      text='Нет',
                                      bg='#E32636',
                                      fg='white',
                                      font='arial 15',
                                      command=lambda: repetitions('No'))
    b_repetitions_no.place(anchor='center',
                           relx=0.75, rely=0.75,
                           relwidth=0.35,
                           relheight=0.1)

    b_back = tkinter.Button(settings_window,  # Кнопка возврата в главное меню
                            text='Назад',
                            bg='#E32636',
                            fg='white',
                            font='arial 15',
                            command=lambda: back_to_main(settings_window))
    b_back.place(anchor='center',
                 relx=0.5, rely=0.9,
                 relwidth=0.35,
                 relheight=0.1)


def size_of_alph_error():
    """Всплывает, если размер алфавита меньше длины последовательности и если не должно быть повторений"""
    error_window = tkinter.Tk()
    error_window["bg"] = bgcolor
    error_window.geometry('400x150')
    error_window.title('Ошибка')
    text_of_error = tkinter.Label(error_window,  # Текст ошибки
                                  text='Если вы играете бех повторений,\n'
                                       'размер загаданного не может превышать\n'
                                       'общего количества цветов',
                                  bg=bgcolor,
                                  font='Times 15')
    text_of_error.place(anchor='center',
                        relx=0.5, rely=0.3,
                        relwidth=1,
                        relheight=1)

    b_back = tkinter.Button(error_window,  # Кнопка возврата в главное меню
                            text='Назад',
                            bg='#E32636',
                            fg='white',
                            font='arial 15',
                            command=lambda: back_to_main(error_window))
    b_back.place(anchor='n',
                 relx=0.5, rely=0.65,
                 relwidth=0.4,
                 relheight=0.2)


def make_guess(color, all_buttons, current_attempt):
    """Определяет, что происходит, если нажать на один из доступных цыетов"""
    global digits_will_be_repeated
    cur_colors = [x['bg'] for x in all_buttons[current_attempt[0]]]  # Сохранили цвета (догадку игрока)
    for button in all_buttons[current_attempt[0]]:
        if digits_will_be_repeated == 'No' and color in cur_colors:
            break  # Если повторений не должно быть, то нажатие не делает ничего, если на этот цвет уже нажимали
        if button['bg'] == bgcolor:
            button['bg'] = color
            break  # Иначе красит самую левую (в текубщей строке) незакрашенную в нужный цвет


def re_guess(button, current_attempt, all_buttons):
    """Отменяет догадку"""
    if button in all_buttons[current_attempt[0]]:  # Если эта кнопка в текущей строке, то можно вернуть как было
        button.config(bg=bgcolor)


def victory(new_game_window):
    """Определяет, что происходит, если игрок догадался"""
    victory_window = tkinter.Tk()
    victory_window["bg"] = bgcolor
    victory_window.geometry('400x150')
    victory_window.title('Победа')
    text_of_error = tkinter.Label(victory_window,  # Выводит окно с текстом
                                  text='Красавчик',
                                  bg=bgcolor,
                                  font='Times 20')
    text_of_error.place(anchor='center',
                        relx=0.5, rely=0.3,
                        relwidth=1,
                        relheight=1)

    b_back = tkinter.Button(victory_window,  # Кнопка возврата в главное меню
                            text='Назад',
                            bg='#E32636',
                            fg='white',
                            font='arial 15',
                            command=lambda: back_to_main(victory_window, new_game_window))
    b_back.place(anchor='n',
                 relx=0.5, rely=0.65,
                 relwidth=0.4,
                 relheight=0.2)


def defeat(new_game_window):
    """Определяет, что происходит, если игрок не успел догадаться"""
    victory_window = tkinter.Tk()
    victory_window["bg"] = bgcolor
    victory_window.geometry('410x150')
    victory_window.title('Победа')
    text_of_error = tkinter.Label(victory_window,  # Выводит окно с текстом
                                  text='Ай-ай-ай, сплошное разочарование!',
                                  bg=bgcolor,
                                  font='Times 20')
    text_of_error.place(anchor='center',
                        relx=0.5, rely=0.3,
                        relwidth=1,
                        relheight=1)

    b_back = tkinter.Button(victory_window,  # Кнопка возврата в главное меню
                            text='Назад',
                            bg='#E32636',
                            fg='white',
                            font='arial 15',
                            command=lambda: back_to_main(victory_window, new_game_window))
    b_back.place(anchor='n',
                 relx=0.5, rely=0.65,
                 relwidth=0.4,
                 relheight=0.2)


def guess_confirm(new_game_window, current_attempt, all_buttons, guessed_colors):
    """Определяет, что происходит, когда игрок нажал на "подтвердить", то есть когда хочет узнать, угадал или нет"""
    cows = 0  # Количество коров - угаданных цветов с неугаданной позицией
    bulls = 0  # Количество быков - угаданных цветов с угаданной позицией
    current_colors = [x['bg'] for x in all_buttons[current_attempt[0]]]  # Догадка игрока (лист цветов)
    for i in range(size_of_sequence):
        if current_colors[i] == guessed_colors[i]:
            bulls += 1
        elif current_colors[i] in guessed_colors:
            cows += 1

    cows_button = tkinter.Button(new_game_window,  # Покажет количество коров
                                 text='{}'.format(cows),
                                 bg='grey',
                                 fg='white',

                                 font='arial 10')
    cows_button.place(anchor='n',
                      relx=0.90,
                      y=4.4 + current_attempt[0] * 22,
                      relwidth=0.045,
                      relheight=0.03)

    bulls_button = tkinter.Button(new_game_window,  # Покажет количество быков
                                  text='{}'.format(bulls),
                                  bg='black',
                                  fg='white',
                                  font='arial 10')
    bulls_button.place(anchor='n',
                       relx=0.95,
                       y=4.4 + current_attempt[0] * 22,
                       relwidth=0.045,
                       relheight=0.03)
    current_attempt[0] += 1  # Увеличивает номер попытки
    if bulls == size_of_sequence:  # Если все быки, то победа
        victory(new_game_window)
    if current_attempt[0] == number_of_attempts:  # Если попытки кончились, то поражение
        defeat(new_game_window)


def new_game():
    """Отвечает, что будет происходить при нажатии "Новая игра" """
    global size_of_alphabet
    global size_of_sequence
    global digits_will_be_repeated
    guessed_colors = make_sequence(digits_will_be_repeated, size_of_sequence, size_of_alphabet)  # Загадываются цвета
    current_attempt = [0]  # Какая по счету попытка. Лист, чтобы можно было менять в функциях

    main_window.withdraw()
    new_game_window = tkinter.Tk()
    new_game_window["bg"] = bgcolor
    new_game_window.geometry('400x500')
    new_game_window.title('Быки и Коровы')

    back_button = tkinter.Button(new_game_window,  # Кнопка возврата в главное меню
                                 text='Назад',
                                 bg='#E32636',
                                 fg='white',
                                 font='arial 15',
                                 command=lambda: back_to_main(new_game_window))

    back_button.place(anchor='n',
                      relx=0.87, rely=0.91,
                      relwidth=0.2,
                      relheight=0.07)

    # Далее - кнопки с доступными цветами для догадок
    names_buttons_alph = (('red', lambda: make_guess('red', all_buttons, current_attempt)),
                          ('orange', lambda: make_guess('orange', all_buttons, current_attempt)),
                          ('yellow', lambda: make_guess('yellow', all_buttons, current_attempt)),
                          ('green', lambda: make_guess('green', all_buttons, current_attempt)),
                          ('blue', lambda: make_guess('blue', all_buttons, current_attempt)),
                          ('purple', lambda: make_guess('purple', all_buttons, current_attempt)),
                          ('pink', lambda: make_guess('pink', all_buttons, current_attempt)),
                          ('brown', lambda: make_guess('brown', all_buttons, current_attempt)),
                          ('magenta', lambda: make_guess('magenta', all_buttons, current_attempt)),
                          ('cyan', lambda: make_guess('cyan', all_buttons, current_attempt)))
    for x, (color, call) in enumerate(names_buttons_alph):
        if x == size_of_alphabet:
            break
        cur_button = tkinter.Button(new_game_window,
                                    bg='{}'.format(color),
                                    command=call)
        cur_button.place(anchor='n',
                         relx=0.08, rely=x/10+0.01,
                         relwidth=0.1,
                         relheight=0.07)

    if size_of_alphabet < size_of_sequence and digits_will_be_repeated == 'No':
        new_game_window.withdraw()
        size_of_alph_error()

    all_buttons = []  # Будет хранить в себе все кнопочки, отвечающие за догадки
    # Далее появляются сначала пустые кнопки, отвечающие за попытки угадать. По мере угадывания они раскрашиваются
    for h in range(number_of_attempts):
        all_buttons.append([])
        for x in range(size_of_sequence):
            cur_button = tkinter.Button(new_game_window,
                                        bg=bgcolor,
                                        relief='ridge')
            cur_button.place(anchor='n',
                             relx=0.23 + x/(1.7 * size_of_sequence),
                             y=4.4 + h*22,
                             relwidth=0.045,
                             relheight=0.03)
            all_buttons[h].append(cur_button)

    for button_list in all_buttons:
        for button in button_list:
            button.config(command=lambda b=button: re_guess(b, current_attempt, all_buttons))

    confirm_button = tkinter.Button(new_game_window,  # Кнопка "подтвердить" догадку, чтобы узнать, угадал или нет
                                    text='Подтвердить',
                                    bg='#E32636',
                                    fg='white',
                                    font='arial 15',
                                    command=lambda: guess_confirm(new_game_window, current_attempt, all_buttons,
                                                                  guessed_colors))
    confirm_button.place(anchor='n',
                         relx=0.45,
                         rely=0.9,
                         relwidth=0.32,
                         relheight=0.07)


main_window = tkinter.Tk()
main_window["bg"] = bgcolor
main_window.geometry("400x500")
main_window.title('Быки и Коровы')
b_NewGame = tkinter.Button(main_window,  # Кнопка "Начать игру"
                           text='Начать игру',
                           bg='#E32636',
                           fg='white',
                           font='arial 15',
                           command=new_game)
b_NewGame.place(anchor='center',
                relx=0.5, rely=0.20,
                relwidth=0.4,
                relheight=0.1)

b_Rules = tkinter.Button(main_window,  # Кнопка "Правила"
                         text='Правила',
                         bg='#E32636',
                         fg='white',
                         font='arial 15',
                         command=rules)
b_Rules.place(anchor='center',
              relx=0.5, rely=0.50,
              relwidth=0.4,
              relheight=0.1)

b_Settings = tkinter.Button(main_window,  # Кнопка "Настройки"
                            text='Настройки',
                            bg='#E32636',
                            fg='white',
                            font='arial 15',
                            command=settings)
b_Settings.place(anchor='center',
                 relx=0.5, rely=0.80,
                 relwidth=0.4,
                 relheight=0.1)

main_window.mainloop()

