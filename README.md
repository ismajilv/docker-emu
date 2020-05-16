
# docker-emu
This docker image runs QEMU system emulation for Raspbian Stretch Lite and ESP32. [raspberry](./raspberry) and [esp32](./esp32) folders contain respective Dockerfiles for emulation.  

Use [examples](./examples) folder for given examples and more info. 

Pre-requirements:
- [esp-idf](https://github.com/espressif/esp-idf) with release/v4.2
- [ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)
- [docker-compose](https://docs.docker.com/compose/install/)

## Some info
- [mount](./mount) is mounted to ESP32 container on startup. It is used to store `flash_image.bin` file in container so that ESP32 emulation can use it on startup. 
- [ansible](./ansible) is used to setup Raspberry Pi for different services. It contains `config` file and `inventory` folder 
- `$ idf.py monitor -p socket://localhost:5555` or just `$ nc localhost 5555` is used to monitor ESP32 serial output
- [img_build.sh](./examples/echo/esp32/img_build.sh) helper script is used to recreate a flash image, combining the bootloader, partition table, and the application
- start with one of the [examples](./examples)

## SSH

SSH is enabled on port `2222`. The username is `pi` and the password is `raspberry`. 

To connect with SSH:

`ssh -p 2222 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no pi@localhost`
