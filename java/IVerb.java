import java.util.ArrayList;
import java.util.Random;

public class IVerb {

	Adjective adj = new Adjective();
	Adverb adv = new Adverb();

	Random rand = new Random();


	public String pick(ArrayList<String> words)  {
		String word = words.get(rand.nextInt(words.size()));
		return word;
	}

	public String generate() {
		String str = adv.generate() + " " + pick(GCG.iverbList) + adj.generate();
		return str;
	}

}

