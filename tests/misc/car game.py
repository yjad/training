#car_status: str = "STOP"
#car_status= {status: "stop", lights: True, gear: "P"}
START: str = 'start'
HELP: str = 'help'
STOP: str = 'stop'
QUIT:str = 'quit'
LIGHTS_ON:str = 'lights on'
LIGHTS_OFF:str= 'lights off'
BREAK_ON:str = 'break on'
BREAK_OFF:str= 'break off'
GEAR = 'gear'
GEAR_P = 'gear p'
GEAR_R = 'gear r'
GEAR_N = 'gear n'
GEAR_D = 'gear d'
INVALID_CMD = 'Invalid cmd'
STATUS = '?'
car_status = {
    'engine': STOP,
    'lights': LIGHTS_OFF,
    'break': BREAK_OFF,
    'gear': 'p',
    'hand break': 'on'}

gear_status = ['p', 'r', 'n', 'd']

def car_game():
    cmd: str
    while True:
        cmd = input("> ").lower()
        if car(cmd) == INVALID_CMD:
            print(f'Invalid cmd: {cmd}')
        elif cmd == QUIT or cmd == 'q':
            break



def process_start():
    global car_status
    if car_status["engine"] == START:
        print("car already started !")
    else:
        print("car started ....")
        car_status["engine"] = START
    return START


def process_stop():
    global car_status
    if car_status["engine"] == STOP:
        print("car already stopped !")
    elif car_status['lights'] == LIGHTS_ON:
        print ('Lights already on !')
    else:
        print("car stopped ....")
        car_status["engine"] = STOP
    return STOP


def process_help():
    print("""
start ......... : start the car
stop  ......... : stop the car (engine started and lights off)
help  ......... : print this help
Lights on|off . : switch lights on or off
break on|off .. : break on or off
gear P|R|N|D .. : switch gear
hand break .... : hand break on|off
?  ............ : display status
quit, q ....... : quit
    """)
    return HELP


def process_lights_on():
    if car_status["lights"] == LIGHTS_ON:
        print ('lights already on !')
    else:
        print('lights switched on')
        car_status["lights"] = LIGHTS_ON


def process_lights_off():
    if car_status["lights"] == LIGHTS_OFF:
        print('lights already off !')
    else:
        print('lights switched off')
        car_status["lights"] = LIGHTS_OFF


def process_display_status():
    print (car_status)


def process_quit():
    if car_status["lights"] == LIGHTS_ON:
        print ('lights still on !')
        return False
    return QUIT


def process_break_off():
    if car_status["break"] == BREAK_OFF:
        print('Breaks already off !')
    else:
        print('Breaks switched off')
        car_status['break'] = BREAK_OFF
    process_display_status()

def process_break_on ():
    if car_status["break"] == BREAK_ON:
        print('Breaks already on !')
    else:
        print('Breaks switched on')
        car_status['break'] = BREAK_ON
    process_display_status()


def process_break (on_off:str):
    if car_status["break"] == BREAK_ON and on_off == 'on':
        print('Breaks already on !')
    else:
        print('Breaks switched on')
        car_status['break'] = BREAK_ON
    process_display_status()

def process_gear_p():
    return process_gear('p')


def process_gear_n():
    return process_gear('n')


def process_gear_d():
    return process_gear('d')


def process_gear_r():
    return process_gear('r')


def process_gear(gear:str):
    if valid_gear_move(gear) == -1:
        print(f'gear already on {gear.upper()}  !')
    elif valid_gear_move(gear) == -2:
        print(f'Invalid move {gear.upper()}  !')
    elif valid_gear_move(gear) == -3:
        print(f'Invalid move sequence from {car_status[GEAR].upper()} to {gear.upper()}  !')
    elif valid_gear_move(gear) == -4:
        print(f'cannot move gear while stopping')
    else:
        car_status[GEAR]= gear
        process_display_status()


def valid_gear_move (new_stat:str):
    current_stat:str = car_status[GEAR]
    current_stat_index:int = gear_status.index(current_stat)
    new_stat_index:int = gear_status.index(new_stat)

    if current_stat == new_stat:
        return -1   #print(f'gear already on {new_stat.upper}  !')
    elif new_stat not in gear_status:
        return -2   #print(f'Invalid move {new_stat.upper}  !')
    elif (current_stat == 'p' and  new_stat != 'r') or \
            (current_stat == 'd' and new_stat != 'n') or \
            (new_stat_index != current_stat_index + 1 and
                new_stat_index != current_stat_index -1):
        return -3   #print(f'Invalid move sequence from {current_stat.upper()} to {new_stat.upper}  !')
    elif car_status[GEAR] != START:
        return -4   # cannot move gear while stopped
    else:
        return 0 # valid


def car(cmd):
    switcher = {
        START: process_start,
        STOP: process_stop,
        HELP: process_help,
        QUIT: process_quit,
        'q' : process_quit,
        LIGHTS_ON: process_lights_on,
        LIGHTS_OFF: process_lights_off,
        STATUS: process_display_status,
        BREAK_ON: process_break_on,
        BREAK_OFF: process_break_off,
        GEAR_P: process_gear_p,
        GEAR_R: process_gear_r,
        GEAR_D: process_gear_d,
        GEAR_N: process_gear_n
    }
    #func = switcher.get(cmd, lambda: "Invalid command")
    func = switcher.get(cmd, -1)
    if func != -1:
        return func()
    else:
        return INVALID_CMD


car_game()
