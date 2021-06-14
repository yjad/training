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
# car_status = {
#     'engine': STOP,
#     'lights': LIGHTS_OFF,
#     'break': BREAK_OFF,
#     'gear': 'p',
#     'hand break': 'on'}


class Car:
    def __init__(self):
        self.engine_state = STOP
        self.lights_state =  LIGHTS_OFF
        self.break_state = BREAK_ON
        self.gear_state = 'p'

    def car_started(self):
        return self.engine_state

    def start_car(self,cmd_str):
        if self.engine_state == START:
            print("car already started !")
        else:
            print("car started ....")
            self.engine_state = START
        self.display_car_status()
        return START


    def stop_car(self,cmd_str):
        if self.engine_state == STOP:
            print("car already stopped !")
            return -1
        elif self.lights_state == LIGHTS_ON:
            print ('Lights already on !')
            return -1
        else:
            print("car stopped ....")
            self.engine_state = STOP
        self.display_car_status()
        return STOP

    def process_lights(self, lights_on_off):
        if self.lights_state == lights_on_off:
            print('no change in the lights !')
        else:
            self.lights_state = lights_on_off
            print('lights switched on/off')
        self.display_car_status()

    def change_breaks(self, breaks_on_off):
        if self.break_state == breaks_on_off:
            print('No change in Breaks status !')
        else:
            self.break_state = breaks_on_off
            print('Breaks status changed')

        self.display_car_status()

    def valid_gear_move(self, new_stat: str):
        gear_status = ['p', 'r', 'n', 'd']
        current_stat = self.gear_state
        current_stat_index: int = gear_status.index(current_stat)
        new_stat_index: int = gear_status.index(new_stat)

        if current_stat == new_stat:
            return -1  # print(f'gear already on {new_stat.upper}  !')
        elif new_stat not in gear_status:
            return -2  # print(f'Invalid move {new_stat.upper}  !')
        elif (current_stat == 'p' and new_stat != 'r') or \
                (current_stat == 'd' and new_stat != 'n') or \
                (new_stat_index != current_stat_index + 1 and
                 new_stat_index != current_stat_index - 1):
            return -3  # print(f'Invalid move sequence from {current_stat.upper()} to {new_stat.upper}  !')
        elif self.engine_state != START:
            return -4  # cannot move gear while stopped
        else:
            return 0  # valid

    def change_gear(self, new_gear):
        new_gear = new_gear.split(' ')[1] # gear p --> p
        status = self.valid_gear_move(new_gear)
        if status == -1:
            print(f'gear already on {new_gear.upper()}  !')
        elif status == -2:
            print(f'Invalid move {new_gear.upper()}  !')
        elif status == -3:
            print(f'Invalid move sequence from {self.gear_state.upper()} to {new_gear.upper()}  !')
        elif status == -4:
            print(f'cannot move gear while stopping')
        else:
            self.gear_state = new_gear
            self.display_car_status()

    def display_car_status(self, cmd_str=''):
        print (f"""
engine : {self.engine_state} 
lights : {self.lights_state}
break : {self.break_state}
gear : {self.gear_state}
""")


def process_help(cmd_str):

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

def process_quit(cmd_str, car):
    if car.engine_state  == START:
        print ('quit with car running !')
        car.display_car_status()
        return False
    return QUIT

# def process_gear_p():
#     return process_gear('p')
#
#
# def process_gear_n():
#     return process_gear('n')
#
#
# def process_gear_d():
#     return process_gear('d')
#
#
# def process_gear_r():
#     return process_gear('r')
#
#
# def process_gear(gear:str):
#     pass


def car_action(cmd, car):
    #print (f'from car action: {cmd}')
    switcher = {
        START: car.start_car,
        STOP: car.stop_car,
        HELP: process_help,
        QUIT: process_quit,
        'q' : process_quit,
        LIGHTS_ON: car.process_lights,
        LIGHTS_OFF: car.process_lights,
        STATUS: car.display_car_status,
        BREAK_ON: car.change_breaks,
        BREAK_OFF: car.change_breaks,
        GEAR_P: car.change_gear,
        GEAR_R: car.change_gear,
        GEAR_D: car.change_gear,
        GEAR_N: car.change_gear,
    }
    #func = switcher.get(cmd, lambda: "Invalid command")
    #print ('before calling fun')
    func = switcher.get(cmd, -1)
    if func == process_quit:
        process_quit(cmd, car)
    elif func != -1:
        #print ('from switcher')
        return func(cmd)
    else:
        return INVALID_CMD

#----------------------------------------
# Execute
# ----------------------------------------
def run_car():
    car = Car()

    while True:
        #cmd = ""
        cmd = input("> ").lower()
        #print ('cmm: ', cmd)
        if car_action(cmd, car) == INVALID_CMD:
            print(f'Invalid cmd: {cmd}')
        elif cmd == QUIT or cmd == 'q':
            break


if __name__ != '__name__':
    run_car()