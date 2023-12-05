class Voter:
    def __init__(self, voter_id, name):
        self.voter_id = voter_id
        self.name = name
        self.has_voted = False

class ElectionSystem:
    def __init__(self):
        self.voters = {}

    def register_voter(self, voter_id, name):
        if voter_id not in self.voters:
            self.voters[voter_id] = Voter(voter_id, name)
            print(f"Voter {name} with ID {voter_id} registered successfully.")
        else:
            print(f"Voter with ID {voter_id} already registered.")

    def display_voters(self):
        print("Registered Voters:")
        for voter_id, voter in self.voters.items():
            print(f"{voter.name} (ID: {voter.voter_id}, Voted: {voter.has_voted})")

# Example usage
election_system = ElectionSystem()

election_system.register_voter(1, "Kamal")
election_system.register_voter(2, "Ganesh")
election_system.register_voter(1, "Duplicate Kamal")  # This should print an error message

election_system.display_voters()
