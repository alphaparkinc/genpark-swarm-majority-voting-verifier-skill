from client import SwarmMajorityVoting

votes = ["Refactor Module", "Refactor Module", "Deprecate Module", "Refactor Module", "Keep As Is"]
res = SwarmMajorityVoting.compute_borda_and_majority(votes)

print(f"Ensemble Winner: {res['winner']} (Confidence: {res['confidence'] * 100:.1f}%)")
print("Vote Breakdown:", res["vote_distribution"])
