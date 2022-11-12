from local import Local

class MoreThanOneRobotException(Exception):
    def __str__(self):
        return 'It is impossible to create another one robot!'

class SingletonRobot(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonRobot, cls).__call__(*args, **kwargs)
            return cls._instances[cls]
        raise MoreThanOneRobotException    

class Robot(metaclass=SingletonRobot):
    def __init__(self):
        self._ = Local(Local.get_default_lang())
        self._serial_number = 'АА001221-56'
        self._name = '-'
        self._place = '-'
        self._functionality = '-'

    def __str__(self):
        def formating(phrases : str):
            if phrases == '-':
                return '-'

            phrases = phrases.split('\n')
            text = []
            for phrase in phrases:
                text.append(self._.traslate(phrase))
            text = ',\n'.join(text)
            if '"' not in text:
                return text.capitalize()
            return text

        return f'{formating("serial number")}: {self._serial_number}.\n' + \
                f'{formating("name")}: {formating(self._name)}.\n' + \
                f'{formating("location")}: {formating(self._place)}.\n' + \
                f'{formating("functionality")}: {formating(self._functionality)}.\n'

class RobotV(Robot):
    def __init__(self, lang : Local = None):
        super().__init__()
        if lang != None:
            self._ = lang
        self._name = 'v'
        self._place = 'factory'

class RobotDecorator(Robot):
    def __init__(self, robot, lang : Local = None):
        super().__init__()
        if lang != None:
            self._ = lang
        self._robot = robot

class RobotVita(RobotDecorator):
    def __init__(self, robot, lang : Local = None):
        super().__init__(robot, lang)
        self._name = 'vita'
        self._place = '"OOO Koshmarik"'
        self._functionality = 'building houses\nshed building'

class RobotVitaliy(RobotDecorator):
    def __init__(self, robot, lang : Local = None):
        super().__init__(robot, lang)
        self._name = 'vitaliy'
        self._place = '"OOO Koshmarik"'
        self._functionality = robot._functionality + '\nadding floors to a building\ndemolition of the upper floor of the building'