# Warsztat7 - Zadanie10.
# -*- encoding: utf-8 -*-

def read_words():
    with open("files/wordlist.txt", "r") as words_file:
        words = words_file.read().split()
    return words


words = read_words()


# (a) All words ending in ime
def zad10a():
    for word in words:
        if word.endswith("ime"):
            print(word)


# (b) All words whose second, third, and fourth letters are ave
def zad10b():
    ave_regex = re.compile(r"\A\wave\w*")
    for word in words:
        if ave_regex.search(word) is not None:
            print(word)


# (c) How many words contain at least one of the letters r, s, t, l, n, e
# (d) The percentage of words that contain at least one of the letters r, s, t, l, n, e
def zad10cd():
    ave_regex = re.compile(r"\w*[rstlne]\w*")
    counter = 0
    for word in words:
        if ave_regex.search(word) is not None:
            counter += 1
    print(f"Number of words containing [rstlne]: {counter}\n Percentage: {counter/len(words) * 100}%")


# (e) All words with no vowels
def zad10e():
    ave_regex = re.compile(r"\w*[oaeiuy]\w*")
    for word in words:
        if ave_regzad.search(word) is None:
            print(word)


# (f) All words that contain every vowel
def contains_all_vowels(string):
    vowels = ["o", "a", "e", "i", "u", "y"]
    for vowel in vowels:
        if string.find(vowel) == -1:
            return False

    return True


def zad10f():
    for word in words:
        if contains_all_vowels(word):
            print(word)


# (g) Whether there are more ten-letter words or seven-letter words
def zad10g():
    count_sevens, count_tens = 0, 0

    for word in words:
        if len(word) == 7:
            count_sevens += 1
        elif len(word) == 10:
            count_tens += 1

    if count_sevens >= count_tens:
        print(f"There are more seven-letter words. {count_sevens} to be exact.")
    else:
        print(f"There are more ten-letter words. {count_tens} to be exact.")


# (h) The longest word in the list
def zad10h():
    print(f"Longest word: {max(words, key=len)}")


# (i) All palindromes
def zad10i():
    for word in words:
        if list(word) == list(reversed(word)):
            print(word)


# (j) All words that are words in reverse, like rat and tar.
def zad10j():
    for word in words:
        reversed_word = "".join(list(reversed(word)))
        if reversed_word in words:
            print(word)


# (k) Same as above, but only print one word out of each pair.
def zad10k():
    custom_words = words
    for word in custom_words:
        reversed_word = "".join(list(reversed(word)))
        if reversed_word in custom_words:
            print(word)
            custom_words.remove(word)


# (l) All words that contain double letters next each other like aardvark or book, excluding words that end in lly
def zad10l():
    for word in words:
        for i in range(len(word) - 1):
            if word[i] == word[i + 1]:
                print(word)
                break


# (m) All words that contain a q that isn’t followed by a u
def zad10m():
    for word in words:
        for i in range(len(word)):
            if word[i] == "q" and word[i + 1] != "u":
                print(word)


# (n) All words that contain zu anywhere in the word
def zad10n():
    for word in words:
        if word.find("zu") != -1:
            print(word)


# (o) All words that contain ab in multiple places, like habitable
def zad10o():
    for word in words:
        first_occurence = word.find("ab")
        if first_occurence != -1:
            if word[first_occurence + 2:].find("ab") != -1:
                print(word)


# (p) All words with four or more vowels in a row
def zad10p():
    regex_vowels = re.compile(r"[oaeiuyOAEIUY]{4,}")
    for word in words:
        if regex_vowels.search(word) is not None:
            print(word)


# (q) All words that contain both a z and a w
def zad10q():
    for word in words:
        if word.find("z") != -1 and word.find("w") != -1:
            print(word)


# (r) All words whose first letter is a, third letter is e and fifth letter is i
def zad10r():
    for word in words:
        if word.find("a") == 0 and word.find("e") == 2 and word.find("i") == 4:
            print(word)


# (s) All two-letter words
def zad10s():
    for word in words:
        if len(word) == 2:
            print(word)


# (t) All four-letter words that start and end with the same letter
def zad10t():
    for word in words:
        if word.endswith(word[0]):
            print(word)


# (u) All words that contain at least nine vowels.
def zad10u():
    regex_vowels = re.compile(r"[oaeiuyOAEIUY]")
    for word in words:
        if len(regex_vowels.findall(word)) >= 9:
            print(word)


# (v) All words that contain each of the letters a, b, c, d, e, and f in any order. There may be other letters in the
# word. Two examples are backfield and feedback.
def zad10v():
    for word in words:
        if word.find("a") != -1 and word.find("b") != -1 and word.find("c") != -1 and word.find(
                "d") != -1 and word.find("f") != -1:
            print(word)


# (w) All words whose first four and last four letters are the same
def zad10w():
    for word in words:
        if word.endswith(word[:4]):
            print(word)


# (x) All words of the form abcd*dcba, where * is arbitrarily long sequence of letters.
def zad10x():
    abcd_regex = re.compile(r"abcd.*dcba")
    for word in words:
        if abcd_regex.search(word) is not None:
            print(word)


# (y) All groups of 5 words, like pat pet pit pot put, where each word is 3 letters, all words share the same first
# and last letters, and the middle letter runs through all 5 vowels.
def zad10y():
    words_list = " ".join(words)
    rhyme_regex = re.compile(f"\wa\w \we\w \wi\w \wo\w \wu\w")
    print(rhyme_regex.findall(words_list))


# (z) The word that has the most i’s.
def zad10z():
    best = ""
    for word in words:
        if word.count("i") > best.count("i"):
            best = word
    print(best)