# Warsztat5 - Zadania.
# -*- encoding: utf-8 -*-

#DICTIONARIES
import numpy as np


#zad1
def zad1():
    list = {}
    while True:
        print('Adding products, to add press enter, to finish press 0.')
        if input() != '0':
            product_name = input('Enter product name: ')
            product_price = input('Enter product price: ')
            if product_name in list:
                print('The previous price has been updated.')
            list[product_name] = product_price

        else:
            print('Your list of products:  ', list)
            break
print(zad1())

#zad2
print(" ")
print("2. ")
dollar = input('Enter amount: ')
print('Showing the products with lesser prices')
for product_name in list:
        if list[product_name] <= dollar:
            print(product_name, ' : ', list[product_name])

#zad3
def zad3():
    days = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31,
            'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31, 'Jan': 31, 'Feb': 28,
            'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30, 'Jul': 31, 'Aug': 31, 'Sep': 30, 'Oct': 31, 'Nov': 30,
            'Dec': 31}
    asked = input('Which month would you like? ')
    if asked not in days:
        print('There\'s no such month')
    else:
        print(asked, ' has ', days[asked], ' days.')

    for i in sorted(days):
        print(i, ' ', days[i])

    print('Months with 31 days')
    for i in days:
        if days[i] == 31:
            print(i, ' ')

    print('Months sorted by number of days')
    for i in sorted(days, key=days.get):
        print(days[i], ' - ', i)

    ask = input('Which month would you like? ')
    asked = str(ask[:3])
    if asked not in days:
        print('There\'s no such month')
    else:
        print(asked, ' has ', days[asked], ' days.')


# zad4

def zad4():
    logs = {}
    for i in range(10):
        login = input("Login: ")
        password = input("Password: ")
        logs[login] = password
    print(logs)
    print("Enter correct login and password")
    your_login = input("Login: ")
    if your_login in logs:
        your_password = input("Password: ")
        if your_password == logs[your_login]:
            print("You\'ve been successfully logged in!")
        else:
            print("Wrong password!")
    else:
        print("There is no user with this login")


# zad5

def zad5():
    base = {}
    games = {}
    won = "won"
    lost = "lost"
    while True:
        answer = input("Do you want to add a team? [Y/N]")
        if answer == "y":
            team_name = input("Enter Team Name: ")
            wins = input("Games won: ")
            games[won] = wins
            loses = input("Games lost: ")
            games[lost] = loses
            base[team_name] = wins, loses
        if answer == "n":
            break
    print(base)
    searching_team_percentage = input("Show winning stats of: ")
    if searching_team_percentage in base:
        team_percentage = int(base[searching_team_percentage][0]) / (int(base[searching_team_percentage][0])
                                                                     + int(base[searching_team_percentage][1]))
        print(team_percentage)
    else:
        print("There\'s no such team")


# zad6

def zad6():
    scores = []
    team_scores = {}
    wins1 = 0
    loses1 = 0
    wins2 = 0
    loses2 = 0
    while True:
        answer = input("Do you want to add game scores? [Y/N]")
        if answer == "y":
            score_line = input("Enter game scores: team score - team score")
            score_line = score_line.replace('-', '')
            score_line = score_line.split()
            team_1 = score_line[0]
            team_2 = score_line[2]
            score_1 = int(score_line[1])
            score_2 = int(score_line[3])

            if team_1 in team_scores:
                if score_1 > score_2:
                    team_scores[team_1][0] += 1
                else:
                    team_scores[team_1][1] += 1

            if team_2 in team_scores:
                if score_1 > score_2:
                    team_scores[team_2][1] += 1
                else:
                    team_scores[team_2][0] += 1

            if team_1 not in team_scores:
                if score_1 > score_2:
                    if team_1 not in team_scores:
                        team_scores[team_1] = [1, 0]
                else:
                    if team_1 not in team_scores:
                        team_scores[team_1] = [0, 1]

            if team_2 not in team_scores:
                if score_1 > score_2:
                    if team_2 not in team_scores:
                        team_scores[team_2] = [0, 1]
                else:
                    if team_2 not in team_scores:
                        team_scores[team_2] = [1, 0]

        if answer == "n":
            print(team_scores)
            break


# zad7


def zad7():
    x = 5
    y = 5
    matrix = np.random.randint(10, size=(5, 5))
    print(matrix)
    repeats = {}

    for number in matrix.flat:
        if number in repeats:
            repeats[number] += 1
        else:
            repeats[number] = 1

    for i in range(3):
        max_key = max(repeats, key=lambda key: repeats[key])
        print(max_key)
        repeats.pop(max_key)


# zad8
import random

