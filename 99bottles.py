beers = range(1,99)

for each_beer in beers :
	print "{0} bottles of beer on the wall, {0} bottles of beer...".format(100 - each_beer)
	print "If one of those bottles should happen to fall, {0} bottles of beer on the wall".format(99 - each_beer)
