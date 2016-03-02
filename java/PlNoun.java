import java.util.ArrayList;
import java.util.Arrays;
import java.util.Random;

public class PlNoun {

	ArrayList<String> rules = new ArrayList<>(Arrays.asList("1", "2"));

	Random rand = new Random();


	public String pick(ArrayList<String> words)  {
		String word = words.get(rand.nextInt(words.size()));
		return word;
	}

	public String generate() {
		String str = null;
		String rule = pick(rules);

		switch(rule) {
		case "1":
			str = pick(GCG.plnounList);
			break;
		case "2":
			str = pick(GCG.nounList) + " " + pick(GCG.plnounList);
			break;

		}
		return str;

	}

}