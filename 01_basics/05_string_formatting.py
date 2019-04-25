__author__ = 'dev'
age = 24
print("my age is " + str(age) + " years")
# Old replacement syntax
print("My age is %d years" % age)
print("My age is %d %s, %d %s" % (age, "years", 6, "months"))
# New replacement syntax
print("my age is {0} years".format(age))

