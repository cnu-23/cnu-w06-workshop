import numpy as np
import matplotlib.pyplot as plt

# Task 1

def f(x):
    return np.sin(x)

def monte_carlo(f, a, b, N):
    '''
    Returns a Monte Carlo approximation of the integral
    of f(x) over [a, b], using N points.
    '''
    # Generate N random points in the interval
    x = (b - a) * np.random.random(N) + a

    # Compute and return the approx. integral of f(x)
    return (b - a) * np.mean(f(x))

# Test the function
a, b = 0, np.pi
I_exact = 2
I_approx = monte_carlo(f, a, b, 1000)
print(I_exact, I_approx)

# Task 2: estimate the error.
# We test 20 logarithmically spaced values of N
# between 10 and 10 million.
err = []
N_vals = np.logspace(1, 7, 20, dtype=int)
for N in N_vals:
    I_approx = monte_carlo(f, a, b, N)
    err.append(abs(I_exact - I_approx))

fig, ax = plt.subplots()
ax.plot(np.log(N_vals), np.log(err), 'rx')
ax.set(title='Error for Monte Carlo integration',
       xlabel=r'$\log(N)$',
       ylabel=r'$\log(E)$')
plt.show()

# Estimate q using linear regression (see week 6)
q = np.polyfit(np.log(N_vals), np.log(err), 1)[0]
print(f'The error is proportional to N^{q:.2f}.')

# q = -0.5 indicates that the error is proportional to 1/sqrt(N).
# This means that to divide the error by 2, we have to use 4 times as many sample points.


# Task 3

def monte_carlo_2d(f, a, b, N):
    '''
    Returns a Monte Carlo approximation of the integral
    of f(x, y) for x in [a[0], b[0]], and y in [a[1], b[1]]
    using N points.
    '''
    # Generate N random points in the rectangle
    x = (b[0] - a[0]) * np.random.random(N) + a[0]
    y = (b[1] - a[1]) * np.random.random(N) + a[1]

    # Compute and return the approx. integral of f(x, y)
    return (b[0] - a[0]) * (b[1] - a[1]) * np.mean(f(x, y))


# Test the function
def f(x, y):
    return x * y

a, b = [0, 0], [1, 1]
I_exact = 1/4
I_approx = monte_carlo_2d(f, a, b, 1000)
print(I_exact, I_approx)


# Task 4

def volume_ball(n, N):
    '''
    Estimates the volume of the n-ball using random uniform sampling.
    '''
    # Generate random points in the hypercube (each row is one point)
    x = 2 * np.random.random((N, n)) - 1

    # How many points are inside the ball
    # Points for which x_0^2 + x_1^2 + ... + x_n-1^2 <= 1
    inside = x[np.sum(x**2, axis=1) <= 1]

    # Compute the probability as the ratio inside/all
    p = inside.shape[0] / x.shape[0]

    # Volume is p * volume of the hypercube
    return p * 2**n
    


nvals = np.arange(1, 21, dtype=int)
N = int(1e4)
volumes = []
for n in nvals:
    volumes.append(volume_ball(n, N))


# Note: the "plot" here isn't strictly valid, as the y-axis shows quantities in different units.
# The "function" we are plotting is a dimensionless ratio of volumes (ball/cube), multiplied by 2^n.
fig, ax = plt.subplots()
ax.plot(nvals, volumes, 'kx')
ax.set(xlabel='Number n of dimensions', ylabel='Volume of the n-ball')
plt.show()


# Bonus: recursive volume of the n-ball.
# Multiply volume of (n-1)-ball by the average of
# f(x) = sqrt(1 - sum(x_i^2)) (for vector x).
# This gives the volume of a half-ball; multiply by 2.

def volume_ball(n, N):
    if n == 1:
        return 2

    def f(x):
        return np.sqrt(1 - np.sum(x**2, axis=1))

    x = 2 * np.random.random((N, (n-1))) - 1
    inside = x[np.sum(x**2, axis=1) <= 1]
    f_eval = f(inside)
    return 2 * np.mean(f_eval)*volume_ball(n-1, N)
