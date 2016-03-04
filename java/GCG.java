import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.io.*;
import java.util.*;

import javax.swing.JFrame;
import javax.swing.JTextField;

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

	public static boolean objectRequired = false;
	public static boolean objectNotAllowed = false;

	public static String str = null;


	public static void main(String[] args) {
		createJFrame();
		loadLists();
		generateSentance();
	}

	public static void createJFrame() {
		JTextField textField = new JTextField();
		textField.addKeyListener(new MKeyListener());
		JFrame jframe = new JFrame();
		jframe.add(textField);
		jframe.setSize(400, 50);
		jframe.setVisible(true);
	}

	public static void generateSentance() {
		ArrayList<String> rules = new ArrayList<>(Arrays.asList("S", "PS", "EXS", "PEXS"));

		Random rand = new Random();

		Subject subject = new Subject();
		PlSubject plSubject = new PlSubject();
		ExSubject exSubject = new ExSubject();
		PlExSubject plExSubject = new PlExSubject();
		Verb verb = new Verb();
		PlVerb plVerb = new PlVerb();
		Obj obj = new Obj();

		String rule = rules.get(rand.nextInt(rules.size()));
		switch(rule) {
		case "S":
			str = subject.generate() + " " + verb.generate();
			if((rand.nextInt() % 2 == 0 && !objectNotAllowed) || objectRequired ) 
				str += (" " + obj.generate());
			break;
		case "PS":
			str = plSubject.generate() + " " + plVerb.generate();
			break;
		case "EXS":
			str = exSubject.generate() + " " + verb.generate();
			break;
		case "PEXS":
			str = plExSubject.generate() +  " " + plVerb.generate();
			break;
		}

		objectNotAllowed = false;
		objectRequired = false;
	}



	public static void loadLists() {
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


class MKeyListener extends KeyAdapter {
	int count = 0;
	@Override
	public void keyPressed(KeyEvent event) {
		if(event.getKeyCode() == 'Q') {
			System.exit(1);;
		}
		String[] split = GCG.str.split("\\s+");

		if(count == (split.length -1)) {
			System.out.print(split[count] + ". ");
			GCG.generateSentance();
			count = 0;
		} else {
			System.out.print(split[count] + " ");
			count++;
		}
	}
}
