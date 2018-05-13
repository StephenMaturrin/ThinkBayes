from thinkbayes import Pmf

#Cookies problem
pmf = Pmf()
pmf.Set('Bowl 1', 0.5)
pmf.Set('Bowl 2', 0.5)

pmf.Mult('Bowl 1', 0.75)
pmf.Mult('Bowl 2', 0.5)

pmf.Normalize()

print (pmf.Prob('Bowl 1'))
