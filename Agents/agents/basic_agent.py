from agents import Agent


class BasicAgent(Agent):
    def __init__(self, id, secret=None):
        super(BasicAgent, self).__init__(id=id, secret=secret)
        self.data = {}

    def report(self, secret=None, query=None):

        if not secret == self.secret:
            raise Exception("[Agent {id}] refuses to report: Permission Denied".format(id=self.id))

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

