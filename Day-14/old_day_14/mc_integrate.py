import numpy as np
import matplotlib.pyplot as plt

def is_in_range(x,y):
    '''
    Takes in x,y positions and returns 1 if the point is within
    the bounds of integration, 0 otherwise.
    '''
    r = (x**2+y**2)**.5
    if (r >= 0.5 and r <=1.0):
        return 1
    else:
        return 0

def mc_integral(total_points,xmin,xmax,ymin,ymax):
    '''
    takes in the number of points to be sampled and two tuples
    describing range in x,y direction.  Returns a tuple containing
    calculated area (via MC integration), real area, and the fractional
    error between the calculated area and real area.
    '''
    points_in = 0

    for i in range(0,total_points):

        x = np.random.uniform(xmin,xmax)
        y = np.random.uniform(ymin,ymax)

        # count points if the coordinate is within the bounds of integration
        if is_in_range(x,y) > 0:
            points_in += 1

    # estimated area
    area = (xmax-xmin)*(ymax-ymin)*points_in/total_points
    real_area = 0.75*np.pi
    return area, real_area, np.abs((area-real_area)/real_area)

def main():

    # Make sure that the plot shows up when we call it
    plt.ion()

    # Initialize variables for tracking results
    points_in = 0
    total_points = []
    fractional_error = []

    # Loop over N_points trials; This is a lazy way of doing this! How could you do it better?
    for points in [2, 2**2, 2**3, 2**4, 2**5, 2**6, 2**7, 2**8, 2**10, 2**11, 2**12]:
        area, real_area, error = mc_integral(int(points),-1.0,1.0,-1.0,1.0)
        total_points.append(points)
        fractional_error.append(error)


        err_est_points = (total_points[0], total_points[-1])
        err_est_error = (fractional_error[0], fractional_error[0]/total_points[-1]**0.5)

    plt.plot(total_points, fractional_error, 'bo-', err_est_points, err_est_error, 'r-')
    plt.xlim(2,2**12)
    plt.ylim(1.0e-4,10.0)
    plt.xscale('log')
    plt.yscale('log')
    plt.text(1e2,2,'Actual error',color='blue',size='large')
    plt.text(1e2,0.5,r'Error $\propto N^{-0.5}$',color='red',size='large')
    plt.savefig("MC_error.png")

if __name__ == "__main__":
    main()
