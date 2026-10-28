<div align="center">
  <img src="DemonologEEE.png" alt="DemonologEEE Logo">
</div>

*DemonologEEE* is a terminal-based paranormal investigation game based on the Roblox Game Demonology. Your goal is to clear all 3 floors of the EEE building by identifying the ghost haunting each floor. You start on the 1st floor and advance floor-by-floor upon each successful exorcism.


## Objectives & Mechanics

### Locate
Select *[1] Move Room* from the main menu to navigate through the available rooms on the floor map. 
* The rooms on each floor are laid out in order. 
* Your distance from the ghost affects tool readings—getting closer raises your EMF signal level and lowers ambient room temperature. 
* Plan your path carefully, as moving between rooms consumes mental energy (Sanity).

### Use Tools
Deploy your 6 inventory tools across rooms to discover the entity's traits. Each ghost type is defined by a unique combination of exactly 3 evidences. 
* Items like the Spirit Box can be used anywhere on the floor to get a response (if the ghost possesses that trait).
* Physical tools like the Spirit Book, Blacklight, Flower Pot, and Thermometer require you to pinpoint the ghost's actual haunt room to trigger a positive reading.

### Identify Ghost Type
Cross-reference your confirmed clues against your Ghost Journal (*[4] View Journal*). Once you match all 3 evidences to one of the 9 entity profiles, select *[3] Guess Entity* to execute an exorcism:
* *Correct Guess:* Successfully exorcises the ghost, clearing the floor so you can move up to the next level.
* *Incorrect Guess:* Angers the ghost with a false guess, causing a severe drop in your remaining sanity.


## Sanity System

Sanity represents your mental stamina against the dark paranormal environment. You start with *100% sanity* on each floor, but taking actions in the building steadily wears you down. The higher you go into the building, the faster your sanity drains.

<div align="center">

| Action | Floor 1 (Base) | Floor 2 (2x Drain) | Floor 3 (3x Drain) |
| :--- | :--- | :--- | :--- |
| *Moving Rooms* | -2% | -4% | -6% |
| *Using Items* | -5% | -10% | -15% |
| *Wrong Entity Guess* | -25% | -50% | -75% |

</div>

*0% Sanity (Game Over):* If your sanity reaches 0%, the darkness consumes you and the hunt immediately ends.


## How to Run

1. Run the script using the following command:
   ```bash
   python main.py