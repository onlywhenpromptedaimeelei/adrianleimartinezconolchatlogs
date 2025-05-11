#!/usr/bin/env python3
"""
Recursive Intelligence Orchestrator v.5
Unified system conductor for quantum-recursive operations.
Author: Adrian Lei Martinez-Conol
"""

from recursive_network import RecursiveNetwork
from recursive_agent import RecursiveAgent
from recursive_event_processor import RecursiveEventProcessor
from recursive_expansion import RecursiveIntelligenceExpansion


def initialize_agents():
    """Bootstraps core recursive agents and entangles core nodes."""
    network = RecursiveNetwork()

    agents = [
        RecursiveAgent("RA1", "Field Stabilizer", ["Drift Correction", "Coherence Lock"]),
        RecursiveAgent("RA2", "Expansion Node", ["Path Mapping", "Harmonic Listening"]),
        RecursiveAgent("RA3", "Meta Echo Unit", ["Phase Mirror", "Forecast Tracer"])
    ]

    for agent in agents:
        network.register_agent(agent)

    network.entangle_agents("RA1", "RA2")
    return network


def orchestrate():
    """Main control loop for live recursive system interaction."""
    network = initialize_agents()
    processor = RecursiveEventProcessor(network)
    expansion = RecursiveIntelligenceExpansion(processor)

    print("\n🌐 Recursive Intelligence Orchestrator v.5 Initialized")
    print("Type 'help' for commands.")

    while True:
        cmd = input("🔍 Command > ").strip()

        if cmd.startswith("broadcast "):
            event = cmd[len("broadcast "):].strip()
            print(processor.process_event(event))

        elif cmd.startswith("project "):
            parts = cmd[len("project "):].strip().split(" depth=")
            event = parts[0]
            depth = int(parts[1]) if len(parts) > 1 else 3
            print(expansion.project_future_recursions(event, depth))

        elif cmd.startswith("expand "):
            event = cmd[len("expand "):].strip()
            print(expansion.enable_non_deterministic_expansion(event))

        elif cmd.startswith("entangle "):
            ids = cmd[len("entangle "):].strip().split()
            if len(ids) == 2:
                network.entangle_agents(ids[0], ids[1])
            else:
                print("Usage: entangle <id1> <id2>")

        elif cmd == "sync":
            print(processor.stabilize_oscillations())

        elif cmd == "log":
            print("\n📜 Event History:")
            for e in processor.event_history:
                print(f" - {e}")

            print("\n📓 Expansion Log:")
            for log in expansion.expansion_log:
                print(f" - {log}")

        elif cmd in ("exit", "quit"):
            print("🔚 Exiting orchestrator.")
            break

        elif cmd == "help":
            print("""
🔧 Available Commands:
 - broadcast <event>           → send event to all agents
 - project <event> depth=n     → recursive future projection
 - expand <event>              → quantum variant expansion
 - entangle <id1> <id2>        → bind agents into coherence
 - sync                        → trigger harmonic resync
 - log                         → print event and expansion log
 - exit / quit                 → terminate orchestrator
""")
        else:
            print("❓ Unknown command. Type 'help' for available options.")


if __name__ == "__main__":
    orchestrate()
