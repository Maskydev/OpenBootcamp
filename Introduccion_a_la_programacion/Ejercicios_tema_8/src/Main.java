public class Main {
    public static void main(String[] args) {

        //Crear un objeto persona en el main.
        Persona persona = new Persona();

        //Utiliza los gets y sets para darle valores a las propiedades edad, nombre y telefono, por último muéstralas por consola.
        persona.setEdad(43);
        persona.setNombre("Oscar");
        persona.setTelefono("972211547");

        String nombre = persona.getNombre();
        int edad = persona.getEdad();
        String telefono = persona.getTelefono();
        System.out.println("Mi nombre es "+nombre + ", tengo "+ edad +" años y mi telefono es el "+ telefono);
    }
}

// Crear clase Persona
class Persona {
    //Crear variables las privadas edad, nombre y telefono de la clase Persona
    private int edad;
    private String nombre;
    private String telefono;

    //Crear gets y sets de cada propiedad.
    public int getEdad() {
        return edad;
    }

    public void setEdad(int edad) {
        this.edad = edad;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getTelefono() {
        return telefono;
    }

    public void setTelefono(String telefono) {
        this.telefono = telefono;
    }

}