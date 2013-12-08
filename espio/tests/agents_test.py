import nose
from espio.agents import BasicAgent
from espio.handlers import BasicHandler
from espio.common.exceptions import AgentPermissionError, HandlerPermissionError

__test__ = True

class TestAgents(object):
    """
    Tests espio
    """

    @classmethod
    def setup_class(cls):
        agents = []

        agent = BasicAgent(id="agent1")
        agents.append(agent)

        agent = BasicAgent(id="agent2")
        agents.append(agent)

        agent = BasicAgent(id="agent3")
        agents.append(agent)

        paranoid_agents = []

        agent = BasicAgent(id="paronoid_agent1", authorized_ids=["cia", "ring", "god"])
        paranoid_agents.append(agent)

        agent = BasicAgent(id="paronoid_agent2", authorized_ids=["nsa", "ring", "god"])
        paranoid_agents.append(agent)

        agent = BasicAgent(id="paronoid_agent3", authorized_ids=["nsa", "cia", "god"])
        paranoid_agents.append(agent)

        TestAgents.agents = agents
        TestAgents.paranoid_agents = paranoid_agents

    def test_agent_permissions(self):
        """
        Test if you can ask shit to unsecure agents
        """
        try:
            for agent in TestAgents.agents:
                agent.report()
        except AgentPermissionError as e:
            raise e


    def test_paranoid_agent_permissions(self):
        """
        Testing if agents respond if an authorized handler asks
        """

        for paranoid_agent in TestAgents.paranoid_agents:
            paranoid_agent.report(handler_id="god")
        

    @nose.tools.raises(AgentPermissionError)
    def test_0_paranoid_agent_incorrect_permissions(self):
        """
        Testing if agents raise error if an unauthorized handler asks
        """

        for paranoid_agent in TestAgents.paranoid_agents:
            paranoid_agent.report(handler_id="asfasdfasfawesfadsfas")


    @nose.tools.raises(AgentPermissionError)
    def test_1_paranoid_agent_incorrect_permissions(self):
        """
        Testing if agents raise error if an unauthorized handler asks
        """

        for paranoid_agent in TestAgents.paranoid_agents:
            paranoid_agent.report(handler_id="cia")
        

    @nose.tools.raises(AgentPermissionError)
    def test_1_paranoid_agent_incorrect_permissions(self):
        """
        Testing if agents raise error if an unauthorized handler asks
        """

        for paranoid_agent in TestAgents.paranoid_agents:
            paranoid_agent.report(handler_id="nsa")


    @nose.tools.raises(AgentPermissionError)
    def test_1_paranoid_agent_incorrect_permissions(self):
        """
        Testing if agents raise error if an unauthorized handler asks
        """

        for paranoid_agent in TestAgents.paranoid_agents:
            paranoid_agent.report(handler_id="ring")



















