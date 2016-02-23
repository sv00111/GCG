import java.util.*;

public class Subject {

	public String[] rules = { "S", "PS", "EXS" };

	public Random rand = new Random();
	public Determiner det = new Determiner();
	public Adjective adj = new Adjective();
	public Noun noun = new Noun();



	public String pick(String[] words)  {
    	String word = words[rand.nextInt(words.length)];
    	return word;
  	}

	public String generate() {
		String str = null;
		String rule = "S";
		switch(rule) {
			case "S":
				str = det.generate() + " " + adj.generate() + " " + noun.generate();
				break;
			case "PS":
				//Adjective + PlNoun | pdet + Adjective + PlNoun
				System.out.println("PS");
				//str = pick(nouns) + " " + pick(noun);
				break;
			case "EXS":
				//(“here” / “there”) + (“is” / Verb) + Subject + “that” 
				// | (“here” / “there”) + (“are” / Verb) + PlSubject + “that”

				System.out.println("EXS");
				break;

		
		}
		return str;
	}

}

