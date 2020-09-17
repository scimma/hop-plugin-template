from dataclasses import dataclass
import json

from hop.models import MessageModel
from hop import plugins


@dataclass
class Example(MessageModel):
    """
    Example custom message.

    """
    myattr: str

    @classmethod
    def load(cls, input_):
        if hasattr(input_, "read"):
            payload = json.load(input_)
        else:
            payload = json.loads(input_)
        return cls(**payload)


@plugins.register
def get_models():
    return {
        "example": Example,
    }
