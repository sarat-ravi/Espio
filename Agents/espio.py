#!/usr/bin/env python

from agents import BasicAgent
from handlers import BasicHandler

def main():
    sarat = BasicAgent(id="sarat", secret="pass")
    sarat.record({"age": 21})
    sarat.record({"temperature": 97})

    jon = BasicAgent(id="jon", secret="pass")
    jon.record({"age": 26})
    jon.record({"height": 5.3})

    raj = BasicAgent(id="raj", secret="pass")
    raj.record({"height": 5.1})
    raj.record({"type": "bear"})


    cia = BasicHandler(id="cia", secret="pass")
    nsa = BasicHandler(id="nsa", secret="pass")
    god = BasicHandler(id="god", secret="pass")

    cia.add_subordinate(sarat) 
    cia.add_subordinate(jon) 

    nsa.add_subordinate(sarat) 
    nsa.add_subordinate(raj) 

    god.add_subordinate(cia)
    god.add_subordinate(nsa)

    cia.report(secret="pass")


    import IPython; IPython.embed()



if __name__ == "__main__":
    main()
