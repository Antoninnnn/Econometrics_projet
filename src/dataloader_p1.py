#import numpy as py
import pandas as pd

mroz = pd.read_fwf('../data/MROZ.txt', sep="/t", header=None)
mroz = mroz[mroz[6] != '.']
mroz[6] = pd.to_numeric(mroz[6])
mroz[20] = pd.to_numeric(mroz[20])
mroz = mroz[mroz[6] > 0]

inlf = mroz[0]     # =1 if in labor force, 1975
hours = mroz[1]  # hours worked, 1975
kidslt6 = mroz[2]                  # kids < 6 years
kidsge6 = mroz[3]                 # kids 6-18
age = mroz[4]                    # woman's age in yrs
educ = mroz[5]  # years of schooling
wage = mroz[6]                       # estimated wage from earns., hours
repwage = mroz[7]                   # reported wage at interview in 1976
hushrs = mroz[8]  # hours worked by husband, 1975
husage = mroz[9]  # husband's age
huseduc = mroz[10]  # husband's years of schooling
huswage = mroz[11]  # husband's hourly wage, 1975
faminc = mroz[12]  # family income, 1975
mtr = mroz[13]  # fed. marginal tax rate facing woman
motheduc = mroz[14]  # mother's years of schooling
fatheduc = mroz[15]  # father's years of schooling
unem = mroz[16]  # unem. rate in county of resid.
city = mroz[17]                      # =1 if live in SMSA
exper = mroz[18]  # actual labor mkt exper
nwifeinc = mroz[19]  # (faminc - wage*hours)/1000
lwage = mroz[20]  # log(wage)
expersq = mroz[21]  # exper^2
