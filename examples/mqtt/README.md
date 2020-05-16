# ESP-MQTT sample application

mqtt broker runs on Raspberry Pi. ESP32 mqtt client publish message to `test/message` topic via `mqtt` protocol. Because it's also subscriced to same topic, it recieve the message itself. 

ESP32
 - mqtt borker listen on port 8000

Raspberry Pi
 - mqtt client subscribe/publish message on topic `test/message`

How to run:
```
in root directory 
$ sudo docker-compose build
$ cd ./examples/mqtt/esp32
$ idf.py build
$ ./img_build.sh mqtt_tcp.bin
$ cp flash_image.bin ../../../mount/
$ cd ../../ansible
$ ansible-playbook -i inventory/hosts ../examples/mqtt/raspberry/setup.yml
EASY WAY
$ nc localhost 5555
OR HARD WAY
$ cd ./examples/echo/esp32/
$ idf.py monitor -p socket://localhost:5555
```

Now you should see this output
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
