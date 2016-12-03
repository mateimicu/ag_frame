## Genetic algorithms simple framework

This is a simple framework that implements some basic
genetic algorithms used in the college course.

---
To Do:
- Add a fitness function for each function that we have and
  we need to use that in our algorithms
- Introduce some new representaions for the date 
  (that will allow for mutations and crossover)
- Introduce some crossover and mutations classes and actions
- Introduce some selections ( for crossover or mutations ) methods
  that can be swapped 
- Implement and algorithm that can take all the parameters and use run
  (seed the random function for debug purposes)
- Implement an supervised GA to figure out the parameters for other algorithms
  (This means figuring out some fitness function)

---
To Do(enchanting):
- There is some redundant code in the algorithms section,
  some in the algorithms and some in the functions section
- Introduce a new base for the rmhc, nahc and sahc
- Consider allowing for more diversity for our algorithms, and more control
  over the starting positions
- Eliminate the need for the `run.sh` and `test.py` and add a new runner object
- Control the output better and allow for formating (csv, json, xml)
- Add some logging method with verbosity level
- Add an option for seeding the random function (for debuging)
- Try to use `numpy` to speed up the runs
- Integrate pylint and flake8 with tox
- Add a CI for this project
- Implement the other output methods(json, xml)
- Implement and append and rewrite mode for the output

