import java.util.ArrayList;
import java.util.Arrays;
import java.util.Random;

public class PlLVerb {

	ArrayList<String> rules = new ArrayList<>(Arrays.asList("1", "2", "3", "4"));

	Random rand = new Random();

	Adverb adv = new Adverb();
	Preposition prep = new Preposition();

	public String pick(ArrayList<String> words)  {
		String word = words.get(rand.nextInt(words.size()));
		return word;
	}

	public String generate() {
		String str = null;
		String rule = pick(rules);
		switch(rule) {
		case "1":
			str = pick(GCG.pllverbList) + adv.generate() + " " + pick(GCG.adjList);
			GCG.objectNotAllowed = true;
			break;
		case "2":
			str = adv.generate() + " " + pick(GCG.pllverbList) + " " + pick(GCG.adjList);
			GCG.objectNotAllowed = true;
			break;
		case "3":
			str = pick(GCG.pllverbList) + adv.generate() + prep.generate();
			GCG.objectRequired = true;
			break;
		case "4":
			str = adv.generate() + " " + pick(GCG.pllverbList) + prep.generate();	
			GCG.objectRequired = true;
			break;
		}
		return str;

	}

}
