from espio.handlers import Handler
from espio.agents import Agent
from collections import defaultdict
import time


class BasicHandler(Handler):
    def __init__(self, id, secret):
        """
        id ==> string id, Ex: '3234tjegje9834sf'
        secret ==> string secret, Ex: '3234tjegje9834sf', None by default
        """
        super(BasicHandler, self).__init__(id=id, secret=secret)
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


    def report(self, secret, query=None):

        report = {}

        # TODO: clean up this code
        for sub_id, subordinate in self.subordinates.items():

            if query:

                try:
                    sub_report = subordinate.report(secret=self.secret, query=query)
                except KeyError as e:
                    sub_report = None

                if sub_report:
                    if not sub_id in report: report[sub_id] = {}
                    if isinstance(subordinate, Agent):
                        if not query in report[sub_id]: report[sub_id][query] = {}
                        report[sub_id][query] = sub_report 
                    else:
                        report[sub_id].update(sub_report)
            else:
                if not sub_id in report: report[sub_id] = {}
                report[sub_id] = subordinate.report(secret=self.secret)

        return report


    def flush(self):
        """
        oh no!!! BasicHandler caught by enemy operatives!!
        flush() will delete all state immediately
        handler will still be functional though
        """

        self.subordinate = {}
        self.subordinate_meta = {}












