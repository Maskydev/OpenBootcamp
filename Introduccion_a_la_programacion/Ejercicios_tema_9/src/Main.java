public class Main {
    public static void main(String[] args) {

        //Crea ahora un objeto de la clase Cliente que debe tener como propiedades la edad, el telefono, el nombre y
        // el credito, tienes que darles valor y mostrarlas por pantalla.
        Cliente cliente = new Cliente();
        cliente.setEdad(43);
        cliente.setNombre("Oscar");
        cliente.setTelefono(912365478);
        System.out.println(cliente.getNombre()+" tiene "+ cliente.getEdad()+" años y su telefono es " + cliente.getTelefono());

        // Una vez hecho esto, haz lo mismo con la clase Trabajador que herede de Persona, y con una variable salario
        // que solo tenga la clase Trabajador.
        Trabajador trabajador = new Trabajador();
        trabajador.setEdad(25);
        trabajador.setNombre("Pedro");
        trabajador.setTelefono(912365478);
        trabajador.setSalario(1100);
        System.out.println(trabajador.getNombre()+" tiene "+ trabajador.getEdad()+" años, su telefono es " + trabajador.getTelefono()+" y su salario es de "+trabajador.getSalario());
    }
}

/*
Crea una clase Persona con las siguientes variables:
 - La edad
 - El nombre
 - El teléfono
 */

class Persona {
    int edad;
    String nombre;
    int telefono;
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

    public int getTelefono() {
        return telefono;
    }

    public void setTelefono(int telefono) {
        this.telefono = telefono;
    }

}

// Una vez creada la clase, crea una nueva clase Cliente que herede de Persona, esta nueva clase tendrá la
// variable credito solo para esa clase.
class Cliente extends Persona{
    int credito;

    public int getCredito() {
        return credito;
    }

    public void setCredito(int credito) {
        this.credito = credito;
    }
}

class Trabajador extends Persona{
    int salario;
    public int getSalario() {
        return salario;
    }

    public void setSalario(int salario) {
        this.salario = salario;
    }
}