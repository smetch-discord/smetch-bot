# SMETCH Bot

This is the server bot for SMETCH

### Contributing
1. Clone the GitHub repo
2. Run `python3 -m pip install pipenv`
3. Run `pipenv shell`
4. Run `pipenv install`
5. Add a file called `config.yml` and add the necessary fields:
    - **Required**: `bot-token`, `prefix`
    - **Optional**(at least should be): `mongo-uri`, `github-token`
    example config file
    ```yml
    bot-token: 
    mongo-uri: 
    github-token: 
    ```
    > if you somehow update .gitignore, make sure `config.yaml` is included
6. Run `pipenv run pre-commit`
7. Make any changes to your code
8. Run `pipenv run bot` to run the bot
