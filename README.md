# validate-cpf
<p align="center">

<a href="https://pypi.python.org/pypi/validate_cpf">
<img src="https://img.shields.io/pypi/v/validate_cpf.svg" /></a>
<!-- <a href="https://travis-ci.org/drummerzzz/validate_cpf"><img src="https://travis-ci.org/drummerzzz/validate_cpf.svg?branch=master" /></a> -->
</p>
Validates Brazilian CPF

## Features
-   CPF Validation with mask
-   CPF Validation without mask

## Modes of use
```python
#!/usr/bin/python
import validate_cpf

# Without mask
validate_cpf.is_valid('52998224725') # True

# With mask
validate_cpf.is_valid('529.982.247-25') # True
```

or

```python
#!/usr/bin/python
from validate_cpf import is_valid

# Without mask
is_valid('11111111111') # False

# With mask
is_valid('111.111.111-11') # False
```
# Author

<a href="https://joaofilho.dev">João Filho Drummerzzz</a>

<a href="https://github.com/drummerzzz">Github</a>

# Credits


This package was created with Cookiecutter and the `cs01/cookiecutter-pypackage` project template.

[Cookiecutter](https://github.com/audreyr/cookiecutter)

[cs01/cookiecutter-pypackage](https://github.com/cs01/cookiecutter-pypackage)
