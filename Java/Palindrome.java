import java.util.Scanner;
public class Palindrome{	
  String sentence;
  String ns_sentence;
  String s_inv;

  public void palindrome(){
    Scanner input = new Scanner(System.in);
    System.out.print("Escriba la palabra a evaluar: ");
    sentence = input.nextLine();
    ns_sentence = "";
    s_inv = "";

    for (int i = 0; i < sentence.length(); i++){
      if (sentence.charAt(i) == ' '){
        continue;
      }else{
        ns_sentence = ns_sentence + sentence.charAt(i);
      } 
    }

    System.out.println("Palabra sin espacios: " + ns_sentence);

    for (int i = 0; i < ns_sentence.length(); i++){
      s_inv = ns_sentence.charAt(i) + s_inv;
    }

    System.out.println("Palabra invertida: " + s_inv);

    if (s_inv.equals(ns_sentence)){
      System.out.println("Es palindrome");
    }else{ 
      System.out.println("No es palindrome");
    }
  }
}
