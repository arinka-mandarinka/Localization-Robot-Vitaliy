import shutil
import os

from progress_bar import ProgressBar
from local import Local
from robot import RobotV, RobotVita, RobotVitaliy

def print_page(title : str, text : str, continue_text : str):
    width = shutil.get_terminal_size().columns
    text = title.upper() + '\n\n' + str(text)
    for line in (text + '\n\n' + continue_text).split('\n'):
        print(line.center(width))
    input()
    os.system('cls')

def input_lang():
    _ = Local(Local.get_default_lang())

    input_text = _.traslate('choose language').capitalize()
    error_text = _.traslate('the language you selected does not exist in the database').capitalize() + \
                            '! ' + _.traslate('try again').capitalize() + '...'
    langs = _.get_langs_list()

    print(input_text + ':')
    for i in range(len(langs)):
        print(str(i + 1) + ' - ' + langs[i])

    while True:
        num = int(input('- '))

        if num < 1 or num > len(langs):
            print('\033[31m{}\033[0m'.format(error_text))
            continue
        
        return Local(langs[num - 1])

if __name__ == '__main__':
    _ = input_lang()

    def formating(*phrases):
        text = []
        for phrase in phrases:
            text.append(_.traslate(phrase))
        return ' '.join(text).capitalize()

    createRobotMsg = formating('create of robot') + ':'
    robotTrainMsg = formating('robot training') + ':'
    robotOperationMsg = formating('robot operation') + ':'
    chsRobotCreateMsg = formating('characteristics of the robot', 
                                    'after creation') + ':'
    chsRobotPrimEdMsg = formating('characteristics of the robot',
                                    'after primary education') + ':'
    chsRobotOperationMsg = formating('characteristics of the robot',
                                    'after operation') + ':'
    continueMsg = formating('press enter for continue') + '...'
    doneMsg = formating('completed')

    ProgressBar(prefix=createRobotMsg, suffix=doneMsg)
    robotV = RobotV(lang=_)
    print_page(title=chsRobotCreateMsg, 
                text=robotV,
                continue_text=continueMsg)
    
    ProgressBar(prefix=robotTrainMsg, suffix=doneMsg)
    robotVita = RobotVita(robotV, lang=_)
    print_page(title=chsRobotPrimEdMsg, 
                text=robotVita,
                continue_text=continueMsg)
    
    ProgressBar(prefix=robotOperationMsg, suffix=doneMsg)
    robotVitaliy = RobotVitaliy(robotVita, lang=_)
    print_page(title=chsRobotOperationMsg, 
                text=robotVitaliy,
                continue_text=continueMsg)