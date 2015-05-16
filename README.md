# A Python wrapper around the unoffical Padherder Puzzle and Dragon API

API being wrapped: https://www.padherder.com/api/

I've only just started to use the API, but it looks pretty complete.  The short
term goal is to be able to fuse efficiently, without having to do too much
legwork.

## Installation

    pip install requests urllib3
    python pad.py

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

