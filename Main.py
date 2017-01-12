from tkinter import *
from Modules_for_game import *
import re
import copy

root = Tk()
root.title('Морской бой')
root.minsize(width= 800, height=450)
root.maxsize(width= 800, height=450)

img = Image('photo', file='Ship.png')
root.tk.call('wm', 'iconphoto', root._w, img)
photo1 = PhotoImage(file="bang.png")
photo2 = PhotoImage(file="miss.png")

my_desk = [[0,] * 10 for i in [0,] * 10]
opponent_desk = [[0,] * 10 for i in [0,] * 10]
Flag = False

players_ships = 20
opponent_ships = 20

shoot_op_ship = []


ships_player = {4 : 1, 3 : 2, 2 : 3, 1 : 4}
ships_op = {4 : 1, 3 : 2, 2 : 3, 1 : 4}

count = 20


########################################



fra1 = Frame(root,width=300,height=200, bd = 5, relief=GROOVE)
fra1.grid(row = 1, column = 0, padx = 15)

fra2 = Frame(root,width=300,height=200, bd = 5, relief=GROOVE)
fra2.grid(row = 1, column = 11, padx = 15, pady = 15)

lab1 = Label(root, text = 'Ваша доска:' , font='Arial 12')
lab1.grid(column = 0, row = 0, sticky = W, padx = 15, pady = 10)

lab2 = Label(root, text = 'Доска оппонента:' , font='Arial 12')
lab2.grid(column = 11, row = 0, sticky = W, padx = 15, pady = 10)

lab3 = Label(root, text = 'Расставь свой флот, адмирал!' , font='Arial 15 bold', justify = LEFT)
lab3.grid(column = 0, row = 11, sticky = W, padx = 15, pady = 10, columnspan = 2)



########################################################################### Functions


def control_right_placement(*args):
    global my_desk, count, lab3
    button_num = args[0]
    name = args[1]

    if count >= 0:
        row = int(re.findall('bt_player_([\d]+)_', name)[0])
        column = int(re.findall('bt_player_[\d]+_([\d]+)', name)[0])
        if button_num.__getitem__('background') != 'green':
            my_desk[row][column] = 1
            button_num.configure(background='green')
            my_desk[row][column] = 1
            count -= 1
            if count == 0:
                desk = copy.deepcopy(my_desk)
                sh_pl = copy.deepcopy(ships_player)

                tmp = scan_desk(desk, sh_pl)
                if type(tmp) == type(''):
                    lab3.configure(text=tmp)
                    but1.configure(state=DISABLED)

                else:
                    my_desk = desk
                    # for k in my_desk:
                    #     for z in k:
                    #         print(z, end=' ')
                    #     print()
                    lab3.configure(text='Все корабли расставлены!')
                    for i in player_buttons:
                        for j in i:
                            j.configure(state=DISABLED)


                    but1.configure(state=ACTIVE)

        else:
            if button_num.__getitem__('background') == 'green' and count == 0:
                row = int(re.findall('bt_player_([\d]+)_', name)[0])
                column = int(re.findall('bt_player_[\d]+_([\d]+)', name)[0])
                button_num.configure(background='light gray')
                my_desk[row][column] = 0
                count += 1
            else:
                button_num.configure(background='light gray')
                my_desk[row][column] = 0
                count += 1

        #print('count = ', count)









########################################################################### Players desk

##### Первая - СТРОКА, вторая - СТОЛБЕЦ


bt_player_0_0 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_0_0, 'bt_player_0_0'))
bt_player_0_0.grid(column=0, row=0, sticky=E, padx = 2, pady = 2)
bt_player_0_1 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_0_1, 'bt_player_0_1'))
bt_player_0_1.grid(column=1, row=0, sticky=E, padx = 2, pady = 2)
bt_player_0_2 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_0_2, 'bt_player_0_2'))
bt_player_0_2.grid(column=2, row=0, sticky=E, padx = 2, pady = 2)
bt_player_0_3 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_0_3, 'bt_player_0_3'))
bt_player_0_3.grid(column=3, row=0, sticky=E, padx = 2, pady = 2)
bt_player_0_4 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_0_4, 'bt_player_0_4'))
bt_player_0_4.grid(column=4, row=0, sticky=E, padx = 2, pady = 2)
bt_player_0_5 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_0_5, 'bt_player_0_5'))
bt_player_0_5.grid(column=5, row=0, sticky=E, padx = 2, pady = 2)
bt_player_0_6 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_0_6, 'bt_player_0_6'))
bt_player_0_6.grid(column=6, row=0, sticky=E, padx = 2, pady = 2)
bt_player_0_7 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_0_7, 'bt_player_0_7'))
bt_player_0_7.grid(column=7, row=0, sticky=E, padx = 2, pady = 2)
bt_player_0_8 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_0_8, 'bt_player_0_8'))
bt_player_0_8.grid(column=8, row=0, sticky=E, padx = 2, pady = 2)
bt_player_0_9 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_0_9, 'bt_player_0_9'))
bt_player_0_9.grid(column=9, row=0, sticky=E, padx = 2, pady = 2)

bt_player_1_0 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_1_0, 'bt_player_1_0'))
bt_player_1_0.grid(column=0, row=1, sticky=E, padx = 2, pady = 2)
bt_player_1_1 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_1_1, 'bt_player_1_1'))
bt_player_1_1.grid(column=1, row=1, sticky=E, padx = 2, pady = 2)
bt_player_1_2 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_1_2, 'bt_player_1_2'))
bt_player_1_2.grid(column=2, row=1, sticky=E, padx = 2, pady = 2)
bt_player_1_3 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_1_3, 'bt_player_1_3'))
bt_player_1_3.grid(column=3, row=1, sticky=E, padx = 2, pady = 2)
bt_player_1_4 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_1_4, 'bt_player_1_4'))
bt_player_1_4.grid(column=4, row=1, sticky=E, padx = 2, pady = 2)
bt_player_1_5 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_1_5, 'bt_player_1_5'))
bt_player_1_5.grid(column=5, row=1, sticky=E, padx = 2, pady = 2)
bt_player_1_6 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_1_6, 'bt_player_1_6'))
bt_player_1_6.grid(column=6, row=1, sticky=E, padx = 2, pady = 2)
bt_player_1_7 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_1_7, 'bt_player_1_7'))
bt_player_1_7.grid(column=7, row=1, sticky=E, padx = 2, pady = 2)
bt_player_1_8 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_1_8, 'bt_player_1_8'))
bt_player_1_8.grid(column=8, row=1, sticky=E, padx = 2, pady = 2)
bt_player_1_9 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_1_9, 'bt_player_1_9'))
bt_player_1_9.grid(column=9, row=1, sticky=E, padx = 2, pady = 2)

