# A Python wrapper around the unoffical Padherder Puzzle and Dragon API

API being wrapped: https://www.padherder.com/api/

I've only just started to use the API, but it looks pretty complete.  The short
term goal is to be able to fuse efficiently, without having to do too much
legwork.

## Installation

    pip install requests urllib3
    python pad.py

It gets the json from the API and saves it to your drive. Writing the wrappers.

## Goals

* Wrap the following so they're not plain dicts
  * ActiveSkills
  * Awakenings
  * Events
  * Evolutions
  * Food
  * LeaderSkills
  * Materials
  * Monsters

* Query on monsters
  * Get by id
  * Get all monsters in the evolution chain
  * filter by whatever

* Figure out the feed xp you get

