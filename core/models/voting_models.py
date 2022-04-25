from django.db import models
from core.models.millionaire_models import Millionaire
from system.models import BaseModel


class VoteMillionaire(BaseModel):
    millionaire = models.ForeignKey(Millionaire, on_delete=models.CASCADE, related_name='votes')

    def __str__(self) -> str:
        votes= self.millionaire.votes.count()
        return f"{self.millionaire.name} {votes}"
