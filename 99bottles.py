
#define how man beers you will have
beers = range(1,99)

# Using a loop to go through each value. Since we want to start with 99 bottles we used the 100-each_beer to do that.
for each_beer in beers :
	print "{0} bottles of beer on the wall, {0} bottles of beer...".format(100 - each_beer)
	print "If one of those bottles should happen to fall, {0} bottles of beer on the wall".format(99 - each_beer)
