# Les capteurs 
## L'idée d'un micro controleur 
Une archi qui dans l'idée est bcp plus simple qu'un proco (genre i7 )

On peut trouvé des I/O style i2c, GPIO, SPI, art 

## Le GPIO
Un fils, soit utilisé en lecture, soit en ecriture 
-> Niveau Logique (A quelle Voltage est le 1 logique) 
-> Peut etre configuré soit en Input ou Output 
Si on est en output :

Warning: Intensité délivré 
	1 led  15-20 mA -> OK 
	1 relai/1moteur -> Magic Smoke 
Warning: Le mode 
Pullup /pulldown /pullupdown 


## Les Can (ADC)

Les convertiseur analogiques numeriques 
Comment dimensionner un CAN 
Par rapport à la tension MAX
Par rapport à la Periode d'echantillon
Le nombre de bit de la représentation 

Pour les CNA C'est l'inverse mais meme problematique 


## Les UART Port serie
Au moins 3 fils ( - /tx/rx)

	GND --------------GND 
	TX ---------\-------TX
	RX -------/  \ ----RX
	
En Port Serie on peut aller sur du 10 M 
Attention au voltage 

9600       8     N1 
Baud   -Taille de la data -Parité 


parité: soit N : None 
		O: odd( pair)
		E: impaire 
		
## i2c
	      |-------------------sda (DATA)
MASTER |-------------------scl (clock)


slave sda branché sur le sda du maitre
	sdl branché sur le sdl du maitre
	
1: C'est le maitre qui génère l'Horloge sur le scl

Chaques slave possedent un ID unique sur 7bits


En I2C on sait mettre la ligne en etat bas, mais pas en etat haut 
ducoup fraudra mettre 2 ressitances de Pullup sur nos lignes pour que ca fonctionne


2 Un esclave peut maintenir la clock lorsqu'il est pas pret à causer 
on appelle ca du HoldDown 
il existe une signalisation sur un bus I2C 
START  
ACK 
NACK 
STOP 
RESTART 

 Etats de sda/ SDL on joue sur les etats de lignes notament 
 
# SPI 
La on aura deux lignes et une clock 


1ligne : MOSI (Master Out, Slave In )
2ligne : MISO (Master In, Slave out )

Meme branchement, soit Mosi sur le slave de mosi etc  
et pour cahque salve un "Chip Select" pour que le slave se sente concérné: avec un GPIO 

# PWM
A la base sert a contorlé les servo
Transmis sous forme de signal carré 
On fait varier le pulse de mon signal carré, ce qui donne une ratio : SIgnal sur signal Max 
on peut calé plusieurs pulse dans une periode








 


	
	
	
	