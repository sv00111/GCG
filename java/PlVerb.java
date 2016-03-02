import java.util.ArrayList;
import java.util.Arrays;
import java.util.Random;

public class PlVerb {

	ArrayList<String> rules = new ArrayList<>(Arrays.asList("1", "2", "3", "4", "5"));

	Random rand = new Random();
	PlTVerb plTVerb = new PlTVerb();
	PlIVerb plIVerb = new PlIVerb();
	PlLVerb plLVerb = new PlLVerb();



	public String pick(ArrayList<String> words)  {
		String word = words.get(rand.nextInt(words.size()));
		return word;
	}

	public String generate() {
		String str = null;
		String rule = pick(rules);

		switch(rule) {
		case "1":
			str = plTVerb.generate();
			break;
		case "2":
			str = plIVerb.generate();
			break;
		case "3":
			str = plLVerb.generate();
			break;
		case "4":
			str = pick(GCG.phverbList) + " " + plTVerb.generate();
			break;
		case "5":
			str = pick(GCG.phverbList) + " " + plIVerb.generate();
			break;

		}
		return str;

	}

}