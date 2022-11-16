import random
from scipy import rand


class Rocket:
    """Klasa Rakieta
    """
    def __init__(self,hight:float=0.0,power:float=1.0) -> None:
        """Konstruktor

        Args:
            hight (float, optional): _description_. Defaults to 0.0.
            power (float, optional): _description_. Defaults to 1.0.
        """
        self.hight = hight
        self.power = power
    
    def __str__(self) -> str:
        return "Rakieta o mocy " + str(self.power) + " znajduje się na wysokości " + str(self.hight)


    def move_up(self) -> None:
        """Metoda do poruszania się do góry w zalerzności od mocy rakiety
        """
        self.hight += 1 * self.power   #liniowy wzrost
        #self.hight = random.randint(1,10) * self.power  # randomowy wzrost wysokości na podstawie mocy




class BlockOfRockets:
    def __init__(self,AmmoutOfRockets:int=3) -> None:
        """Class which creates a block of rockets
        Args:
            AmmoutOfRockets (int, optional): Ammount of rocketst that we want to have in our block . Defaults to 3.
        """
        self.AmmountOfRockets = AmmoutOfRockets
        self.rockets = [Rocket(i,i) for i in range(self.AmmountOfRockets)]

    def MoveBlock(self):
        """ Moves rocket up accordingly to power of the specyfic rocket
        """
        for rocket in self.rockets:
            rocket.hight += 1 * rocket.power

    def __getitem__(self,key:int=0) -> Rocket:
        """Returns one rocket item when we try to call specyfiv index
        Args:
            key (int, optional): Number of rocket we chose. Defaults to 0.
        Returns:
            Rocket: Rocket object
        """
        return self.rockets[key]

    def __setitem__(self,key:int=0,value:float=1.0) -> None:
        """Sets chosen value as new power atribute

        Args:
            key (int, optional): Number of the chosen rocket. Defaults to 0.
            value (float, optional): New power atribute of a chosen rocket. Defaults to 1.0.
        """
        self.rockets[key].power = value

    def __str__(self) -> str:
        """ Print info about Block of rockets
        """
        Print = ''
        for Rocket in self.rockets:
            Print += Rocket.__str__() + '\n'
        return Print
            
        