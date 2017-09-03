import sys
import re
from scipy.stats import ttest_rel
from numpy import std
from numpy import mean

## the database for kf calculation
file = open('pain.txt')

d = {}

d2 = {
	0.16 : 3.22,
	0.4 : 3.61,
	0.6 : 3.84,
	1.0 : 4.08,
	1.4 : 4.17,
	2.0 : 4.31
}

## load pain.txt context to the dictionary 
## (each row of pain.txt contains 4 key:value)
for line in file.readlines():
	line = line.rstrip()
	arr = line.split()	
	d[arr[0]] = arr[1]
	d[arr[2]] = arr[3]
	d[arr[4]] = arr[5]
	d[arr[6]] = arr[7]

file.close()
	
data = raw_input('Please enter your data\'s filename\n' )
n = raw_input('Please enter your n number\n')
n = int(n)
result = 'result.txt'


try:
    file2 = open(data)
except IOError:
    print "File is not accessible. Check your data\'s filename!!"
    sys.exit()

file3 = open(result, 'w+')

print >> file3, 'Xf k Xf+k*0.224 molecular 50%threshold'

t_test_pain = []
for line in file2.readlines():
	pattern = re.compile(r'@')
	match = pattern.search(line)
	if match == None:
		line = line.strip()
		k, Xf = line.split()
		Xf = float(Xf)
		Xf = d2.get(Xf); k = d.get(k)
		if Xf == None or k == None: print >> file3, line, 'No such Kf.'
		else:
			Xf = float(Xf); k = float(k)
			sum = Xf + k*0.224 
			power = pow(10, sum)
			pain = power/10000
			t_test_pain.append(pain) 
			print >> file3, Xf, k, sum, power, pain
	else: print >> file3, line,
if len(t_test_pain) == n * 2:
	group1 = t_test_pain[0:n-1]; group2 = t_test_pain[n:n*2-1]
	mean1 = mean(group1); mean2 = mean(group2)
	sd1 = std(group1); sd2 = std(group2)
	p = ttest_rel(group1, group2)[1]
	print >> file3, '\n', 'mean1 =', mean1, 'sd1 =', sd1, 'mean2 =', mean2, 'sd2 =', sd2, 'p =', p
print 'The analysis has been done.'
file2.close()
file3.close()

