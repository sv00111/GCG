def main():
	print "Hello World"
	helpingVerbs = [line.rstrip('\n') for line in open('helpingVerbs.txt')]
	intransitiveVerbs = [line.rstrip('\n') for line in open('intransitiveVerbs.txt')]
	transitiveVerbs = [line.rstrip('\n') for line in open('transitiveVerbs.txt')]
	print "helping: "
	print("\n".join(helpingVerbs))
	print "\n\nintranstive: "
	print("\n".join(intransitiveVerbs))
	print "\n\ntransitiveVerbs: "
	print("\n".join(transitiveVerbs))
	


if __name__ == "__main__":
	 main()