bt_player_2_0 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_2_0, 'bt_player_2_0'))
bt_player_2_0.grid(column=0, row=2, sticky=E, padx = 2, pady = 2)
bt_player_2_1 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_2_1, 'bt_player_2_1'))
bt_player_2_1.grid(column=1, row=2, sticky=E, padx = 2, pady = 2)
bt_player_2_2 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_2_2, 'bt_player_2_2'))
bt_player_2_2.grid(column=2, row=2, sticky=E, padx = 2, pady = 2)
bt_player_2_3 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_2_3, 'bt_player_2_3'))
bt_player_2_3.grid(column=3, row=2, sticky=E, padx = 2, pady = 2)
bt_player_2_4 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_2_4, 'bt_player_2_4'))
bt_player_2_4.grid(column=4, row=2, sticky=E, padx = 2, pady = 2)
bt_player_2_5 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_2_5, 'bt_player_2_5'))
bt_player_2_5.grid(column=5, row=2, sticky=E, padx = 2, pady = 2)
bt_player_2_6 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_2_6, 'bt_player_2_6'))
bt_player_2_6.grid(column=6, row=2, sticky=E, padx = 2, pady = 2)
bt_player_2_7 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_2_7, 'bt_player_2_7'))
bt_player_2_7.grid(column=7, row=2, sticky=E, padx = 2, pady = 2)
bt_player_2_8 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_2_8, 'bt_player_2_8'))
bt_player_2_8.grid(column=8, row=2, sticky=E, padx = 2, pady = 2)
bt_player_2_9 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_2_9, 'bt_player_2_9'))
bt_player_2_9.grid(column=9, row=2, sticky=E, padx = 2, pady = 2)

bt_player_3_0 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_3_0, 'bt_player_3_0'))
bt_player_3_0.grid(column=0, row=3, sticky=E, padx = 2, pady = 2)
bt_player_3_1 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_3_1, 'bt_player_3_1'))
bt_player_3_1.grid(column=1, row=3, sticky=E, padx = 2, pady = 2)
bt_player_3_2 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_3_2, 'bt_player_3_2'))
bt_player_3_2.grid(column=2, row=3, sticky=E, padx = 2, pady = 2)
bt_player_3_3 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_3_3, 'bt_player_3_3'))
bt_player_3_3.grid(column=3, row=3, sticky=E, padx = 2, pady = 2)
bt_player_3_4 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_3_4, 'bt_player_3_4'))
bt_player_3_4.grid(column=4, row=3, sticky=E, padx = 2, pady = 2)
bt_player_3_5 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_3_5, 'bt_player_3_5'))
bt_player_3_5.grid(column=5, row=3, sticky=E, padx = 2, pady = 2)
bt_player_3_6 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_3_6, 'bt_player_3_6'))
bt_player_3_6.grid(column=6, row=3, sticky=E, padx = 2, pady = 2)
bt_player_3_7 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_3_7, 'bt_player_3_7'))
bt_player_3_7.grid(column=7, row=3, sticky=E, padx = 2, pady = 2)
bt_player_3_8 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_3_8, 'bt_player_3_8'))
bt_player_3_8.grid(column=8, row=3, sticky=E, padx = 2, pady = 2)
bt_player_3_9 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_3_9, 'bt_player_3_9'))
bt_player_3_9.grid(column=9, row=3, sticky=E, padx = 2, pady = 2)

bt_player_4_0 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_4_0, 'bt_player_4_0'))
bt_player_4_0.grid(column=0, row=4, sticky=E, padx = 2, pady = 2)
bt_player_4_1 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_4_1, 'bt_player_4_1'))
bt_player_4_1.grid(column=1, row=4, sticky=E, padx = 2, pady = 2)
bt_player_4_2 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_4_2, 'bt_player_4_2'))
bt_player_4_2.grid(column=2, row=4, sticky=E, padx = 2, pady = 2)
bt_player_4_3 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_4_3, 'bt_player_4_3'))
bt_player_4_3.grid(column=3, row=4, sticky=E, padx = 2, pady = 2)
bt_player_4_4 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_4_4, 'bt_player_4_4'))
bt_player_4_4.grid(column=4, row=4, sticky=E, padx = 2, pady = 2)
bt_player_4_5 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_4_5, 'bt_player_4_5'))
bt_player_4_5.grid(column=5, row=4, sticky=E, padx = 2, pady = 2)
bt_player_4_6 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_4_6, 'bt_player_4_6'))
bt_player_4_6.grid(column=6, row=4, sticky=E, padx = 2, pady = 2)
bt_player_4_7 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_4_7, 'bt_player_4_7'))
bt_player_4_7.grid(column=7, row=4, sticky=E, padx = 2, pady = 2)
bt_player_4_8 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_4_8, 'bt_player_4_8'))
bt_player_4_8.grid(column=8, row=4, sticky=E, padx = 2, pady = 2)
bt_player_4_9 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_4_9, 'bt_player_4_9'))
bt_player_4_9.grid(column=9, row=4, sticky=E, padx = 2, pady = 2)

