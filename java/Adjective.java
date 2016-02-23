import java.util.*;

public class Adjective {
	
	ArrayList<String> rules = new ArrayList<>(Arrays.asList("1", "2", "3", "4", "5"));

	public Random rand = new Random();
	public Adverb adv = new Adverb();


	public String pick(ArrayList<String> words)  {
    	String word = words.get(rand.nextInt(words.size()));
    	return word;
  	}

	public String generate() {
		String str = null;
		String rule = pick(rules);

		switch(rule) {
			case "1":
				str = pick(GCG.adjList);
				break;
			case "2":
				str = adv.generate() + " " + pick(GCG.adjList);	
				break;
			case "3":
				str = pick(GCG.adjList) + " " + pick(GCG.adjList);
				break;
			case "4":
				str = adv.generate() + " " + pick(GCG.adjList) + " " + pick(GCG.adjList);
				break;
			case "5":
				str = "";
				break;
		
		}
		return str;

	}

}