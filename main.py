def benchmark(iters: int):
    def decorator(func):
        import time

        def wrapper(*args, **kwargs):
            return_value = None

            start = time.time_ns()
            for i in range(iters):
                return_value = func(*args, **kwargs)

            end = time.time_ns()
            total = (end - start) / (iters * 10 ** 9)

            benchmark_msg = 'Среднее время выполнения {}: {:.12f} секунд.'
            print(benchmark_msg.format(func.__name__, total))
            return return_value

        return wrapper

    return decorator


def cache_result(func):
    results = {}

    def wrapper(arg):
        if arg not in results:
            results[arg] = func(arg)
        return results[arg]

    return wrapper


def fib_number(n: int):
    if n <= 1:
        return n
    return fib_number(n - 1) + fib_number(n - 2)


@cache_result
def memoize_fib_number(n: int):
    if n <= 1:
        return n
    return memoize_fib_number(n - 1) + memoize_fib_number(n - 2)


@benchmark(iters=5)
def fib_benchmark(n: int):
    return fib_number(n)


@benchmark(iters=50000)
def memoize_fib_benchmark(n: int):
    return memoize_fib_number(n)


def main():
    n = 30
    result_msg = 'Число Фиббоначи под номером {}: {}'
    print(result_msg.format(n, fib_benchmark(n)))
    print(result_msg.format(n, memoize_fib_benchmark(n)))


if __name__ == '__main__':
    main()

