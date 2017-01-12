from random import *


ships_for_place = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
errors = {0 : 'Неправильно расположены корабли', 1 : 'Неправильное количество кораблей'}
shot_ship = []

########################################################################### Постановка кораблей игрока

def scan_desk(desk_to_scan, ships):
    for i in range(10):
        for j in range(10):
            if desk_to_scan[i][j] == 1:
                res = what_a_ship(i, j, desk_to_scan, ships)
                if type(res) == type(''):
                    return res

                # for k in desk_to_scan:
                #     for z in k:
                #         print(z, end=' ')
                #     print()
                # print()



def look_around(coord_x, coord_y, my_desk, where_we_were):
    znak = [-1, 0, 1]
    count = 0
    flag = False
    coord = tuple()
    for i in znak:
        for j in znak:
            if 0 <= (coord_x + i) <= 9 and 0 <= (coord_y + j) <= 9:
                count = 0
                if my_desk[coord_x + i][coord_y + j] != 0 and (coord_x + i, coord_y + j) not in where_we_were:
                    count += 1
                    coord = (coord_x + i, coord_y + j)
                    flag = True
    if flag == False:
        return (None, None)
    if count > 1:
        return (99, 99)
    return coord


def what_a_ship(coord_x, coord_y, desk, ships):
    point_lst = [(coord_x, coord_y),]
    ship = [(coord_x, coord_y),]
    ver = True
    gor = True

    while len(point_lst) != 0:
        x, y = point_lst.pop(0)
        next_point = look_around(x, y, desk, ship)
        if next_point[0] != None:
            point_lst.append((next_point[0], next_point[1]))
            ship.append((next_point[0], next_point[1]))
        elif next_point[0] == 99:
            return errors[0]
        else:
            break


    if len(ship) != 1:
        for i in range(1, len(ship)):
            if ship[i][0] != ship[i - 1][0]:
                gor = False
            if ship[i][1] != ship[i - 1][1]:
                ver = False
        if gor == False and ver == False:
            return errors[0]

    if len(ship) < 5:
        if ships[len(ship)] != 0:
            for i in ship:
                desk[i[0]][i[1]] = str(len(ship)) + '_' + str(ships[len(ship)])
        else:
            return errors[1]
    else:
        return errors[0]

    if ships[len(ship)] == 0:
        return '1'

    ships[len(ship)] -= 1


########################################################################### Постановка кораблей компьютера

def opponent_fill_desk(computer_desk, opponent_buttons):
    for i in ships_for_place:
        ship_place = True
        while ship_place:
            x = randint(0, 9)
            y = randint(0, 9)
            orient_way  =  randint(0, 1)

            if orient_way == 0:
                res = place_and_mark_ship(computer_desk, x, y, i, orient_way)
                if len(res) != 0:
                    for j in res:
                        computer_desk[j[0]][j[1]] = 1
                    ship_place = False


            else:
                res = place_and_mark_ship(computer_desk, x, y, i, orient_way)
                if len(res) != 0:
                    for j in res:
                        computer_desk[j[0]][j[1]] = 1

                    ship_place = False
    return True



def place_and_mark_ship(computer_desk, coord_x, coord_y, ship, vector):
    where_we_were = []
    znak_b = [1, -1]


    if vector == 0:
        for z in znak_b:
            if len(where_we_were) == ship:
                return where_we_were
            else:
                where_we_were.clear()

            for k in range(ship):
                if 0 <= coord_x + k*z <= 9 and 0 <= coord_y <= 9:
                    if computer_desk[coord_x + k*z][coord_y] == 0 and look_around_to_mark(coord_x + k*z, coord_y, computer_desk, where_we_were, vector):
                        where_we_were.append((coord_x + k*z, coord_y))

        return []

    if vector == 1:
        for z in znak_b:
            if len(where_we_were) == ship:
                return where_we_were
            else:
                where_we_were.clear()
            for k in range(ship):
                if 0 <= coord_x <= 9 and 0 <= coord_y + k*z <= 9:
                    if computer_desk[coord_x][coord_y + k*z] == 0 and look_around_to_mark(coord_x, coord_y + k*z, computer_desk, where_we_were, vector):
                        where_we_were.append((coord_x, coord_y + k*z))

        return []


