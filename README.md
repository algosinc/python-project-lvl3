### Hexlet tests and linter status:
[![Actions Status](https://github.com/algosinc/python-project-lvl3/workflows/hexlet-check/badge.svg)](https://github.com/algosinc/python-project-lvl3/actions)

[![Maintainability](https://api.codeclimate.com/v1/badges/f881dac8fee81813cf90/maintainability)](https://codeclimate.com/github/algosinc/python-project-lvl3/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/f881dac8fee81813cf90/test_coverage)](https://codeclimate.com/github/algosinc/python-project-lvl3/test_coverage)

---

## Basic information

**Page loader** downloads the web page to an existing folder allowing the user to open it offline. This is achieved, as the program also downloads local resources of the web page to the computer. The web page is downloaded to the directory chosen by the user or by default to the current working directory.

## Quickstart

**Page loader** at the moment is stored only at GitHub so the quickest and easiest way to install it is to use pip with the URL of the repository.
```bash
pip install git+https://github.com/algosinc/python-project-lvl3.git
```

## Running

Basic **Page loader** syntax looks like this:
```bash
page-loader --output --loglevel url
```
The *output* is an optional argument that sets the folder to download the page. By default, it is set to the current working directory.

The *loglevel* is an optional argument that sets the logging level. There are five valid options available: 'DEBUG', 'INFO', 'WARNING', 'ERROR' and 'CRITICAL'.

You can also recall about main features and syntax of a program using the *help command*:
```bash
page-loader -h
```

## Asciinema demonstration:

Installing the whole package and the main features of the program is demonstrated in the asciinema below:
