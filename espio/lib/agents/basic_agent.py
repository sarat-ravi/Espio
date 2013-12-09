from espio.agents import Agent
from espio.common.exceptions import AgentPermissionError


class BasicAgent(Agent):
    def __init__(self, id, authorized_ids=None):
        super(BasicAgent, self).__init__(id=id, authorized_ids=authorized_ids)
        self.data = {}

    def report(self, handler_id=None, query=None):

        self.handle_auth(handler_id=handler_id)

        # if no query specified, return everything
        if not query: return self.data

        # if query specified, only return the specific data
        if query in self.data: return self.data[query]
        else:
            raise KeyError("[Agent {id}] unable to report {query}: Key not found".format(id=self.id, query=query))

    def record(self, data):
        self.data.update(data)

    def flush(self):
        self.data = {}

