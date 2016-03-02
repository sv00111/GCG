import java.util.ArrayList;
import java.util.Arrays;
import java.util.Random;

public class Verb {

	ArrayList<String> rules = new ArrayList<>(Arrays.asList("1", "2", "3", "4", "5"));

	Random rand = new Random();
	TVerb tVerb = new TVerb();
	IVerb iVerb = new IVerb();
	LVerb lVerb = new LVerb();

	public String pick(ArrayList<String> words)  {
		String word = words.get(rand.nextInt(words.size()));
		return word;
	}

	public String generate() {
		String str = null;
		String rule = pick(rules);

		switch(rule) {
		case "1":
			str = tVerb.generate();
			break;
		case "2":
			str = iVerb.generate();
			break;
		case "3":
			str = lVerb.generate();
			break;
		case "4":
			str = pick(GCG.hverbList) + " " + tVerb.generate();
			break;
		case "5":
			str = pick(GCG.hverbList) + " " + iVerb.generate();
			break;

		}
		return str;

	}

}