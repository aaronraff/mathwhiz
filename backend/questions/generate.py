import random
import operator
from typing import Any, Callable, Dict, List

from .models import Question


class Generator():
    min_num = -20
    max_num = 20
    operators = [operator.add, operator.sub, operator.mul]

    def __init__(self):
        random.seed()

    def generate(self, count: int) -> List[Question]:
        return [self._generate_question() for i in range(count)]

    def _generate_question(self) -> Question:
        num1 = random.randint(self.min_num, self.max_num)
        num2 = random.randint(self.min_num, self.max_num)
        fun = self.operators[random.randint(0, len(self.operators)-1)]

        question = Question()
        question.prompt = '{} {} {}'.format(num1, self._op_to_str(fun), num2)
        question.answer = fun(num1, num2)
        question.choices = self._generate_choices(question.answer, 4)
        return question

    def _generate_choices(self, real_ans: int, count: int) -> List[int]:
        choices = [real_ans]
        choice_count = 0

        while choice_count < (count-1):
            num = random.randint(real_ans-10, real_ans+10)

            # Make sure all choices are unique
            if num in choices:
                continue

            choice_count += 1
            choices.append(num)

        random.shuffle(choices)
        return choices

    def _op_to_str(self, op_fun: Callable[[int, int], int]) -> str:
        if op_fun == operator.add:
            return '+'
        elif op_fun == operator.sub:
            return '-'
        else:
            return 'x'
