# lc-lowtiers-resources
Functions to help maintaining the tier, like creating VR post of downloading images to update the tier maker

# How to use
Assuming you have no coding knowledge, use AI to guide your setup steps, otherwise this should be clear enough
- install python
- create a virtual environment
- activate the environment
- pip install requirements.txt
- python tiermaker.py (or whatever file you need)

# vr_post.py
Very bare bones script to help format the VR post. You can copy the list of pokemon in order of rating from the Google doc, paste it into the list mons, fix the formatting so there are '' and commas, and run it. It will output a printed list of the pokemon in vr order. It will not tell you which pokemon is in which tier, but it makes it a bit easier to copy paste the formatting.
In the future you need to change the mons list with the updated VR one

# tiermaker.py
This is my attempt to make the process easier so that when i disappear you can still easily create a VR tiermaker by inputting the images from the output folder. It's also set up so it can be useful to LC Ubers and LC RU resources.
The tiers.json file contains the list of pokemon divided by tiers. When a tier shift happens, that will need to be fixed.
When the json file is fixed, running the tier maker script will do a lot of things
On a high level, it just downloads the sprite images for all the mons listed, and puts them in the correct folder. It is a pretty fast process, but for funsies I added something a bit more intelligent.
Before downloading a pokemon sprite, it checks that it's not already present in the folder you're trying to save it. Sneasel will always be LC Ubers, we don't need to update that sprite image every time LCUU has a tier shift.
The output folders are the following (all sorted alphabetically so it's easier to find the right pokemon)
- all_downloads, useful only for LC Ubers, it has every possible LC pokemon
- LC OU, LC UU, LC UU BL, LC UU, LC RU BL, LC RU, The rest (self-explanatory, rarely needed, just contain the pokemon in that specific tier)
- all_but_lc_ubers: all the pokemon legal outside of LC Ubers pokemon, if someone for some reason wants to use it for LC OU tierlists
- all_but_lc_ubers_and_lc_ou_and_lc_uu_bl: all the pokemon legal in the LCUU metagame, this is the folder where you pick the pokemon when creating a tiermaker for LCUU
- all_but_lc_ubers_and_lc_ou_and_lc_uu_bl_and_lc_uu_and_lc_ru_bl: all the pokemon legal in the LCRU metagame, this is the folder where you pick the pokemon when creating a tiermaker for LCRU
