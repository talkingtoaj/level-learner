from pydantic import BaseModel
from typing import List

class QuizQuestion(BaseModel):
    question: str
    answer: str

class User(BaseModel):
    username: str
    current_level: int
    quiz_scores: List[float]