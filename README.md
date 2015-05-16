# A Python wrapper around the unoffical Padherder Puzzle and Dragon API

API being wrapped: https://www.padherder.com/api/

I've only just started to use the API, but it looks pretty complete.  The short
term goal is to be able to fuse efficiently, without having to do too much
legwork.

## Installation

    pip install requests urllib3
    git clone git@github.com:tankorsmash/padpy.git
    
*(Optional)* Running `pad.py` the first time will download the data and cache it for next time. This will happen no matter when you use it, so it's optional.
    python pad.py 
    
## Usage
    

It gets the json from the API and saves it to your drive. Writing the wrappers.

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
  * LeaderSkills

* Query on monsters
  * filter by whatever

* Determine optimum feed path
* Dream goal: Monster Box Image parsing, so you can quickly import your monster
  list

