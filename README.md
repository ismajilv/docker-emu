
# docker-emu
This docker image runs QEMU system emulation for Raspbian Stretch Lite and ESP32. MQTT broker is installed on Raspbian and mqtt client on esp32 connects to this broker and send/recieve data. esp-idf compiled `flash_image.bin` and `raspbian` qcow2 image are persented in download link in [scripts](./scripts/raspberry_and_esp32.sh) / also [dropbox link](https://www.dropbox.com/sh/e71mzurg42qnrha/AACb_gYygq7fKqhUJ-RFMdEHa?dl=1/). This [script](./scripts/raspberry_and_esp32.sh) also configure Docker.

Source code for built `raspbian` qcow2 image (raspberry) and `flash_image.bin` file (esp32):
- [esp-mqtt-tcp](./esp-mqtt-tcp)
- [raspbian](./raspberry)

Pre-requirements:
- [esp-idf](https://github.com/espressif/esp-idf) with release/v4.2, installation guide is presented in github, don't forget to update environment variables

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

### Start docker with
It starts docker and waits for connection on both 5555 and 6666 ports
```
$ sudo docker run -it -p 2222:2222 -p 5555:5555 -p 6666:6666 --privileged docker-emu:mqtt
```

### Connect to raspberry pi serial output on port 6666
on new terminal run:
```
$ nc localhost 6666
```
DO NOT CONTINUE TO NEXT STEP UNTIL it asks for login/username  
Enter `pi` for login and `raspberry` for password

### Connect to esp32 serial output on port 5555
After entering login/password on new terminal run:
```
$ cd esp-mqtt-tcp
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
