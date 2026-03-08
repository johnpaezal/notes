# SUPER EJEMPLO MINIMALISTA DE POO EN PYTHON
# Este ejemplo muestra lo esencial de la Programación Orientada a Objetos:
# - Clases, objetos
# - Atributos públicos, protegidos y privados
# - Encapsulamiento (get/set con @property)
# - Herencia
# - Polimorfismo
# - Composición
# - Métodos especiales (__str__)

# ---------------------- CLASE BASE ----------------------
# Clase principal que sirve como punto de partida para herencia.
class Animal:
    def sonido(self):  # método que se sobreescribirá en clases hijas
        pass

# ---------------------- CLASE PADRE ----------------------
class Mascota(Animal):  # hereda de Animal
    especie = "Animal domestico"  # atributo de clase

    def __init__(self, nombre, edad):
        self.nombre = nombre      # atributo público
        self._edad = edad         # atributo protegido (convención)
        self.__energia = 100      # atributo privado (encapsulado)

    # ------------------ ENCAPSULAMIENTO ------------------
    # Getter estándar para obtener un atributo privado
    @property
    def energia(self):
        return self.__energia

    # Setter estándar para modificar un atributo privado
    @energia.setter
    def energia(self, valor):
        self.__energia = valor

    # ------------------ MÉTODO DE INSTANCIA ------------------
    def comer(self):  # método que modifica estado interno
        self.energia += 10

    # ------------------ MÉTODO TIPO FACTORY ------------------
    def crear_bebe(nombre):  # método simple que crea un objeto
        return Mascota(nombre, 0)

    # ------------------ MÉTODO ESPECIAL ------------------
    def __str__(self):  # define cómo se imprime el objeto
        return f"{self.nombre} ({self._edad} años, energía: {self.energia})"

# ---------------------- HERENCIA + POLIMORFISMO ----------------------
# Cada subclase redefine "sonido", demostrando polimorfismo.
class Perro(Mascota):
    def sonido(self): return "Guau"

class Gato(Mascota):
    def sonido(self): return "Miau"

# ---------------------- COMPOSICION ----------------------
# Un Auto "tiene un" Motor → ejemplo de composición.
class Motor:
    def arrancar(self): return "Motor encendido"

class Auto:
    def __init__(self, marca, motor):
        self.marca = marca
        self.motor = motor

    def encender(self): return self.motor.arrancar()

# ---------------------- USO ----------------------
# Aquí se crean objetos y se demuestra:
# - Instancia de clases
# - Herencia
# - Polimorfismo
# - Composición
if __name__ == "__main__":
    p = Perro("Firulais", 5)
    g = Gato("Michi", 2)

    p.comer()           # modifica energía
    g.energia = 50      # usa setter

    mascotas = [p, g, Mascota.crear_bebe("Bebito")]  # lista de objetos

    for m in mascotas:
        print(m, "=>", m.sonido())  # polimorfismo

    coche = Auto("Toyota", Motor())  # composición
    print(coche.encender())

