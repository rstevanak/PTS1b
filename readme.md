#PTS - Domáca úloha 1
Program uchováva zoznam uèastníkov a ich aktuálny stav bodov v sútai.
Po spustení si program od uívate¾a vypıta heslo. Potom program èaká na príkazy od uívate¾a,
ktoré následne vykoná.

##Zoznam príkazov:

'points <name> <number>'
  Pridá hráèovi <name> <number> bodov. Èíslo môe by aj záporné.
  Ak hráè <name> ešte nie je evidovanı pridá ho do zoznamu s <number> bodmi.

'reduce <number>'
  Zníi poèet bodov kadého hráèa o <number>%. Vısledok sa zaokrúhli na celé èísla nadol.

'junior <name>'
  Oznaèí, e hráè <name> je junior

'ranking'
  Vypíše celé poradie. Hráèov zoradíme pod¾a poètu bodov.

'ranking junior'
  Vypíše poradie medzi juniormi.

'quit'
  Ukonèí program.


Ak uívate¾ zadá príkazy points, reduce, junior, a quit systém si najprv vypıta password
a príkaz vykoná iba v prípade, e password je správny. 
Ak zadanı príkaz program nerozozná, vypíše "Nerozpoznany prikaz"










