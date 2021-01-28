# python-rpg-api

## Description

This project is an RPG API. In this game, you can fight monsters in a fantasy world (dragons, rats, wolves, chicken, ...).
It's made in Python using Fast API, Docker, docker-compose and SQL Alchemy.

## Endpoints

### Player

- GET /api/players/ : List all the players and their information (name and level)
- POST /api/players/create : Create a new player with the given username (must be specified as 'username' in the body).
- POST /api/players/info/{username} : Get all the information about a player using its username. The information are:
  - a status message about their health points
  - level
  - gold
  - experience
- POST /api/players/rest : Rest a player to get back some hp using its username.
- POST /api/players/{username}/attack/{monsterId} : Make a player using its username attack a monster using its monsterId.  
  When attacking a monster, it fights back and damages the player.  
  By killing monsters, the player earns gold and experience points. With this experience, the player can level up.
  When dying, the player loses half of his gold but revives.

### Monster

- GET /api/monsters/list : List all the monsters currently alive (with their id, names and health points).
- GET /api/monsters/info/{monsterId} : Get the information about a monster using its monsterId:
  - name
  - id
  - health points
  - damage
  - gold reward
  - experience reward

## How to use

The project requires Docker and docker-compose.

Run the API:
    
    sudo ./run.sh
    
Run the tests:

    sudo ./run_tests.sh
    
## Authors

* [James RICHET (Doomky)](https://github.com/Doomky)
* [Ingo BRAEKMAN (Inkech)](https://github.com/Inkech)
* [Bastien SEIRA (bastien-seira)](https://github.com/bastien-seira)
* [Allan CANTIN (xDSx77)](https://github.com/xDSx77)