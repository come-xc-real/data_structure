import inspect

import inspect


def get_local_variables(func):
    """Get the local variables of a function.

    Args:
        func: The function to get local variables from.

    Returns:
        A dictionary containing all the local variables of the function.
    """
    # Get the source code of the function
    source = inspect.getsource(func)

    print(inspect.signature(func))

    print(inspect.me)

    a = inspect.getargvalues(inspect.currentframe())
    print(a)
    print(a.locals)

    # Execute the source code in a temporary namespace
    namespace = {}
    exec(source, namespace)

    # Get the local variables from the namespace
    local_variables = {name: value for name, value in namespace.items() if not name.startswith('__')}

    return local_variables


class TimeComplexityCalculator:
    def __init__(self, fuc):
        self.fuc = fuc

    def run_fuc(self, *args):
        self.fuc(*args)
        print(str(self.fuc))


def test_fuc(a, b, c):
    a = a
    print(a, b, c)


local_variables = get_local_variables(test_fuc)
# print(local_variables)


#
# timecomplex = TimeComplexityCalculator(test_fuc)
#
# timecomplex.run_fuc(1, 2, 3)