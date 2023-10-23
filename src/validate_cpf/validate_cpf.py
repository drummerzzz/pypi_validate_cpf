import re
from typing import List


def __clean(cpf: str) -> str:
    return re.sub(r'\D', '', cpf)


def __has_correct_length(cpf: str) -> bool:
    CPF_VALID_SIZE = 11
    return len(cpf) == CPF_VALID_SIZE


def __is_allowed(cpf: str) -> bool:
    first_digit = cpf[0]
    return not all(first_digit == digit for digit in cpf)


def __generate_factories(factory: int, min_factory: int = 2) -> List[int]:
    return [i for i in reversed(range(min_factory, factory + 1))]  # Número magico


def __caculate_digit(cpf: str, is_first_digit: bool = True) -> bool:
    FACTORY = 10 if is_first_digit else 11
    FACTORIES = __generate_factories(factory=FACTORY)
    result_sum = sum(map(lambda item: item[0] * int(item[1]), zip(FACTORIES, cpf)))
    REST = result_sum % 11  # Número magico
    if REST < 2 or REST > 10:
        return 0
    return 11 - REST


def is_valid(cpf: str) -> bool:
    cpf: str = __clean(cpf)
    if not __has_correct_length(cpf):
        return False
    if not __is_allowed(cpf):
        return False
    first_verification_digit: int = __caculate_digit(cpf)
    last_verification_digit: int = __caculate_digit(cpf, is_first_digit=False)
    return cpf[-2:] == f'{first_verification_digit}{last_verification_digit}'
