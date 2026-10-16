# tool: collatz_sequence
# description: Collatz sequence from n down to 1
# author: @Enard52
# example: collatz_sequence "6" -> "6,3,10,5,16,8,4,2,1"


def run(*args) -> str:
    if not args:
        return "Error: expected an integer"
    val = str(args[0]).strip()
    if not val:
        return "Error: expected an integer"

    try:
        n = int(val)
    except ValueError:
        return "Error: argument must be an integer"

    if n <= 0:
        return "Error: argument must be a positive integer"

    seq = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        seq.append(n)

    return ",".join(str(x) for x in seq)
