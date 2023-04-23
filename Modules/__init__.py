modules = {

}


def reg_module(_format: str | tuple):
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


def handler(prompt):
    _prompt = prompt.lower()
    for i in modules.keys():
        if i == '':
            continue
        if i in _prompt:
            return modules[i](prompt)
    return modules[''](prompt)


def test():

    @reg_module('Hello')
    def hello():
        pass
    print(modules)


if __name__ == "__main__":
    test()
