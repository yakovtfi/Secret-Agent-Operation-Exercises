from modle.Agent import Agent

class Mission:
    def __init__(self, mission_name: str, target_location: str):
        self.mission_name = mission_name
        self.target_location = target_location
        self.assigned_agent = None

    def assign_agent(self, agent: Agent):
        self.assigned_agent = agent

    def brief(self):
        agent_name = self.assigned_agent.code_name if self.assigned_agent else "Unassigned"
        print(f"Mission: {self.mission_name}, Target: {self.target_location}, Agent: {agent_name}")


def agents_report(agents):
    for agent in agents:
        agent.report()