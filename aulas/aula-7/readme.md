# Execução
## Testes:
```bash
PYTHON_PATH=src:tests python3 -m unittest tests/test_assignments.py
PYTHON_PATH=src:tests python3 -m unittest tests/test_creations.py
```

## Verificação de Cobertura
```bash
PYTHON_PATH=src:tests coverage run --branch -m unittest tests.test_creations.TestCreation tests.test_assignments.TestAssignments
```