def look_around_to_mark(coord_x, coord_y, computer_desk, where_we_were, orient):
    znak = [0, -1, 1]
    for i in znak:
        for j in znak:
            if 0 <= (coord_x + i) <= 9 and 0 <= (coord_y + j) <= 9:
                if computer_desk[coord_x + i][coord_y + j] != 0:
                    if (coord_x + i, coord_y + j) not in where_we_were:
                        return False
            else:
                if orient == 0 and coord_y == (coord_y + j):
                    return False
                if orient == 1 and coord_x == (coord_x + i):
                    return False

    return True


########################################################################### Начало игры

def mark_area(my_desk, player_buttons, shot_ship):
    znak = [0, -1, 1]
    for k in shot_ship:
        coord_x = k[0]
        coord_y = k[1]
        for i in znak:
            for j in znak:
                if 0 <= (coord_x + i) <= 9 and 0 <= (coord_y + j) <= 9:
                    if my_desk[coord_x + i][coord_y + j] == 0:
                        my_desk[coord_x + i][coord_y + j] = 1
                        player_buttons[coord_x + i][coord_y + j].configure(background='white')



def opponent_shoot(my_desk, player_buttons, photo1, players_ships):
    global shot_ship

    if len(shot_ship) == 0:
        while True:
            x = randint(0, 9)
            y = randint(0, 9)
            if my_desk[x][y] == 0:
                my_desk[x][y] = 1
                player_buttons[x][y].configure(background= 'white')
                return players_ships
            if my_desk[x][y] != 0 and my_desk[x][y] != 1 and my_desk[x][y] != 99:
                player_buttons[x][y].config(image=photo1, width="23", height="20")
                #print('my_desk[x][y] = ', my_desk[x][y])
                if my_desk[x][y][0] == '1':
                    my_desk[x][y] = 99
                    players_ships -= 1
                    shot_ship.append((x, y))
                    mark_area(my_desk, player_buttons, shot_ship)
                    shot_ship.clear()
                    return players_ships
                my_desk[x][y] = 99
                players_ships -= 1
                shot_ship.append((x, y))
                return players_ships

################################################# 1 попадание

    else:
        if len(shot_ship) == 1:
            coord = []
            if 0 <=(shot_ship[0][1] - 1) <= 9:
                coord.append((shot_ship[0][0], shot_ship[0][1] - 1))
            if 0 <=(shot_ship[0][1] + 1) <= 9:
                coord.append((shot_ship[0][0], shot_ship[0][1] + 1))
            if 0 <=(shot_ship[0][0] - 1) <= 9:
                coord.append((shot_ship[0][0] - 1, shot_ship[0][1]))
            if 0 <=(shot_ship[0][0] + 1) <= 9:
                coord.append((shot_ship[0][0] + 1, shot_ship[0][1]))

            while True:
                choise = randint(0, len(coord) - 1)
                coord_temp = coord[choise]
                coord_x = coord_temp[0]
                coord_y = coord_temp[1]
                #print('coord = ', coord)
                #print('coord_x = ', coord_x, ' , coord_y = ', coord_y)
                #print('my_desk[coord_x][coord_y] = ', my_desk[coord_x][coord_y])
                if 0 <= coord_x <= 9 and 0 <= coord_y <= 9:
                    if my_desk[coord_x][coord_y] != 99 and my_desk[coord_x][coord_y] != 1:
                        if my_desk[coord_x][coord_y] == 0:
                            #print('1')
                            my_desk[coord_x][coord_y] = 1
                            #print('my_desk[coord_x][coord_y] = ', my_desk[coord_x][coord_y])
                            player_buttons[coord_x][coord_y].configure(background='white')
                            return players_ships
                        elif my_desk[coord_x][coord_y] != 1:
                            player_buttons[coord_x][coord_y].config(image=photo1, width="23", height="20")
                            if my_desk[coord_x][coord_y][0] == '2':
                                shot_ship.append((coord_x, coord_y))
                                my_desk[coord_x][coord_y] = 99
                                mark_area(my_desk, player_buttons, shot_ship)
                                shot_ship.clear()
                                players_ships -= 1
                                return players_ships
                            my_desk[coord_x][coord_y] = 99
                            shot_ship.append((coord_x, coord_y))
                            players_ships -= 1
                            return players_ships
                    elif my_desk[coord_x][coord_y] == 1:
                        coord.pop(choise)

