class Agent:
    total_agents = 0

    def __init__(self, code_name: str, clearance_level: int):
        self.code_name = code_name
        self._clearance_level = clearance_level
        Agent.total_agents += 1

    def report(self):
        print(f"Agent {self.code_name} reporting. Clearance Level: {self._clearance_level}")

    def get_clearance_level(self):
        return self._clearance_level

    def set_clearance_level(self, level: int):
        if 1 <= level <= 10:
            self._clearance_level = level
        else:
            print(" Clearance level must be between 1 and 10.")

    @staticmethod
    def get_total_agents():
        print(f"Total agents created: {Agent.total_agents}")



class FieldAgent(Agent):
    def __init__(self, code_name: str, clearance_level: int, region: str):
        super().__init__(code_name, clearance_level)
        self.region = region

    def report(self):
        print(f"Field Agent {self.code_name} reporting from {self.region}. Clearance: {self._clearance_level}")



class CyberAgent(Agent):
    def __init__(self, code_name: str, clearance_level: int, specialty: str):
        super().__init__(code_name, clearance_level)
        self.specialty = specialty

    def report(self):
        print(f"Cyber Agent {self.code_name}, Specialty: {self.specialty}, Clearance: {self._clearance_level}")



# class AgencyDirector:
#     _instance = None
#
#     def __new__(cls, name):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#             cls._instance.name = name
#         return cls._instance
#
#     def __repr__(self):
#         print(f"Agency Director: {self.name}")