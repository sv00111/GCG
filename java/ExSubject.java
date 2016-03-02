import java.util.ArrayList;
import java.util.Random;

public class ExSubject {


	Random rand = new Random();

	Subject sub = new Subject();

	TVerb tVerb = new TVerb();


	public String pick(ArrayList<String> words)  {
		String word = words.get(rand.nextInt(words.size()));
		return word;
	}

	public String generate() {
		String str = null;

		String firstWord;
		String secondWord;

		if(rand.nextInt() % 2 == 0) {
			firstWord = "here";
		} else{
			firstWord = "there"; 
		}

		if(rand.nextInt() % 2 == 0) {
			secondWord = "its";
		} else{
			secondWord = tVerb.generate();
			GCG.objectRequired = true;
		}

		str = firstWord + " " + secondWord + " " + sub.generate() + " that";

		return str;

	}

}