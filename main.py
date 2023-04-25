import Configuration
import Modules


def main():
    # Creating and initializing the configuration object
    config = Configuration.Config('local/Dorrin.conf')
    if not config.get('mode', 'prompts'):
        config.set('mode', group='prompts', value='max')

    runner = Modules.Modules(config)
    runner.loop(text=True, speech=False)


if __name__ == '__main__':
    main()
