"""Swarm Majority Voting & Self-Consistency Verifier.
100% Python Standard Library.
"""

import collections

class SwarmMajorityVoting:
    """Ensemble consensus aggregator computing majority winner and confidence distribution."""
    @staticmethod
    def compute_borda_and_majority(votes):
        counts = collections.Counter(votes)
        majority_winner, max_votes = counts.most_common(1)[0]
        confidence = max_votes / len(votes)
        return {
            "winner": majority_winner,
            "vote_distribution": dict(counts),
            "confidence": round(confidence, 4),
            "consensus_reached": confidence >= 0.5
        }
