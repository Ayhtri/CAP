import requests

class BasePuller:

    def __init__(self, *args, **kwargs):

        pass


class WebPuller(BasePuller):

    def __init__(self, url, method, params=None):

        self.url = url
        self.method = method.lower()
        self.params = params
        self.pulled = None

    def pull(self):

        if self.method == "get":
            self.pulled = requests.get(self.url, params=self.params).text

        elif self.method == "post":
            self.pulled = requests.post(self.url, data=self.params).text

        return self.pulled

