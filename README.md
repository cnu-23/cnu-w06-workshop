# Week 6 workshop: Monte Carlo integration

Remember to **pair program**. Choose one of you to be the driver first; then, every 15 minutes or so, **swap roles**. The driver writes code and shares their screen, the navigator is an active observer/helper.

Work in the script `montecarlo.py`.

## Monte Carlo integration

There are many ways to estimate integrals numerically. In the course, we have been looking at quadrature methods; Monte Carlo integration uses an entirely different approach.

Monte Carlo integration is a numerical method which allows us to approximate definite integrals. The integral of a continuous function f over some interval [a, b] is equal to the **average** of that function over the interval, multiplied by the interval width. The idea is to evaluate the function at many randomly chosen points over [a, b]. Computing the mean of all function evaluations gives an estimate for the integral.

## Task 1

Write a function `monte_carlo(f, a, b, N)` which estimates and returns the integral of a function `f` over some domain [`a`, `b`], by sampling `N` points x<sub>i</sub> chosen randomly in the interval, evaluating f(x<sub>i</sub>) at all these points, computing the average of the `N` values, and multiplying the result by `b - a`.

Test your function by defining a function `f()` with a known integral. You can use the example functions in the Week 5 or 6 tutorial sheets for instance.

## Task 2

Using a test function `f()` of your choice, investigate the accuracy of the Monte Carlo method by calculating the error between exact integral and approximation for several values of `N`.

The error should be roughly proportional to N<sup>q</sup> (q is a real number). Can you estimate q?

## Task 3: Monte Carlo in multiple dimensions

An advantage of this method over those we've seen so far is that the computational cost does not increase as rapidly for higher-dimensional integrals.

Write a function `monte_carlo_2d()` which adapts your `monte_carlo()` function to estimate the integral of a function `f(x, y)` over some finite rectangular domain. You will need to sample `N` points with 2 coordinates each.

## Task 4: estimating the volume of the n-dimensional ball

Write a function `volume_ball(n, N)` which uses random sampling in a similar way, to estimate the volume of an n-dimensional ball with radius 1 and centred around the origin, using `N` uniformly distributed random points.

Compute the estimated volume of this n-dimensional ball for different values of n (say, 1 to 20). Is this what you expected?

#### Hints

- Start with n = 2. A 2-dimensional ball is a disc. Think about how the following helps you estimate the area of the disc (assuming you don't know the formula):
    - Assuming a uniform distribution, if you generate a random point inside the square domain [-1, 1] x [-1, 1], what is the probability that it is also inside the disc of radius 1 centred at the origin?
    - If you generate a large number of points in that same square, say 10,000, approximately how many of them will be inside the disc?
    - How can you tell whether a given random point with 2 coordinates is inside the disc?
- Following your reasoning to expand this method to 2 dimensions for Task 3, think about how to expand it further to an arbitrary number of dimensions. Each point in an n-dimensional space has n coordinates.

### Bonus question

How would you tackle the n-ball problem with a Monte Carlo integration approach?
