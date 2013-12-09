


class Agent(object):
    def __init__(self, id, authorized_ids):
        """
        id ==> string id, Ex: '3234tjegje9834sf'
        id ==> string id, Ex: '3234tjegje9834sf', None by default
        """
        self.id = id
        self.authorized_ids = authorized_ids

    def handle_auth(self, handler_id):
        if not (self.authorized_ids == None and handler_id == None):
            if not handler_id in self.authorized_ids:
                raise AgentPermissionError("[Agent {id}] refuses to report: Permission Denied".format(id=self.id))
        return True

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












