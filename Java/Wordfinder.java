import java.util.Scanner;

public class Wordfinder{
  String sentence;
  String word;
  String ns_sentence;

  public void findWord(){
    Scanner input = new Scanner(System.in);
    ns_sentence = "";
    System.out.print("Escriba una frase: ");
    sentence = input.nextLine();
    System.out.print("Escriba la palabra a buscar: ");
    word = input.nextLine();

    for (int i = 0; i < sentence.length(); i++){
      if (sentence.charAt(i) == ' '){
        continue;
      }else{
        ns_sentence = ns_sentence + sentence.charAt(i); 
      }
    }

    if (ns_sentence.contains(word)){
      System.out.println("Verdadero");
    }else{
      System.out.println("Falso");
    }
  }
}
