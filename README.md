# Solve-for-tomorow-Sargasum-tracker-bz
# Coastline Sargassum & Water Quality Tracker

A low-cost water quality monitoring system designed to help coastal communities monitor changes in water conditions associated with sargassum decomposition.

This project is being developed for the Samsung Solve for Tomorrow Latin America competition.

## About the Project

Sargassum can cause problems for coastal communities when large amounts accumulate and begin to decompose. This project aims to build a floating monitoring system that can collect water quality data and provide early warnings when conditions begin to deteriorate.

The system uses an ESP32 to collect sensor readings, process the data, and communicate the results to a monitoring dashboard.

## What It Measures

The system is designed to monitor:

* pH
* Dissolved oxygen (DO)
* Hydrogen sulfide (H2S)
* Ammonia (NH3)

The readings will be compared with normal ranges and project-defined warning conditions.

## How It Works

```text
Water Sensors
     |
     v
   ESP32
     |
     +----> Local alerts
     |
     +----> Data storage
     |
     +----> Wireless communication
                  |
                  v
            Web Dashboard
```

The ESP32 collects readings from the sensors at regular intervals. The firmware processes the readings and determines the current status of the water conditions.

The physical system is planned to use solar power and a floating HDPE enclosure so that it can operate in a coastal environment.

## Hardware

Planned hardware includes:

* ESP32
* pH sensor
* Dissolved oxygen sensor
* MQ-136 H2S sensor
* MQ-137 NH3 sensor
* microSD module
* RGB LED
* Buzzer
* SIM800L
* Solar power system
* HDPE floating enclosure
* PETG mounting parts

## Software

The project currently uses:

* MicroPython
* Python
* Flask
* HTML
* CSS
* JavaScript
* Wokwi
* Git

## Current Progress

The project is currently being developed and tested using a simulated ESP32 before the physical hardware is integrated.

* [x] ESP32 simulation
* [x] Simulated sensor inputs
* [x] Basic sensor status classification
* [x] Flask API
* [ ] Complete dashboard
* [ ] Physical sensor integration
* [ ] Sensor calibration
* [ ] microSD data logging
* [ ] SIM800L communication
* [ ] Physical buoy
* [ ] Field testing

## Project Structure

```text
coastline-sargassum-tracker/
├── esp32/
├── dashboard/
├── wokwi/
├── docs/
├── .gitignore
└── README.md
```

The structure may change as development continues.

##Team

## Status

This project is still under development. The current version is a prototype and has not yet been validated for real-world deployment.

More documentation, testing results, calibration data, and hardware information will be added as development continues.
