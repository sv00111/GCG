import java.util.*;

public class Subject {

	public Random rand = new Random();
	public Determiner det = new Determiner();
	public Adjective adj = new Adjective();
	public Adverb adv = new Adverb();

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
				//det+Adverb+Adjective+Adjective+Noun
				str = det.generate() + " " + adv.generate() + " " + adj.generate() + " " + adj.generate() + " " + noun.generate(); 
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
			case "PEXS":
					//PlExSubject+PlVerb+[Object]

				System.out.println("PEXS");
				break;

		
		}
		return str;
	}

}

