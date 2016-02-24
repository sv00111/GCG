import sys
import random

helpingVerbs = []
intransitiveVerbs = []
transitiveVerbs = []
adjectives = []
adverbs = []
determiners = []
linkingVerbs = []
nouns = []
pluralDeterminers = []
pluralNouns = []
prepositions = []


class Sentence:
    def generate(self):
        preposition = False
        return S.generate(S()) + " " + V.generate(V(), preposition) + " " + O.generate(O(), preposition) + "."


class S:
    def generate(self):
        subject_rules = ["subject", "psubject", "esubject"]
        subject_rule = random.choice(subject_rules)
        if subject_rule == "subject":
            ss = Subject.generate(Subject())
            # print "subkjct is " + ss
            return ss
        elif subject_rule == "psubject":
            ss = PluralSubject.generate(PluralSubject())
            # print " psug " + ss
            return ss
        elif subject_rule == "esubject":
            ss = ExistentialSubject.generate(ExistentialSubject())
            # print "esubjject " + ss
            return ss


class Subject:
    def generate(self):
        ss = Determiner.generate(Determiner()) + " " + Adjective.generate(Adjective()) + " " + Noun.generate(Noun())
        # print ss
        return ss


class PluralSubject:
    def generate(self):
        psubject_rules = ["1", "2"]
        psubject_rule = random.choice(psubject_rules)
        if psubject_rule == "1":
            return Adjective.generate(Adjective()) + PluralNoun.generate(PluralNoun())
        elif psubject_rule == "2":
            return PluralDeterminer.generate(PluralDeterminer()) + Adjective.generate(
                Adjective()) + PluralNoun.generate(PluralNoun())


class ExistentialSubject:
    def generate(self):
        esubject_rules = ["1", "2"]
        esubject_rule = random.choice(esubject_rules)
        if esubject_rule == "1":
            return random.choice(["here",
                                  "there"]) + " " + random.choice(["is", TransVerb.generate(TransVerb())]) + " " + \
                   Subject.generate(Subject()) + " that"
        elif esubject_rule == "2":
            return random.choice(["here",
                                  "there"]) + " " + random.choice(["are", TransVerb.generate(TransVerb())]) + " " + \
                   PluralSubject.generate(PluralSubject()) + " that"


class Noun:
    def generate(self):
        rules = ["n", "nn"]
        rule = random.choice(rules)
        if rule == "n":
            ss = random.choice(nouns)
            # print ss + " thats a noun"
            return ss
        elif rule == "nn":
            return random.choice(nouns) + " " + random.choice(nouns)


class PluralNoun:
    def generate(self):
        rules = ["p", "np"]
        rule = random.choice(rules)
        if rule == "p":
            return random.choice(pluralNouns)
        elif rule == "np":
            return random.choice(nouns) + " " + random.choice(pluralNouns)


class V:
    def generate(self, preposition):
        rules = ["TV", "IV", "LV", "HV_V"]
        rule = random.choice(rules)
        preposition = random.choice([True, False])
        pstr = ""
        if preposition:
            pstr = " " + Preposition.generate(Preposition())
        if (rule == "TV"):
            return TransVerb.generate(TransVerb()) + pstr
        elif (rule == "IV"):
            return IntransVerb.generate(IntransVerb()) + pstr
        elif (rule == "LV"):
            return LinkVerbs.generate(LinkVerbs()) + pstr
        elif (rule == "HV_V"):
            rules = ["TV", "IV", "LV"]
            ruleHV = random.choice(rules)
            if (ruleHV == "TV"):
                return HelpVerb.generate(HelpVerb()) + " " + TransVerb.generate(TransVerb()) + pstr
            elif (ruleHV == "IV"):
                return HelpVerb.generate(HelpVerb()) + " " + IntransVerb.generate(IntransVerb()) + pstr
            elif (ruleHV == "LV"):
                return HelpVerb.generate(HelpVerb()) + " " + LinkVerbs.generate(LinkVerbs()) + pstr


class TransVerb:
    def generate(self):
        return Adverbs.generate(Adverbs()) + " " + random.choice(transitiveVerbs)


