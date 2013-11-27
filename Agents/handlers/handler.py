


class Handler(object):
    def __init__(self, id, secret):
        """
        id ==> string id, Ex: '3234tjegje9834sf'
        secret ==> string secret, Ex: '3234tjegje9834sf', None by default
        """
        self.id = id
        self.secret = secret
        self.subordinates = {}

    def report(self, secret, query=None):
        """
        report any data agent has to whoever asks for it
        the handler who asks has established a secret with you right?
        """
        raise NotImplementedError("Handler.report function not implemented")

    def record(self, data):
        """
        records the given data such that agent can later 'report'
        """
        raise NotImplementedError("Handler.record function not implemented")

    def flush(self):
        """
        oh no!!! Handler caught by enemy operatives!!
        flush() will delete all state immediately
        agent will still be functional though
        """
        raise NotImplementedError("Handler.flush function not implemented")












