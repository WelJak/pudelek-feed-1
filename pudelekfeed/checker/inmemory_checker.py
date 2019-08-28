from .checker import Checker

class InMemoryChecker(Check):
    def __init__(self, entries):
        self.entries = list(entries)

    def check(self, entry):
        if entry in self.entries:
            print('message was already sent')
            return False
        else:
            print('message has not been sent yet')
            return True

    def mark(self, entry):
        self.entries.append(entry)
        print('message added to list of already sent messages')


