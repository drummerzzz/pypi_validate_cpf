import re

def clean(cpf:str):
  return ''.join(re.findall('[0-9]+', cpf))

def has_correct_length(cpf:str):
  CPF_VALID_SIZE = 11
  return len(cpf) == CPF_VALID_SIZE

def is_allowed(cpf:str):
  first_digit = cpf[0]
  return all(first_digit == digit for digit in cpf)

def generate_factories(factory:int, min_factory:int = 2):
    return [i for i in reversed(range(min_factory, factory + 1))] # Número magico

def caculate_digit(cpf:str, is_first_digit:bool=True):
  FACTORY = 10 if is_first_digit else 11
  FACTORIES = generate_factories(factory=FACTORY)
  result_sum = 0
  for index, factory, in enumerate(FACTORIES, 0):
    result_sum += factory * int(cpf[index])
  REST = result_sum % 11 # Número magico
  if REST < 2 or REST > 10:
    return 0
  return 11 - REST

def is_valid(cpf:str):
  cpf = clean(cpf)
  if not has_correct_length(cpf):
    return False
  if is_allowed(cpf):
    return False
  first_verification_digit = caculate_digit(cpf)
  last_verification_digit = caculate_digit(cpf, is_first_digit=False)
  return cpf[-2:] == f'{first_verification_digit}{last_verification_digit}'