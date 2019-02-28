def loop_thru_messages(messages):
    value = ''
    for message in messages:
        value += '\r\n' + str(message)
    return str(value)


def dictionary_printer(dictionary):
    value = ''
    for key in dictionary:
        value += '\r\n%s - %s' % (key, dictionary[key])
    return str(value)


class LoopThruMessagesException(Exception):

    def __init__(self, messages):
        self.value = ''
        for message in messages:
            self.value += '\r\n' + str(message)

    def __str__(self):
        return str(self.value)
