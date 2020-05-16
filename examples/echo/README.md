# ECHO sample application

ESP32 launches TCP server that listens on socket for incoming characters. After receiving character data from terminal, sends it to server running on Rasppberry Pi via POST request. Server runnin on Raspberry Pi keeps request data in list and it can be obtained by GET request.

ESP32
 - TCP server listen on port 3333
 - HTTP client POST 

Raspberry Pi
 - Accets POST on server running on port 8000
 - Keeps ESP32 input data in list

How to run:
```
in root directory 
$ sudo docker-compose build
$ cd ./examples/echo/esp32
$ idf.py build
$ ./img_build.sh tcp_server.bin
$ cp flash_image.bin ../../../mount/
$ cd ../../../ansible
$ ansible-playbook -i inventory/hosts ../examples/echo/raspberry/setup.yml
EASY WAY
$ nc localhost 5555
OR HARD WAY
$ cd ./examples/echo/esp32/
$ idf.py monitor -p socket://localhost:5555
```
Now you should see this output:
```
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
entry 0x40080688
I (157) boot: ESP-IDF v4.2-dev-1303-gcd4fa46f5 2nd stage bootloader
I (161) boot: compile time 21:04:29
I (166) boot: chip revision: 0
I (170) boot.esp32: SPI Speed      : 40MHz
I (172) boot.esp32: SPI Mode       : DIO
I (172) boot.esp32: SPI Flash Size : 2MB
I (179) boot: Enabling RNG early entropy source...
I (187) boot: Partition Table:
I (188) boot: ## Label            Usage          Type ST Offset   Length
I (188) boot:  0 nvs              WiFi data        01 02 00009000 00006000
I (190) boot:  1 phy_init         RF data          01 01 0000f000 00001000
I (191) boot:  2 factory          factory app      00 00 00010000 00100000
I (197) boot: End of partition table
I (202) esp_image: segment 0: paddr=0x00010020 vaddr=0x3f400020 size=0x17a00 ( 96768) map
I (269) esp_image: segment 1: paddr=0x00027a28 vaddr=0x3ffb0000 size=0x022c0 (  8896) load
I (284) esp_image: segment 2: paddr=0x00029cf0 vaddr=0x40080000 size=0x00404 (  1028) load
I (299) esp_image: segment 3: paddr=0x0002a0fc vaddr=0x40080404 size=0x05f1c ( 24348) load
I (332) esp_image: segment 4: paddr=0x00030020 vaddr=0x400d0020 size=0x5bab4 (375476) map
I (549) esp_image: segment 5: paddr=0x0008badc vaddr=0x40086320 size=0x04ce4 ( 19684) load
I (599) boot: Loaded app from partition at offset 0x10000
I (600) boot: Disabling RNG early entropy source...
I (607) cpu_start: Pro cpu up.
I (608) cpu_start: Application information:
I (608) cpu_start: Project name:     tcp_server
I (609) cpu_start: App version:      091a1e4-dirty
I (609) cpu_start: Compile time:     May 13 2020 23:02:48
I (610) cpu_start: ELF file SHA256:  d23b425172c23f33...
I (611) cpu_start: ESP-IDF:          v4.2-dev-1303-gcd4fa46f5
I (612) cpu_start: Starting app cpu, entry point is 0x400814cc
I (3318) cpu_start: App cpu up.
I (3816) heap_init: Initializing. RAM available for dynamic allocation:
I (3824) heap_init: At 3FFAE6E0 len 00001920 (6 KiB): DRAM
I (3829) heap_init: At 3FFB3CE8 len 0002C318 (176 KiB): DRAM
I (3832) heap_init: At 3FFE0440 len 00003AE0 (14 KiB): D/IRAM
I (3836) heap_init: At 3FFE4350 len 0001BCB0 (111 KiB): D/IRAM
I (3841) heap_init: At 4008B004 len 00014FFC (83 KiB): IRAM
I (3851) cpu_start: Pro cpu start user code
I (1241) spi_flash: detected chip: gd
I (1253) spi_flash: flash io: dio
W (1257) spi_flash: Detected size(4096k) larger than the size in the binary image header(2048k). Using the size in the binary image header.
I (1259) cpu_start: Starting scheduler on PRO CPU.
I (0) cpu_start: Starting scheduler on APP CPU.
I (1470) system_api: Base MAC address is not set
I (1480) system_api: read default base MAC address from EFUSE
I (1490) esp_eth.netif.glue: 00:00:00:00:00:03
I (1490) esp_eth.netif.glue: ethernet attached to netif
I (1500) example_connect: Waiting for IP
I (4470) esp_netif_handlers: eth ip: 10.0.2.15, mask: 255.255.255.0, gw: 10.0.2.2
I (4470) example_connect: Got IP event!
I (4480) example_connect: Connected to Ethernet
I (4480) example_connect: IPv4 address: 10.0.2.15
I (4490) example: Socket created
I (4490) example: Socket bound, port 3333
I (4490) example: Socket listening

WHEN CONNECTED TO SOCKET ON PORT 3333

I (4466) example: Socket created
I (4476) example: Socket bound, port 3333
I (4476) example: Socket listening
I (11686) example: Socket accepted ip address: 172.18.0.1

on new terminal:
$ nc localhost 3333
HI FROM ESP 32 (press enter)

on browser enter http://localhost:8000/data and response is:
{"input data from ESP32": "['HI FROM ESP 32']"}
```