bt_player_5_0 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_5_0, 'bt_player_5_0'))
bt_player_5_0.grid(column=0, row=5, sticky=E, padx = 2, pady = 2)
bt_player_5_1 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_5_1, 'bt_player_5_1'))
bt_player_5_1.grid(column=1, row=5, sticky=E, padx = 2, pady = 2)
bt_player_5_2 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_5_2, 'bt_player_5_2'))
bt_player_5_2.grid(column=2, row=5, sticky=E, padx = 2, pady = 2)
bt_player_5_3 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_5_3, 'bt_player_5_3'))
bt_player_5_3.grid(column=3, row=5, sticky=E, padx = 2, pady = 2)
bt_player_5_4 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_5_4, 'bt_player_5_4'))
bt_player_5_4.grid(column=4, row=5, sticky=E, padx = 2, pady = 2)
bt_player_5_5 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_5_5, 'bt_player_5_5'))
bt_player_5_5.grid(column=5, row=5, sticky=E, padx = 2, pady = 2)
bt_player_5_6 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_5_6, 'bt_player_5_6'))
bt_player_5_6.grid(column=6, row=5, sticky=E, padx = 2, pady = 2)
bt_player_5_7 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_5_7, 'bt_player_5_7'))
bt_player_5_7.grid(column=7, row=5, sticky=E, padx = 2, pady = 2)
bt_player_5_8 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_5_8, 'bt_player_5_8'))
bt_player_5_8.grid(column=8, row=5, sticky=E, padx = 2, pady = 2)
bt_player_5_9 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_5_9, 'bt_player_5_9'))
bt_player_5_9.grid(column=9, row=5, sticky=E, padx = 2, pady = 2)

bt_player_6_0 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_6_0, 'bt_player_6_0'))
bt_player_6_0.grid(column=0, row=6, sticky=E, padx = 2, pady = 2)
bt_player_6_1 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_6_1, 'bt_player_6_1'))
bt_player_6_1.grid(column=1, row=6, sticky=E, padx = 2, pady = 2)
bt_player_6_2 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_6_2, 'bt_player_6_2'))
bt_player_6_2.grid(column=2, row=6, sticky=E, padx = 2, pady = 2)
bt_player_6_3 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_6_3, 'bt_player_6_3'))
bt_player_6_3.grid(column=3, row=6, sticky=E, padx = 2, pady = 2)
bt_player_6_4 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_6_4, 'bt_player_6_4'))
bt_player_6_4.grid(column=4, row=6, sticky=E, padx = 2, pady = 2)
bt_player_6_5 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_6_5, 'bt_player_6_5'))
bt_player_6_5.grid(column=5, row=6, sticky=E, padx = 2, pady = 2)
bt_player_6_6 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_6_6, 'bt_player_6_6'))
bt_player_6_6.grid(column=6, row=6, sticky=E, padx = 2, pady = 2)
bt_player_6_7 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_6_7, 'bt_player_6_7'))
bt_player_6_7.grid(column=7, row=6, sticky=E, padx = 2, pady = 2)
bt_player_6_8 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_6_8, 'bt_player_6_8'))
bt_player_6_8.grid(column=8, row=6, sticky=E, padx = 2, pady = 2)
bt_player_6_9 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_6_9, 'bt_player_6_9'))
bt_player_6_9.grid(column=9, row=6, sticky=E, padx = 2, pady = 2)

bt_player_7_0 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_7_0, 'bt_player_7_0'))
bt_player_7_0.grid(column=0, row=7, sticky=E, padx = 2, pady = 2)
bt_player_7_1 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_7_1, 'bt_player_7_1'))
bt_player_7_1.grid(column=1, row=7, sticky=E, padx = 2, pady = 2)
bt_player_7_2 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_7_2, 'bt_player_7_2'))
bt_player_7_2.grid(column=2, row=7, sticky=E, padx = 2, pady = 2)
bt_player_7_3 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_7_3, 'bt_player_7_3'))
bt_player_7_3.grid(column=3, row=7, sticky=E, padx = 2, pady = 2)
bt_player_7_4 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_7_4, 'bt_player_7_4'))
bt_player_7_4.grid(column=4, row=7, sticky=E, padx = 2, pady = 2)
bt_player_7_5 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_7_5, 'bt_player_7_5'))
bt_player_7_5.grid(column=5, row=7, sticky=E, padx = 2, pady = 2)
bt_player_7_6 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_7_6, 'bt_player_7_6'))
bt_player_7_6.grid(column=6, row=7, sticky=E, padx = 2, pady = 2)
bt_player_7_7 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_7_7, 'bt_player_7_7'))
bt_player_7_7.grid(column=7, row=7, sticky=E, padx = 2, pady = 2)
bt_player_7_8 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_7_8, 'bt_player_7_8'))
bt_player_7_8.grid(column=8, row=7, sticky=E, padx = 2, pady = 2)
bt_player_7_9 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_7_9, 'bt_player_7_9'))
bt_player_7_9.grid(column=9, row=7, sticky=E, padx = 2, pady = 2)

bt_player_8_0 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_8_0, 'bt_player_8_0'))
bt_player_8_0.grid(column=0, row=8, sticky=E, padx = 2, pady = 2)
bt_player_8_1 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_8_1, 'bt_player_8_1'))
bt_player_8_1.grid(column=1, row=8, sticky=E, padx = 2, pady = 2)
bt_player_8_2 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_8_2, 'bt_player_8_2'))
bt_player_8_2.grid(column=2, row=8, sticky=E, padx = 2, pady = 2)
bt_player_8_3 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_8_3, 'bt_player_8_3'))
bt_player_8_3.grid(column=3, row=8, sticky=E, padx = 2, pady = 2)
bt_player_8_4 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_8_4, 'bt_player_8_4'))
bt_player_8_4.grid(column=4, row=8, sticky=E, padx = 2, pady = 2)
bt_player_8_5 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_8_5, 'bt_player_8_5'))
bt_player_8_5.grid(column=5, row=8, sticky=E, padx = 2, pady = 2)
bt_player_8_6 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_8_6, 'bt_player_8_6'))
bt_player_8_6.grid(column=6, row=8, sticky=E, padx = 2, pady = 2)
bt_player_8_7 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_8_7, 'bt_player_8_7'))
bt_player_8_7.grid(column=7, row=8, sticky=E, padx = 2, pady = 2)
bt_player_8_8 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_8_8, 'bt_player_8_8'))
bt_player_8_8.grid(column=8, row=8, sticky=E, padx = 2, pady = 2)
bt_player_8_9 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_8_9, 'bt_player_8_9'))
bt_player_8_9.grid(column=9, row=8, sticky=E, padx = 2, pady = 2)

