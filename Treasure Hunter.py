import random

#class to represent a Treasure Hunter
class TreasureHunter:
    def __init__(self, num_locations, location_with_treasure=0):
        # Initialize the TreasureHunter with the number of locations and the location with the treasure (default is 0).
        self.num_locations = num_locations
        self.beliefs = [1 / num_locations] * num_locations  # Initialize beliefs as uniform probabilities.
        self.location_with_treasure = location_with_treasure  # Store the actual location with the treasure.

    def updateBeliefs(self, observed_location):
        # Update beliefs based on the observed location
        for i in range(self.num_locations):
            if i == observed_location:
                self.beliefs[i] = 0
            else:
                self.beliefs[i] *= 1 / (self.num_locations - 1)

    def chooseLoc(self):
        # Choose a location with the highest belief (randomly among candidates).
        max_belief = max(self.beliefs)
        candidate_locations = [i for i, belief in enumerate(self.beliefs) if belief == max_belief]
        return random.choice(candidate_locations)

# Define a function to simulate a single agent's behavior over turns
def singleAgentSim(numTurns, numLocs):
    location_with_treasure = random.randint(0, numLocs - 1)
    treasure_hunter = TreasureHunter(numLocs, location_with_treasure)
    location_counts = [0] * numLocs  # Initialize location counts.

    for _ in range(numTurns):
        chosen_location = treasure_hunter.chooseLoc()  # Choose a location based on beliefs.
        location_counts[chosen_location] += 1  # Update the count for the chosen location.
        treasure_hunter.updateBeliefs(chosen_location)  # Update beliefs based on the chosen location.

    return location_counts

# Define a function to simulate multiple agents' behavior and collect location counts.
def multiAgentSim(turnNum, locNum, agentNum):
    location_with_treasure = random.randint(0, locNum - 1)
    location_counts = [0] * locNum  # Initialize location counts.

    for _ in range(agentNum):
        treasure_hunter = TreasureHunter(locNum, location_with_treasure)
        for _ in range(turnNum):
            chosen_location = treasure_hunter.chooseLoc()  # Choose a location based on beliefs.
            location_counts[chosen_location] += 1  # Update the count for the chosen location.
            treasure_hunter.updateBeliefs(chosen_location)  # Update beliefs based on the chosen location.

    return location_counts

# Define the main function (Iterations as well)
def main():
    num_turns = 1000
    num_locations = 10
    num_agents = 10

    # Single-agent-World simulation
    single_agent_location_counts = singleAgentSim(num_turns, num_locations)
    print("Single Agent Location Counts:", single_agent_location_counts)

    # Multi-agent-World simulation
    multi_agent_location_counts = multiAgentSim(num_turns, num_locations, num_agents)
    print("Multi-Agent Location Counts:", multi_agent_location_counts)

if __name__ == "__main__":
    main()  # Run the main function
