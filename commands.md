# Run tests

```bash
PYTHONPATH:src:tests -m unittest <path_to_test_files>
```

## Example
```bash
PYTHONPATH=src:tests python3 -m unittest tests/test_tasks.py tests/test_assignments.py tests/test_creations.py
```

# Check test coverage

```bash
PYTHONPATH=src:tests coverage run --branch -m unittest <path>.<file>.<class>
```

## Example
```bash
PYTHONPATH=src:tests coverage run --branch -m unittest tests.test_creations.TestCreation tests.test_assignments.TestAssignments tests.test_tasks.TestTasks
```

# Mutation checking

```bash
PYTHONPATH=conteudo:tests mutmut run
```

## Example

```bash
mutmut results | grep -E "(move_tile|get_tile)__mutmut_[0-9]+"
```