import json
import sys
from py3votecore.schulze_method import SchulzeMethod, SchulzeHelper
# from py3votecore.condorcet import CondorcetHelper

def ballot_iterator(results):
    """
    Converts the ballots into a nice format that py3votecore can use
    """
    for each_result in results:
        count = 1
        preferences = []
        for ranking in each_result.keys():
            if "preference" in ranking and each_result[ranking]:
                preferences.append(each_result[ranking])
                print([each_result[ranking]])

        if preferences:
            yield {"count": 1, "ballot": [preferences]}
        # yield {"ballot": [preferences]}


if __name__ == "__main__":
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = "results.json"

    with open(filename) as f:
        results = json.load(f)

    ballots = list(ballot_iterator(results))
    # print(ballots)
    winner_results = SchulzeMethod(ballots, ballot_notation = SchulzeMethod.BALLOT_NOTATION_GROUPING).as_dict()

    print(winner_results.get("pairs"))

    winner = winner_results.get("winner")
    print("Winner:", winner)


