# trailtracker-api

[![standard-readme compliant](https://img.shields.io/badge/standard--readme-OK-green.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)
TODO: Put more badges here.

>  Trail tracking app for manipulating trail data with granular details.

TODO: Fill out this long description.

## Table of Contents

- [Security](#security)
- [Background](#background)
- [Install](#install)
- [Usage](#usage)
- [API](#api)
- [Maintainers](#maintainers)
- [Contribute](#contribute)
- [License](#license)

## Security

## Background

## Install

### VirtualEnvWrapper
Allows you to create an isolated environment for your python dependecies.

[VirtualEnvWrapper] (http://virtualenvwrapper.readthedocs.io/en/latest/install.html)

### Vagrant
Vagrant boxes allow you to set a standardized VM across multiple development platforms.

**Dependecies**
*Virutal Box

**Config**
*Download from [Vagrant] (https://www.vagrantup.com/downloads.html)
*clone repo
*`vagrant up`
*`vagrant help` displays man pages

## Usage

```
```

## API

## Maintainers

## Contribute

See [the contribute file](contribute.md)!



Small note: If editing the README, please conform to the [standard-readme](https://github.com/RichardLitt/standard-readme) specification.

## License

MIT © Ben Adamski, Phil Schoof, Oliver Scarborough, Susan Daitue.


*   parse_gpx management command currently returns json blob with all trail info
*   Need to strip out data points to reduce frequency (maybe every minute?)
*   Create the `Ride` model, serializer
*   Figure out how to move from mgmt command to `Ride` model instance


## User Stories
*   AU I want to upload exported trail data
*   AU I want that to be easy
*   AU I want to be able to easily manipulate data
  **  clean UX
*   AU I want to store euipment data
*   AU I want my data to be secure


## Tech
*   D3
*   Mongo?
