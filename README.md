### Hexlet tests and linter status:
[![Actions Status](https://github.com/algosinc/python-project-lvl3/workflows/hexlet-check/badge.svg)](https://github.com/algosinc/python-project-lvl3/actions)

[![Maintainability](https://api.codeclimate.com/v1/badges/f881dac8fee81813cf90/maintainability)](https://codeclimate.com/github/algosinc/python-project-lvl3/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/f881dac8fee81813cf90/test_coverage)](https://codeclimate.com/github/algosinc/python-project-lvl3/test_coverage)

---

## Basic information

**Page loader** downloads the web page to an existing folder allowing user to open it offline. This is achieved due to the fact that the program also downloads local resources of the web page to the computer. Web page is downloaded to the directory chosen by user or by default to the current working directory.

## Quickstart

**Page loader** at the moment is stored only at *github* so the quickest and the easiest way to install it is to use *pip* with URL of repository.
```bash
pip install git+https://github.com/algosinc/python-project-lvl3.git
```

## Running

Basic **Page loader** syntax looks like this:
```bash
page-loader --output url
```
*output* is an optional argument which means a folder where to download the page. By default it is to current working directory.

You can also recall about main features and syntax of a program using *help command*:
```bash
page-loader -h
```

## Asciinema demonstration:

Installing the whole package and main features of the programm are demonstrated in the asciinema below: