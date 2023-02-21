# Meme Generator Repository

This repository contains python code for the Meme Generator project.
The project contains a flask app that can be used to generate memes, and a command line tool that can be used to generate memes from the command line.

## Installation

To install the project, clone the repository and install the requirements.
The requirements are listed in requirements.txt.
There is also a pyproject.toml file that can be used to install the requirements using poetry.

### Using virtualenv and requirements.txt

Clone the repository.
```bash
git clone repo_link
```

Create a virtual environment inside the repository and activate it.
```bash
cd meme-generator
python3 -m venv venv
source venv/bin/activate
```

Install the requirements.
```bash
pip install -r requirements.txt
```

### Using poetry and pyenv

Clone the repository.
```bash
git clone repo_link
```

Navigate to the repository, create a virtual environment and install the requirements.
```bash
cd meme-generator
pyenv virtualenv 3.9.5 meme-generator
pyenv local meme-generator
poetry update && poetry install
```

## Usage

### Flask App

To run the flask app, navigate to the repository and run the following command.
```bash
python app.py
```
You should see the app running on http://127.0.0.1:5000/.

### Command Line Tool

To run the command line tool, navigate to the repository and run the following command.
```bash
python meme.py --help
```

## Modules

The project contains the following modules.

### MemeEngine

The MemeEngine module contains the MemeEngine class.
The MemeEngine class is used to generate memes.

#### Dependencies

The MemeEngine module depends on the following modules.

##### Pillow - Used to generate memes
#### Os - Used to get the path of the image
#### Random - Used to generate random numbers
#### Typing - Used to define types


### QuoteEngine

The QuoteEngine module contains the QuoteModel and Ingestor classes.
The QuoteModel class is used to represent a quote.
The Ingestor class is used to ingest quotes from different file types.

#### Dependencies

The QuoteEngine module depends on the following modules.

##### Pandas - Used to read csv files
##### Docx - Used to read docx files
##### pdftotext - Used in command line tool to read pdf files
##### Subprocess - Used to run pdftotext in command line tool
##### Typing - Used to define types
##### Random - Used to generate random numbers
##### os - Used to get the path of the image
##### abc - Used to define abstract classes

