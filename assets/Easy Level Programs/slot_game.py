import random

# Constant variables
MAX_LINE = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbols_count = {
    'A':2,
    'B':4,
    'C':6,
    'D':8
}

symbols_values = {
    'A':5,
    'B':3,
    'C':4,
    'D':2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    lines_won = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            lines_won.append(line + 1)
        
    return winnings, lines_won




def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbols_count in symbols.items():
        for _ in range(symbols_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns

def print_slot(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row],end=' | ')
            else:
                print(column[row], end='')
        print()




def deposit():
    while True:
        amount = input('How much would you like to deposit: $')
        if amount.isdigit():
            amount = float(amount)
            if amount > 0:
                break
            else:
                print('Amount must be greater than zero!')
        else:
            print('Please enter a number!')
    print('----------------------------------------------------------------')

    return amount

def get_number_of_lines():
    while True:
        lines = input('Enter the number of lines to bet on(1-' + str(MAX_LINE) + '): ')
        if lines.isdigit():
            lines = int(lines)
            if 0 < lines <= MAX_LINE:
                break
            else:
                print('Enter a valid number of lines!')
        else:
            print('Please enter a number!')
    print('----------------------------------------------------------------')

    return lines

def get_bet():
    while True:
        amount = input('How much would you like to bet: $')
        if amount.isdigit():
            amount = float(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f'Betting amount must be between ${MIN_BET} - ${MAX_BET} !')
        else:
            print('Please enter a number!')
    
    print('----------------------------------------------------------------')

    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print('You do not have enough balance to bet!')
            print(f'Current balance: ${balance}')
            print('----------------------------------------------------------------')
        else:
            break

    print(f'You are betting ${bet} on ${lines} lines.\n Total bet: ${total_bet}')
    print('----------------------------------------------------------------')

    slots = get_slot_machine_spin(ROWS, COLS, symbols_count)
    print_slot(slots)
    winnings, lines_won = check_winnings(slots, lines, bet, symbols_values)
    print('----------------------------------------------------------------')
    print(f'You won ${winnings}. ')
    print(f'You won on lines:', *lines_won)
    print('----------------------------------------------------------------')
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f'Current balance: ${balance}')
        answer = input('Press enter to play (q to quit): ')
        if answer == 'q':
            break
        balance +=spin(balance)
    
    print(f'Current balance: ${balance}')

if __name__ == '__main__':
    main()