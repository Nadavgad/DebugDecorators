def debug(func):
    """
    A decorator that prints input arguments, calls the decorated function,
    prints the result, and handles exceptions by printing the exception details.

    :param func: The function to be decorated.
    :return: The decorated function.
    """

    def wrapper(*args, **kwargs):
        """
        Wrapper function that prints input arguments, calls the decorated function,
        prints the result, and handles exceptions by printing the exception details.

        :param args: Positional arguments passed to the decorated function.
        :param kwargs: Keyword arguments passed to the decorated function.
        :return: The result of the decorated function.
        """
        print(f"{func.__name__} got {args} {kwargs}")

        results = []
        for arg in args:
            try:
                result = func(arg, **kwargs)
                results.append(result)
                print(f"returned: {result}")
            except Exception as e:
                print(f"Raised: {type(e).__name__} - {e}")
        return results

    return wrapper


@debug
def div2(n):
    """
    Function that performs division by 2.

    :param n: The numerator.
    :return: The result of the division.
    """
    return n / 2


@debug
def div0(n):
    """
    Function that raises a ZeroDivisionError for demonstration purposes.

    :param n: The numerator.
    :return: The result of the division (will not be reached in this example).
    """
    return n / 0


# Test
try:
    div2_results = div2(4, 10)
    print(div2_results)
except Exception as e:
    print(f"Error: {type(e).__name__} - {e}")

try:
    div2_result_zero = div2(0)
    print(div2_result_zero)
except Exception as e:
    print(f"Error: {type(e).__name__} - {e}")

try:
    div0_result = div0(10, 3)
    print(div0_result)
except Exception as e:
    print(f"Error: {type(e).__name__} - {e}")
