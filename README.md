#Students finder
##Problem description:
Given each student has a geolocation lat/lon point, how would you determine which students are physically in any classroom?  

Write a function that returns the students if they are in a classroom.  

##Solution approach
As we have the geolocation and dimension of the classroom, we only need to calculate
the sides (top, bottom, left, right) geolocation of the classroom and check if the student
geolocation is inside the classroom. The result is the list of students that are present in one of the classrooms.

For the bonus, the approach is to have a dictionary of classrooms and their attendance (the students present in the
class), and filter all the classrooms that have less than the expected attendance. The result is the list of
students in the filtered classrooms. 

##Code organization
* resources directory: contains json files with input data
* DataLoader.py: Helper functions to load input data
* LocationCalculator.py: Main functions to calculate new latitude and longitude. Also contains the logic to create the 
classroom box and check if a student is the classroom
* StudentFinder.py: Implements the problem solution(s) using LocationCalculator.py
* StudentFinderTestSuite: Contains test cases for several scenarios

##Run the code
```python -m unittest StudentFinderTestSuite```