def zad8():
    deck_0 = {'king': 13, 'queen': 12, 'jack': 11, 'ten': 10, 'nine': 9, 'eight': 8, 'seven': 7, 'six': 6, 'five': 5,
              'four': 4, 'three': 3, 'two': 2, 'ace': 1}
    deck = {13: 'king', 12: 'queen', 11: 'jack', 10: 'ten', 9: 'nine', 8: 'eight', 7: 'seven', 6: 'six', 5: 'five',
            4: 'four', 3: 'three', 2: 'two', 1: 'ace'}

    player_1 = {}
    player_2 = {}

    print('DEALING CARDS')
    for i in range(3):
        card_dealt_1 = random.randint(1, 13)
        card_dealt_2 = random.randint(1, 13)
        player_1[deck[card_dealt_1]] = card_dealt_1
        player_2[deck[card_dealt_2]] = card_dealt_2
        print('Player 1:\t', deck[card_dealt_1], '\t', 'Player 2:\t', deck[card_dealt_2])

    pl_1 = sorted(list(player_1.values()), reverse=True)
    pl_2 = sorted(list(player_2.values()), reverse=True)

    if pl_1[0] > pl_2[0]:
        print('Player 1 wins!')
    if pl_1[0] < pl_2[0]:
        print('Player 2 wins!')
    if pl_1[0] == pl_2[0]:
        if pl_1[1] > pl_2[1]:
            print('Player 1 wins!')
        if pl_1[1] < pl_2[1]:
            print('Player 2 wins!')
        if pl_1[1] == pl_2[1]:
            print('Player 1 wins!')
            if pl_1[2] > pl_2[2]:
                print('Player 1 wins!')
            if pl_1[2] < pl_2[2]:
                print('Player 2 wins!')
            if pl_1[2] == pl_2[2]:
                print('It\'s a draw!')


# BASIC EXERCISES SETS

def basic_exercises_sets():
    # zad1
    print('Created set')
    set_0 = {'One', 'Two', 33, 77, 1, 'Banana'}
    print(set_0)

    # zad2
    print('\nIterating over set')
    for i in set_0:
        print(i)

    # zad3
    print('\nAdding to a set')
    set_0.add('added')
    print(set_0)

    # zad4
    print('\nRemoving from set')
    set_0.remove(77)
    print(set_0)

    # zad5
    print('\nRemoving from set if present')
    to_remove = 1
    if to_remove in set_0:
        set_0.remove(to_remove)
    print(set_0)

    # zad6
    print('\nCreating intersection of sets')
    set_1 = {'Cherry', 'Apple', 'Banana'}
    inter_set = set_0.intersection(set_1)
    print(inter_set)

    # zad7
    print('\nCreating union of sets')
    union_set = set_0.union(set_1)
    print(union_set)

    # zad8
    print('\nCreating set difference')
    dif_set = set_0.difference(set_1)
    print(dif_set)

    # zad9
    print('\nCreating symmetric difference')
    sym_set = set_0.symmetric_difference(set_1)
    print(sym_set)

    # zad10
    print('\nIssubset and issuperset')
    issubset_set = set_0.issubset(set_1)
    issuperset_set = set_0.issuperset(set_1)
    print(issubset_set)
    print(issuperset_set)

    # zad11
    print('\nCreating shallow copy of set')
    copy_set_0 = set_0.copy()
    print(set_0)
    print(copy_set_0)

    # zad12
    print('\nClearing a set')
    copy_set_0.clear()
    print(copy_set_0)


# EXERCISES
#zad1
def zad1S():
    distinct_int = lambda integers: sum([1 for integer in integers if integers.count(integer) == 1])
    print(distinct_int([12, 15, 15, 6, 7, 9, 9, 9, 4, 15]))


#zad2
def zad2S():
    unique_num = lambda x, y: sum(1 for el in x + y if (x + y).count(el) == 1)
    print(unique_num([1, 2, 3, 4, 5, 6, 7], [0, 5, 6, 7]))


#zad3
def zad3S():
    list_x = [1, 2, 3, 4, 5]
    list_y = [1, 3, 5, 7, 9]
    asc_sum = lambda x, y: sorted([value for value in list_x if value in list_y])
    print(asc_sum(list_x, list_y))


#zad4
import itertools


def zad4S():
    sequence = [0, 1, 1, 2, 3, 3, 3, 5, 7, 8, 8, 9]
    print(sequence[0])
    for i in range(len(sequence) - 1):
        print(sequence[i + 1], end='\t')
        if sequence[i] == sequence[i + 1]:
            print('Yes')
        else:
            print('No')


#zad5

def zad5S():
    Alices_set = set()
    Bobs_set = set()
    Alice_set_len = random.randint(20, 60)
    Bobs_set_len = random.randint(20, 60)
    for i in range(Alice_set_len):
        Alices_set.add(random.randint(0, 108))
    for i in range(Bobs_set_len):
        Bobs_set.add(random.randint(0, 108))

    print('Number of elements in both sets ', len(Alices_set.intersection(Bobs_set)), '\t',
          sorted(Alices_set.intersection(Bobs_set)))

    print('Number of elements in Alice\'s set ', len(Alices_set.difference(Bobs_set)), '\t',
          Alices_set.difference(Bobs_set))

    print('Number of elements in Bob\'s set ', len(Bobs_set.difference(Alices_set)), '\t',
          Bobs_set.difference(Alices_set))

