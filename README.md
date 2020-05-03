
# docker-emu
This docker image runs QEMU system emulation for Raspbian Stretch Lite and ESP32. [raspberry](./raspberry) and [esp32](./esp32) folders containd Dockerfiles.  

Use [examples](./examples) folder for given examples and more info. 

Pre-requirements:
- [esp-idf](https://github.com/espressif/esp-idf) with release/v4.2
- [ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)
- [docker-compose](https://docs.docker.com/compose/install/)

## Instruction

### Clone repository
```
$ git clone https://github.com/ismajilv/docker-emu/ -b mqtt
$ cd docker-emu 
```

### Copy `flash_image.bin` file to [mount](./mount) folder
We will use [mqtt](./examples/mqtt) example. Please read [esp32 README](./examples/mqtt/esp32/README.md) and [MQTT README](./examples/mqtt/README.md).

Copy `flash_image.bin` file to [mount](./mount) folder from the `esp32` folder of [mqtt example](./examples/mqtt/esp32). This folder will be mounted to `esp32` service on startup and `esp32` will use this file to load emulator
```
$ cp ./examples/mqtt/esp32/flash_image.bin ./mount
```

### Build via docker-compose
This builds, (re)creates, starts, and attaches containers for `esp32` and `raspberry pi` services 
- `5555` - for esp32 serial output
- `6666` - for raspberry pi serial output 
```
$ docker-compose up
```

### Run ansible setup.yml file in `raspberry` folder
Setup `raspbian` image. This ansible script waits for image being reachable and setups image (in case of [mqtt](./examples/mqtt) installs mosquitto)
```
$ cd ansible/ 
$ ansible-playbook -i inventory/hosts ../examples/mqtt/raspberry/setup.yml
 ```

### Connect to raspberry pi serial output on port 6666
on new terminal run:
```
$ nc localhost 6666
```

### Connect to esp32 serial output on port 5555
Wait `ansible` setup to be completed and then on new terminal run:
```
EASY WAY:
$ nc localhost 5555
OR HARD WAY:
$ cd examples/mqtt/esp32/
$ idf.py build
$ idf.py monitor -p socket://localhost:5555
```
Now `mosquitto` client is connected to `raspberry pi` that sends/recieve message and will see output similar to this:
```
Executing action: monitor
Running idf_monitor in directory /home/ismajilv/Documents/iot/code/git/docker-emu/esp-mqtt-tcp
Executing "/home/ismajilv/.espressif/python_env/idf4.2_py3.6_env/bin/python /home/ismajilv/esp/esp-idf/esp-idf-4.2/tools/idf_monitor.py -p socket://localhost:5555 -b 115200 --toolchain-prefix xtensa-esp32-elf- /home/ismajilv/Documents/iot/code/git/docker-emu/esp-mqtt-tcp/build/mqtt_tcp.elf -m '/home/ismajilv/.espressif/python_env/idf4.2_py3.6_env/bin/python' '/home/ismajilv/esp/esp-idf/esp-idf-4.2/tools/idf.py'"...
--- idf_monitor on socket://localhost:5555 115200 ---
--- Quit: Ctrl+] | Menu: Ctrl+T | Help: Ctrl+T followed by Ctrl+H ---
I (5261) example_connect: Got IPv6 address: fe80:0000:0000:0000:0200:00ff:fe00:0003, type: ESP_IP6_ADDR_IS_LINK_LOCAL
I (5261) example_connect: Connected to Ethernet
I (5261) example_connect: IPv4 address: 10.0.2.15
I (5261) example_connect: IPv6 address: fe80:0000:0000:0000:0200:00ff:fe00:0003
I (5261) system_api: Base MAC address is not set
I (5261) system_api: read default base MAC address from EFUSE
I (5271) MQTT_EXAMPLE: Other event id:7
I (5291) MQTT_CLIENT: Sending MQTT CONNECT message, type: 1, id: 0000
I (5291) MQTT_EXAMPLE: MQTT_EVENT_CONNECTED
I (5301) MQTT_EXAMPLE: sent publish successful, msg_id=2996
I (5311) MQTT_EXAMPLE: sent subscribe successful, msg_id=25090
I (5311) MQTT_EXAMPLE: sent subscribe successful, msg_id=33704
I (5321) MQTT_EXAMPLE: sent unsubscribe successful, msg_id=41154
I (5331) MQTT_EXAMPLE: MQTT_EVENT_PUBLISHED, msg_id=2996
I (5341) MQTT_EXAMPLE: MQTT_EVENT_SUBSCRIBED, msg_id=25090
I (5341) MQTT_EXAMPLE: sent publish successful, msg_id=0
I (5351) MQTT_EXAMPLE: MQTT_EVENT_DATA
TOPIC=test/message   <- sent/retained messages
DATA=data_3
I (5351) MQTT_EXAMPLE: MQTT_EVENT_SUBSCRIBED, msg_id=33704
I (5361) MQTT_EXAMPLE: sent publish successful, msg_id=0
I (5361) MQTT_EXAMPLE: MQTT_EVENT_DATA
TOPIC=test/message   <- sent/retained message
DATA=data_3
I (5381) MQTT_EXAMPLE: MQTT_EVENT_UNSUBSCRIBED, msg_id=41154
```

## SSH

SSH is enabled on port `2222`. The username is `pi` and the password is `raspberry`. 

To connect with SSH:

`ssh -p 2222 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no pi@localhost`
