
# docker-emu
This docker image runs QEMU system emulation for Raspbian Stretch Lite and ESP32. [build](./build) folder contains necessary scripts to configure emulator.  

[virt-customize](http://libguestfs.org/virt-customize.1.html) is used to configure `raspbian` image before docker run.

Use [examples](./examples) folder for given examples and more info. 

Pre-requirements:
- [esp-idf](https://github.com/espressif/esp-idf) with release/v4.2

## Instruction

### Clone repository
```
$ git clone https://github.com/ismajilv/docker-emu/ -b mqtt
$ cd docker-emu 
```

### Build docker (do not forget . at the end)
Will download/resize/enable ssh in `raspbian` qcow2 image and download esp32 `flash_image.bin` file
```
$ docker build -t docker-emu:mqtt .
```

### Start docker with [examples](./examples) folder mounted
Choose example [examples](./examples) you wish, as an example [mqtt](./examples/mqtt), then start docker. Wait it initiate start until it asks for connection on port.  
- `5555` - for esp32 serial output
- `6666` - for raspberry pi serial output 
```
$ sudo docker run -it -v $(pwd)/examples/mqtt:/root/mount -p 2222:2222 -p 5555:5555 -p 6666:6666 --privileged ismajilv/docker-emu:mqtt
```

### Connect to raspberry pi serial output on port 6666
on new terminal run:
```
$ nc localhost 6666
```
DO NOT CONTINUE TO NEXT STEP UNTIL `virt-customize` configure `raspbian` image. (which is showing `Setting up mosquitto` line and starting service)

### Connect to esp32 serial output on port 5555
After install complete on new terminal run:
```
EASY WAY:
$ nc localhost 5555
OR HARD WAY:
$ cd examples/mqtt/esp32/
$ idf.py build
$ idf.py monitor -p socket://localhost:5555
```
and will see output similar to this:
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
