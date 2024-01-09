import traceback


def debug(func):
    """
    Decorator that prints information about the function call. It also prints the
    returned result if the function call is successful. If an exception occurs
    during the function call, it prints a traceback and the exception message.

    :param func: The function to be decorated.
    :return: The decorated function.
    """

    def module(*args, **kwargs):
        """
        The decorated function that wraps the original function.

        :param args: Positional arguments passed to the original function.
        :param kwargs: Keyword arguments passed to the original function.
        :return: The result of the original function.
        """
        try:
            result = func(*args, **kwargs)
            print(f"{func.__name__} got {args} {kwargs}")
            print(f"returned: {result}\n")
            return result
        except Exception as e:
            print(f"raised: {e}")
            traceback.print_exc()

    return module


@debug
def div0(n):
    """
    A function that attempts to perform integer division by zero.

    :param n: The numerator for the division operation.
    :return: The result of the division if successful , if not exception will execute
    """
    print(f">>> div0({n})")
    return n // 0


@debug
def div2(n):
    """
    A function that performs integer division by 2.

    :param n: The number for the division operation.
    :return: The result of the division.
    """
    print(f">>> div2({n})")
    return int(n / 2)


# Test cases
div2_result = div2(10)

div0_result = div0(10)
