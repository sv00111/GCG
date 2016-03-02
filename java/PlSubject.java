import java.util.ArrayList;
import java.util.Arrays;
import java.util.Random;

public class PlSubject {

	ArrayList<String> rules = new ArrayList<>(Arrays.asList("1", "2"));

	Random rand = new Random();

	Adverb adv = new Adverb();
	Adjective adj = new Adjective();
	PlNoun plNoun = new PlNoun();


	public String pick(ArrayList<String> words)  {
		String word = words.get(rand.nextInt(words.size()));
		return word;
	}

	public String generate() {
		String str = null;
		String rule = pick(rules);

		switch(rule) {
		case "1":
			str = pick(GCG.pdetList) + adv.generate() + adj.generate() 
			+ adj.generate() + " " + plNoun.generate();
			break;
		case "2":
			str = adv.generate() + adj.generate() + adj.generate() + " " + plNoun.generate();
			break;

		}
		return str;

	}

}