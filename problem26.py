def longestRecurringCycle(deno):
    max_cycle_length = -1
    max_res = 1
    for i in range(2, deno, 1):
        decimal_tail = set()
        quotient = 0
        remainder = 1
        while remainder > 0:
            quotient = remainder * 10 / i
            remainder = remainder * 10 % i
            if (quotient, remainder) in decimal_tail:
                break
            decimal_tail.add((quotient, remainder))
        if len(decimal_tail) > max_cycle_length and remainder != 0:
            max_cycle_length = len(decimal_tail)
            max_res = i
    return max_res

if __name__ == '__main__':
    print(longestRecurringCycle(1000))
