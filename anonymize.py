import csv
import hashlib
import csv
from argon2 import PasswordHasher
import json
import sys

"""
This utility is designed to prevent directly dumping people's Choate emails in the public.
It hashes, salts, and peppers each email to maintain *some* privacy. It is not perfect and is not intended to be perfect.
It is only intended to (not) dump everybody's email into the wide open web.
"""

# Here we drastically increase the cost for computing each hash function since this is a one-time computation
TIME_COST = 100 # default=2
PARALLELISM = 8 # default=4
MEMORY_COST = 152400 # default=102400

def hash_email(email: str) -> str:
    """
    Here we use the argon2 hashing function composed of the sha256 hash function, which has some nice properties and is slow.
    We haven't audited or completely checked the argon2 hashing implementation and it isn't extremely popular, which is why we first apply the sha256 function.

    In this way, we're treating an email similarly to the way we'd treat a password: hard to discover/brute-force, easy to verify.
    """
    sha_hashed_password = hashlib.sha256(
        str(email).rstrip().encode("utf-8")
    ).hexdigest()

    ph = PasswordHasher(time_cost=TIME_COST, memory_cost=MEMORY_COST, parallelism=PARALLELISM)
    password_hash = ph.hash(sha_hashed_password)
    return password_hash


def verify_hash(email: str, email_hash: str) -> bool:
    """
    verify_hash(string, hash_password(string)) is True for all strings
    """
    ph = PasswordHasher(time_cost=TIME_COST, memory_cost=MEMORY_COST, parallelism=PARALLELISM)
    sha_hashed_password = hashlib.sha256(
        str(email).rstrip().encode("utf-8")
    ).hexdigest()

    try:
        if ph.verify(email_hash, sha_hashed_password.rstrip()):
            return True
    except argon2.exceptions.VerifyMismatchError:
        return False

    return False


if __name__ == "__main__":
    output = []

    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = "ballots.csv"

    with open(filename) as f:
        for each_line in csv.DictReader(f):
            if each_line:
                if each_line["Email Address"]:
                    each_line["Email Address"] = hash_email(each_line["Email Address"])
                output.append(each_line)

    with open("results.json", "w") as f:
        json.dump(output, f)

    print(output) # debug
