# p2s
## Python Piloting Software

This is the codebase for the TJHSST Underwater ROV team's piloting software. 

### Contributing
The contributing guidelines can be found [here](CONTRIBUTING.md).

### Running the piloting software
* First copy over `config/template.yml` to `config/config.yml` and update the IP addresses for both the ground_station device and the `rov-pi`

* Run `python main.py ground` to run the ground station software.
* Run `python main.py ground_station` to run the ground station software.


* Run `python main.py flight` to run the flight software on `rov-pi`
* Run `python main.py flight_software` to run the flight software on `rov-pi`


* Run `python main.py` to choose to run the ground station software or the flight software
