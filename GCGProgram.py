import sys
import random


def main():
    print "Hello World"
    helpingVerbs = [line.rstrip('\n') for line in open('helpingVerbs.txt')]
    intransitiveVerbs = [line.rstrip('\n') for line in open('intransitiveVerbs.txt')]
    transitiveVerbs = [line.rstrip('\n') for line in open('transitiveVerbs.txt')]
    adjectives = [line.rstrip('\n') for line in open('adjectives.txt')]
    adverbs = [line.rstrip('\n') for line in open('adverbs.txt')]
    determiners = [line.rstrip('\n') for line in open('determiners.txt')]
    linkingVerbs = [line.rstrip('\n') for line in open('linkingVerbs.txt')]
    nouns = [line.rstrip('\n') for line in open('nouns.txt')]
    pluralDeterminers = [line.rstrip('\n') for line in open('pluralDeterminers.txt')]
    pluralNouns = [line.rstrip('\n') for line in open('pluralNouns.txt')]
    prepositions = [line.rstrip('\n') for line in open('prepositions.txt')]


    picking = True
    listsDictionary = {"helpingVerbs":helpingVerbs, "intransitiveVerbs":intransitiveVerbs, "transitiveVerbs":transitiveVerbs,
                       "adjectives":adjectives, "adverbs":adverbs, "determiners":determiners, "linkingVerbs":linkingVerbs,
                       "nouns":nouns, "pluralDeterminers":pluralDeterminers, "pluralNouns":pluralNouns, "prepositions":prepositions,
                       }

    while(picking):
        name = raw_input("what do you want to pick out of? (write quit to quit)\n-> ")
        if (name == 'quit'):
            picking = False
            continue
        print "name is: " + name
        try:
            print("word is: " + random.choice(listsDictionary[name]))
        except NameError:
            print "list errored"





if __name__ == "__main__":
	 main()