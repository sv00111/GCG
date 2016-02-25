import java.io.*;
import java.util.*;

public class GCG {
	public static ArrayList<String> adjList;
	public static ArrayList<String> advList;
	public static ArrayList<String> nounList;
	public static ArrayList<String> detList;
	public static ArrayList<String> hverbList;
	public static ArrayList<String> iverbList;
	public static ArrayList<String> lverbList;
	public static ArrayList<String> pdetList;
	public static ArrayList<String> phverbList;
	public static ArrayList<String> pliverbList;
	public static ArrayList<String> pllverbList;
	public static ArrayList<String> plnounList;
	public static ArrayList<String> pltverbList;
	public static ArrayList<String> prepList;
	public static ArrayList<String> tverbList;

	public static void main(String[] args) {
		adjList = loadDict("adjectives.txt");
		advList = loadDict("adverbs.txt");
		nounList = loadDict("nouns.txt");
		detList = loadDict("determiners.txt");
		hverbList = loadDict("helpingVerbs.txt");
		iverbList = loadDict("intransitiveVerbs.txt");
		lverbList = loadDict("linkingVerbs.txt");
		pdetList = loadDict("pluralDeterminers.txt");
		phverbList = loadDict("pluralHelpingVerbs.txt");
		pliverbList = loadDict("pluralIntransitiveVerbs.txt");
		pllverbList = loadDict("pluralLinkingVerbs.txt");
		plnounList = loadDict("pluralnouns.txt");
		pltverbList = loadDict("pluralTransitiveVerbs.txt");
		prepList = loadDict("prepositions.txt");
		tverbList = loadDict("transitiveVerbs.txt");
		
		//ArrayList<String> rules = new ArrayList<>(Arrays.asList("S", "PS", "EXS", "PEXS"));
		//Random rand = new Random();
		Determiner det = new Determiner();
		Adverb adv = new Adverb();
		Adjective adj = new Adjective();
		Noun noun = new Noun();
		PlSubject plSubject = new PlSubject();
		//String word = rules.get(rand.nextInt(rules.size()));

		String rule = "PS";
		String str = null;
		switch(rule) {
			case "S":
				//det+Adverb+Adjective+Adjective+Noun
				str = det.generate() + " " + adv.generate() + " " + adj.generate() + " " + adj.generate() + " " + noun.generate(); 
				break;
			case "PS":
				//Adjective + PlNoun | pdet + Adjective + PlNoun
				str = plSubject.generate();
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
		System.out.println(str);
	}

	private static ArrayList<String> loadDict (String filename) {
		ArrayList<String> list = new ArrayList<>();
		Scanner scan;
		try {
			scan = new Scanner (new File (filename));
		}
		catch (FileNotFoundException e) {
			System.out.println("Error: File not found: " + filename);
			return null;
		}
		while (scan.hasNextLine()) {
			list.add(scan.next());
		}
		scan.close();
		return list;
	}
}
