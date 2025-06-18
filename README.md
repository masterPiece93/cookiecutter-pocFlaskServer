# Cookiecutter - Flask Server PoC 

this will create a project structre for a flask server for a quick poc .


### How to Install

- Create a venv
    ```sh
    python3 -m venv venv
    ```

- Installing cookiecutter

    ```sh
    pip install cookiecutter
    ```

- Running 

    ```sh
    cookiecutter <name/git-link>
    ```

    - exmaple

        ```sh
        cookiecutter https://github.com/masterPiece93/cookiecutter-pocFlaskServer.git
        ```
### TODO:

- python version input
    - validate user input for supported python versions only
    - generate pyenv virtual env based on this input
    - find a way to auto read the versioned requirement files based on user selection of python verion
    - create
        - requirements.py3.10._.txt
        - requirements.py3.11._.txt
        - requirements.py3.12._.txt
        
- enahnce Makefile
    - auto generate .env from .env.template if not exists

- `check-env` makefile target not working expectedly .

# REFERENCES

[tutorial](https://raphael.codes/blog/create-your-own-cookiecutter-template/)
