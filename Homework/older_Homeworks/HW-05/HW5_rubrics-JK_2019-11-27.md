# HW 5 - Grading - rubrics (by JK, 2019-11-27)

## Part 1: Exploring the grape harvest data (18 points total)
  - **Section 1:**  Loading and inspecting the data (3 points)
    - 1 pt loading the data
    - 2 pts for inspecting the date: using 'head' and 'describe', columns and number of rows
  - **Section 2:** Determining the earliest and latest harvest dates and where they occurred (4 points)
    - 2 pts for Q1 - the earlies harvest: year [1822], region [champagne_2], how early [-13]
    - 2 pts for Q2 - the latest harvest: year [1851], region [luxembourg], how early [75]
  - **Section 3:** Finding median harvest dates in 50 year intervals (4 points)
    - 3 pts for getting the median harvest dates [35.95, 33.8, 27.9, 28.0, 19.9]
    - 1 pt for answsering the question
  - **Section 4:** Visualizing trends by region (3 points)
    - 2 pts for plot
    - 1 pt for answering the question about latitude effect on harvest date [no effect]
  - **Section 5:** Looking for correlation in harvest date between Burgundy and Switzerland (4 points)
    - 3 pts for plot, deduct pts for: 1pt if no regression, or any part of plot is missing
    - 1 pt for answering the question about correlation

## Part 2: Modeling grape harvest dates and climate change (**17 points**)
  - **Section 1:**  Graphing temperature anomaly vs year and harvest date vs temperature anomaly (3 points)
    - 1 pt for each graph: temperature vs. year, harvest date vs. temperature
    - 1 pt for answer about correlation
  - **Section 2:** Modeling harvest date as a function of temperature anomaly using `curve_fit` (7 points)
    - 1 pt for function for linear fit
    - 2 pts for calling fit function and printing values of 'm' and 'b' [-5.656,  32.0485]
    - 2 pts for plotting the origial data and fit function
    - 2 pts for answers (1 for each answer)
  - **Section 3:** Graphing harvest date vs year (2 point)
    - 2 pts for plot harvest date vs. year
  - **Section 4:** Modeling harvest date as a function year using `polyfit` (5 points)
    - 2 pt for creating function with selected fitting order (polyfit + poly1d)
    - 1 pt for printing parameters values
    - 1 pt plot the actual data and fit function
    - 1 pt for explanation of selectged order of fit function

## Part 3: Writing a simple Python class (**15 points**)
  - **Section 1:**  Enhancing and using a pre-existing class (10 points)
    - 2 pts for adding new attribute 'year'
    - 2 pts for adding new method 'enroll', adding courses to the list
    - 2 pts for adding new method 'display_courses', printing the courses
    - 2 pts for adding new method 'years_until_graduation', returning number of years
    - 2 pts for prnting student's data using the provided roster list and class student
  - **Section 2:** Inheriting a class (5 points)
    - 2 pts for adding the method 'motto', accepting a parameter and setting new attribute
    - 2 pts for adding the method 'school_spirit' and printing out the 'motto'
    - 1 pt for using new methods: create a student, use 'school_spirit'

---