########################################################################## более 1 попадания
        else:
            gorizon = True
            vertic = True
            tmp_x = []
            tmp_y = []
            #print('shot_ship = ', shot_ship)
            for i in range(1, len(shot_ship) + 1):
                tmp_x.append(shot_ship[i - 1][0])
                tmp_y.append(shot_ship[i - 1][1])
                if i < (len(shot_ship)):
                    if shot_ship[i][0] != shot_ship[i - 1][0]:
                        gorizon = False
                    if shot_ship[i][1] != shot_ship[i - 1][1]:
                        vertic = False

            tmp_x.sort()
            tmp_y.sort()
            #print('tmp_x = ', tmp_x)
            #print('tmp_y = ', tmp_y)
            #print('gorizon = ', gorizon, ' , vertic = ', vertic)
            if gorizon:
                #print('[tmp_x[0]][tmp_y[0] - 1] = ', tmp_x[0],tmp_y[0] - 1)
                #print('my_desk[tmp_x[0]][tmp_y[0] - 1] = ', my_desk[tmp_x[0]][tmp_y[0] - 1])
                if 0 <= (tmp_y[0] - 1) <= 9 and my_desk[tmp_x[0]][tmp_y[0] - 1] != 1 and my_desk[tmp_x[0]][tmp_y[0] - 1] != 99:
                    if my_desk[tmp_x[0]][tmp_y[0] - 1] != 0:
                        player_buttons[tmp_x[0]][tmp_y[0] - 1].config(image=photo1, width="23", height="20")
                        #print('tmp_x[0] = ', tmp_x[0], '(tmp_y[0] - 1) = ', (tmp_y[0] - 1))
                        if my_desk[tmp_x[0]][tmp_y[0] - 1][0] == '3' and len(shot_ship) == 2:
                            my_desk[tmp_x[0]][tmp_y[0] - 1] = 99
                            shot_ship.append((tmp_x[0], tmp_y[0] - 1))
                            mark_area(my_desk, player_buttons, shot_ship)
                            shot_ship.clear()
                            players_ships -= 1
                            return players_ships
                        elif my_desk[tmp_x[0]][tmp_y[0] - 1][0] == '4' and len(shot_ship) == 3:
                            my_desk[tmp_x[0]][tmp_y[0] - 1] = 99
                            shot_ship.append((tmp_x[0], tmp_y[0] - 1))
                            mark_area(my_desk, player_buttons, shot_ship)
                            shot_ship.clear()
                            players_ships -= 1
                            return players_ships
                        else:
                            my_desk[tmp_x[0]][tmp_y[0] - 1] = 99
                            shot_ship.append((tmp_x[0], tmp_y[0] - 1))
                            players_ships -= 1
                            return players_ships
                    else:
                        my_desk[tmp_x[0]][tmp_y[0] - 1] = 1
                        player_buttons[tmp_x[0]][tmp_y[0] - 1].configure(background='white')

                #print('[tmp_x[0]][tmp_y[-1] + 1] = ', tmp_x[0], tmp_y[-1] + 1)
                #print('my_desk[tmp_x[0]][tmp_y[-1] + 1] = ', my_desk[tmp_x[0]][tmp_y[-1] + 1])
                if 0 <= (tmp_y[-1] + 1) <= 9 and my_desk[tmp_x[0]][tmp_y[-1] + 1] != 1 and my_desk[tmp_x[0]][tmp_y[-1] + 1] != 99:
                    if my_desk[tmp_x[0]][tmp_y[-1] + 1] != 0:
                        player_buttons[tmp_x[0]][tmp_y[-1] + 1].config(image=photo1, width="23", height="20")

                        #print('tmp_x[0] = ', tmp_x[0], '(tmp_y[-1] + 1) = ', (tmp_y[-1] + 1))
                        if my_desk[tmp_x[0]][tmp_y[-1] + 1][0] == '3' and len(shot_ship) == 2:
                            my_desk[tmp_x[0]][tmp_y[-1] + 1] = 99
                            shot_ship.append((tmp_x[0], tmp_y[-1] + 1))
                            mark_area(my_desk, player_buttons, shot_ship)
                            shot_ship.clear()
                            players_ships -= 1
                            return players_ships
                        elif my_desk[tmp_x[0]][tmp_y[-1] + 1][0] == '4' and len(shot_ship) == 3:
                            my_desk[tmp_x[0]][tmp_y[-1] + 1] = 99
                            shot_ship.append((tmp_x[0], tmp_y[-1] + 1))
                            mark_area(my_desk, player_buttons, shot_ship)
                            shot_ship.clear()
                            players_ships -= 1
                            return players_ships
                        else:
                            my_desk[tmp_x[0]][tmp_y[-1] + 1] = 99
                            shot_ship.append((tmp_x[0], tmp_y[-1] + 1))
                            players_ships -= 1
                            return players_ships
                    else:
                        my_desk[tmp_x[0]][tmp_y[-1] + 1] = 1
                        player_buttons[tmp_x[0]][tmp_y[-1] + 1].configure(background='white')

            if vertic:
                #print('[tmp_x[0] - 1][tmp_y[0]] = ', tmp_x[0] - 1, tmp_y[0])
                #print('my_desk[tmp_x[0] - 1][tmp_y[0]] = ', my_desk[tmp_x[0] - 1][tmp_y[0]])
                if 0 <= (tmp_x[0] - 1) <= 9 and my_desk[tmp_x[0] - 1][tmp_y[0]] != 1 and my_desk[tmp_x[0] - 1][tmp_y[0]] != 99:
                    if my_desk[tmp_x[0] - 1][tmp_y[0]] != 0:
                        player_buttons[tmp_x[0] - 1][tmp_y[0]].config(image=photo1, width="23", height="20")
                        if my_desk[tmp_x[0] - 1][tmp_y[0]][0] == '3' and len(shot_ship) == 2:
                            my_desk[tmp_x[0] - 1][tmp_y[0]] = 99
                            shot_ship.append((tmp_x[0] - 1, tmp_y[0]))
                            mark_area(my_desk, player_buttons, shot_ship)
                            shot_ship.clear()
                            players_ships -= 1
                            return players_ships
                        elif my_desk[tmp_x[0] - 1][tmp_y[0]][0] == '4' and len(shot_ship) == 3:
                            my_desk[tmp_x[0] - 1][tmp_y[0]] = 99
                            shot_ship.append((tmp_x[0] - 1, tmp_y[0]))
                            mark_area(my_desk, player_buttons, shot_ship)
                            shot_ship.clear()
                            players_ships -= 1
                            return players_ships
                        else:
                            my_desk[tmp_x[0] - 1][tmp_y[0]] = 99
                            shot_ship.append((tmp_x[0] - 1, tmp_y[0]))
                            players_ships -= 1
                            return players_ships
                    else:
                        my_desk[tmp_x[0] - 1][tmp_y[0]] = 1
                        player_buttons[tmp_x[0] - 1][tmp_y[0]].configure(background='white')

                #print('[tmp_x[-1] + 1][tmp_y[0]] = ', tmp_x[-1] + 1, tmp_y[0])
                #print('my_desk[tmp_x[-1] + 1][tmp_y[0]] = ', my_desk[tmp_x[-1] + 1][tmp_y[0]])
                if 0 <= (tmp_x[-1] + 1) <= 9 and my_desk[tmp_x[-1] + 1][tmp_y[0]] != 1 and my_desk[tmp_x[-1] + 1][tmp_y[0]] != 99:
                    if my_desk[tmp_x[-1] + 1][tmp_y[0]] != 0:
                        player_buttons[tmp_x[-1] + 1][tmp_y[0]].config(image=photo1, width="23", height="20")
                        if my_desk[tmp_x[-1] + 1][tmp_y[0]][0] == '3' and len(shot_ship) == 2:
                            my_desk[tmp_x[-1] + 1][tmp_y[0]] = 99
                            shot_ship.append((tmp_x[-1] + 1, tmp_y[0]))
                            mark_area(my_desk, player_buttons, shot_ship)
                            shot_ship.clear()
                            players_ships -= 1
                            return players_ships
                        elif my_desk[tmp_x[-1] + 1][tmp_y[0]][0] == '4' and len(shot_ship) == 3:
                            my_desk[tmp_x[-1] + 1][tmp_y[0]] = 99
                            shot_ship.append((tmp_x[-1] + 1, tmp_y[0]))
                            mark_area(my_desk, player_buttons, shot_ship)
                            shot_ship.clear()
                            players_ships -= 1
                            return players_ships
                        else:
                            my_desk[tmp_x[-1] + 1][tmp_y[0]] = 99
                            shot_ship.append((tmp_x[-1] + 1, tmp_y[0]))
                            players_ships -= 1
                            return players_ships
                    else:
                        my_desk[tmp_x[-1] + 1][tmp_y[0]] = 1
                        player_buttons[tmp_x[-1] + 1][tmp_y[0]].configure(background='white')

    return players_ships