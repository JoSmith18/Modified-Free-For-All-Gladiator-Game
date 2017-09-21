# Free For All Gladiator Game
___
## About This Project
This is a terminal based game written in python3.5


This is an Object Oriented Programming game, and I modeled it after a similar 
application using a Dictionary data structure. 

It has:


*class FighterWorld* where the gameplay takes place.


*class Fighter* where the fighter attributes are given.


*class Battle* where the battle is set up.

___

## Getting Started
clone this repository to your local machine to play the game

this application uses termcolor, so you will need to install that.


termcolor documentation: [https://pypi.python.org/pypi/termcolor]


```$ pip3 install termcolor```


the user interactions are programmed in the shell


```/Modified-Free-For-All-Gladiator-Game $ python3 shell.py```
___

## Using the Application
After starting up the application the user is asked rather the fighter will be a computer controlled AI,their is a limit, or a human. This last until done is typed into the terminal.


When the battle begins each AI randomly chooses an attack option given to them based on rage and health and human users pick which option they want.


If the battle has more than two fighters the human user pick who they want to attack(if that is the option they chose) and the AI randomly chooses someone.


When health is zero the fighter is taken out of the arena and no longer has a turn. The battle last as long as more than one person is alive.


## What I Learned
This was my first time implementing classes into an application.


I learned the use of termcolor.
