# p2s
## Python Piloting Software

This is the codebase for the TJHSST Underwater ROV team's piloting software. 

### Contributing
The contributing guidelines can be found [here](CONTRIBUTING.md).

### Running the piloting software
* Run `python main.py development` to run in a development environment
* Run `python main.py` to run in a production environment
    * Requires a serial connection to a device running the piloting framework code
    * Requires at least one camera connection from the ROV
* Run `python main.py test` to run tests
