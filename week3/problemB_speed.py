def balancesplit(i, sum1):
    if i ==n:
        sum2 = total_sum - sum1
        return abs(sum1 - sum2)
    if sum1 > total_sum - sum1:
        return abs(2 * sum1 - total_sum)
    else:
        return min(balancesplit(i + 1, sum1 + values[i]), balancesplit(i + 1, sum1))
    
values = [40269, 57181, 56421, 76170, 10867, 76502, 70083, 1854, 16234, 25843]
n = len(values)
total_sum = sum(values)
min_difference = balancesplit(0,0)
print(min_difference)