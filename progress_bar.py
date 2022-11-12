import time
import os

class ProgressBar():
    def __init__(self, prefix = '', suffix = 'Выполнено', execTimeOneIter = 0.08):
        os.system('cls')
        items = list(range(0, 57))
        l = len(items)
        self.printProgressBar(0, l, prefix = prefix, suffix = suffix, length = 50)
        for i, item in enumerate(items):
            time.sleep(execTimeOneIter)
            self.printProgressBar(i + 1, l, prefix = prefix, suffix = suffix, length = 50)
        os.system('cls')

    @staticmethod
    def printProgressBar (iteration, total, prefix, suffix, decimals = 1, length = 100, fill = '█', printEnd = "\r"):
        """
        Вызывать в цикле для создания прогресс бара
        @params:
            iteration   - Обязательный  : текущая итерация (Int)
            total       - Обязательный  : общее количество итераций (Int)
            prefix      - Опциональный  : префиксная строка (Str)
            suffix      - Опциональный  : суффиксная строка (Str)
            decimals    - Опциональный  : положительное число десятичных знаков в процентах выполнения (Int)
            length      - Опциональный  : количество символов прогресс бара (Int)
            fill        - Опциональный  : символ заполнения прогресс бара (Str)
            printEnd    - Опциональный  : последний символ (e.g. "\r", "\r\n") (Str)
        """
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{prefix} |{bar}| ' + '\033[92m{}\033[0m'.format(f'{percent}%') + f' {suffix}', end = printEnd)
        # Print New Line on Complete
        if iteration == total: 
            print()