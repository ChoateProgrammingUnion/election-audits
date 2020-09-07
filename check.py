import json
import sys
import anonymize
from typing import Union
import pprint


"""
Usage: python3 check.py [email] [results json filename]
"""

def audit(ballots: list, email: str) -> Union[bool, str]:
    """
    Prints the ballot associated with the email
    """
    for each_ballot in ballots:
        if anonymize.verify_hash(email.rstrip().lower(), each_ballot["Email Address"]):
            return each_ballot

    return False

if __name__ == "__main__":
    if len(sys.argv) == 3:
        filename = sys.argv[2]
        email = sys.argv[1]
    elif len(sys.argv) == 2:
        email = sys.argv[1]
    else:
        raise ValueError("Please provide [email] [json filename]!")

    with open(filename) as f:
        ballots = json.load(f)
        specific_ballot = audit(ballots, email)
        print("Was this your ballot:")
        pprint.pprint(specific_ballot)
