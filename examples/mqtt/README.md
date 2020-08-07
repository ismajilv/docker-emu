# ESP-MQTT sample application

mqtt broker runs on Raspberry Pi. ESP32 mqtt client publish message to `test/message` topic via `mqtt` protocol. Because it's also subscriced to same topic, it recieve the message itself. 

ESP32
 - mqtt borker listen on port 8000

Raspberry Pi
 - mqtt client subscribe/publish message on topic `test/message`

How to run:
```
Inisde examples/mqtt/esp32 folder
$ emu start             # Start 1 instance of Raspberry Pi and 1 instance of ESP32
$ emu flash --id 1      # Flash into ESP32 device with id 1
$ cd ../raspberry
$ ansible-playbook -i ../../../ansible/inventory/hosts setup.yml // may output some warnings, but should continue
$ cd ../esp32/
$ emu monitor --id 1
```

Now you should see this output
```
Executing action: monitor
Running idf_monitor in directory /home/ismajilv/Documents/iot/code/git/docker-emu/examples/mqtt/esp32
Executing "/home/ismajilv/.espressif/python_env/idf4.2_py3.6_env/bin/python /home/ismajilv/esp/esp-idf/esp-idf-4.2/tools/idf_monitor.py -p socket://localhost:5555 -b 115200 --toolchain-prefix xtensa-esp32-elf- /home/ismajilv/Documents/iot/code/git/docker-emu/examples/mqtt/esp32/build/mqtt_tcp.elf -m '/home/ismajilv/.espressif/python_env/idf4.2_py3.6_env/bin/python' '/home/ismajilv/esp/esp-idf/esp-idf-4.2/tools/idf.py'"...
--- idf_monitor on socket://localhost:5555 115200 ---
--- Quit: Ctrl+] | Menu: Ctrl+T | Help: Ctrl+T followed by Ctrl+H ---
ets Jun  8 2016 00:22:57

rst:0x1 (POWERON_RESET),boot:0x12 (SPI_FAST_FLASH_BOOT)
configsip: 0, SPIWP:0xee
clk_drv:0x00,q_drv:0x00,d_drv:0x00,cs0_drv:0x00,hd_drv:0x00,wp_drv:0x00
mode:DIO, clock div:2
load:0x3fff0030,len:4
load:0x3fff0034,len:7200
ho 0 tail 12 room 4
load:0x40078000,len:13696
load:0x40080400,len:4000
0x40080400: _init at ??:?

entry 0x40080688
I (268) boot: ESP-IDF v4.2-dev-1303-gcd4fa46f5 2nd stage bootloader
I (290) boot: compile time 12:45:29
I (294) boot: chip revision: 0
I (296) boot.esp32: SPI Speed      : 40MHz
I (296) boot.esp32: SPI Mode       : DIO
I (296) boot.esp32: SPI Flash Size : 2MB
I (316) boot: Enabling RNG early entropy source...
I (328) boot: Partition Table:
I (329) boot: ## Label            Usage          Type ST Offset   Length
I (329) boot:  0 nvs              WiFi data        01 02 00009000 00006000
I (331) boot:  1 phy_init         RF data          01 01 0000f000 00001000
I (331) boot:  2 factory          factory app      00 00 00010000 00100000
I (336) boot: End of partition table
I (340) esp_image: segment 0: paddr=0x00010020 vaddr=0x3f400020 size=0x17668 ( 95848) map
I (417) esp_image: segment 1: paddr=0x00027690 vaddr=0x3ffb0000 size=0x022c4 (  8900) load
I (437) esp_image: segment 2: paddr=0x0002995c vaddr=0x40080000 size=0x00404 (  1028) load
0x40080000: _WindowOverflow4 at /home/ismajilv/esp/esp-idf/esp-idf-4.2/components/freertos/xtensa/xtensa_vectors.S:1730

I (459) esp_image: segment 3: paddr=0x00029d68 vaddr=0x40080404 size=0x062b0 ( 25264) load
I (496) esp_image: segment 4: paddr=0x00030020 vaddr=0x400d0020 size=0x58d40 (363840) map
0x400d0020: _stext at ??:?

I (700) esp_image: segment 5: paddr=0x00088d68 vaddr=0x400866b4 size=0x04a40 ( 19008) load
0x400866b4: mwdt_ll_config_stage at /home/ismajilv/esp/esp-idf/esp-idf-4.2/components/soc/src/esp32/include/hal/mwdt_ll.h:103
 (inlined by) wdt_hal_config_stage at /home/ismajilv/esp/esp-idf/esp-idf-4.2/components/soc/src/hal/wdt_hal_iram.c:119

I (737) boot: Loaded app from partition at offset 0x10000
I (740) boot: Disabling RNG early entropy source...
I (746) cpu_start: Pro cpu up.
I (747) cpu_start: Application information:
I (747) cpu_start: Project name:     mqtt_tcp
I (747) cpu_start: App version:      0765bba-dirty
I (748) cpu_start: Compile time:     May 30 2020 12:45:05
I (749) cpu_start: ELF file SHA256:  a1a806d963da35f7...
I (750) cpu_start: ESP-IDF:          v4.2-dev-1303-gcd4fa46f5
I (750) cpu_start: Starting app cpu, entry point is 0x400814d4
0x400814d4: call_start_cpu1 at /home/ismajilv/esp/esp-idf/esp-idf-4.2/components/esp32/cpu_start.c:286

I (3847) cpu_start: App cpu up.
I (4700) heap_init: Initializing. RAM available for dynamic allocation:
I (4707) heap_init: At 3FFAE6E0 len 00001920 (6 KiB): DRAM
I (4712) heap_init: At 3FFB3D00 len 0002C300 (176 KiB): DRAM
I (4714) heap_init: At 3FFE0440 len 00003AE0 (14 KiB): D/IRAM
I (4718) heap_init: At 3FFE4350 len 0001BCB0 (111 KiB): D/IRAM
I (4721) heap_init: At 4008B0F4 len 00014F0C (83 KiB): IRAM
I (4731) cpu_start: Pro cpu start user code
I (1479) spi_flash: detected chip: gd
I (1496) spi_flash: flash io: dio
W (1506) spi_flash: Detected size(4096k) larger than the size in the binary image header(2048k). Using the size in the binary image header.
I (1507) cpu_start: Starting scheduler on PRO CPU.
I (20) cpu_start: Starting scheduler on APP CPU.
I (1552) MQTT_EXAMPLE: [APP] Startup..
I (1552) MQTT_EXAMPLE: [APP] Free memory: 294708 bytes
I (1552) MQTT_EXAMPLE: [APP] IDF version: v4.2-dev-1303-gcd4fa46f5
I (1672) system_api: Base MAC address is not set
I (1672) system_api: read default base MAC address from EFUSE
I (1682) esp_eth.netif.glue: 00:00:00:00:00:03
I (1682) esp_eth.netif.glue: ethernet attached to netif
I (1692) example_connect: Waiting for IP
I (3692) example_connect: Ethernet Link Up
I (4662) esp_netif_handlers: eth ip: 10.0.2.15, mask: 255.255.255.0, gw: 10.0.2.2
I (4662) example_connect: Got IP event!
I (5662) example_connect: Got IPv6 address: fe80:0000:0000:0000:0200:00ff:fe00:0003, type: ESP_IP6_ADDR_IS_LINK_LOCAL
I (5672) example_connect: Connected to Ethernet
I (5672) example_connect: IPv4 address: 10.0.2.15
I (5672) example_connect: IPv6 address: fe80:0000:0000:0000:0200:00ff:fe00:0003
I (5682) system_api: Base MAC address is not set
I (5692) system_api: read default base MAC address from EFUSE
I (5722) MQTT_EXAMPLE: Other event id:7
I (5792) MQTT_CLIENT: Sending MQTT CONNECT message, type: 1, id: 0000
I (5872) MQTT_EXAMPLE: MQTT_EVENT_CONNECTED
I (5882) MQTT_EXAMPLE: sent publish successful, msg_id=50733
I (5892) MQTT_EXAMPLE: sent subscribe successful, msg_id=40129
I (5892) MQTT_EXAMPLE: sent subscribe successful, msg_id=37524
I (5892) MQTT_EXAMPLE: sent unsubscribe successful, msg_id=64575
I (5902) MQTT_EXAMPLE: MQTT_EVENT_PUBLISHED, msg_id=50733
I (5922) MQTT_EXAMPLE: MQTT_EVENT_SUBSCRIBED, msg_id=40129
I (5922) MQTT_EXAMPLE: sent publish successful, msg_id=0
I (5932) MQTT_EXAMPLE: MQTT_EVENT_DATA
TOPIC=test/message
DATA=data_3
I (5942) MQTT_EXAMPLE: MQTT_EVENT_SUBSCRIBED, msg_id=37524
I (5942) MQTT_EXAMPLE: sent publish successful, msg_id=0
I (5952) MQTT_EXAMPLE: MQTT_EVENT_DATA
TOPIC=test/message
DATA=data_3
I (5962) MQTT_EXAMPLE: MQTT_EVENT_UNSUBSCRIBED, msg_id=64575
```
