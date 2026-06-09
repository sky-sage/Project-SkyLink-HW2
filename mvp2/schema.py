from dataclasses import dataclass, field

@dataclass
class RequirementIR:

    req_id: str

    subject: str = ""

    verb: str = ""

    objects: list = field(default_factory=list)

    sources: list = field(default_factory=list)

    destinations: list = field(default_factory=list)

    constraints: list = field(default_factory=list)