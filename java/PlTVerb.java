import java.util.ArrayList;
import java.util.Random;

public class PlTVerb {
	Random rand = new Random();

	Adverb adv = new Adverb();
	Preposition prep = new Preposition();

	public String pick(ArrayList<String> words)  {
		String word = words.get(rand.nextInt(words.size()));
		return word;
	}

	public String generate() {
		String str = adv.generate() + " " + pick(GCG.pltverbList) + prep.generate();
		GCG.objectRequired = true;
		return str;

	}
}