import java.util.*;

public class Adjective {

	ArrayList<String> rules = new ArrayList<>(Arrays.asList("1", "2"));

	Random rand = new Random();
	Adverb adv = new Adverb();


	public String pick(ArrayList<String> words)  {
		String word = words.get(rand.nextInt(words.size()));
		return word;
	}

	public String generate() {
		String str = null;
		String rule = pick(rules);

		switch(rule) {
		case "1":
			str = " " + pick(GCG.adjList);
			break;
		case "2":
			str = "";
			break;

		}
		return str;

	}

}