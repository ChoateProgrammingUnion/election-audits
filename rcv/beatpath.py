import csv
from pydantic import BaseModel
from typing import List
import networkx

"""
Beatpath, also known as Schulze is the preferred ranked-choice voting mechanism for CPU
"""

class Ballot(BaseModel):
    choices: List[Choice]

class Choice(BaseModel):
    name: str
    ranking: int