#zad6

def zad6S():
    text = 'Given a number n, followed by n lines of text, print the number of distinct words that appear in the text. ' \
           'For this, we define a word to be a sequence of non-whitespace characters, separated by one or more ' \
           'whitespace or newline characters. Punctuation marks are part of a word, in this definition.'
    word = text.split(' ')
    print('There are ', len(word), ' words')
    print('There are ', len(set(word)), ' distinct elements')


#zad7

def zad7S():
    helps = input('Type: <HELP> <range> <your guess> <Augustus\' response>')
    help = helps.split(' ')
    print(help[1])
    game_range = int(help[1])
    right_guesses = []
    wrong_guesses = []
    for i in range(len(help) - 3):
        if help[i + 3] == 'yes':
            right_guesses.append(int(help[i + 2]))
        if help[i + 3] == 'no':
            wrong_guesses.append(int(help[i + 2]))
    print('Right guesses ', right_guesses, '\tWrong guesses ', wrong_guesses)

    possible_guesses = []
    for i in range(game_range):
        if i not in right_guesses + wrong_guesses:
            possible_guesses.append(i)

    print(possible_guesses)


# #EXERCISES
#zad1

def rectangle(m, n):
    for i in range(n):
        for j in range(m):
            print('*', end=' ')
        print('')


#zad2

def add_excitement(list_of_strings):
    for i in range(len(list_of_strings)):
        list_of_strings[i] = list_of_strings[i] + '!'
    print(list_of_strings)


#zad2b

def add_excitement_modified(list_of_strings):
    new_list = []
    for i in list_of_strings:
        new_list.append(i + '!')
    print(new_list)


#zad3
def sum_digits():
    num = input('Give a number ')
    digits = list(num)
    sum = 0
    for i in digits:
        sum += int(i)
    print('Sum of all digits equals ', sum)


#zad4

def root():
    num = input('Enter a number: ')
    digits = (list(num))

    for i in range(len(list(num))):
        sumup = sum(int(i) for i in digits)
        digits = str(sumup)

    print(sumup)


#zad5

def first_diff():
    str_1 = 'There is nothing i would do'
    str_2 = 'There is nothing i would do'

    if list(str_1) == list(str_2):
        print('-1')
    else:
        if len(list(str_1)) > len(list(str_2)):
            for i in range(len(list(str_1))):
                if list(str_1)[i] != list(str_2)[i]:
                    print('First differing on index: ', i)
                    break
        else:
            for i in range(len(list(str_2))):
                if list(str_1)[i] != list(str_2)[i]:
                    print('First differing on index: ', i)
                    break


#zad6

from scipy import special


def binom(n, k):
    binn = special.binom(n, k)
    print(binn)


#zad7

def digit_numbers(n):
    number = []
    for i in range(n):
        if i == 0:
            number.append(random.randint(1, 9))
        else:
            number.append(random.randint(0, 9))
    print(''.join(str(el) for el in number))


#zad8
def number_of_factors(x):
    counter = 0
    for i in range(1, x + 1):
        if x % i == 0:
            counter += 1
    print(counter)


#zad9
def factors(x):
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)

#zad10

def closest(list_of_numbers, number):
    for i in range(len(list_of_numbers)):
        if number in list_of_numbers:
            print(number)
        else:
            list_of_numbers = sorted(list_of_numbers)
            if number < list_of_numbers[i]:
                print(list_of_numbers[i - 1])
                break


#zad11

def matches(str_1, str_2):
    counter = 0
    if len(str_1) < len(str_2):
        for i in range(len(str_1)):
            if str_1[i] == str_2[i]:
                counter += 1
    else:
        for i in range(len(str_2)):
            if str_1[i] == str_2[i]:
                counter += 1
    print(counter)


#zad12

def findall(str, letter):
    counter = 0
    indexes = []
    for i in range(len(list(str))):
        if letter == str[i]:
            indexes.append(i)
    print(indexes)


#zad13

def change_case(str):
    print(str.swapcase())


#zad14

def is_sorted(a_list):
    if a_list == sorted(a_list):
        print('True')
    else:
        print('False')


#zad15

def roott(x, n=2):
    print(x * (1 / n))


#zad16

def one_away(str_1, str_2):
    falses = 0
    if len(str_1) == len(str_2):
        for x, y in zip(str_1, str_2):
            if x != y:
                falses += 1
        if falses < 2:
            print('True')
        else:
            print('False')


#zad17

def primes(n=100):
    primes_ = []

    for a in range(1, n * n):
        for b in range(2, a):
            if a % b == 0:
                break
        else:
            primes_.append(a)
        if len(primes_) == n:
            break
    print(primes_)
    print(len(primes_))


#zad17b

def primes_2(n=100, start=2):
    primes_ = []

    for a in range(start, n * n):
        for b in range(2, a):
            if a % b == 0:
                break
        else:
            primes_.append(a)
        if len(primes_) == n:
            break
    print(primes_)
    print(len(primes_))
