#PTS - Dom�ca �loha 1
Program uchov�va zoznam u�astn�kov a ich aktu�lny stav bodov v s�ta�i.
Po spusten� si program od u��vate�a vyp�ta heslo. Potom program �ak� na pr�kazy od u��vate�a,
ktor� n�sledne vykon�.

##Zoznam pr�kazov:

'points <name> <number>'
  Prid� hr��ovi <name> <number> bodov. ��slo m��e by� aj z�porn�.
  Ak hr�� <name> e�te nie je evidovan� prid� ho do zoznamu s <number> bodmi.

'reduce <number>'
  Zn�i po�et bodov ka�d�ho hr��a o <number>%. V�sledok sa zaokr�hli na cel� ��sla nadol.

'junior <name>'
  Ozna��, �e hr�� <name> je junior

'ranking'
  Vyp�e cel� poradie. Hr��ov zorad�me pod�a po�tu bodov.

'ranking junior'
  Vyp�e poradie medzi juniormi.

'quit'
  Ukon�� program.


Ak u��vate� zad� pr�kazy points, reduce, junior, a quit syst�m si najprv vyp�ta password
a pr�kaz vykon� iba v pr�pade, �e password je spr�vny. 
Ak zadan� pr�kaz program nerozozn�, vyp�e "Nerozpoznany prikaz"










