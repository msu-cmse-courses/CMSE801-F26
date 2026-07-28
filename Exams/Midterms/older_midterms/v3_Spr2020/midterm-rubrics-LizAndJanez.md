# Rubrics for parts 1 & 2 in midterm exam, CMSE 801, SS20

## Part 1: Modeling a system using ODEINT (35 points total)
  - Q1: (4) 1 pt for each parameter explained
  - Q2: (11) evolving the model for 12 months
    - 1 pt for importing numpy and odeint
    - 1 pt for defining initial values for parameters
    - 2 pts for correctly defining time list; deduct 1pt of either end time of time step is wrong
    - 4 correctly defined 'derivate' function; accept 'y' with 2 values, return results with 2 values
    - 3 pt for correct call to 'odeint', correct parameters and storing the results

  - Q3: (8) plot the results; 0 pt is not plot
    - deduct 1 pt if any of the following in missing: title, legend, x-axis, y-axis

  - Q4: (6) numpy array slicing
    - deduct 2 pt if plot is not correct
    - deduct 2 pt if plot is correct, but not done with numpy array indexing
    - deduct 1or 2 points of any part of the plot is missing

  - Q5: (3) all pts if the answer is around 1.74 months (close to 2 months is also OK)
  - Q6: (3) all pts if the answer is around 1 month

## Part 2:  Load, manipulate, and visualize data using NumPy and Matplotlib (35 points)
  - Q7: (8) loading header row;
    - deduct 2 pt if not loaded as strings
    - deduct 2 pt if array is not printed

  - Q8: (8) loading the data; 2 pt if they have np.loadtxt()
    - deduct 2 pts if loaded columns are not 1-6
    - deduct 2 pts if loaded values are not stored into variables/one variable
    - deduct 2 pts if not loaded as floats
    - deduct 2 pts if column '“Number of drivers involved in fatal collisions per billion miles' is not printed

  - Q9: (4) all pts if correct number (805.3) is printed
  - Q10: (4) 1 pt for correctly printing each of the following:
    - [Speeding] mean: 31.725490196078432 standard deviation: 9.538525457163843
    - [Alcohol-impaired] mean: 30.686274509803923 standard deviation: 5.081647857167222

  - Q11: (4) 1 pt for printing each percentage and each state, where people not distracted is < 50%: 2 values and 2 states
        - values: [10. 39.]
        - states: ['Mississippi' 'Wisconsin']

  - Q12: (4) scatter plot; 0 points if there is not plot; deduct points for:
    - 1 pt if using standard marker or color
    - 1 pt if any of the plot element is missing: title, x-axis, y-axis

  - Q13: (3) all pts if answer says variables are not correlated

## Total parts 1 & 2: 70 pts, Graded by Janez Krek

## Part 3: Describe what a compartmental model is and come up with a plan for building one (30 pts)
  - Q13: (8) Explain what a compartmental model is
    - 4/8 for more of an example than an explanation.  Lack of compartment *AND* movement in description.
    - 4/8 We use the differential equations to evaluate the model, but the model itself is the combo of compartments and interactions.
    - 6/8 Lack of compartment *OR* movement in description.
    - 6/8 Mostly, but mixing up agents and compartments
    - 7/8 Some slight nuance with what the model is (compartments and interactions) and what we use to solve hte model (diff eq)
  - Q14: (6) Give two examples of systems that can be modeled using compartmental models, describe the compartments
    - (3) for each example
  - Q15: (16) PFAS example
    - (4) Identify the compartments
    - (4) Define interactions
    - (4) List parameters
    - (4) Write down system of equations
      - 2/4 if only description and not mathematical equations
      - 2/4 if not enough/wrong equations
