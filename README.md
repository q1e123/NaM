# Not a Moneky
Collection of bots made for educational purposes O:)

# Current bots
* ninjamanager

# Usage

I am going to use one pipenv for all bots, so it doesn't matter what bot you want to use, you need to do this first:

> pipenv install

After it all depends on the bot.

## ninjamanager

> pipenv run python ninjamanager.py <OPTIONS>

Current options:
* -h : firefox will run in headless mode (you won't see it)
* -r : routine, must be proceeded by a file that contains a list of accounts and their routines
* -ca: create accounts, must be proceeded by an ammount and a file in which emails and passwords will be stored

### Using routines
The account list must be in the next format
username_or_email password first_action;second_action;...

Actions:
* AF - Attack friends
* AR - Attack random
* FGF - Farm gold frozen island
* FGD - Farm gold deadshore
* FGT - Farm gold tsunade
* FGP - Farm gold panda
* Dice - Farm dice
* Ink - Farm Ink
* Web - Farm Web
* Wood - Farm Wood

**AR and Farm actions will take place until energy is depleted**

#### Example:
user pass AF;AR;FGF