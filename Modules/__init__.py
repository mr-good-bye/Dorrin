import Configuration as c
import SpeechWork

modules = {

}


def reg_module(_format: str | tuple | list):
    if _format in modules.keys():
        raise ValueError(f"{_format} already exists in modules")

    def act_wrapper(func):
        if type(_format) is str:
            modules[_format] = func
        else:
            for _f in _format:
                modules[_f] = func

        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    return act_wrapper


from Modules import SampleModule
from Modules import TalkToYalm


class Modules:
    _modules = modules

    def __init__(self, config: c.Config):
        """
        :param config: Configuration.Config object of main config
        """
        self.config = config
        self.modules = Modules._modules

    def handle(self, prompt: str):
        # Extract possible module names from prompt
        _prompt = prompt.lower()
        samples = []
        for i in modules.keys():
            if i in _prompt:
                samples.append(i)

        # Get mode from config and choose correct module
        mode = self.config.get('mode', group='prompts', default='max')
        if mode == 'max':
            sample = max(samples, key=lambda x: len(x))
        elif mode == 'first':
            sample = ('', float('inf'))
            for s in samples:
                if s == '':
                    continue
                if s.find(s) < sample[1]:
                    sample = (s, s.find(s))
        else:
            raise ValueError(f"Invalid mode: {mode}")

        # Run chosen module
        return modules[sample](prompt)

    def loop(self, text=False, speech=True):
        """
        :param text:
        """
        prompt = ''
        while True:
            if text:
                prompt = input('> ')
            else:
                prompt = SpeechWork.recognise()
            if prompt in ['exit', 'quit', 'выход', 'выйти']:
                break
            if speech:
                print(SpeechWork.speak(self.handle(prompt)))
            else:
                print(self.handle(prompt))
