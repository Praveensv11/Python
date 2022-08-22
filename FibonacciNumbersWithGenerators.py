def fibonacciGenerator(n = None):
    """
        Generating function up to n fibonacci numbers iteratively
        Params:
            n: int
        Return:
            int
    """
    f0, f1 = 0, 1
    yield f1
    while n == None or n > 1:
        fn = f0 + f1
        yield fn
        f0, f1 = f1, fn
        n -= 1

for n_fibo in fibonacci(7):
    print(n_fibo)
