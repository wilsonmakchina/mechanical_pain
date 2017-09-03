# mechanical_pain
This script is designed to analyze the behavior test of mice mechanical pain

## preparation
behavior data should be changed to such format:
```
@VgatChR2-CPN one week
@pre
OXOXOX 0.4
OXOOXO 0.4
OXXOOX 1.0
OXOXXO 0.6
OXOOXO 0.6
@after
OXOXXO 0.6
OXOOXO 0.6
OXOOXO 1.4
OXOXXO 1.0
OXOOXO 0.6
```

## starting
* running script on Liunx or Mac OS
`python kf.py`
* running script on Windows: click on it

## parameters
After starting, such parameter should be enterd in the shell envrionment
* data filename
* n number for each group
```
Apple$ python kf.py
Please enter your data's filename
test.txt
Please enter your n number
5
```

## output file
The pair t-test result of the data based on 50%threshold value
```
Xf k Xf+k*0.224 molecular 50%threshold
@VgatChR2-CPN one week
@pre
3.61 -0.5 3.498 3147.7483141 0.31477483141
3.61 0.372 3.693328 4935.46413128 0.493546413128
4.08 -0.831 3.893856 7831.69922295 0.783169922295
3.84 1.169 4.101856 12643.1706551 1.26431706551
3.84 0.372 3.923328 8381.6206329 0.83816206329
@after
3.84 1.169 4.101856 12643.1706551 1.26431706551
3.84 0.372 3.923328 8381.6206329 0.83816206329
4.17 0.372 4.253328 17919.5871617 1.79195871617
4.08 1.169 4.341856 21971.3124424 2.19713124424
3.84 0.372 3.923328 8381.6206329 0.83816206329

mean1 = 0.713952058085 sd1 = 0.359031287196 mean2 = 1.5228922723 sd2 = 0.51543950644 p = 0.013834553629 # pair t-test p value
```
