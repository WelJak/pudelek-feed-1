from pudlas.pudelekfeed.checker.checker import Checker


class InMemoryChecker(Checker):
    def __init__(self):
        self.entries = []

    def check(self, entry):
        if entry in self.entries:
            print('message: {} has been already sent'.format(entry))
            return False
        else:
            print('message: {} has not been sent yet'.format(entry))
            return True

    def mark(self, entry):
        self.entries.append(entry)
        print('message: {} has been added to list of already sent messages'.format(entry))
