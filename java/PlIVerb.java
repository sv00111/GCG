import java.util.ArrayList;
import java.util.Random;

public class PlIVerb {

	Preposition prep = new Preposition();
	Adverb adv = new Adverb();

	Random rand = new Random();


	public String pick(ArrayList<String> words)  {
		String word = words.get(rand.nextInt(words.size()));
		return word;
	}

	public String generate() {
		String str = adv.generate() + " " + pick(GCG.pliverbList) + prep.generate();
		return str;
	}

}

