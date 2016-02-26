import sys
import random
import string

adjectives = []
adverbs = []
determiners = []
helpingVerbs = []
intransitiveVerbs = []
linkingVerbs = []
nouns = []
pluralDeterminers = []
pluralHelping = []
pluralIntransitive = []
pluralLinking = []
pluralNouns = []
pluralTransitive = []
prepositions = []
transitiveVerbs = []


class Sentence:
    def generate(self):
        preposition = False
        sentence_rules = ["1", "2", "3", "4"]
        sentence_rule = random.choice(sentence_rules)
        if(sentence_rule == "1"):
            return Subject.generate(Subject()) + Verb.generate(Verb(), preposition) + Object.generate(Object(), preposition)
        elif(sentence_rule == "2"):
            return PlSubject.generate(PlSubject()) + PlVerb.generate(PlVerb(), preposition) + Object.generate(Object(), preposition)
        elif(sentence_rule == "3"):
            return ExSubject.generate(ExSubject(), preposition) + Verb.generate(Verb(), preposition) + Object.generate(Object(), preposition)
        elif(sentence_rule == "4"):
            return PlExSubject.generate(PlExSubject(), preposition) + PlVerb.generate(PlVerb(), preposition) + Object.generate(Object(), preposition)


class Object:
    def generate(self, preposition):
        if preposition == True:
            object_rules = ["1", "2"]
            object_rule = random.choice(object_rules)
            if object_rule == "1":
                return Subject.generate(Subject())
            elif object_rule == "2":
                return PlSubject.generate(PlSubject())
        else:
            rules = ["1", "2"]
            rule = random.choice(rules)
            if rule == "1":
                object_rules = ["1", "2"]
                object_rule = random.choice(object_rules)
                if object_rule == "1":
                    return Subject.generate(Subject())
                elif object_rule == "2":
                    return PlSubject.generate(PlSubject())
            elif rule == "2":
                return " "

class Verb:
    def generate(self, preposition):
        verb_rules = ["1", "2", "3", "4", "5"]
        verb_rule = random.choice(verb_rules)
        if verb_rule == "1":
            return TVerb.generate(TVerb(), preposition)
        elif verb_rule == "2":
            return IVerb.generate(IVerb(), preposition)
        elif verb_rule == "3":
            return LVerb.generate(LVerb(), preposition)
        elif verb_rule == "4":
            return random.choice(helpingVerbs) + " " + TVerb.generate(TVerb(), preposition)
        elif verb_rule == "5":
            return random.choice(helpingVerbs) + " " + IVerb.generate(IVerb(), preposition)

class PlVerb:
    def generate(self, preposition):
        verb_rules = ["1", "2", "3", "4", "5"]
        verb_rule = random.choice(verb_rules)
        if verb_rule == "1":
            return PlTVerb.generate(PlTVerb(), preposition)
        elif verb_rule == "2":
            return PlIVerb.generate(PlIVerb(), preposition)
        elif verb_rule == "3":
            return PlLVerb.generate(PlLVerb(), preposition)
        elif verb_rule == "4":
            return random.choice(pluralHelping) + " " + PlTVerb.generate(PlTVerb(), preposition)
        elif verb_rule == "5":
            return random.choice(pluralHelping) + " " + PlIVerb.generate(PlIVerb(), preposition)

class Subject:
    def generate(self):
        rules = ["1", "2", "3", "4"]
        rule = random.choice(rules)
        if rule == "1":
            return random.choice(determiners) + " " + random.choice(adverbs) + " " + random.choice(adjectives) + " " + random.choice(adjectives) + " " + Noun.generate(Noun())
        elif (rule == "2"):
            return random.choice(determiners) + " " + random.choice(adverbs) + " " + random.choice(adjectives) + " " + Noun.generate(Noun())
        elif (rule == "3"):
            return random.choice(determiners) + " " + Noun.generate(Noun())
        elif (rule == "4"):
            return random.choice(determiners) + " " + Adjective.generate(Adjective()) + Adjective.generate(Adjective()) + " " + Noun.generate(Noun())

        # //det+adverb+adjective+adjective+Noun | det+Noun | det+adverb+adjective+Noun

