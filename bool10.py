def main(a):
    """check that the number "a" is a perfect square.
    Args:
        a: int
    Returns:
        bool
    """
    from math import sqrt    
    return sqrt(a)//1*(a//sqrt(a))==a  