bt_player_9_0 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_9_0, 'bt_player_9_0'))
bt_player_9_0.grid(column=0, row=9, sticky=E, padx = 2, pady = 2)
bt_player_9_1 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_9_1, 'bt_player_9_1'))
bt_player_9_1.grid(column=1, row=9, sticky=E, padx = 2, pady = 2)
bt_player_9_2 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_9_2, 'bt_player_9_2'))
bt_player_9_2.grid(column=2, row=9, sticky=E, padx = 2, pady = 2)
bt_player_9_3 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_9_3, 'bt_player_9_3'))
bt_player_9_3.grid(column=3, row=9, sticky=E, padx = 2, pady = 2)
bt_player_9_4 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_9_4, 'bt_player_9_4'))
bt_player_9_4.grid(column=4, row=9, sticky=E, padx = 2, pady = 2)
bt_player_9_5 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_9_5, 'bt_player_9_5'))
bt_player_9_5.grid(column=5, row=9, sticky=E, padx = 2, pady = 2)
bt_player_9_6 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_9_6, 'bt_player_9_6'))
bt_player_9_6.grid(column=6, row=9, sticky=E, padx = 2, pady = 2)
bt_player_9_7 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_9_7, 'bt_player_9_7'))
bt_player_9_7.grid(column=7, row=9, sticky=E, padx = 2, pady = 2)
bt_player_9_8 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_9_8, 'bt_player_9_8'))
bt_player_9_8.grid(column=8, row=9, sticky=E, padx = 2, pady = 2)
bt_player_9_9 = Button(fra1, width = 3, height = 1, background='light gray', command=lambda : control_right_placement(bt_player_9_9, 'bt_player_9_9'))
bt_player_9_9.grid(column=9, row=9, sticky=E, padx = 2, pady = 2)



player_buttons = [[bt_player_0_0, bt_player_0_1, bt_player_0_2, bt_player_0_3, bt_player_0_4, bt_player_0_5, bt_player_0_6, bt_player_0_7, bt_player_0_8, bt_player_0_9],
                  [bt_player_1_0, bt_player_1_1, bt_player_1_2, bt_player_1_3, bt_player_1_4, bt_player_1_5, bt_player_1_6, bt_player_1_7, bt_player_1_8, bt_player_1_9],
                  [bt_player_2_0, bt_player_2_1, bt_player_2_2, bt_player_2_3, bt_player_2_4, bt_player_2_5, bt_player_2_6, bt_player_2_7, bt_player_2_8, bt_player_2_9],
                  [bt_player_3_0, bt_player_3_1, bt_player_3_2, bt_player_3_3, bt_player_3_4, bt_player_3_5, bt_player_3_6, bt_player_3_7, bt_player_3_8, bt_player_3_9],
                  [bt_player_4_0, bt_player_4_1, bt_player_4_2, bt_player_4_3, bt_player_4_4, bt_player_4_5, bt_player_4_6, bt_player_4_7, bt_player_4_8, bt_player_4_9],
                  [bt_player_5_0, bt_player_5_1, bt_player_5_2, bt_player_5_3, bt_player_5_4, bt_player_5_5, bt_player_5_6, bt_player_5_7, bt_player_5_8, bt_player_5_9],
                  [bt_player_6_0, bt_player_6_1, bt_player_6_2, bt_player_6_3, bt_player_6_4, bt_player_6_5, bt_player_6_6, bt_player_6_7, bt_player_6_8, bt_player_6_9],
                  [bt_player_7_0, bt_player_7_1, bt_player_7_2, bt_player_7_3, bt_player_7_4, bt_player_7_5, bt_player_7_6, bt_player_7_7, bt_player_7_8, bt_player_7_9],
                  [bt_player_8_0, bt_player_8_1, bt_player_8_2, bt_player_8_3, bt_player_8_4, bt_player_8_5, bt_player_8_6, bt_player_8_7, bt_player_8_8, bt_player_8_9],
                  [bt_player_9_0, bt_player_9_1, bt_player_9_2, bt_player_9_3, bt_player_9_4, bt_player_9_5, bt_player_9_6, bt_player_9_7, bt_player_9_8, bt_player_9_9]]

########################################################################### Opponent desk 


bt_opponent_0_0 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_0_0, 'bt_opponent_0_0', Flag))
bt_opponent_0_0.grid(column=0, row=0, sticky=E, padx = 2, pady = 2)
bt_opponent_0_1 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_0_1, 'bt_opponent_0_1', Flag))
bt_opponent_0_1.grid(column=1, row=0, sticky=E, padx = 2, pady = 2)
bt_opponent_0_2 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_0_2, 'bt_opponent_0_2', Flag))
bt_opponent_0_2.grid(column=2, row=0, sticky=E, padx = 2, pady = 2)
bt_opponent_0_3 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_0_3, 'bt_opponent_0_3', Flag))
bt_opponent_0_3.grid(column=3, row=0, sticky=E, padx = 2, pady = 2)
bt_opponent_0_4 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_0_4, 'bt_opponent_0_4', Flag))
bt_opponent_0_4.grid(column=4, row=0, sticky=E, padx = 2, pady = 2)
bt_opponent_0_5 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_0_5, 'bt_opponent_0_5', Flag))
bt_opponent_0_5.grid(column=5, row=0, sticky=E, padx = 2, pady = 2)
bt_opponent_0_6 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_0_6, 'bt_opponent_0_6', Flag))
bt_opponent_0_6.grid(column=6, row=0, sticky=E, padx = 2, pady = 2)
bt_opponent_0_7 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_0_7, 'bt_opponent_0_7', Flag))
bt_opponent_0_7.grid(column=7, row=0, sticky=E, padx = 2, pady = 2)
bt_opponent_0_8 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_0_8, 'bt_opponent_0_8', Flag))
bt_opponent_0_8.grid(column=8, row=0, sticky=E, padx = 2, pady = 2)
bt_opponent_0_9 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_0_9, 'bt_opponent_0_9', Flag))
bt_opponent_0_9.grid(column=9, row=0, sticky=E, padx = 2, pady = 2)

