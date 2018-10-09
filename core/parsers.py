

class BaseParser(object):

    def __init__(self, *args, **kwargs):

        pass


class SimpleList(BaseParser):

    def __init__(self, separator="\n", ignore="#", label=None, strip=True):

        self.separator = separator
        self.ignore = ignore
        self.label = label
        self.strip = strip

    def parse(self, text):

        separated_text = text.split(self.separator)

        if self.strip:
            separated_and_stripped_text = [x.strip() for x in separated_text]
            separated_text = separated_and_stripped_text

        separated_text = [x for x in separated_text if x and not x.startswith(self.ignore)]

        if not self.label:

            self.label = next(separated_text)

        return [{self.label: x} for x in separated_text]
