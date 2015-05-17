# A Python wrapper around the unoffical Padherder Puzzle and Dragon API

API being wrapped: https://www.padherder.com/api/

I've only just started to use the API, but it looks pretty complete.  The short
term goal is to be able to fuse efficiently, without having to do too much
legwork.

## Installation

    pip install requests urllib3 enum34
    git clone git@github.com:tankorsmash/padpy.git
    
*(Optional)* Running `pad.py` the first time will download the data and cache it for next time. This will happen no matter when you use it, so it's optional.
    python pad.py 
    
If you get the warning about OpenSSL import failing, you might need some [additional dependencies](https://stackoverflow.com/questions/18578439/using-requests-with-tls-doesnt-give-sni-support/18579484#18579484)
    
## Usage
    
    >>> pad = Pad(verbose=False) #verbosity tells you whether or not the data is retrieved from API or cache
    >>> monsters = pad.get_all_monsters() #get fill list of monsters
    >>> ice_ogre = pad.get_monster(65) #get only #65
    
    >>> ice_ogre.feed_xp
    <FeedExp 413.0>
    >>> ice_ogre.feed_xp.calc_for_level(12)
    4956.0
    >>> ice_ogre.atk
    <Attribute 277/875 * 1.0> # min/max * scale
    
    >>> monsters_in_ice_ogre_tree = pad.get_evolution_tree(ice_ogre)
    [<Monster #64 Blue Ogre>,
     <Monster #65 Ice Ogre>,
     <Monster #312 Blazing Ice Ogre>,
     <Monster #313 Wood Ice Ogre>]
     
     >>> print ice_ogre.__dict__ #for much more data


It gets the json from the API and saves it to your drive, saving some time. This is under active development.

## Features

* Thin wrappers around:
  * Monsters
  * ActiveSkills
  * Awakenings
  * Evolutions
  * LeaderSkills

* Getting monsters
  * ...by id
  * ...in a given monsters evolution tree

* Getting a given monster's
  * Exp to level up
  * Feed exp at a given level

## Goals

* Wrap the following so they're not plain dicts
  * Events
  * Food

* Query on monsters
  * filter by whatever

* Integrate with PADHerder's box system (thanks [aznwings](http://www.reddit.com/r/PuzzleAndDragons/comments/367a7c/misc_started_working_on_a_python_api_wrapper_full/crbll31))
  * Build the best team for ATK, HP, RCV, type, cost etc
  * Build the closest team according to another team (preset, user generated)

* Determine optimum feed path
* Dream goal: Monster Box Image parsing, so you can quickly import your monster
  list

