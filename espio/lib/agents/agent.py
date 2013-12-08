


class Agent(object):
    def __init__(self, id, authorized_ids):
        """
        id ==> string id, Ex: '3234tjegje9834sf'
        id ==> string id, Ex: '3234tjegje9834sf', None by default
        """
        self.id = id
        self.authorized_ids = authorized_ids

    def report(self, handler_id, query=None):
        """
        report any data agent has to whoever asks for it
        the handler who asks has established a secret with you right?
        """
        raise NotImplementedError("Agent.report function not implemented")

    def record(self, data):
        """
        records the given data such that agent can later 'report'
        """
        raise NotImplementedError("Agent.record function not implemented")

    def flush(self):
        """
        oh no!!! Agent caught by enemy operatives!!
        flush() will delete all state immediately
        agent will still be functional though
        """
        raise NotImplementedError("Agent.flush function not implemented")












