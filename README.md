
# docker-emu
This docker image runs QEMU system emulation for Raspbian Stretch Lite and ESP32 with scalability. [raspberry](./raspberry) and [esp32](./esp32) folders contain respective Dockerfiles for emulation and system is built with docker-compose.  

## Setup guide:
- Install [git](https://git-scm.com/downloads) and [git lfs](https://git-lfs.github.com/)
- Clone with `git clone https://github.com/ismajilv/docker-emu/`
- Build with: `sudo docker-compose build` in the root directory then setup all the required packages versions below:
  - [install and setup esp-idf with release/v4.2](https://github.com/espressif/esp-idf/tree/release/v4.2) (choose `stable version` in Getting Started Guides for ESP-IDF next to ESP32 chip) `v4.2`
  - [install ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html) `>= 2.7`
  - install [docker](https://docs.docker.com/engine/install/) `>= 19.*`  and [docker-compose](https://docs.docker.com/compose/install/) `>= 1.25.*`
  - [setup cli_interface with `click` version 7.21 described in requirements.txt](./cli_interface)
  - install [sshpass](https://gist.github.com/arunoda/7790979)

## Examples
- Start with one of the [examples](./examples), follow instructions

## Some info
- [ansible](./ansible) is used to setup Raspberry Pi for different services. It contains `config` file and `inventory` folder 
- adviced to build docker-compose from scratch if not working with `--no-cache` option
- tested in Ubuntu 18.04, WSL might not work
