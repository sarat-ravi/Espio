import nose
from espio.agents import BasicAgent
from espio.handlers import BasicHandler
from espio.common.exceptions import AgentPermissionError, HandlerPermissionError

__test__ = True

class TestHandlers(object):
    """
    Tests espio
    """

    @classmethod
    def setup_class(cls):
        paranoid_agents = []

        agent = BasicAgent(id="paranoid_agent1", authorized_ids=["cia", "ring", "god"])
        agent.record({"one": 1, "type": "paranoid", "ring": True})
        paranoid_agents.append(agent)

        agent = BasicAgent(id="paranoid_agent2", authorized_ids=["nsa", "ring", "god"])
        agent.record({"two": 2, "type": "paranoid", "ring": True})
        paranoid_agents.append(agent)

        agent = BasicAgent(id="paranoid_agent3", authorized_ids=["nsa", "cia", "god"])
        agent.record({"three": 3, "type": "paranoid"})
        paranoid_agents.append(agent)

        cia = BasicHandler(id="cia", authorized_ids=["chuck", "sarat"])
        cia.add_subordinate(subordinate=paranoid_agents[0])
        cia.add_subordinate(subordinate=paranoid_agents[1])

        nsa = BasicHandler(id="cia", authorized_ids=["snowden", "sarat"])
        nsa.add_subordinate(subordinate=paranoid_agents[1])
        nsa.add_subordinate(subordinate=paranoid_agents[2])

        ring = BasicHandler(id="cia", authorized_ids=["shaw", "sarat"])
        nsa.add_subordinate(subordinate=paranoid_agents[0])
        nsa.add_subordinate(subordinate=paranoid_agents[2])

        god = BasicHandler(id="god", authorized_ids=["sarat"])
        god.add_subordinate(subordinate=paranoid_agents[0])
        god.add_subordinate(subordinate=paranoid_agents[1])
        god.add_subordinate(subordinate=paranoid_agents[2])

        sarat = BasicHandler(id="sarat", authorized_ids=[])
        sarat.add_subordinate(subordinate=cia)
        sarat.add_subordinate(subordinate=nsa)
        sarat.add_subordinate(subordinate=ring)
        sarat.add_subordinate(subordinate=god)

        TestHandlers.paranoid_agents = paranoid_agents
        TestHandlers.cia = cia
        TestHandlers.nsa = nsa
        TestHandlers.ring = ring
        TestHandlers.god = god
        TestHandlers.sarat = sarat

    
    def test_god(self):
        """
        Test if god can indeed get all possible answers
        """
        expected_result = {}
        expected_result["paranoid_agent1"] = {"one": 1, "type": "paranoid", "ring": True}
        expected_result["paranoid_agent2"] = {"two": 2, "type": "paranoid", "ring": True}
        expected_result["paranoid_agent3"] = {"three": 3, "type": "paranoid"}

        result = TestHandlers.god.report(handler_id="sarat")
        assert expected_result == result

    def test_god_with_query(self):
        """
        Test if god can indeed get all possible answers for a query
        """
        expected_result = {}
        expected_result["paranoid_agent1"] = {"ring": True}
        expected_result["paranoid_agent2"] = {"ring": True}

        result = TestHandlers.god.report(handler_id="sarat", query="ring")
        assert expected_result == result, str(result)

    def test_cia(self):
        """
        Test if cia is only able to get information from subordinates 
        sworn to cia
        """
        expected_result = {}
        expected_result["paranoid_agent1"] = {"one": 1, "type": "paranoid", "ring": True}

        result = TestHandlers.cia.report(handler_id="sarat")
        assert expected_result == result, str(result)





















