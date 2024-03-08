'''
Create 2 lists from a given list where 1st list will contain all the odd numbers from the original list and the 2nd one will contain all the even numbers
'''

def split_odds_even(lst):
    odds = [num for num in lst if num % 2 != 0]
    evens = [num for num in lst if num % 2 == 0]
    return odds,evens

odds, evens = split_odds_even([1,2,3,4,5,6,7,8,9])
print("Odds: ",odds)
print("Evens: ",evens)