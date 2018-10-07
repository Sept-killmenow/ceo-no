from time import *
from colorama import *


class Player:
    def __init__(self, name,):
        self.name = name
        self.input = input


class GeneriCorp:
    def __init__(self, stock, assets, money, income):
        self.stock = stock
        self.assets = assets
        self.money = money
        self.income = income


class Property:
    def __init__(self, name, cost, value, income, production, stock_increase):
        self.name = name
        self.cost = cost
        self.value = value
        self.income = income
        self.production = production
        self.stock_increase = stock_increase


# Store
confirm_purchase = ''
value = 0
asset = ''
income = 0

# Player
gc = GeneriCorp(200, [''], 10000, 0)
p1 = Player('')
# Trackers
day = 30
stock = 0
stock_gained = 0
money_gained = 0
# Property's
copper_mine = Property('Copper Mine', 5000, 2500, 500, 1, 0.5)
coal_mine = Property('Coal Mine', 7500, 3750, 1500, 1, 1)
iron_mine = Property('Iron Mine', 25000, 12500, 3000, 1, 2)
gold_mine = Property('Gold Mine', 100000, 50000, 7500, 1, 3)
refinery = Property('Refinery', 25000, 12500, 3000, 1, 5)


def clear():
    print('\n'*55)


def start_menu():
    clear()
    print(Fore.BLACK + '████████████████████████████████\n\n                    ',
          Fore.BLUE + 'CEO -', Fore.RED + 'NO\n' + Fore.BLACK)
    print('████████████████████████████████\n')
    print(Fore.YELLOW + '1. Start')
    print('2. Instructions\n' + Fore.BLACK)
    print('████████████████████████████████')
    print(Fore.YELLOW + 'Input a number to begin' + Fore.BLACK)
    p1.input = input(Fore.RED + '>>' + Fore.BLACK)
    if p1.input == '1':
        start()
    elif p1.input == '2':
        menu_instructions()
    else:
        start_menu()


def menu_instructions():
    clear()
    print('████████████████████████████████\n\n                  ',
          Fore.BLUE + 'Instructions\n' + Fore.BLACK)
    print('████████████████████████████████\n')
    print(Fore.YELLOW + 'To navigate the user interface you must type the\nnumber corrosponding to what you want to do.'
                        '\n\nThe objective of the game is to please your\ncompany''s investors'
                        ' if you cannot do this you will '
                        '\nlose your job and lose the game.\n\n''Press enter to go back.' + Fore.BLACK)
    print('████████████████████████████████')
    p1.input = input()
    if p1.input == '':
        start_menu()
    else:
        start_menu()


def start():
    clear()
    print('████████████████████████████████')
    p1.name = input(Fore.YELLOW + 'Please type your name ...' + Fore.BLACK)
    if p1.name == '':
        start()
    clear()
    print('████████████████████████████████\n')
    print(Fore.YELLOW + 'Welcome', Fore.BLUE + p1.name, Fore.YELLOW + 'to your new position as CEO of')
    print(Fore.RED + 'Generi-corp', Fore.YELLOW + 'DONT MESS IT UP\n' + Fore.BLACK)
    print('████████████████████████████████')
    sleep(5.5)
    main_screen()


def main_screen():
    clear()
    print('████████████', Fore.RED + 'GENERI-CORP', Fore.BLACK + '████████████\n')
    print(Fore.YELLOW + 'Days Left:' + Fore.BLUE, day)
    print(Fore.YELLOW + "You're making" + Fore.BLUE, gc.income, Fore.YELLOW + 'dollars per day.')
    print('You have:' + Fore.BLUE, gc.money)
    print(Fore.RED + "GENERI-CORP'S" + Fore.YELLOW, 'stock is valued at', gc.stock, 'dollars')
    print()
    print(Fore.BLACK + '█████████████' + Fore.RED + ' CHOICES ' + Fore.BLACK + '█████████████\n')
    print(Fore.YELLOW + '1. Property')
    print('2. Shop')
    print('3. Advance time')
    print('4. Give up\n')
    print(Fore.BLACK + '████████████████████████████████')
    p1.input = input(Fore.RED + '>>' + Fore.BLACK)
    if p1.input == '1':  # if the user inputs 1 they will be brought to a display screen of all owned assets
        assets_view()

    elif p1.input == '2':  # If the user inputs 2 they will be brought to a shop with property to buy/sell or upgrade
        shop_main()        # previous  owned property

    elif p1.input == '3':  # If the user inputs 3 they will be brought to a screen
        time_advance()     # to advance time giving them more or less money

    elif p1.input == '4':  # If the user inputs 4 they shall give up and will brought back to the main menu
        gameover()

    else:  # If any input other than the given options is pressed the function will replay
        main_screen()


