from espio.agents import Agent
from espio.common.exceptions import AgentPermissionError
import time
import firebase


class FirebaseAgent(Agent):
    def __init__(self, id, firebase_url, authorized_ids=None):
        super(FirebaseAgent, self).__init__(id=id, authorized_ids=authorized_ids)

        self.firebase_url = firebase_url
        self.firebase = firebase.FirebaseApplication(firebase_url, None)

        meta = {}
        meta["created"] = time.time()
        meta["type"] = self.__class__.__name__
        self.firebase.put("agents/{id}".format(id=id), "meta", meta)

    def report(self, handler_id=None, query=None):
        self.handle_auth(handler_id=handler_id)
        
        path = 'agents/{id}'.format(id=self.id)
        if query: path += '/{query}'.format(query=query)

        data = self.firebase.get(path, '')
        return data

    def record(self, data):
        path = 'agents/{id}'.format(id=self.id)
        self.firebase.patch(path, data)


