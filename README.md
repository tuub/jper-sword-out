# JPER SWORD OUT

Consumes notifications from JPER and pushes them to repositories via SWORDv2

## Installation

Clone the project:

    git clone https://github.com/JiscPER/jper-sword-out.git

get all the submodules

    cd jper-sword-out
    git submodule init
    git submodule update

This will initialise and clone the esprit and magnificent octopus libraries

Then get the submodules for Magnificent Octopus

    cd jper-sword-out/magnificent-octopus
    git submodule init
    git submodule update

Create your virtualenv and activate it

    virtualenv /path/to/venv
    source /path/tovenv/bin/activate

Either use the requirements.txt file:

    pip install -r requirements.txt

Or follow these instructions:

    cd jper-sword-out/python-client-sword2
    pip install - e.

    cd jper-sword-out/esprit
    pip install -e .
    
    cd jper-sword-out/magnificent-octopus
    pip install -e .
    
Create your local config

    cd jper-sword-out
    touch local.cfg

Then you can override any config values that you need to

To start the application, you'll also need to install it into the virtualenv just this first time

    cd jper-sword-out
    pip install -e .

Then, start your app with

    python service/web.py