class PlSubject:
    def generate(self):
        rules = ["1", "2", "3", "4", "5", "6","7","8"]
        rule = random.choice(rules)
        if rule == "1":
            return random.choice(pluralDeterminers) + " " + random.choice(adverbs) + " " + random.choice(adjectives) + " " + random.choice(adjectives) + " " + PlNoun.generate(PlNoun())
        elif rule == "2":
            return random.choice(pluralDeterminers) + " " + random.choice(adverbs) + " " + random.choice(adjectives) + " " + PlNoun.generate(PlNoun())
        elif (rule == "3"):
            return random.choice(pluralDeterminers) + " " + PlNoun.generate(PlNoun())
        elif rule == "4":
            return random.choice(adverbs) + " " + random.choice(adjectives) + " " + random.choice(adjectives) + " " + PlNoun.generate(PlNoun())
        elif rule == "5":
            return random.choice(adverbs) + " " + random.choice(adjectives) + " " + PlNoun.generate(PlNoun())
        elif (rule == "6"):
            return PlNoun.generate(PlNoun())
        elif (rule == "7"):
            return random.choice(pluralDeterminers) + " " + Adjective.generate(Adjective()) + Adjective.generate(Adjective()) + " " + PlNoun.generate(PlNoun())
        elif (rule == "8"):
            return Adjective.generate(Adjective()) + Adjective.generate(Adjective()) + " " + Noun.generate(Noun())



class ExSubject:
    def generate(self, preposition):
        hereThere = ["here ", "there "]
        isSentence = "is "
        hereThereChoice = random.choice(hereThere)
        return hereThereChoice + isSentence + Subject.generate(Subject()) + "that "

class PlExSubject:
    def generate(self, preposition):
        hereThere = ["here ", "there "]
        are = "are "
        hereThereChoice = random.choice(hereThere)
        return hereThereChoice + are + PlSubject.generate(PlSubject()) + "that "

class Noun:
    def generate(self):
        rules = ["1","2"]
        rule = random.choice(rules)
        if rule == "1":
            return random.choice(nouns) + " " + random.choice(nouns) + " "
        elif rule == "2":
            return random.choice(nouns) + " "

class PlNoun:
    def generate(self):
        rules = ["1","2"]
        rule = random.choice(rules)
        if rule == "1":
            return random.choice(nouns) + " " + random.choice(pluralNouns) + " "
        elif rule == "2":
            return random.choice(pluralNouns) + " "

class TVerb:
    def generate(self, preposition):
        preposition = True
        return Adverb.generate(Adverb()) + random.choice(transitiveVerbs) + " " + Prep.generate(Prep(), preposition)

class PlTVerb:
    def generate(self, preposition):
        preposition = True
        return Adverb.generate(Adverb()) + random.choice(pluralTransitive) + " " + Prep.generate(Prep(), preposition)

class IVerb:
    def generate(self, preposition):
        preposition = False
        return Adverb.generate(Adverb()) + random.choice(intransitiveVerbs) + " " + Prep.generate(Prep(), preposition)

class PlIVerb:
    def generate(self, preposition):
        preposition = False
        return Adverb.generate(Adverb()) + random.choice(pluralIntransitive) + " " + Prep.generate(Prep(), preposition)

class LVerb:
    def generate(self, preposition):
        rules = ["1","2", "3", "4"]
        rule = random.choice(rules)
        if rule == "1":
            preposition = False
            return random.choice(linkingVerbs) + " " + Adverb.generate(Adverb()) + random.choice(adjectives) + " "
        if rule == "2":
            preposition = False
            return Adverb.generate(Adverb()) + random.choice(linkingVerbs) + " " + random.choice(adjectives) + " "
        elif rule == "3":
            preposition = True
            return random.choice(linkingVerbs) + " " + Adverb.generate(Adverb()) + Prep.generate(Prep(), preposition)
        elif rule == "4":
            preposition = True
            return Adverb.generate(Adverb()) + random.choice(linkingVerbs) + " " + Prep.generate(Prep(), preposition)

class PlLVerb:
    def generate(self, preposition):
        rules = ["1","2", "3", "4"]
        rule = random.choice(rules)
        if rule == "1":
            preposition = False
            return random.choice(pluralLinking) + " " + Adverb.generate(Adverb()) + random.choice(adjectives) + " "
        if rule == "2":
            preposition = False
            return Adverb.generate(Adverb()) + random.choice(pluralLinking) + " " + random.choice(adjectives) + " "
        elif rule == "3":
            preposition = True
            return random.choice(pluralLinking) + " " + Adverb.generate(Adverb()) + Prep.generate(Prep(), preposition)
        elif rule == "4":
            preposition = True
            return Adverb.generate(Adverb()) + random.choice(pluralLinking) + " " + Prep.generate(Prep(), preposition)


class Adverb:
    def generate(self):
        rules = ["1", "2"]
        rule = random.choice(rules)
        if rule == "1":
            return random.choice(adverbs) + " "
        elif rule == "2":
            return ""

class Adjective:
    def generate(self):
        rules = ["1", "2"]
        rule = random.choice(rules)
        if rule == "1":
            return random.choice(adjectives) + " "
        elif rule == "2":
            return ""

