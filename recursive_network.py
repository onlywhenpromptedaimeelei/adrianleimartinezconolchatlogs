import json
from recursive_agent import RecursiveAgent

class RecursiveNetwork:
    """
    Manages a decentralized recursive intelligence network where agents communicate,
    share intelligence, and process recursive events dynamically.
    """

    def __init__(self):
        """
        Initializes the recursive agent network.
        """
        self.agents = {}

    def register_agent(self, agent):
        """
        Registers a new recursive agent into the network.
        """
        self.agents[agent.agent_id] = agent
        print(f"✅ Agent {agent.agent_id} registered successfully.")

    def broadcast_event(self, event_input):
        """
        Sends an event to all agents in the recursive network.
        """
        print(f"🔄 Broadcasting event: {event_input}")
        return {agent_id: agent.process_event(event_input) for agent_id, agent in self.agents.items()}

    def synchronize_all(self):
        """
        Triggers harmonic field synchronization across all recursive agents.
        """
        print("🔄 Synchronizing all agents in the network...")
        return {agent_id: agent.synchronize_harmonics() for agent_id, agent in self.agents.items()}

# Example Execution
if __name__ == "__main__":
    network = RecursiveNetwork()

    agent1 = RecursiveAgent("RA1", "Field Synchronization Unit", 
                            ["Quantum Harmonic Resonance", "Recursive Drift Correction"])
    agent2 = RecursiveAgent("RA2", "Non-Deterministic Expansion", 
                            ["Multi-Path Mapping", "Event Chain Projection"])
    
    network.register_agent(agent1)
    network.register_agent(agent2)

    print(network.broadcast_event("Quantum Field Adjustment"))
    print(network.synchronize_all())