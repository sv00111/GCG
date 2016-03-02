import java.util.ArrayList;
import java.util.Random;

public class TVerb {

	Adjective adj = new Adjective();
	Adverb adv = new Adverb();
	Noun noun = new Noun();
	Preposition prep = new Preposition();

	Random rand = new Random();


	public String pick(ArrayList<String> words)  {
		String word = words.get(rand.nextInt(words.size()));
		return word;
	}

	public String generate() {
		String str = adv.generate() + " " + pick(GCG.tverbList) + prep.generate();
		GCG.objectRequired = true;
		return str;
	}

}