bt_opponent_1_0 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_1_0, 'bt_opponent_1_0', Flag))
bt_opponent_1_0.grid(column=0, row=1, sticky=E, padx = 2, pady = 2)
bt_opponent_1_1 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_1_1, 'bt_opponent_1_1', Flag))
bt_opponent_1_1.grid(column=1, row=1, sticky=E, padx = 2, pady = 2)
bt_opponent_1_2 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_1_2, 'bt_opponent_1_2', Flag))
bt_opponent_1_2.grid(column=2, row=1, sticky=E, padx = 2, pady = 2)
bt_opponent_1_3 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_1_3, 'bt_opponent_1_3', Flag))
bt_opponent_1_3.grid(column=3, row=1, sticky=E, padx = 2, pady = 2)
bt_opponent_1_4 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_1_4, 'bt_opponent_1_4', Flag))
bt_opponent_1_4.grid(column=4, row=1, sticky=E, padx = 2, pady = 2)
bt_opponent_1_5 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_1_5, 'bt_opponent_1_5', Flag))
bt_opponent_1_5.grid(column=5, row=1, sticky=E, padx = 2, pady = 2)
bt_opponent_1_6 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_1_6, 'bt_opponent_1_6', Flag))
bt_opponent_1_6.grid(column=6, row=1, sticky=E, padx = 2, pady = 2)
bt_opponent_1_7 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_1_7, 'bt_opponent_1_7', Flag))
bt_opponent_1_7.grid(column=7, row=1, sticky=E, padx = 2, pady = 2)
bt_opponent_1_8 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_1_8, 'bt_opponent_1_8', Flag))
bt_opponent_1_8.grid(column=8, row=1, sticky=E, padx = 2, pady = 2)
bt_opponent_1_9 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_1_9, 'bt_opponent_1_9', Flag))
bt_opponent_1_9.grid(column=9, row=1, sticky=E, padx = 2, pady = 2)

bt_opponent_2_0 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_2_0, 'bt_opponent_2_0', Flag))
bt_opponent_2_0.grid(column=0, row=2, sticky=E, padx = 2, pady = 2)
bt_opponent_2_1 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_2_1, 'bt_opponent_2_1', Flag))
bt_opponent_2_1.grid(column=1, row=2, sticky=E, padx = 2, pady = 2)
bt_opponent_2_2 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_2_2, 'bt_opponent_2_2', Flag))
bt_opponent_2_2.grid(column=2, row=2, sticky=E, padx = 2, pady = 2)
bt_opponent_2_3 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_2_3, 'bt_opponent_2_3', Flag))
bt_opponent_2_3.grid(column=3, row=2, sticky=E, padx = 2, pady = 2)
bt_opponent_2_4 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_2_4, 'bt_opponent_2_4', Flag))
bt_opponent_2_4.grid(column=4, row=2, sticky=E, padx = 2, pady = 2)
bt_opponent_2_5 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_2_5, 'bt_opponent_2_5', Flag))
bt_opponent_2_5.grid(column=5, row=2, sticky=E, padx = 2, pady = 2)
bt_opponent_2_6 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_2_6, 'bt_opponent_2_6', Flag))
bt_opponent_2_6.grid(column=6, row=2, sticky=E, padx = 2, pady = 2)
bt_opponent_2_7 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_2_7, 'bt_opponent_2_7', Flag))
bt_opponent_2_7.grid(column=7, row=2, sticky=E, padx = 2, pady = 2)
bt_opponent_2_8 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_2_8, 'bt_opponent_2_8', Flag))
bt_opponent_2_8.grid(column=8, row=2, sticky=E, padx = 2, pady = 2)
bt_opponent_2_9 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_2_9, 'bt_opponent_2_9', Flag))
bt_opponent_2_9.grid(column=9, row=2, sticky=E, padx = 2, pady = 2)

bt_opponent_3_0 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_3_0, 'bt_opponent_3_0', Flag))
bt_opponent_3_0.grid(column=0, row=3, sticky=E, padx = 2, pady = 2)
bt_opponent_3_1 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_3_1, 'bt_opponent_3_1', Flag))
bt_opponent_3_1.grid(column=1, row=3, sticky=E, padx = 2, pady = 2)
bt_opponent_3_2 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_3_2, 'bt_opponent_3_2', Flag))
bt_opponent_3_2.grid(column=2, row=3, sticky=E, padx = 2, pady = 2)
bt_opponent_3_3 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_3_3, 'bt_opponent_3_3', Flag))
bt_opponent_3_3.grid(column=3, row=3, sticky=E, padx = 2, pady = 2)
bt_opponent_3_4 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_3_4, 'bt_opponent_3_4', Flag))
bt_opponent_3_4.grid(column=4, row=3, sticky=E, padx = 2, pady = 2)
bt_opponent_3_5 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_3_5, 'bt_opponent_3_5', Flag))
bt_opponent_3_5.grid(column=5, row=3, sticky=E, padx = 2, pady = 2)
bt_opponent_3_6 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_3_6, 'bt_opponent_3_6', Flag))
bt_opponent_3_6.grid(column=6, row=3, sticky=E, padx = 2, pady = 2)
bt_opponent_3_7 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_3_7, 'bt_opponent_3_7', Flag))
bt_opponent_3_7.grid(column=7, row=3, sticky=E, padx = 2, pady = 2)
bt_opponent_3_8 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_3_8, 'bt_opponent_3_8', Flag))
bt_opponent_3_8.grid(column=8, row=3, sticky=E, padx = 2, pady = 2)
bt_opponent_3_9 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_3_9, 'bt_opponent_3_9', Flag))
bt_opponent_3_9.grid(column=9, row=3, sticky=E, padx = 2, pady = 2)

