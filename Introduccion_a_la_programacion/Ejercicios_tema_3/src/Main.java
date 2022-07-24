public class Main {
    public static void main(String[] args) {
        int resultadoSuma;
        resultadoSuma = sumaNumeros(5,6,10);
        System.out.println("la suma de a, b y c es: " + resultadoSuma);

        Coche miCoche = new Coche();
        miCoche.incrementaPuertas();
        System.out.println("El coche tiene " + miCoche.puertas + " puertas.");
    }

    public static int sumaNumeros(int a, int b, int c){
        return a+b+c;
    }

    static class Coche{
        public int puertas = 0;

        public void incrementaPuertas(){
            this.puertas++;
        }
    }
}