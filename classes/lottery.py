import random

possible_numbers = [7, 13, 24, 11, 22, 3, 9, 1, 32, 19, 'A', 'N', 'V', 'Z', 'I'] # list of possible winning elements

def get_winning_ticket():
#Returns a winning ticket from a list of possible numbers.
    winning_ticket = []

    while len(winning_ticket) < 4:
        i = random.choice(possible_numbers)
        if i not in winning_ticket:
            winning_ticket.append(i)
    return winning_ticket

def get_random_ticket():
# Returns a random ticket from a list of possible numbers.
    my_ticket = []

    while len(my_ticket) < 4:
        i = random.choice(possible_numbers)
        if i not in my_ticket:
            my_ticket.append(i)
    return my_ticket

def check_ticket(winning_ticket, my_ticket):
# Checks if a new random ticket mathes the winning ticket.
    for element in my_ticket:
        if element not in winning_ticket:
            return False
    return True

def main():
    winning_ticket = get_winning_ticket()
    print('Any ticket matching the following numbers and/or letter is winning: ', *winning_ticket, '\n', sep=' ')

    my_ticket = get_random_ticket()
    counter = 1

    while not check_ticket(winning_ticket, my_ticket):
        my_ticket = get_random_ticket()
        counter += 1
    print('Your ticket: ', *my_ticket, '\n', sep=' ')
    print(f'It took you {counter} times to win!')



if __name__ == '__main__':
    main()