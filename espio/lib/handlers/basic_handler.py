from espio.handlers import StrictHandler
from espio.agents import Agent
from collections import defaultdict
from espio.common.exceptions import HandlerPermissionError
import time


class BasicHandler(StrictHandler):
    def __init__(self, id, authorized_ids):
        super(BasicHandler, self).__init__(id=id, authorized_ids=authorized_ids)


    def generate_sub_report(self, subordinate, query):
        if not subordinate.authorized_ids == None:
            if not self.id in subordinate.authorized_ids:
                return None

        return super(BasicHandler, self).generate_sub_report(subordinate=subordinate, query=query)







