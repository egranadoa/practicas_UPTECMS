import java.util.Scanner;

public class Main{
  public static void main(String args[]){
    int selector = 0;
    Scanner select = new Scanner(System.in);
    System.out.println("************************************");
    System.out.println("PROYECTO PROGRAMACION 2 VERSION JAVA");
    System.out.println("************************************");
    System.out.println(" ");
    System.out.println("Elija el programa:\n(1)Palindromes\n(2)Encontrar Palabra\n(3)Letras Contiguas\n(4)Generador de Semillas");
    System.out.print("Opcion: ");
    selector = select.nextInt();

    switch(selector){
      case 1:
	Palindrome palindrom = new Palindrome();
	palindrom.palindrome();
	break;
      
      default:
	System.out.println("Valor incorrecto");
	break;
    }
  }
}