class IntransVerb:
    def generate(self):
        rules = ["Adverb", "iverb"]
        rule = random.choice(rules)
        if (rule == "Adverb"):
            return Adverbs.generate(Adverbs()) + " " + random.choice(intransitiveVerbs)
        if (rule == "iverb"):
            return random.choice(intransitiveVerbs) + " " + Adverbs.generate(Adverbs())


class LinkVerbs:
    def generate(self):
        rules = ["1", "2"]
        rule = random.choice(rules)
        if (rule == "1"):
            return Adverbs.generate(Adverbs()) + " " + random.choice(linkingVerbs) + " " + Adjective.generate(Adjective())
        elif rule == "2":
            return random.choice(linkingVerbs) + " " + Adverbs.generate(Adverbs()) + " " + Adjective.generate(Adjective())


class HelpVerb:
    def generate(self):
        return random.choice(helpingVerbs)


class Adverbs:
    def generate(self):
        rules = ["1", "2"]
        rule = random.choice(rules)
        if rule == "1":
            return random.choice(adverbs)
        elif rule == "2":
            return ""


class Preposition:
    def generate(self):
        rules = ["1", "2"]
        rule = random.choice(rules)
        if rule == "1":
            return random.choice(prepositions)
        elif rule == "2":
            return ""


class Adjective:
    def generate(self):
        rules = ["1", "2", "3", "4", "5"]
        rule = random.choice(rules)
        if rule == "1":
            return random.choice(adjectives)
        elif rule == "2":
            return random.choice(adverbs) + " " + random.choice(adjectives)
        elif rule == "3":
            return random.choice(adjectives) + " " + random.choice(adjectives)
        elif rule == "4":
            return random.choice(adverbs) + " " + random.choice(adjectives) + " " + random.choice(adjectives)
        elif rule == "5":
            return ""


class Determiner:
    def generate(self):
        ss = random.choice(determiners)
        # print "DET IS: " + ss
        return ss


class PluralDeterminer:
    def generate(self):
        return random.choice(pluralDeterminers)


class O:
    def generate(self, preposition):
        if preposition == True:
            return Object.generate(Object())
        else:
            rules = ["1", "2"]
            rule = random.choice(rules)
            if rule == "1":
                return Object.generate(Object())
            elif rule == "2":
                return " "

class Object:
    def generate(self):
        rules = ["1", "2"]
        rule = random.choice(rules)
        if rule == "1":
            return Subject.generate(Subject())
        elif rule == "2":
            return PluralSubject.generate(PluralSubject())


def main():
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
    global transitiveVerbs
    with open('transitiveVerbs.txt', 'r') as handle:
        for lineTV in handle:
            lineTV = lineTV.strip()
            transitiveVerbs.append(lineTV)
    # transitiveVerbs = [line.rstrip('\n') for line in open('transitiveVerbs.txt')]
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

        # print line
    # pluralDeterminers = [line.rstrip('\n') for line in open('pluralDeterminers.txt')]

    global pluralNouns
    with open('pluralNouns.txt', 'r') as handle:
        for linePN in handle:
            linePN = linePN.strip()
            pluralNouns.append(linePN)

    # pluralNouns = [line.rstrip('\n') for line in open('pluralNouns.txt')]
    global prepositions
    with open('prepositions.txt', 'r') as handle:
        for linePrep in handle:
            linePrep = linePrep.strip()
            prepositions.append(linePrep)
    # prepositions = [line.rstrip('\n') for line in open('prepositions.txt')]


    # print pluralNouns

    # picking = True
    # listsDictionary = {"helpingVerbs": helpingVerbs, "intransitiveVerbs": intransitiveVerbs,
    #                    "transitiveVerbs": transitiveVerbs,
    #                    "adjectives": adjectives, "adverbs": adverbs, "determiners": determiners,
    #                    "linkingVerbs": linkingVerbs,
    #                    "nouns": nouns, "pluralDeterminers": pluralDeterminers, "pluralNouns": pluralNouns,
    #                    "prepositions": prepositions,
    #                    }

    print Sentence.generate(Sentence())
    # while(picking):
    #     name = raw_input("what do you want to pick out of? (write quit to quit)\n-> ")
    #     if (name == 'quit'):
    #         picking = False
    #         continue
    #     print "name is: " + name
    #     try:
    #         print("word is: " + random.choice(listsDictionary[name]))
    #     except NameError:
    #         print "list errored"


if __name__ == "__main__":
    main()
