from validate_cpf import validate_cpf

VALID_CPF_WITH_MASK = '529.982.247-25'
VALID_CPF_WITHOUT_MASK = '52998224725'

INVALID_CPF_WITH_MASK = '111.111.111-11'
INVALID_CPF_WITHOUT_MASK = '11111111111'

def test_validate_cpf():
    assert validate_cpf is not None

def test_clean_cpf():
    assert validate_cpf.clean(INVALID_CPF_WITH_MASK) == INVALID_CPF_WITHOUT_MASK

def test_correct_cpf_length():
    assert validate_cpf.is_allowed(INVALID_CPF_WITHOUT_MASK) == True

def test_incorrect_cpf_length():
    assert validate_cpf.is_allowed(INVALID_CPF_WITH_MASK) == False

def test_is_allowed_cpf():
    assert validate_cpf.is_allowed(INVALID_CPF_WITHOUT_MASK) == True

def test_not_is_allowed_cpf():
    assert validate_cpf.is_allowed(VALID_CPF_WITHOUT_MASK) == False

def test_fist_verification_digit():
    CPF = VALID_CPF_WITHOUT_MASK
    CORRECT_FIST_DIGIT = 2
    assert validate_cpf.caculate_digit(CPF) == CORRECT_FIST_DIGIT

def test_last_verification_digit():
    CPF = VALID_CPF_WITHOUT_MASK
    CORRECT_LAST_DIGIT = 5
    assert validate_cpf.caculate_digit(CPF, is_first_digit=False) == CORRECT_LAST_DIGIT

def test_invalid_cpf_whitout_mask():
    CPF = INVALID_CPF_WITHOUT_MASK
    assert validate_cpf.is_valid(CPF) == False

def test_invalid_cpf_whit_mask():
    CPF = INVALID_CPF_WITH_MASK
    assert validate_cpf.is_valid(CPF) == False

def test_valid_cpf_whitout_mask():
    CPF = VALID_CPF_WITHOUT_MASK
    assert validate_cpf.is_valid(CPF) == True

def test_valid_cpf_whit_mask():
    CPF = VALID_CPF_WITH_MASK
    assert validate_cpf.is_valid(CPF) == True

