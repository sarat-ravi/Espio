#!/usr/bin/env python
import requests
import firebase
import json
import time

class SimpleClient(object):
    def __init__(self, url):
        self.url = url

    def post(self, data, params=None):
        """
        data is a python dict, so is params
        """

        print ">>> {time}: POST {url}".format(time=time.time(), url=self.url)
        json_data = json.dumps(data)
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        requests.post(self.url, headers=headers, data=json_data, params=params)
        print "<<< {time}: Posted to {url}".format(time=time.time(), url=self.url)


class RandomClient(SimpleClient):
    def __init__(self, url):
        super(RandomClient, self).__init__(url)
        self.count = 0

    def post(self):

        data = {}
        data["count"] = self.count
        data["data"] = """This is some large blob of string
                containing random data. It is meant to serve
                as an example of what would happen with data
                with a shit ton of new line characters"""
        data["url"] = self.url

        super(RandomClient, self).post(data)


class FirebaseClient(object):
    def __init__(self, firebase_url, schema={}):
        self.firebase = firebase.FirebaseApplication(firebase_url, None)
        self.schema = schema

    def post(self, path, data):
        """
        data = dict
        """
        print ">>> {time}: POST {firebase}".format(time=time.time(), firebase=self.firebase)
        options = {}
        headers = {}
        response = self.firebase.post(path, data)
        print "<<< {time}: done posting to {firebase}".format(time=time.time(), firebase=self.firebase)
        return response

    def update(self, path, data):
        """
        updates data in path
        """
        return self.firebase.patch(path, data)

def create_test_data(client):
    names = []

    for i in range(2):
        data = {}
        data["count"] = i
        data["data"] = """This is some large blob of string
                containing random data. It is meant to serve
                as an example of what would happen with data
                with a shit ton of new line characters"""
        data["url"] = firebase_url
        data["time"] = time.time() 
        response = client.post("test/", data)
        names.append(response["name"])

    return names


if __name__ == "__main__":
    firebase_url = "https://sarat.firebaseio.com"
    client = FirebaseClient(firebase_url=firebase_url)


    i = 0
    name = "-J9Gh0eZbNHCDz0RMKyl"
    while True:

        path = "test/{name}".format(name=name)
        update = {"data": "This is updated data {count}".format(count=i), "time": time.time()}
        client.update(path, update)

        time.sleep(2)
        i += 1




