def assets_view():
    clear()
    global copper_count, iron_count, gold_count, refinery_count
    copper_count = gc.assets.count('Copper Mine')
    coal_count = gc.assets.count('Coal Mine')
    iron_count = gc.assets.count('Iron Mine')
    gold_count = gc.assets.count('Gold Mine')
    refinery_count = gc.assets.count('Refinery')
    print('█████████', Fore.RED + "GENERI-CORP'S ASSETS", Fore.BLACK + '█████████\n')
    print('Copper Mines:', copper_count)
    print('Coal Mines:  ', coal_count)
    print('Iron Mines:  ', iron_count)
    print('Gold Mines:  ', gold_count)
    print('Refinerys:   ', refinery_count)
    print()
    print(Fore.BLACK + '█████████████' + Fore.RED + ' CHOICES ' + Fore.BLACK + '█████████████')
    print(Fore.YELLOW + '1. Sell')
    print(Fore.YELLOW + '2. Buy')
    print(Fore.YELLOW + '3. Back')
    print(Fore.BLACK + '████████████████████████████████')
    p1.input = input(Fore.RED + '>>' + Fore.BLACK)
    if p1.input == '1':
        sell()
    elif p1.input == '2':
        shop_main()
    else:
        main_screen()


def shop_main():
    global confirm_purchase, asset, stock_increase, income, production, cost, stock_gained
    clear()
    print(Fore.BLACK + '██████████████' + Fore.RED + ' SHOP ' + Fore.BLACK + '██████████████\n')
    print(Fore.YELLOW + '1.', copper_mine.name)
    print('2.', coal_mine.name)
    print('3.', iron_mine.name)
    print('4.', gold_mine.name)
    print('5.', refinery.name)
    print()
    print(Fore.BLACK + '████████████████████████████████\n')
    print(Fore.YELLOW + 'Press Return to go back\n')
    print(Fore.BLACK + '████████████████████████████████')
    p1.input = input(Fore.RED + '>>' + Fore.BLACK)

    if p1.input == '2':
        confirm_purchase = coal_mine.name
        asset = coal_mine.name
        cost = coal_mine.cost
        production = coal_mine.production
        income = coal_mine.income
        stock_increase = coal_mine.stock_increase
        stock_gained = stock_gained + coal_mine.stock_increase
        confirm()

    elif p1.input == '1':
        confirm_purchase = copper_mine.name
        asset = copper_mine.name
        cost = copper_mine.cost
        production = copper_mine.production
        income = copper_mine.income
        stock_increase = copper_mine.stock_increase
        stock_gained = stock_gained + copper_mine.stock_increase
        confirm()

    elif p1.input == '3':
        confirm_purchase = iron_mine.name
        asset = iron_mine.name
        cost = iron_mine.cost
        production = iron_mine.production
        income = iron_mine.income
        stock_increase = iron_mine.stock_increase
        stock_gained = stock_gained + iron_mine.stock_increase
        confirm()

    elif p1.input == '4':
        confirm_purchase = gold_mine.name
        asset = gold_mine.name
        cost = gold_mine.cost
        production = gold_mine.production
        income = gold_mine.income
        stock_increase = gold_mine.stock_increase
        stock_gained = stock_gained + gold_mine.stock_increase
        confirm()
    elif p1.input == '5':
        confirm_purchase = refinery.name
        asset = refinery.name
        cost = refinery.cost
        production = refinery.production
        income = refinery.income
        stock_increase = refinery.stock_increase
        stock_gained = stock_gained + refinery.stock_increase
        confirm()
    else:
        main_screen()


