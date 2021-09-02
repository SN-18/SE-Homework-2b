# Software Engineering: Homework-2b

## Description

The primary purpose of this repository was to get familiar with the various features of Github and to concisely integrate them. This repository was created as a homework assignment (HW-2b) for our Software Engineering (CSC-510) course under [Prof. Timothy Menzies](http://menzies.us/).

We have included a simple `src/validate.py` file which consists of a class `Calculator` consisting of methods performing certain list-based manipulations. We have integrated this `src` directory with our `setup.py`. This file not only eases installation but provides functionality to integrate testing using Pytest. As can be observed in [`main.yml`](https://github.com/SN-18/SE-Homework-2b/blob/main/.github/workflows/main.yml), our argument passed to the Github Actions workflow is `python setup.py develop && pytest` which runs the tests in `./tests/` directory.

Apart from this, we have ensured that the following practices are included while creating this repository -
1. [Adding a Kanban style project board](https://github.com/SN-18/SE-Homework-2b/projects/2)
2. Creating Github Issues for proposals/bugs
3. Creating branches/forks and submitting Pull Requests (PRs)
4. These PRs are being reviewed before getting commited
5. Adding descriptive badges
6. Providing an appropriate `LICENSE`, `CODE_OF_CONDUCT`, and `CONTRIBUTING` file with `CITATION.cff`

## Authors

* Saurabh Nanda    (snanda2@ncsu.edu)
* Radhika Toravi   (rtoravi@ncsu.edu)
* Parth Parikh     (pmparikh@ncsu.edu)
* Jessica Vargas   (jrvargas@ncsu.edu)
* Rushikesh Deodhar (rdeodha@ncsu.edu)

### Dependencies

* Python 3
[![Python-3](https://img.shields.io/badge/Python-v3.7-blue)](https://www.python.org/download/releases/3.0/)
* Pytest: [![Pytest](https://img.shields.io/badge/Pytest-v6.2.5-blue)](https://docs.pytest.org/en/6.2.x/)

## Help

If you have specific queries, please use [Issues](https://github.com/SN-18/SE-Homework-2b/issues). If you would like to contribute, we suggest the following steps:
1. Fork the repository (https://github.com/SN-18/SE-Homework-2b/)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

For more details, please read our [Contributing.md](https://github.com/SN-18/SE-Homework-2b/blob/main/CONTRIBUTING.md#contributing).

## Workflow Status
[![Workflow-Status](https://img.shields.io/github/workflow/status/SN-18/SE-Homework-2b/on%20push)](https://github.com/SN-18/SE-Homework-2b/tree/main/.github/workflows)

## Version History

* v1.0.0
    * Initial Release
* v1.1.0
    * New features: Includes executable src code, updated LICENSE info, updated COC and README.md to reflect progress made in project 

## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Citation Data
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5348588.svg)](https://doi.org/10.5281/zenodo.5348588)
