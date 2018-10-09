from core import pullers, parsers, pushers
import inspect
import datetime

class Collector:

    AVAILABLE_PULLERS = inspect.getmembers(pullers, inspect.isclass)
    AVAILABLE_PARSERS = inspect.getmembers(parsers, inspect.isclass)
    AVAILABLE_PUSHERS = inspect.getmembers(pushers, inspect.isclass)

    def __init__(self, freq="24"):

        self.freq = freq
        self.last_run = None
        self.puller = None
        self.parser = None
        self.pusher = None

    def is_ready(self):

        if not self.last_run:
            return True

        elif datetime.datetime.now() >= (self.last_run + datetime.timedelta(hours=self.freq)):
            return True

        else:
            return False

    def add_puller(self, puller_class, *args, **kwargs):

        for name, obj in self.AVAILABLE_PULLERS:

            if puller_class == name.lower():
                self.puller = obj(*args, **kwargs)
                break

        if not self.puller:
            return "{} is not an available class".format(puller_class)

    def add_parser(self, parser_class, *args, **kwargs):

        for name, obj in self.AVAILABLE_PARSERS:

            if parser_class == name.lower():
                self.parser = obj(*args, **kwargs)
                break

        if not self.parser:
            return "{} is not an available class".format(parser_class)

    def add_pusher(self, pusher_class, *args, **kwargs):

        for name, obj in self.AVAILABLE_PUSHERS:

            if pusher_class == name.lower():
                self.pusher = obj(*args, **kwargs)
                break

        if not self.pusher:
            return "{} is not an available class".format(pusher_class)

    def collect(self):

        pulled = self.puller.pull()
        pulled_at = datetime.datetime.now()

        parsed = self.parser.parse(pulled)
        pushed = self.pusher.push(parsed)

        self.last_run = pulled_at