def sell():
    clear()
    global copper_count, iron_count, gold_count, refinery_count, stock_gained, asset, income, value, stock
    copper_count = gc.assets.count('Copper Mine')
    coal_count = gc.assets.count('Coal Mine')
    iron_count = gc.assets.count('Iron Mine')
    gold_count = gc.assets.count('Gold Mine')
    refinery_count = gc.assets.count('Refinery')
    print('█████████', Fore.RED + "GENERI-CORP'S ASSETS", Fore.BLACK + '█████████\n')
    print('1. Copper Mines:', copper_count)
    print('2. Coal Mines:  ', coal_count)
    print('3. Iron Mines:  ', iron_count)
    print('4. Gold Mines:  ', gold_count)
    print('5. Refinerys:   ', refinery_count)
    print()
    print(Fore.BLACK + '████████████████████████████████')
    print(Fore.YELLOW + 'Press return to go back' + Fore.BLACK)
    print(Fore.BLACK + '████████████████████████████████')
    p1.input = input(Fore.RED + '>>' + Fore.BLACK)
    if p1.input == '1':
        asset = copper_mine.name
        income = income - copper_mine.income
        value = copper_mine.value
        stock = copper_mine.stock_increase + 2
        stock_gained = stock_gained - copper_mine.stock_increase
        sell_confirm()
    if p1.input == '2':
        asset = coal_mine.name
        income = income - coal_mine.income
        value = coal_mine.value
        stock = coal_mine.stock_increase + 2
        stock_gained = stock_gained - coal_mine.stock_increase
        sell_confirm()
    if p1.input == '3':
        asset = iron_mine.name
        income = income - iron_mine.income
        value = iron_mine.value
        stock = iron_mine.stock_increase + 5
        stock_gained = stock_gained - iron_mine.stock_increase
        sell_confirm()
    if p1.input == '4':
        asset = gold_mine.name
        income = income - gold_mine.income
        value = gold_mine.value
        stock = gold_mine.stock_increase + 8
        stock_gained = stock_gained - gold_mine.stock_increase
        sell_confirm()
    if p1.input == '5':
        asset = refinery.name
        income = income - refinery.income
        value = refinery.value
        stock = refinery.stock_increase + 10
        stock_gained = stock_gained - refinery.stock_increase
        sell_confirm()
    else:
        assets_view()


def sell_confirm():
    global stock_gained
    clear()
    print(Fore.BLACK + '████████████████████████████████\n')
    print(Fore.YELLOW + 'Are you sure you would like to sell a' + Fore.RED, asset)
    print()
    print(Fore.BLACK + '████████████████████████████████')
    print(Fore.YELLOW + '1. Yes')
    print('2. No')
    print(Fore.BLACK + '████████████████████████████████')
    p1.input = input(Fore.RED + '>>' + Fore.BLACK)
    if p1.input == '1':
        gc.income = - income
        gc.money = gc.money + value
        gc.stock = gc.stock - stock
        gc.assets.remove(asset)
        assets_view()


def confirm():
    clear()
    print(Fore.BLACK + '████████████████████████████████')
    print(Fore.YELLOW + 'Price:', Fore.BLUE + str(cost) + '$',)
    print(Fore.YELLOW + 'Income per day:', Fore.BLUE + '+', income)
    print(Fore.YELLOW + 'Stock gain:', Fore.BLUE + '+', stock_increase)
    print(Fore.YELLOW + 'Production:', Fore.BLUE + '+', production)

    print(Fore.BLACK + '████████████████████████████████\n')
    print(Fore.YELLOW + 'Are you sure you would like to buy a' + Fore.RED, confirm_purchase)
    print()
    print(Fore.BLACK + '████████████████████████████████')
    print(Fore.YELLOW + '1. Yes')
    print('2. No')
    print(Fore.BLACK + '████████████████████████████████')
    p1.input = input(Fore.RED + '>>' + Fore.BLACK)
    if p1.input == '1':
        if gc.money >= cost:
            gc.income = gc.income + income * production
            gc.stock = gc.stock + stock_increase
            gc.money = gc.money - cost
            gc.assets.append(asset)
            assets_view()
        else:
            print(Fore.RED + 'You dont have enough money for this')
            p1.input = input(Fore.YELLOW + 'Press return')
            shop_main()

    else:
        shop_main()


