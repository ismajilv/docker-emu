
# docker-emu
This docker image runs QEMU system emulation for Raspbian Stretch Lite and ESP32. [raspberry](./raspberry) and [esp32](./esp32) folders contain respective Dockerfiles for emulation.  

Use [examples](./examples) folder for given examples and more info. 

Pre-requirements:
- [install and setup esp-idf with release/v4.2](https://github.com/espressif/esp-idf) 
- [install ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)
- [install docker-compose](https://docs.docker.com/compose/install/)
- [setup cli_interface](./cli_interface)

## Examples
- Start with one of the [examples](./examples), follow instructions

## Some info
- [ansible](./ansible) is used to setup Raspberry Pi for different services. It contains `config` file and `inventory` folder 
- adviced to build docker-compose from scratch if not working with `--no-cache` option

## SSH

SSH is enabled on port `2222`. The username is `pi` and the password is `raspberry`. 
To connect with SSH, run:

`$ emu ssh`
