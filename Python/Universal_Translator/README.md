# Welcome to my Universal Translator!

This is a universal translation app that is containerized through Docker, or usable through the CLI.
It handles errors with exceptions without breaking the program and is very easy to read and understand.
This will be used in the restaurant that I work in to facilitate communicaton between English and 
Spanish speaking employees. I actually plan on making it a web app that is easily accessible.


## How to Use in the CLI

1.  Before running main.py, make sure that you have ran this in the command line:

    `pip install translate`

    This is the only required installation beyond Python.

2.  Run `python3 main.py` and follow the prompts. It's that simple.


## How to Use through Docker

1.  Pull the image using this command (assuming you have docker installed properly):

    `docker pull tkduncan/universal_translator:1.0`

2.  Make sure to run the container in interactive mode with auto-remove and follow the prompts:

    `docker run -it --rm tkduncan/universal_translator:1.0`