bt_opponent_4_0 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_4_0, 'bt_opponent_4_0', Flag))
bt_opponent_4_0.grid(column=0, row=4, sticky=E, padx = 2, pady = 2)
bt_opponent_4_1 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_4_1, 'bt_opponent_4_1', Flag))
bt_opponent_4_1.grid(column=1, row=4, sticky=E, padx = 2, pady = 2)
bt_opponent_4_2 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_4_2, 'bt_opponent_4_2', Flag))
bt_opponent_4_2.grid(column=2, row=4, sticky=E, padx = 2, pady = 2)
bt_opponent_4_3 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_4_3, 'bt_opponent_4_3', Flag))
bt_opponent_4_3.grid(column=3, row=4, sticky=E, padx = 2, pady = 2)
bt_opponent_4_4 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_4_4, 'bt_opponent_4_4', Flag))
bt_opponent_4_4.grid(column=4, row=4, sticky=E, padx = 2, pady = 2)
bt_opponent_4_5 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_4_5, 'bt_opponent_4_5', Flag))
bt_opponent_4_5.grid(column=5, row=4, sticky=E, padx = 2, pady = 2)
bt_opponent_4_6 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_4_6, 'bt_opponent_4_6', Flag))
bt_opponent_4_6.grid(column=6, row=4, sticky=E, padx = 2, pady = 2)
bt_opponent_4_7 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_4_7, 'bt_opponent_4_7', Flag))
bt_opponent_4_7.grid(column=7, row=4, sticky=E, padx = 2, pady = 2)
bt_opponent_4_8 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_4_8, 'bt_opponent_4_8', Flag))
bt_opponent_4_8.grid(column=8, row=4, sticky=E, padx = 2, pady = 2)
bt_opponent_4_9 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_4_9, 'bt_opponent_4_9', Flag))
bt_opponent_4_9.grid(column=9, row=4, sticky=E, padx = 2, pady = 2)

bt_opponent_5_0 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_5_0, 'bt_opponent_5_0', Flag))
bt_opponent_5_0.grid(column=0, row=5, sticky=E, padx = 2, pady = 2)
bt_opponent_5_1 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_5_1, 'bt_opponent_5_1', Flag))
bt_opponent_5_1.grid(column=1, row=5, sticky=E, padx = 2, pady = 2)
bt_opponent_5_2 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_5_2, 'bt_opponent_5_2', Flag))
bt_opponent_5_2.grid(column=2, row=5, sticky=E, padx = 2, pady = 2)
bt_opponent_5_3 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_5_3, 'bt_opponent_5_3', Flag))
bt_opponent_5_3.grid(column=3, row=5, sticky=E, padx = 2, pady = 2)
bt_opponent_5_4 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_5_4, 'bt_opponent_5_4', Flag))
bt_opponent_5_4.grid(column=4, row=5, sticky=E, padx = 2, pady = 2)
bt_opponent_5_5 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_5_5, 'bt_opponent_5_5', Flag))
bt_opponent_5_5.grid(column=5, row=5, sticky=E, padx = 2, pady = 2)
bt_opponent_5_6 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_5_6, 'bt_opponent_5_6', Flag))
bt_opponent_5_6.grid(column=6, row=5, sticky=E, padx = 2, pady = 2)
bt_opponent_5_7 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_5_7, 'bt_opponent_5_7', Flag))
bt_opponent_5_7.grid(column=7, row=5, sticky=E, padx = 2, pady = 2)
bt_opponent_5_8 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_5_8, 'bt_opponent_5_8', Flag))
bt_opponent_5_8.grid(column=8, row=5, sticky=E, padx = 2, pady = 2)
bt_opponent_5_9 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_5_9, 'bt_opponent_5_9', Flag))
bt_opponent_5_9.grid(column=9, row=5, sticky=E, padx = 2, pady = 2)

bt_opponent_6_0 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_6_0, 'bt_opponent_6_0', Flag))
bt_opponent_6_0.grid(column=0, row=6, sticky=E, padx = 2, pady = 2)
bt_opponent_6_1 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_6_1, 'bt_opponent_6_1', Flag))
bt_opponent_6_1.grid(column=1, row=6, sticky=E, padx = 2, pady = 2)
bt_opponent_6_2 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_6_2, 'bt_opponent_6_2', Flag))
bt_opponent_6_2.grid(column=2, row=6, sticky=E, padx = 2, pady = 2)
bt_opponent_6_3 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_6_3, 'bt_opponent_6_3', Flag))
bt_opponent_6_3.grid(column=3, row=6, sticky=E, padx = 2, pady = 2)
bt_opponent_6_4 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_6_4, 'bt_opponent_6_4', Flag))
bt_opponent_6_4.grid(column=4, row=6, sticky=E, padx = 2, pady = 2)
bt_opponent_6_5 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_6_5, 'bt_opponent_6_5', Flag))
bt_opponent_6_5.grid(column=5, row=6, sticky=E, padx = 2, pady = 2)
bt_opponent_6_6 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_6_6, 'bt_opponent_6_6', Flag))
bt_opponent_6_6.grid(column=6, row=6, sticky=E, padx = 2, pady = 2)
bt_opponent_6_7 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_6_7, 'bt_opponent_6_7', Flag))
bt_opponent_6_7.grid(column=7, row=6, sticky=E, padx = 2, pady = 2)
bt_opponent_6_8 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_6_8, 'bt_opponent_6_8', Flag))
bt_opponent_6_8.grid(column=8, row=6, sticky=E, padx = 2, pady = 2)
bt_opponent_6_9 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_6_9, 'bt_opponent_6_9', Flag))
bt_opponent_6_9.grid(column=9, row=6, sticky=E, padx = 2, pady = 2)

