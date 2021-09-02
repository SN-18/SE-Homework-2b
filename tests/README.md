Pytest was used to integrate testing functionality with Github Actions. 
As can be seen in `test_validate.py`, `@pytest.mark.parametrize()` is a clean way to manage unit tests in Pytest.

After `setup.py` is run, `pytest` can be enabled from the root directory of this repository. This will run the test cases present in this directory (`/tests/`).
For a more detailed description, please check [README.md#description](https://github.com/SN-18/SE-Homework-2b/tree/updated-readme#description).
