"""
    Echo your input.
"""

def greeting(you):
    """Returns hello, you.

    Args:
        you (string): string

    Returns:
        string: "hello, you"
    
    Example:
        greeting('George') = 'Hello, George'

    """
    return "Hello, %s" % you