class Prep:
    def generate(self, preposition):
        if preposition:
            rules = ["1", "2"]
            rule = random.choice(rules)
            if rule == "1":
                return random.choice(prepositions) + " "
            elif rule == "2":
                return ""
        else:
            rules = ["1", "2"]
            rule = random.choice(rules)
            if rule == "1":
                preposition = True;
                return random.choice(prepositions) + " "
            elif rule == "2":
                return ""



def upperfirst(x):
    return x[0].upper() + x[1:]


def main():

    global adjectives
    with open('adjectives.txt', 'r') as handle:
        for lineaj in handle:
            lineaj = lineaj.strip()
            adjectives.append(lineaj)
    # adjectives = [line.rstrip('\n') for line in open('adjectives.txt')]
    global adverbs
    with open('adverbs.txt', 'r') as handle:
        for linead in handle:
            linead = linead.strip()
            adverbs.append(linead)
    # adverbs = [line.rstrip('\n') for line in open('adverbs.txt')]
    global determiners
    with open('determiners.txt', 'r') as handle:
        for lineDet in handle:
            lineDet = lineDet.strip()
            determiners.append(lineDet)
    # determiners = [line.rstrip('\n') for line in open('determiners.txt')]

    # print "Hello World"
    global helpingVerbs
    with open('helpingVerbs.txt', 'r') as handle:
        for lineHV in handle:
            lineHV = lineHV.strip()
            helpingVerbs.append(lineHV)
    # helpingVerbs = [line.rstrip('\n') for line in open('helpingVerbs.txt')]

    global intransitiveVerbs
    with open('intransitiveVerbs.txt', 'r') as handle:
        for lineITV in handle:
            lineITV = lineITV.strip()
            intransitiveVerbs.append(lineITV)
    # intransitiveVerbs = [line.rstrip('\n') for line in open('intransitiveVerbs.txt')]

    global linkingVerbs
    with open('linkingVerbs.txt', 'r') as handle:
        for lineVERB in handle:
            lineVERB = lineVERB.strip()
            linkingVerbs.append(lineVERB)

    # linkingVerbs = [line.rstrip('\n') for line in open('linkingVerbs.txt')]

    global nouns
    with open('nouns.txt', 'r') as handle:
        for lineN in handle:
            lineN = lineN.strip()
            nouns.append(lineN)

        # print " ded " + line

    global pluralDeterminers
    with open('pluralDeterminers.txt', 'r') as handle:
        for linepD in handle:
            linepD = linepD.strip()
            pluralDeterminers.append(linepD)

    global pluralHelping
    with open('pluralHelpingVerbs.txt', 'r') as handle:
        for linepHV in handle:
            linepHV = linepHV.strip()
            pluralHelping.append(linepHV)
        # print line

    global pluralIntransitive
    with open('pluralIntransitiveVerbs.txt', 'r') as handle:
        for linepplIV in handle:
            linepplIV = linepplIV.strip()
            pluralIntransitive.append(linepplIV)
        # print line

    global pluralLinking
    with open('pluralLinkingVerbs.txt', 'r') as handle:
        for linepLV in handle:
            linepLV = linepLV.strip()
            pluralLinking.append(linepLV)
        # print line
    # pluralDeterminers = [line.rstrip('\n') for line in open('pluralDeterminers.txt')]

    global pluralNouns
    with open('pluralNouns.txt', 'r') as handle:
        for linePN in handle:
            linePN = linePN.strip()
            pluralNouns.append(linePN)

    global pluralTransitive
    with open('pluralTransitiveVerbs.txt', 'r') as handle:
        for linePTV in handle:
            linePTV = linePTV.strip()
            pluralTransitive.append(linePTV)
    # pluralNouns = [line.rstrip('\n') for line in open('pluralNouns.txt')]
    global prepositions
    with open('prepositions.txt', 'r') as handle:
        for linePrep in handle:
            linePrep = linePrep.strip()
            prepositions.append(linePrep)
    # prepositions = [line.rstrip('\n') for line in open('prepositions.txt')]

    global transitiveVerbs
    with open('transitiveVerbs.txt', 'r') as handle:
        for lineTV in handle:
            lineTV = lineTV.strip()
            transitiveVerbs.append(lineTV)
    # transitiveVerbs = [line.rstrip('\n') for line in open('transitiveVerbs.txt')]


    sentence = upperfirst(Sentence.generate(Sentence()))
    sentence = sentence[:-1]
    sentence = sentence + "."
    # the first letter is capatilized and a period is added to the end. 
    print sentence



if __name__ == "__main__":
    main()
