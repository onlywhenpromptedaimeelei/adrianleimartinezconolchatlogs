import random

class RecursiveIntelligenceExpansion:
    def __init__(self):
        self.projection_log = []

    def project_future_recursions(self, event_input, depth=3):
        """Simulates deterministic projection of recursive futures."""
        print(f"🔮 Projecting future paths for: '{event_input}' to depth {depth}")
        projections = [f"{event_input} > echo:{i}" for i in range(1, depth + 1)] 
        self.projection_log.extend(projections)
        return projections

    def enable_non_deterministic_expansion(self, event_input):
        """Expands the event input into variant mirrors."""
        variants = [
            f"{event_input} :: {suffix}"
            for suffix in random.sample(
                ["resonance drift", "mirror fold", "phase scatter", "recursive bloom", "entropy fork"], 3
            )
        ]
        self.projection_log.extend(variants)
        print("🎭 Expansion Variants:")
        for v in variants:
            print(f" - {v}")
        return variants


