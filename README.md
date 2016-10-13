# aaas
Ainsley As A Service. It's [placekittens](https://placekiteens.com) but for Ainsley Harriot

## Development
If you want to contribute to AaaS, or self host the project, follow these steps
### Requirements
- PostgreSQL
- Python
- NodeJS
- NVM

### Setup
To setup the the project locally run the following commands:

    ./scripts/build

This command setup the virtual environment, get the required models, and create the database

    ./scripts/migrate

This command applies database migrations, and will need to run whenever a database model is changed

### Usage
To run the server locally execute the following command

    ./scripts/runserver

### Tests
Test can be run by executing the following command.

    ./scripts/runtests

## Contributors
 - **Jake Howard** - [RealOrangeOne](https://github.com/RealOrangeOne)
 - **James Seden Smith** - [sedders123](https://github.com/sedders123)
 - **Dominik Kwiatek** - [mltnhm](https://github.com/mltnhm)

If you want to contribute to this project see [CONTRIBUTING.md](CONTRIBUTING.md)
## License

This project is licensed under the MIT License - see [LICENSE.md](LICENSE.md) file for details