bt_opponent_7_0 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_7_0, 'bt_opponent_7_0', Flag))
bt_opponent_7_0.grid(column=0, row=7, sticky=E, padx = 2, pady = 2)
bt_opponent_7_1 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_7_1, 'bt_opponent_7_1', Flag))
bt_opponent_7_1.grid(column=1, row=7, sticky=E, padx = 2, pady = 2)
bt_opponent_7_2 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_7_2, 'bt_opponent_7_2', Flag))
bt_opponent_7_2.grid(column=2, row=7, sticky=E, padx = 2, pady = 2)
bt_opponent_7_3 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_7_3, 'bt_opponent_7_3', Flag))
bt_opponent_7_3.grid(column=3, row=7, sticky=E, padx = 2, pady = 2)
bt_opponent_7_4 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_7_4, 'bt_opponent_7_4', Flag))
bt_opponent_7_4.grid(column=4, row=7, sticky=E, padx = 2, pady = 2)
bt_opponent_7_5 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_7_5, 'bt_opponent_7_5', Flag))
bt_opponent_7_5.grid(column=5, row=7, sticky=E, padx = 2, pady = 2)
bt_opponent_7_6 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_7_6, 'bt_opponent_7_6', Flag))
bt_opponent_7_6.grid(column=6, row=7, sticky=E, padx = 2, pady = 2)
bt_opponent_7_7 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_7_7, 'bt_opponent_7_7', Flag))
bt_opponent_7_7.grid(column=7, row=7, sticky=E, padx = 2, pady = 2)
bt_opponent_7_8 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_7_8, 'bt_opponent_7_8', Flag))
bt_opponent_7_8.grid(column=8, row=7, sticky=E, padx = 2, pady = 2)
bt_opponent_7_9 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_7_9, 'bt_opponent_7_9', Flag))
bt_opponent_7_9.grid(column=9, row=7, sticky=E, padx = 2, pady = 2)

bt_opponent_8_0 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_8_0, 'bt_opponent_8_0', Flag))
bt_opponent_8_0.grid(column=0, row=8, sticky=E, padx = 2, pady = 2)
bt_opponent_8_1 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_8_1, 'bt_opponent_8_1', Flag))
bt_opponent_8_1.grid(column=1, row=8, sticky=E, padx = 2, pady = 2)
bt_opponent_8_2 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_8_2, 'bt_opponent_8_2', Flag))
bt_opponent_8_2.grid(column=2, row=8, sticky=E, padx = 2, pady = 2)
bt_opponent_8_3 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_8_3, 'bt_opponent_8_3', Flag))
bt_opponent_8_3.grid(column=3, row=8, sticky=E, padx = 2, pady = 2)
bt_opponent_8_4 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_8_4, 'bt_opponent_8_4', Flag))
bt_opponent_8_4.grid(column=4, row=8, sticky=E, padx = 2, pady = 2)
bt_opponent_8_5 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_8_5, 'bt_opponent_8_5', Flag))
bt_opponent_8_5.grid(column=5, row=8, sticky=E, padx = 2, pady = 2)
bt_opponent_8_6 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_8_6, 'bt_opponent_8_6', Flag))
bt_opponent_8_6.grid(column=6, row=8, sticky=E, padx = 2, pady = 2)
bt_opponent_8_7 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_8_7, 'bt_opponent_8_7', Flag))
bt_opponent_8_7.grid(column=7, row=8, sticky=E, padx = 2, pady = 2)
bt_opponent_8_8 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_8_8, 'bt_opponent_8_8', Flag))
bt_opponent_8_8.grid(column=8, row=8, sticky=E, padx = 2, pady = 2)
bt_opponent_8_9 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_8_9, 'bt_opponent_8_9', Flag))
bt_opponent_8_9.grid(column=9, row=8, sticky=E, padx = 2, pady = 2)

bt_opponent_9_0 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_9_0, 'bt_opponent_9_0', Flag))
bt_opponent_9_0.grid(column=0, row=9, sticky=E, padx = 2, pady = 2)
bt_opponent_9_1 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_9_1, 'bt_opponent_9_1', Flag))
bt_opponent_9_1.grid(column=1, row=9, sticky=E, padx = 2, pady = 2)
bt_opponent_9_2 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_9_2, 'bt_opponent_9_2', Flag))
bt_opponent_9_2.grid(column=2, row=9, sticky=E, padx = 2, pady = 2)
bt_opponent_9_3 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_9_3, 'bt_opponent_9_3', Flag))
bt_opponent_9_3.grid(column=3, row=9, sticky=E, padx = 2, pady = 2)
bt_opponent_9_4 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_9_4, 'bt_opponent_9_4', Flag))
bt_opponent_9_4.grid(column=4, row=9, sticky=E, padx = 2, pady = 2)
bt_opponent_9_5 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_9_5, 'bt_opponent_9_5', Flag))
bt_opponent_9_5.grid(column=5, row=9, sticky=E, padx = 2, pady = 2)
bt_opponent_9_6 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_9_6, 'bt_opponent_9_6', Flag))
bt_opponent_9_6.grid(column=6, row=9, sticky=E, padx = 2, pady = 2)
bt_opponent_9_7 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_9_7, 'bt_opponent_9_7', Flag))
bt_opponent_9_7.grid(column=7, row=9, sticky=E, padx = 2, pady = 2)
bt_opponent_9_8 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_9_8, 'bt_opponent_9_8', Flag))
bt_opponent_9_8.grid(column=8, row=9, sticky=E, padx = 2, pady = 2)
bt_opponent_9_9 = Button(fra2, width = 3, height = 1, background='white', command=lambda : player_shoot(bt_opponent_9_9, 'bt_opponent_9_9', Flag))
bt_opponent_9_9.grid(column=9, row=9, sticky=E, padx = 2, pady = 2)

