
class LoopThruMessagesException(Exception):

    def __init__(self, messages):
        self.value = ''
        for message in messages:
            self.value += '\r\n' + str(message)

    def __str__(self):
        return str(self.value)
