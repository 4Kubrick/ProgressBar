from progress.bar import Bar


class Subject:
    def __init__(self):
        self.__obs_list = []

    def add_observer(self, obs):
        self.__obs_list.append(obs)

    def notify(self, *args, **kwargs):
        with Bar('Processing..') as bar:
            for obs in self.__obs_list:
                obs.update(*args, **kwargs)
                bar.next()
