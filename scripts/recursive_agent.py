class RecursiveAgent:
    def __init__(self, agent_id, role, capabilities):
        self.id = agent_id
        self.role = role
        self.capabilities = capabilities
        self.entangled_with = None

