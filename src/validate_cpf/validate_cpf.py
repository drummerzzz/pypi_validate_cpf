import re

def clean(cpf:str):
  return ''.join(re.findall('[0-9]+', cpf))

def has_correct_length(cpf:str):
  CPF_VALID_SIZE = 11
  return len(cpf) == CPF_VALID_SIZE

def is_allowed(cpf:str):
  first_digit = cpf[0]
  return all(first_digit == digit for digit in cpf)

def caculate_digit(cpf:str, is_first_digit:bool=True):
  FACTORY = 10 if is_first_digit else 11
  FACTORIES = [i for i in reversed(range(2, FACTORY + 1))] # Número magico
  result_sum = 0
  for index, factory, in enumerate(FACTORIES, 0):
    result_sum += factory * int(cpf[index])
  REST = result_sum % 11 # Número magico
  DIGIT = 11 - REST if REST > 2 and REST < 10 else 0 # Números magicos
  return DIGIT

def is_valid(cpf:str):
  cpf = clean(cpf)
  if not has_correct_length(cpf):
    return False
  if is_allowed(cpf):
    return False
  
  first_verification_digit = caculate_digit(cpf)
  last_verification_digit = caculate_digit(cpf, is_first_digit=False)
  return cpf[-2:] == f'{first_verification_digit}{last_verification_digit}'