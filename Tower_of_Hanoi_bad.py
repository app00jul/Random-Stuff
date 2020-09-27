# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 21:20:42 2020
"""

""" 
Program Objective: 
This is a program that solve the logic problem called the Tower of Hanoi. 
The Tower of Hanoi is a mathematical game or puzzle. It consists of three rods and a number of disks of different sizes, 
which can slide onto any rod. The puzzle starts with the disks in a neat stack in ascending order of size on one rod,  
the smallest at the top, thus making a conical shape. 

The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules: 

    1. Only one disk can be moved at a time. 
    2. Each move consists of taking the upper disk from one of the stacks and placing it  
        on top of another stack or on an empty rod. 
    3. No larger disk may be placed on top of a smaller disk. 

With 3 disks, the puzzle can be solved in 7 moves.  
The minimal number of moves required to solve a Tower of Hanoi puzzle is 2n − 1, where n is the number of disks.  

This program will use dynamic programming algorithm with any given amount of disks. 

The logic behind this program is to make the last pillar has the maximum numbers of disks it possibly can and 
at the same time still follow the three given rules.  
"""

import time
import timeit


def blocks_print(l1, l2, l3):
    list1 = []  # list is actually the pillar #the first pillar (origin)
    list2 = []  # the second pillar
    list3 = []  # the third pillar
    for element in l1:  # the element is the disks
        list1.append(element)
    for element in l2:
        list2.append(element)
    for element in l3:
        list3.append(element)

    height = max(len(list1), len(list2), len(list3))
    for current_list in [list1, list2, list3]:
        while len(current_list) < height:
            current_list.append(0)
    width = max(max(list1), max(list2), max(list3))
    print_key = []

    for i in range(0, width + 1):
        print_key.append('# ' * i)
        print_key[i] = print_key[i].strip()
        print_key[i] = print_key[i].center(width * 2 + 1, ' ')
        """make the # that represents  the disks centralize so it looks good."""

    while len(list1) > 0:
        print(print_key[list1.pop()], print_key[list2.pop()], print_key[list3.pop()], sep=' ')
    print('\n')


def move_block(home, target):
    if home:
        target.append(home.pop())


def move_counter():  # counter):
    # time.sleep(0.5)

    # print(f"The number of moves is {counter}")
    count = timeit.default_timer()
    count = count - 3.1
    time.sleep(0.5)



def tower_of_hanoi(home, target, other, level):
    """ This is function that determine how the disks are going to move around."""
    """ It will keep the block moving until one of the pillar is full."""
    """ However, it will not stop working until the last pillar is the one that is full."""
    move_counter()
    if level != 0:
        tower_of_hanoi(home, other, target, level - 1)
        tower_of_hanoi(home, target, other, 0)
        tower_of_hanoi(other, target, home, level - 1)
    else:
        move_block(home, target)  # if the last pillar is not full, the process will run all over again.
        blocks_print(L1, L2, L3) #print the disks everytime an action is made
        """The L1, L2, L3 are the pillar. Here, when the function blocks_print is called,
        it will print the pillar and the disk, showing any action is made."""


L1 = [4, 3, 2, 1]
L2 = []
L3 = []

blocks_print(L1, L2, L3) #print the disk before any actions begin
""" This function will print the disk and the pillar before any action are made.
The L1, L2, L3 are the pillar. Everytime an element of them are change, it is considered an action"""

tower_of_hanoi(L1, L3, L2, len(L1))
