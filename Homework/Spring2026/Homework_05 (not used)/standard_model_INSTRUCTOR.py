"""Module containing the elementary particle classes. """

import numpy as np


class ElementaryParticle:
    """ Elementary particle class.

    Attributes
    ----------
    x : float
        x-position of the particle.

    y: float
        y-position of the particle.

    ptype: str
        Statistics obeyed by the particle.

    charge : float
        Electric charge of the particle.

    mass : float
        Rest mass in MeV of the particle.

    spin: float
        Spin of the particle.

    Methods
    -------
    info():
        Prints particles information.

    is_antiparticle(other):
        Check if the other is this particle anti-particle

    move()
        Move the particle randomly.

    place_at(coord):
        Place the particle at passed coord.


    """
    x = None
    y = None

    ### ANSWER: Students can put the ptype in here or in the __init__
    ptype = None

    def __init__(self, charge, mass, spin):
        """Initialize the particle's attributes.

        Parameters
        ----------
        charge : float
            Electric charge of the particle.

        mass : float
            Rest mass in MeV of the particle.

        spin: float
            Spin of the particle.

        """
        self.charge = charge
        self.mass = mass
        self.spin = spin

    def info(self):
        """Print to scree information about the particle."""

        print(f"The particle has a mass of {self.mass} MeV")
        print(f"The particle's charge is {self.charge} e")
        print(f"The particle's spin is {self.spin}")

    def place_at(self, coord):
        """Place particles at coordinates (x,y).

        Parameters
        ----------
        coord: tuple
            (x,y) coordinates where to place the particle.
        """
        self.x = coord[0]
        self.y = coord[1]

    def move(self):
        """Move the particle by randomly pushing it in both directions."""
        self.x += np.random.randint(low=-1, high=2)
        self.y += np.random.randint(low=-1, high=2)

    ### ANSWER
    def check_type(self):
        """Check whether the particle is a Fermion or a Boson and update the corresponding attribute."""

        if float(self.spin).is_integer():
            self.ptype = "boson"
        else:
            self.ptype = "fermion"

        return self.ptype

    ### ANSWER
    def compare(self, other):
        """Compare this particle with another particle.

        Parameters
        ----------

        other: ElementaryParticle
            Particle to compare with.

        """
        # Check whether you are passing a particle or something else
        if isinstance(other, ElementaryParticle):
            print(f"The two particles have the same charge: {self.charge == other.charge}")
            print(f"The two particles have the same mass: {self.mass == other.mass}")
            print(f"The two particles have the same spin: {self.spin == other.spin}")
        else:
            print(f"Can't compare an elementary particle with {type(other)}. \n"
                  f"Please pass a valid ElementaryParticle object")


class Fermion(ElementaryParticle):
    """
    Fermion: elementary particle that obeys Fermi-Dirac statistics.
    This class inherits the ElementaryParticle class.
    """

    def __init__(self, name, charge, mass, spin):
        """
        Initialize the quark with its name, color charge, electric charge, mass, and spin.

        Parameters
        ----------
        name: string
            Name of the quark.

        charge: float
            Electric charge.

        mass: float
            Mass in MeV.

        spin: float, int
            Spin of the quark. Must be fractional.

        """
        self.name = name
        super().__init__(charge=charge, mass=mass, spin=spin)
        self.check_existence()

    def check_existence(self):

        if self.check_type() == "boson":
            raise ValueError(f"The particle {self.name} cannot exist. Fermions must have fractional spin")

    def is_antiparticle(self, other):

        ret_bool = False
        # Check whether you are passing a particle or something else
        if isinstance(other, Fermion) and self.mass == other.mass and self.spin == other.spin:
            ret_bool = self.charge == - 1.0 * other.charge
        else:
            raise ValueError ("Not a Fermion")

        return ret_bool


class Boson(ElementaryParticle):
    """
    GaugeBoson: elementary particles that obey Bose-Einstein statistics and are force carriers.
    This class inherits the ElementaryParticle class.
    """

    def __init__(self, name, charge, mass, spin):
        """
        Initialize the quark with its name, color charge, electric charge, mass, and spin.

        Parameters
        ----------
        name: string
            Name of the quark.

        charge: float
            Electric charge.

        mass: float
            Mass in MeV.

        spin: float, int
            Spin of the quark. Must be integral number.

        """
        self.name = name
        self.ptype = "boson"
        super().__init__(charge=charge, mass=mass, spin=spin)
        self.check_existence()

    def check_existence(self):

        if self.check_type() == "fermion":
            raise ValueError (f"The particle {self.name} cannot exist. Bosons must have fractional spin")


class CompositeParticle:

    def __init__(self, name, particles):
        """Initialize the composite particles from the component of its attributes.

        Parameters
        ----------
        name: str
            Name of the particle.

        particles : list
            Elementary particles that compose this particle.
        """

        self.name = name
        self.elements = particles

        self.charge = 0.0
        self.mass = 0.0
        self.spin = 0.0

        for ip in self.elements:

            self.charge += ip.charge
            self.mass += ip.mass
            self.spin += ip.spin
