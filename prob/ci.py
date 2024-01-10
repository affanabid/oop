from scipy import stats
n1 = 12
n2=12
xbar1 = 36300
xbar2 = 38100
s1 = 5000
s2 = 6100
cl = 0.95

v = ((((s1**2)/n1) + ((s2**2)/n2)) ** 2) / (((((s1**2) / n1) ** 2)/(n1-1)) + ((((s2**2)/n1)**2)/(n2-1)))
t_value = stats.t.ppf((1+cl)/2, v)
error = t_value * ((((s1**2)/n1) + ((s2**2)/n2)) ** 0.5)

diff = xbar1 - xbar2
print(diff+error)
print(diff-error)