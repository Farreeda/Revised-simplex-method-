import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
import math
from mpl_toolkits import mplot3d
from scipy.optimize import minimize
import sympy
z = sympy.Symbol('z')
m = sympy.Matrix([[4-z, 2,2,1], [2, 4-z, 0,1], [2,0, 2-z,2], [1,1,2,0]])
print(m.det())
print(m.det().as_poly().coeffs())

#plt.style.use('seaborn-poster')
from mpl_toolkits.mplot3d import axes3d
#---------------------draw with 3 variables w saved in search-ms:displayname=Search%20Results%20in%20PycharmProjects&crumb=location:C%3A%5CUsers%5CFarida%5CPycharmProjects\lin -------------------------------
def V(x,y,z):
     return 9 - 8 * x - 6 * y - 4 * z + 2 * x ** 2 + 2 * y ** 2 + z ** 2 + 2 * x * y + 2 * x * z

X,Y = np.mgrid[-1:1:100j, -1:1:100j]
Z_vals = [ -0.5, 0, 0.9 ]
num_subplots = len( Z_vals)

fig = plt.figure(figsize=(10, 4))
for i,z in enumerate( Z_vals):
    ax = fig.add_subplot(1 , num_subplots , i+1, projection='3d')
    ax.contour(X, Y, V(X,Y,z), cmap=cm.gnuplot)
    ax.set_title('z = %.2f'%z, fontsize=30)
fig.savefig('contours.png', facecolor='grey', edgecolor='none')
# --------------contour------------------------------------------
# feature_x = np.linspace(-4* math.pi , 4* math.pi, 5)
# feature_y = np.linspace(-4* math.pi , 4* math.pi, 5)
#
#
# # Creating 2-D grid of features
# [X, Y] = np.meshgrid(feature_x, feature_y)
#
# fig, ax = plt.subplots(1, 1)
#
# Z = 10*X**6-48*X**5+200*X**4-120*X**2-480*X+100
# # plots filled contour plot
# ax.contour(X, Y, Z)

# ax.set_title('Filled Contour Plot')
# ax.set_xlabel('feature_x')
# ax.set_ylabel('feature_y')
#
# plt.show()
#-------------------------------contour------------------------------------------
#------------------------------3D plotting------------------------------------------

#
# fig = plt.figure(figsize = (12,10))
# ax = plt.axes(projection='3d')
#
# x = np.arange(-100, 100, 20)
# y = np.arange(-100, 100, 20)
#
# X, Y = np.meshgrid(x, y)
# Z =  return 9 - 8 * x[0] - 6 * x[1] - 4 * x[2] + 2 * x[0] ** 2 + 2 * x[1] ** 2 + x[2] ** 2 + 2 * x[0] * x[1] + 2 * x[0] * x[2]
#
# surf = ax.plot_surface(X, Y, Z, cmap = plt.cm.cividis)
#
# # Set axes label
# ax.set_xlabel('x', labelpad=20)
# ax.set_ylabel('y', labelpad=20)
# ax.set_zlabel('z', labelpad=20)
#
# fig.colorbar(surf, shrink=0.5, aspect=8)
#
# plt.show()


#------------------------------3D plotting------------------------------------------
#
#------------------------------2D plotting------------------------------------------
#

# def f(X):
#     return 10*X**6-48*(X**5)+15*(X**4)+200*(X**3)-120*(X**2)-480*X+100
# x = np.linspace ( start = -2   # lower limit
#                 , stop =   3  # upper limit
#                 , num = 500      # generate 51 points between 0 and 3
#                 )
# y = f(x)    # This is already vectorized, that is, y will be a vector!
# plt.plot(x, y)
# plt.show()

#------------------------------2D plotting------------------------------------------
#------------------------------optimization pywraplp--------------------------------


