# bubble_sort.py simple sorting algorithm
from random import shuffle

def get_list():
    """Returns an array populated with a list of numbers from the user."""
    err = True
    print("Enter your numbers.\nPlease leave a space between each one.")
    while err == True:
        err = False
        temp = input("Data: ")
        my_list = temp.split()
        for i in range (len(my_list)):
            try:
                my_list[i] = int(my_list[i])
            except:
                try:
                    my_list[i] = float(my_list[i])
                except:
                    print("Try again, only numbers and spaces please.")
                    err = True
                    break
    return my_list

def bubble_sort(some_list):
    """Takes a list, sorts it and returns the number of swaps."""
    j = len(some_list)
    made_swap = True
    # A swap-counter    
    swaps = 0
    while made_swap:
        made_swap = False
        # iterate over the whole list 
        for k in range(j-1):
            # if the item is greater than the next in the list ...
            if some_list[k] > some_list[k+1]:
                # ... they are swapped
                some_list[k], some_list[k+1] = some_list[k+1], some_list[k]
                made_swap = True
                # add one to the swap-counter
                swaps += 1
                # uncomment the next line to see the result of  each swap.
                # print(some_list)
    return swaps

# main
print("\nWelcome to bubble sort.")
# setting up a simple text menu
ans = None
while ans != 'q':
    print(
    """\nYou have 3 options:
    1: Use numbers 1-20 shuffled.
    2: Input your own values.
    q: Quit.""")

    ans = input("\nWhat do you want to do? ")
    if ans == '1':
        # initialise the list.
        unsorted = list(range(20))
        # shuffle list.
        shuffle(unsorted)
        print("Randomised list created.")            
    elif ans == '2':
        unsorted = get_list()
        print("You gave me:")
    else:
        if ans != "q":
            print("Unrecognised choice.")
        continue
        
    print(unsorted, end="\n\n")
    print(bubble_sort(unsorted), "swap(s) made.")
    print("Here's the sorted list: \n", unsorted)
