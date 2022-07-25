public class Main {
    public static void main(String[] args) {
        // Usando un if, crear una condición que compare si la variable numeroIf es positivo, negativo, o 0.

        System.out.println("Ejercicio con If:");
        int numeroIf = -5;

        if(numeroIf < 0)  System.out.println("El número es negativo");
        else if (numeroIf > 0) System.out.println("El número es positivo");
        else if (numeroIf == 0) System.out.println("El número es 0");

        /*
            Crea un bucle While, este bucle tendrá que tener como condición que la variable numeroWhile sea inferior a 3, el bloque de código que tendrá el bucle deberá:

            - Incrementar el valor de la variable en uno cada vez que se ejecute.
            - Mostrarlo por pantalla cada vez que se ejecute.
         */

        System.out.println("Ejercicio con While");
        int numeroWhile = 1 ;
        while (numeroWhile < 3) {
            numeroWhile++;
            System.out.println(numeroWhile);
        }

        // Para el bucle Do While, deberás crear la misma estructura que en el While, pero solo se debe ejecutar una vez.

        System.out.println("Ejercicio con Do-While");
        do{
            numeroWhile++;
            System.out.println(numeroWhile);
        } while (numeroWhile < 3);

        // Para el bucle For, crea una variable numeroFor, esta variable tendrá como valor 0 y su condición será que
        // la variable sea igual o menor que 3, se irá incrementando en 1 su valor cada vez que se ejecute y
        // deberá mostrarse por pantalla

        System.out.println("Ejercicio con For");
        for (int numeroFor =0; numeroFor <= 3; numeroFor++){
            System.out.println(numeroFor);
        }

        // Por último, para el Switch, deberás crear la variable estacion, y distintos case para las cuatro estaciones
        // del año. Dependiendo del valor de la variable estacion se deberá mandar un mensaje por consola informando de
        // la estación en la que está. También habrá que poner un default para cuando el valor de la variable no sea
        // una estación.

        System.out.println("Ejercicio con Swift");
        String estacion = "Verano";
        switch (estacion){
            case "Invierno":
                System.out.println("la estación es invierno");
                break;
            case "Primavera":
                System.out.println("la estación es primavera");
                break;
            case "Verano":
                System.out.println("la estación es verano");
                break;
            case "Otoño":
                System.out.println("la estación es otoño");
                break;
            default:
                System.out.println("no se ha introducido ninguna estación");
        }
    }
}