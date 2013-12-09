from espio.handlers import Handler
from espio.agents import Agent
from collections import defaultdict
from espio.common.exceptions import HandlerPermissionError
import time


class StrictHandler(Handler):
    def __init__(self, id, authorized_ids):
        """
        id ==> string id, Ex: '3234tjegje9834sf'
        secret ==> string secret, Ex: '3234tjegje9834sf', None by default
        """
        super(StrictHandler, self).__init__(id=id, authorized_ids=authorized_ids)
        self.subordinates = {}
        self.subordinate_meta = {}


    def add_subordinate(self, subordinate):
        # add subordinate
        key = subordinate.id
        self.subordinates[key] = subordinate

        # store meta related to subordinate
        time_added = time.time()
        self.subordinate_meta[key] = {}
        self.subordinate_meta[key]["joined"] = time_added


    def handle_auth(self, handler_id):
        if not (self.authorized_ids == None and handler_id == None):
            if not handler_id in self.authorized_ids:
                raise HandlerPermissionError("[Handler {id}] refuses to report: Permission Denied".format(id=self.id))
        return True

    
    # TODO: This is the ugliest function ever implemented, must cleanup logic
    def generate_report(self, query):
        report = {}

        # TODO: clean up this code
        for sub_id, subordinate in self.subordinates.items():

            if query:
                
                sub_report = self.generate_sub_report(subordinate=subordinate, query=query)

                if sub_report:
                    if not sub_id in report: report[sub_id] = {}
                    if isinstance(subordinate, Agent):
                        if not query in report[sub_id]: report[sub_id][query] = {}
                        report[sub_id][query] = sub_report 
                    else:
                        report[sub_id].update(sub_report)
            else:
                sub_report = self.generate_sub_report(subordinate=subordinate, query=None) 
                if sub_report:
                    if not sub_id in report: report[sub_id] = {}
                    report[sub_id] = sub_report 

        return report


    def generate_sub_report(self, subordinate, query=None):
        try:
            sub_report = subordinate.report(handler_id=self.id, query=query)
        except KeyError as e:
            sub_report = None
        finally:
            return sub_report


    def report(self, handler_id, query=None):

        self.handle_auth(handler_id=handler_id)
        return self.generate_report(query=query)


    def flush(self):
        """
        oh no!!! StrictHandler caught by enemy operatives!!
        flush() will delete all state immediately
        handler will still be functional though
        """

        self.subordinate = {}
        self.subordinate_meta = {}












