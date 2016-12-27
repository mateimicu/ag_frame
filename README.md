## Genetic algorithms simple framework

This is a simple framework that implements some basic
genetic algorithms used in the college course.

---
To Do:
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
- Add some logging method with verbosity level
- Add an option for seeding the random function (for debuging)
- Try to use `numpy` to speed up the runs
- Integrate pylint and flake8 with tox
- Add a CI for this project
- Implement the other output methods(json, xml)

