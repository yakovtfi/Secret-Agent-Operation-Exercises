from modle.Agent import Agent, FieldAgent, CyberAgent
from modle.mission import Mission, agents_report


a1 = Agent("C7", 7)
a2 = FieldAgent("C8", 8, "Europe")
a3 = CyberAgent("C9", 9, "Hacking")

mission = Mission("Iron swords", "Israel")
mission.assign_agent(a2)
mission.brief()


agents_report([a1, a2, a3])

Agent.get_total_agents()