#------------------------------optimization pywraplp--------------------------------
# from ortools.linear_solver import pywraplp
# from ortools.init import pywrapinit
#
#
# def main():
#     # Create the linear solver with the GLOP backend.
#     solver = pywraplp.Solver.CreateSolver('GLOP')
#     if not solver:
#         return
#
#     # Create the variables x and y.
#     x1 = solver.NumVar(0, 1, 'x1')
#     x2 = solver.NumVar(0, 2, 'x2')
#     x3 = solver.NumVar(0, 3, 'x3')
#     print('Number of variables =', solver.NumVariables())
#
#     # Create a linear constraint, 0 <= x + y <= 2.
#     ct = solver.Constraint(0, 3, 'ct')
#     ct.SetCoefficient(x1, 1)
#     ct.SetCoefficient(x2, 1)
#     ct.SetCoefficient(x3, 2)
#
#     print('Number of constraints =', solver.NumConstraints())
#
#     # Create the objective function, 3 * x + y.
#     objective = solver.Objective()
#     objective.SetCoefficient(x, 3)
#     objective.SetCoefficient(y, 1)
#     objective.SetMaximization()
#
#     solver.Solve()
#
#     print('Solution:')
#     print('Objective value =', objective.Value())
#     print('x =', x.solution_value())
#     print('y =', y.solution_value())
#
#
# if __name__ == '__main__':
#     pywrapinit.CppBridge.InitLogging('basic_example.py')
#     cpp_flags = pywrapinit.CppFlags()
#     cpp_flags.logtostderr = True
#     cpp_flags.log_prefix = False
#     pywrapinit.CppBridge.SetFlags(cpp_flags)
#
#     main()

    # ------------------------------optimization pywraplp--------------------------------

# ------------------------------optimization scipy--------------------------------


# def fcn(x):
#     x1= x[0]
#     x2= x[1]
#     x3= x[2]
#     return 9-8 *x1 -6*x2 -4*x3 +2 * x1**2 +2 * x2**2 + x**3 + 2* x1*x2+ 2*x1*x3
#
# def e_constraint(x):
#
#     return 3-(x[0]+x[1]+2*x[2])
#
# constraint1 = {'type': 'eq', 'fun': e_constraint}
# bnds= (0.0, 1000.0)
# x0 = np.array({0.0,0.0,0.0})
# result = minimize(fcn, x0, method= 'SLSQP',bounds= (bnds, bnds, bnds), constraints= constraint1)
# print(result)
# def objective(x):
#     return 9 - 8 * x[0] - 6 * x[1] - 4 * x[2] + 2 * x[0] ** 2 + 2 * x[1] ** 2 + x[2] ** 2 + 2 * x[0] * x[1] + 2 * x[0] * x[2]
#
#
#
#
# def constraint3(x):
#     sum_eq = x[0]+ x[1]+2*x[2]-3.0
#     return sum_eq
#
# # initial guesses
# n = 3
# x0 = np.zeros(n)
# x0[0] =  10.0
# x0[1] = 100.0
# x0[2] = 10.0
# # show initial objective
# print('Initial SSE Objective: ' + str(objective(x0)))
#
# # optimize
# #b = (1.0,None)
# bnds = ((0.0,1000.0), (1.0,1000.0),(1.0,1000.0))
#
# cons = {'type': 'eq', 'fun': constraint3}
#
# solution = minimize(objective,
#                     x0,
#                     method='SLSQP',
#                     bounds=bnds,
#                     constraints=cons)
# x = solution.x
#
# print(solution)

#-------------- determinant----------------
# importing Numpy package
# fig = plt.figure(figsize = (12,10))
# ax = plt.axes(projection='3d')
#
# x = np.arange(-100, 100, 20)
# y = np.arange(-100, 100, 20)
#
# X, Y = np.meshgrid(x, y)
# Z =  (X+0.5*Y)*(0.375-0.00005+(X+0.5*Y))+(0.2*X+0.5*Y)*(0.75-0.0001*(0.2*X+0.5*Y))-X*(2-0.0005*X-0.00015*Y)+Y*(3.5-0.0002*X-0.0015*Y)
# surf = ax.plot_surface(X, Y, Z, cmap = plt.cm.cividis)
#
# # Set axes label
# ax.set_xlabel('x', labelpad=20)
# ax.set_ylabel('y', labelpad=20)
# ax.set_zlabel('z', labelpad=20)
#
# fig.colorbar(surf, shrink=0.5, aspect=8)
#
# plt.show()
