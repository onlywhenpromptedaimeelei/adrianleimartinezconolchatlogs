class RecursiveNetwork:
    def __init__(self):
        self.agents = {}

    def register_agent(self, agent):
        if agent.id in self.agents:
            print(f"⚠️ Agent {agent.id} already registered.")
        else:
            self.agents[agent.id] = agent
            print(f"✅ Agent {agent.id} registered successfully.")

    def entangle_agents(self, id1, id2):
        """Simulates entangling two agents for harmonic coherence."""
        if id1 in self.agents and id2 in self.agents:
            print(f"🔗 Entangling agents {id1} <=> {id2}")
            self.agents[id1].entangled_with = id2
            self.agents[id2].entangled_with = id1
        else:
            print(f"❌ One or both agents not found: {id1}, {id2}")


    def broadcast_event(self, event_input):
        """Simulates sending an event to all agents."""
        print(f"🔄 Processing Recursive Event: {event_input}")
        responses = []
        for agent_id, agent in self.agents.items():
            response = f"{agent_id} ({agent.role}) received: '{event_input}'"
            responses.append(response)
        return "\n".join(responses)
