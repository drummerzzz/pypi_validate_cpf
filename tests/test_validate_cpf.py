import random
from validate_cpf import validate_cpf

VALID_CPF_WITH_MASK = random.choice(['529.982.247-25', '654.663.508-93', '420.457.238-36', '724.617.518-03'])
VALID_CPF_WITHOUT_MASK = random.choice(['52998224725', '65466350893', '42045723836', '72461751803'])

INVALID_CPF_WITH_MASK = random.choice(['968.982.247-25', '654.063.508-93', '410.457.138-36', '111.111.111-11'])
INVALID_CPF_WITHOUT_MASK = random.choice(['96898224725','65406350932', '41045718366', '11111111111'])

def test_validate_cpf_module():
    assert validate_cpf is not None

def test_clean_cpf():
    clened_cpf = validate_cpf.clean(INVALID_CPF_WITH_MASK)
    assert  all(i.isdigit() == True for i in clened_cpf)
    clened_cpf = validate_cpf.clean(VALID_CPF_WITH_MASK)
    assert  all(i.isdigit() == True for i in clened_cpf)

def test_correct_cpf_length():
    assert validate_cpf.has_correct_length(VALID_CPF_WITHOUT_MASK) == True

def test_incorrect_cpf_length():
    SMALLER_CPF = '123456789'
    assert validate_cpf.has_correct_length(SMALLER_CPF) == False
    BIGGER_CPF = '1234567891011'
    assert validate_cpf.has_correct_length(BIGGER_CPF) == False

def test_is_allowed_cpf():
    ALLOWED_CPF = '11111111111'
    assert validate_cpf.is_allowed(ALLOWED_CPF) == True

def test_not_is_allowed_cpf():
    assert validate_cpf.is_allowed(VALID_CPF_WITHOUT_MASK) == False

def test_fist_verification_digit():
    CORRECT_FIST_DIGIT = int(VALID_CPF_WITHOUT_MASK[-2])
    assert validate_cpf.caculate_digit(VALID_CPF_WITHOUT_MASK) == CORRECT_FIST_DIGIT

def test_last_verification_digit():
    CORRECT_LAST_DIGIT = int(VALID_CPF_WITHOUT_MASK[-1])
    assert validate_cpf.caculate_digit(VALID_CPF_WITHOUT_MASK, is_first_digit=False) == CORRECT_LAST_DIGIT

def test_invalid_cpf_whitout_mask():
    CPF = INVALID_CPF_WITHOUT_MASK
    assert validate_cpf.is_valid(CPF) == False

def test_invalid_cpf_whith_mask():
    CPF = INVALID_CPF_WITH_MASK
    assert validate_cpf.is_valid(CPF) == False

def test_valid_cpf_whitout_mask():
    CPF = VALID_CPF_WITHOUT_MASK
    assert validate_cpf.is_valid(CPF) == True

def test_valid_cpf_whith_mask():
    CPF = VALID_CPF_WITH_MASK
    assert validate_cpf.is_valid(CPF) == True

