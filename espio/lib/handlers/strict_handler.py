from espio.handlers import Handler
from collections import defaultdict
import time


class StrictHandler(Handler):
    def __init__(self, id, secret):
        """
        id ==> string id, Ex: '3234tjegje9834sf'
        secret ==> string secret, Ex: '3234tjegje9834sf', None by default
        """
        super(StrictHandler, self).__init__(id=id, secret=secret)
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

        for sub_id, subordinate in self.subordinates.items():
            if not sub_id in report:
                report[sub_id] = {}
            if query:
                if not query in report[sub_id]: report[sub_id][query] = {}
                report[sub_id][query] = subordinate.report(secret=self.secret, query=query)
            else:
                report[sub_id] = subordinate.report(secret=self.secret)

        return report


    def record(self, data):
        """
        records the given data such that agent can later 'report'
        """
        raise NotImplementedError("StrictHandler.record function not implemented")

    def flush(self):
        """
        oh no!!! StrictHandler caught by enemy operatives!!
        flush() will delete all state immediately
        agent will still be functional though
        """
        raise NotImplementedError("StrictHandler.flush function not implemented")












