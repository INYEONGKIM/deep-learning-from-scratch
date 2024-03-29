def numerical_diff(f, x):
    h = 1e-4
    return (f(x+h) - f(x-h))/(2*h)

def function_1(x):
    return 0.01*x**2 + 0.1*x

def function_2(x):
    return x[0]**2 + x[1]**2    # np.sum(x**2) 랑 동일

print(numerical_diff(function_1, 5))
print(numerical_diff(function_1, 10))