import java.io.*;
import java.util.*;

public class GCG {
	public static ArrayList<String> adjList;
	public static ArrayList<String> advList;
	public static ArrayList<String> nounList;
	public static ArrayList<String> detList;

	
	public static void main(String[] args) {
		adjList = loadDict("adjectives.txt");
		advList = loadDict("adverbs.txt");
		nounList = loadDict("nouns.txt");
		detList = loadDict("determiners.txt");

		Subject subject = new Subject();
		String sub = subject.generate();
		
		System.out.println(sub);

	}
	
	private static ArrayList loadDict (String filename) {
		ArrayList list = new ArrayList();
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
		return list;
	}
}
