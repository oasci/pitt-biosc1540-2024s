# Assessments

!!! danger "DRAFT"

    This page is a work in progress and is subject to change at any moment.

If you get an error like this from the autograder:

```python
Traceback (most recent call last):
  File "/usr/lib/python3.10/unittest/loader.py", line 436, in _find_test_path
    module = self._get_module_from_name(name)
  File "/usr/lib/python3.10/unittest/loader.py", line 377, in _get_module_from_name
    __import__(name)
  File "/autograder/source/tests/test_p05.py", line 4, in <module>
    from student_submission import calculate_grade
ModuleNotFoundError: No module named 'student_submission'
```

this likely means you submitted the Jupyter notebook (`.ipynb`) and not the Python script (`.py`).
