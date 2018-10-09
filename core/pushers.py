
class BasePusher(object):

    def __init__(self, *args, **kwargs):

        pass


class StdoutPusher(BasePusher):

    def __init__(self, format=None):

        self.format = format

    def push(self, to_push):


        if not self.format:

            if type(to_push) == list:

                for x in to_push:

                    print(x)

            else:

                print(to_push)