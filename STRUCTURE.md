# Project Structure

### Layout
    
    ├── comms
    │   ├── __init__.py
    │   ├── reader.py
    │   └── writer.py
    ├── computervision
    │   └── __init__.py
    ├── config
    │   └── config.yml
    ├── frontend
    │   ├── dashboard
    │   │   ├── __init__.py
    │   │   ├── gui.py
    │   │   └── widgets
    │   │       ├── actuators.py
    │   │       ├── cameras.py
    │   │       ├── depth.py
    │   │       ├── gyroscope.py
    │   │       ├── heading.py
    │   │       ├── __init__.py
    │   │       ├── temperature.py
    │   │       └── thrusters.py
    │   ├── __init__.py
    │   ├── frontend.py
    │   └── viewfinder
    │       └── __init__.py
    ├── main.py
    ├── manipulator
    │   └── __init__.py
    ├── rov
    │   └── __init__.py


### Packages

### `comms`
The `__init__.py` defines a `Comms` class. The `comms` package uses a `Reader` and `Writer` classes
 in the `reader.py` and `writer.py` files. The `Writer` class writes packets of data to a serial port off a global queue.
 The `Reader` class reads packets of data from the serial port and dispatches information to the relevant a `Widget` class.

#### `computervision`
In `__init__.py`, there is a method to process an image to find shapes.

#### `frontend`
The `__init__.py` file initializes and handles the refreshing the `dashboard` and `viewfinder`.

#### `frontend/dashboard`
The `dashboard` is the window with `widget`s. The `dashboard` package is responsible for creating the necessary
components for `tkinter`.

### `frontend/dashboard/widget`
The `__init__.py` defines an abstract widget class which the other widget files extend. Each file in the 
`widget` package defines a `widget` for each sensor. Each file should be able to draw information passed in to it on a
`tkinter Canvas` object.

### `viewfinder`
The `__init__.py` file defines a `ViewFinder` class that utilizes `cv2` to display a window with the camera feed.

### `manipulator`
The `manipulator` package is responsible for parsing input from a controller and dispatching the command to the right module.

### `rov`
The `__init__.py` file defines a `ROV` class that converts relevant controller data into packets to write to the serial 
port via the `comms` package. This includes thruster values, thruster adjustments (for control loops), and actuator positions.
