import java.util.Scanner;

public class proyecto1ver2 {
    public static void main(String[] args) {
		Scanner entry = new Scanner(System.in);
        int selectorD = 0, despecho = 0, dinero = 0;
        int[] nivelDespecho = {50, 80, 120};
        int[] ventas = {0, 0, 0, 0, 0};
        int[] fBebidas = {2, 5, 10, 20, 80};
        String[] Bebidas = {"Serenata", "Alpargata", "Agua Miel", 
                            "Olimpo", "Que te perdone Dios"};
		
		System.out.print("Ingrese nivel de Despecho: ");
        selectorD = entry.nextInt();
		
		switch (selectorD) {
            case 1:
                despecho = nivelDespecho[0];
                break;
            case 2:
                despecho = nivelDespecho[1];
                break;
            case 3:
                despecho = nivelDespecho[2];
                break;
        
            default:
                System.out.println("Valor Incorrecto");
                break;
        }
		
		if(despecho == 0){
			System.out.println("El despecho es de 0, vuelva cuando este despechado");
		} else {
			System.out.print("Ingrese Capital(Dinero): ");
			dinero = entry.nextInt();
			
			if (dinero <= 9) {
				System.out.println("No posee suficiente dinero, no podemos atenderle");
		} else {
			while (dinero >= 10 && despecho > 0){
				if (dinero >= 120) {
					dinero -= 120;
					despecho -= fBebidas[4];
					ventas[4] += 1;
				} else if (dinero >= 50) {
						dinero -= 50;
						despecho -= fBebidas[3];
						ventas[3] += 1;
					} else if (dinero >= 25) {
							dinero -= 25;
							despecho -= fBebidas[2];
							ventas[2] += 1;
						} else if (dinero >= 15) {
								dinero -= 15;
								despecho -= fBebidas[1];
								ventas[1] += 1;
							} else if (dinero >= 10) {
									dinero -= 10;
									despecho -= fBebidas[0];
									ventas[0] += 1;
								}
				}
			}
		}
		
		if (despecho > 0) {
            System.out.println("No logro aliviar sus penas");
            System.out.println("Sus compras fueron:");
            for (int i = 0; i < Bebidas.length; i++) {
                System.out.print(Bebidas[i]);
                System.out.print(" = ");
                System.out.println(ventas[i]);
            }
        } else {
			System.out.println("Ha logrado aliviar sus penas");
            System.out.println("Sus compras fueron:");
            for (int i = 0; i < Bebidas.length; i++) {
                System.out.print(Bebidas[i]);
                System.out.print(" = ");
                System.out.println(ventas[i]);
            }
		}
	}
}
