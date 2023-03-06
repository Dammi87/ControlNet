from typing import List, Dict
from pydantic import BaseModel

class Attributes(BaseModel):
    trait_type: str
    value: str

class Result(BaseModel):
    mintAddress: str
    title: str
    img: str
    attributes: List[Attributes]


def parse_result(result: Dict) -> Result:
    return Result(**result)


def parse_request(request: Dict) -> List[Result]:
    for result in request.get('results', []):
        yield parse_result(result)
