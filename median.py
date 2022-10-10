"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

from turtle import position


def CalculateMedian(list_of_numbers):
    list_of_numbers.sort()
    if len(list_of_numbers) % 2 == 1:
        mid_position_index = ( len(list_of_numbers) + 1)/2
        return list_of_numbers[int(mid_position_index) - 1]
    else:
        position = len(list_of_numbers)/2
        index1 = int(position - 1)
        index2 = int(index1 + 1)

        return (list_of_numbers[index1] + list_of_numbers[index2]) / 2


    
 
while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        input_from_user = input()
        input_from_user = input_from_user.split(',')

        numbers = [ int(value) for value in input_from_user]
        numbers.sort()
        print(numbers)
        print(CalculateMedian(numbers))

    except ValueError:
        print("Some input coul2,d not be converted to a number!")
    else:
        break

