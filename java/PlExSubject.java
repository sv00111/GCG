import java.util.ArrayList;
import java.util.Random;

public class PlExSubject {


	Random rand = new Random();

	Subject sub = new Subject();
	TVerb tVerb = new TVerb();
	PlTVerb plTVerb = new PlTVerb();
	PlSubject plSub = new PlSubject();


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
			secondWord = "are";
		} else{
			secondWord = plTVerb.generate();
			GCG.objectRequired = true;
		}

		str = firstWord + " " + secondWord + " " + plSub.generate() + " that";

		return str;

	}

}