def time_advance():
    clear()
    global day, stock_gained, money_gained
    print(Fore.BLACK + '████████████' + Fore.RED + ' DAILY REVIEW ' + Fore.BLACK + '███████████\n')
    print(Fore.YELLOW + 'Money:', Fore.BLUE + str(gc.money))
    print(Fore.YELLOW + 'Stock price:', Fore.BLUE + str(gc.stock))
    print(Fore.YELLOW + 'Stock increase:', Fore.BLUE + str(stock_gained))
    print(Fore.BLACK + '████████████████████████████████')
    p1.input = input(Fore.YELLOW + 'Press return to continue' + Fore.BLACK)
    gc.money = gc.money + gc.income
    money_gained = 0
    stock_gained = 0
    day = day - 1
    if day == 0:
        if gc.stock < 420:
            gameover()
        else:
            win()
    main_screen()


def gameover():
    clear()
    print(Fore.RED + '     ###    ###')
    sleep(0.1)
    print('      ###  ###  ')
    sleep(0.1)
    print('       #####     ########      ##      ##')
    sleep(0.1)
    print('        ###     ##      ##     ##      ##')
    sleep(0.1)
    print('        ###     ##      ##     ##      ##')
    sleep(0.1)
    print('        ###     ##      ##     ##      ##')
    sleep(0.1)
    print('        ###      ########       ########')
    sleep(0.8)
    print('\n'*2)
    print('########         ##           ###     ###           ########    #########')
    sleep(0.1)
    print('##             ##  ##         ###     ###           ###         ##       ##')
    sleep(0.1)
    print('##            ##    ##        ###     ###           ###         ##       ##')
    sleep(0.1)
    print('########     ##########       ###     ###           ########    ##       ##')
    sleep(0.1)
    print('##          ##        ##      ###     ###           ###         ##       ##')
    sleep(0.1)
    print('##         ##          ##     ###     ###           ###         ##       ##')
    sleep(0.1)
    print('##        ##            ##    ###     ##########    ########    #########')
    sleep(0.1)
    print('\n'*2)
    p1.input = input(Fore.BLACK + 'Press any button to return to menu.')
    start_menu()


def win():
    clear()
    print(Fore.GREEN + '   ###    ###')
    sleep(0.1)
    print('    ###  ###  ')
    sleep(0.1)
    print('     #####     ########      ##      ##')
    sleep(0.1)
    print('      ###     ##      ##     ##      ##')
    sleep(0.1)
    print('      ###     ##      ##     ##      ##')
    sleep(0.1)
    print('      ###     ##      ##     ##      ##')
    sleep(0.1)
    print('      ###      ########       ########')
    sleep(0.8)
    print('\n'*1)
    sleep(0.1)
    print('###           #####           ###    ###    ####      ###')
    sleep(0.1)
    print(' ###         ### ###         ###     ###    #####     ###')
    sleep(0.1)
    print('  ###       ###   ###       ###      ###    ######    ###')
    sleep(0.1)
    print('   ###     ###     ###     ###       ###    ### ###   ###')
    sleep(0.1)
    print('    ###   ###       ###   ###        ###    ###  ###  ###')
    sleep(0.1)
    print('     ### ###         ### ###         ###    ###   ### ###')
    sleep(0.1)
    print('      #####           #####          ###    ###     #####')
    print('\n'*2)
    p1.input = input(Fore.BLACK + 'Press any button to return to menu.')
    start_menu()
start_menu()

