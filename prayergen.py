#!/usr/bin/python3

import random

from wonderwords import RandomWord

gods = RandomWord()

def gods_word(part_of_speech):
    return gods.word(include_parts_of_speech=[part_of_speech])

def gods_choice(limit):
    return random.randint(1, limit)

prayer = "Oh " + gods_word("adjectives") + " " + gods.word(ends_with="ey") + "."
for _ in range(random.randint(5, 10)):
    gods_grace = random.random()
    prior_len = len(prayer)
    if gods_grace < 0.2:
        prayer += " " + gods_word("adjectives") + " " + gods_word("noun")
    elif gods_grace < 0.28:
        prayer += "".join(random.choices(",./'[]{}()!@#$%^&*-=_+<>?`~\"", k=gods_choice(6)))
    elif gods_grace < 0.58:
        prayer += " " + gods.word(ends_with="ly") + " " + gods_word("verb")
    elif gods_grace < 0.69:
        prayer += "."
    else:
        prayer += " " + gods.word()
    gods_grace = random.random()
    suffix_len = len(prayer) - prior_len - 1
    if gods_grace < 0.2:
        prayer = prayer[:-suffix_len] + prayer[-suffix_len:-suffix_len+1].upper() + prayer[-suffix_len+1:]
    elif gods_grace < 0.3:
        prayer = prayer[:-suffix_len] + prayer[-suffix_len:].upper()
prayer += " " + gods.word(ends_with="en") + "."

print(prayer)
