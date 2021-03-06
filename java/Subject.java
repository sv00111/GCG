import java.util.*;

public class Subject {

	Adjective adj = new Adjective();
	Adverb adv = new Adverb();
	Noun noun = new Noun();

	Random rand = new Random();


	public String pick(ArrayList<String> words)  {
		String word = words.get(rand.nextInt(words.size()));
		return word;
	}

	public String generate() {
		String str = pick(GCG.detList) + adv.generate() + adj.generate() + adj.generate() + " " + noun.generate();
		return str;
	}

}