opponent_buttons = [[bt_opponent_0_0, bt_opponent_0_1, bt_opponent_0_2, bt_opponent_0_3, bt_opponent_0_4, bt_opponent_0_5, bt_opponent_0_6, bt_opponent_0_7, bt_opponent_0_8, bt_opponent_0_9],
                  [bt_opponent_1_0, bt_opponent_1_1, bt_opponent_1_2, bt_opponent_1_3, bt_opponent_1_4, bt_opponent_1_5, bt_opponent_1_6, bt_opponent_1_7, bt_opponent_1_8, bt_opponent_1_9],
                  [bt_opponent_2_0, bt_opponent_2_1, bt_opponent_2_2, bt_opponent_2_3, bt_opponent_2_4, bt_opponent_2_5, bt_opponent_2_6, bt_opponent_2_7, bt_opponent_2_8, bt_opponent_2_9],
                  [bt_opponent_3_0, bt_opponent_3_1, bt_opponent_3_2, bt_opponent_3_3, bt_opponent_3_4, bt_opponent_3_5, bt_opponent_3_6, bt_opponent_3_7, bt_opponent_3_8, bt_opponent_3_9],
                  [bt_opponent_4_0, bt_opponent_4_1, bt_opponent_4_2, bt_opponent_4_3, bt_opponent_4_4, bt_opponent_4_5, bt_opponent_4_6, bt_opponent_4_7, bt_opponent_4_8, bt_opponent_4_9],
                  [bt_opponent_5_0, bt_opponent_5_1, bt_opponent_5_2, bt_opponent_5_3, bt_opponent_5_4, bt_opponent_5_5, bt_opponent_5_6, bt_opponent_5_7, bt_opponent_5_8, bt_opponent_5_9],
                  [bt_opponent_6_0, bt_opponent_6_1, bt_opponent_6_2, bt_opponent_6_3, bt_opponent_6_4, bt_opponent_6_5, bt_opponent_6_6, bt_opponent_6_7, bt_opponent_6_8, bt_opponent_6_9],
                  [bt_opponent_7_0, bt_opponent_7_1, bt_opponent_7_2, bt_opponent_7_3, bt_opponent_7_4, bt_opponent_7_5, bt_opponent_7_6, bt_opponent_7_7, bt_opponent_7_8, bt_opponent_7_9],
                  [bt_opponent_8_0, bt_opponent_8_1, bt_opponent_8_2, bt_opponent_8_3, bt_opponent_8_4, bt_opponent_8_5, bt_opponent_8_6, bt_opponent_8_7, bt_opponent_8_8, bt_opponent_8_9],
                  [bt_opponent_9_0, bt_opponent_9_1, bt_opponent_9_2, bt_opponent_9_3, bt_opponent_9_4, bt_opponent_9_5, bt_opponent_9_6, bt_opponent_9_7, bt_opponent_9_8, bt_opponent_9_9]]


################################################################

but1 = Button(root, width = 12, text = 'Начать', state=DISABLED , font='Arial 12', command=lambda : start_a_game(my_desk, opponent_desk, opponent_buttons, lab3))
but1.grid(column = 11, row = 11, sticky = E, padx = 15, pady = 10)


def start_a_game(player_desk, computer_desk, opponent_buttons, lab):
    global Flag
    if opponent_fill_desk(computer_desk, opponent_buttons):
        Flag = True
        scan_desk(opponent_desk, ships_op)

        # for i in opponent_desk:
        #     for j in i:
        #         print(j, end = ' ')
        #     print()

        lab.configure(text = 'Компьютер расставил свой флот, \nВаш первый выстрел!')
        lab.configure(font = 'Arial 14 bold')

        for i in opponent_buttons:
            for j in i:
                j.configure(background='light grey')

        return


def mark_area_pl(my_desk, player_buttons, shot_ship):
    znak = [0, -1, 1]
    for k in shot_ship:
        coord_x = k[0]
        coord_y = k[1]
        for i in znak:
            for j in znak:
                if 0 <= (coord_x + i) <= 9 and 0 <= (coord_y + j) <= 9:
                    my_desk[coord_x + i][coord_y + j] = 1
                    player_buttons[coord_x + i][coord_y + j].configure(background='white')
                    player_buttons[coord_x + i][coord_y + j].configure(state = DISABLED)



def player_shoot(*args):
    global opponent_ships, lab3, opponent_desk, opponent_buttons, Flag, shoot_op_ship, players_ships
    if args[2] == False:
        return
    button_num = args[0]
    name = args[1]
    row = int(re.findall('bt_opponent_([\d]+)_', name)[0])
    column = int(re.findall('bt_opponent_[\d]+_([\d]+)', name)[0])

    if opponent_desk[row][column] == 0:
        opponent_buttons[row][column].configure(state = DISABLED)
        opponent_buttons[row][column].configure(background = 'white')
        #opponent_buttons[row][column].configure(image = 'boom-bang-pow.png')
        #opponent_buttons[row][column].config(image=photo2,width="23",height="20")
    else:
        opponent_buttons[row][column].config(image=photo1, width="23", height="20")
        opponent_ships -= 1


        if len(shoot_op_ship) == 0:
            if opponent_desk[row][column][0] == '1':
                shoot_op_ship.append((row, column))
                mark_area_pl(opponent_desk, opponent_buttons, shoot_op_ship)
                shoot_op_ship.clear()
            else:
                shoot_op_ship.append((row, column))
        else:
            shoot_op_ship.append((row, column))
            #print('opponent_desk[row][column][0] = ', opponent_desk[row][column][0], ' ', str(len(shoot_op_ship)))
            if opponent_desk[row][column][0] == str(len(shoot_op_ship)):
                mark_area_pl(opponent_desk, opponent_buttons, shoot_op_ship)
                shoot_op_ship.clear()

    players_ships_tmp = opponent_shoot(my_desk, player_buttons, photo1, players_ships)

    #if players_ships_tmp != players_ships:
        #print('players_ships = ', players_ships)

    if opponent_ships == 0:
        lab3.configure(text='Вы победили!!!')
        lab3.configure(font='Arial 14 bold')
        but1.configure(state=DISABLED)
        return

    if players_ships_tmp == 0:
        lab3.configure(text='Вы проиграли!!!')
        lab3.configure(font='Arial 14 bold')
        but1.configure(state=DISABLED)
        return

    players_ships = players_ships_tmp



root.mainloop()