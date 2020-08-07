# ECHO sample application

ESP32 launches TCP server that listens on socket for incoming characters. After receiving character data from terminal, sends it to server running on Rasppberry Pi via POST request. Server runnin on Raspberry Pi keeps request data in list and it can be obtained by GET request.

ESP32
 - TCP server listen on port 3333
 - HTTP client POST 

Raspberry Pi
 - Accept POST on server running on port 8000
 - Keeps ESP32 input data in list

How to run:
```
Inisde examples/echo/esp32 folder
$ emu start --scale-esp32 2     # Run 2 instances of ESP32 and 1 instance of Raspberry Pi
$ emu flash --id 1              # Flash to ESP32 device with id 1
$ emu flash --id 2              # Flash to ESP32 device with id 2
$ cd ../raspberry
$ ansible-playbook -i ../../../ansible/inventory/hosts setup.yml // TAKES TIME
$ cd ../esp32/
$ emu monitor --id 1            # Monitor ESP32 device with id 1
$ emu monitor --id 2            # Monitor ESP32 device with id 2
```
Now you should see this output for both ESP32 devices:
```
Executing action: monitor
Running idf_monitor in directory /home/ismajilv/Documents/iot/code/git/docker-emu/examples/echo/esp32
Executing "/home/ismajilv/.espressif/python_env/idf4.2_py3.6_env/bin/python /home/ismajilv/esp/esp-idf/esp-idf-4.2/tools/idf_monitor.py -p socket://localhost:5555 -b 115200 --toolchain-prefix xtensa-esp32-elf- /home/ismajilv/Documents/iot/code/git/docker-emu/examples/echo/esp32/build/tcp_server.elf -m '/home/ismajilv/.espressif/python_env/idf4.2_py3.6_env/bin/python' '/home/ismajilv/esp/esp-idf/esp-idf-4.2/tools/idf.py'"...
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
I (205) boot: ESP-IDF v4.2-dev-1303-gcd4fa46f5 2nd stage bootloader
I (214) boot: compile time 12:59:51
I (221) boot: chip revision: 0
I (224) boot.esp32: SPI Speed      : 40MHz
I (228) boot.esp32: SPI Mode       : DIO
I (228) boot.esp32: SPI Flash Size : 2MB
I (238) boot: Enabling RNG early entropy source...
I (244) boot: Partition Table:
I (246) boot: ## Label            Usage          Type ST Offset   Length
I (247) boot:  0 nvs              WiFi data        01 02 00009000 00006000
I (255) boot:  1 phy_init         RF data          01 01 0000f000 00001000
I (265) boot:  2 factory          factory app      00 00 00010000 00100000
I (271) boot: End of partition table
I (276) esp_image: segment 0: paddr=0x00010020 vaddr=0x3f400020 size=0x17a00 ( 96768) map
I (343) esp_image: segment 1: paddr=0x00027a28 vaddr=0x3ffb0000 size=0x022c0 (  8896) load
I (361) esp_image: segment 2: paddr=0x00029cf0 vaddr=0x40080000 size=0x00404 (  1028) load
0x40080000: _WindowOverflow4 at /home/ismajilv/esp/esp-idf/esp-idf-4.2/components/freertos/xtensa/xtensa_vectors.S:1730

I (376) esp_image: segment 3: paddr=0x0002a0fc vaddr=0x40080404 size=0x05f1c ( 24348) load
I (423) esp_image: segment 4: paddr=0x00030020 vaddr=0x400d0020 size=0x5bab4 (375476) map
0x400d0020: _stext at ??:?

I (653) esp_image: segment 5: paddr=0x0008badc vaddr=0x40086320 size=0x04ce4 ( 19684) load
0x40086320: spi_flash_ll_set_addr_bitlen at /home/ismajilv/esp/esp-idf/esp-idf-4.2/components/soc/src/esp32/include/hal/spi_flash_ll.h:345
 (inlined by) spi_flash_hal_configure_host_io_mode at /home/ismajilv/esp/esp-idf/esp-idf-4.2/components/soc/src/hal/spi_flash_hal_common.inc:81

I (702) boot: Loaded app from partition at offset 0x10000
I (704) boot: Disabling RNG early entropy source...
I (711) cpu_start: Pro cpu up.
I (711) cpu_start: Application information:
I (712) cpu_start: Project name:     tcp_server
I (716) cpu_start: App version:      0765bba-dirty
I (717) cpu_start: Compile time:     May 30 2020 12:59:32
I (719) cpu_start: ELF file SHA256:  6c79dd8df45af2c8...
I (719) cpu_start: ESP-IDF:          v4.2-dev-1303-gcd4fa46f5
I (720) cpu_start: Starting app cpu, entry point is 0x400814cc
0x400814cc: call_start_cpu1 at /home/ismajilv/esp/esp-idf/esp-idf-4.2/components/esp32/cpu_start.c:286

I (3856) cpu_start: App cpu up.
I (4527) heap_init: Initializing. RAM available for dynamic allocation:
I (4538) heap_init: At 3FFAE6E0 len 00001920 (6 KiB): DRAM
I (4543) heap_init: At 3FFB3CE8 len 0002C318 (176 KiB): DRAM
I (4546) heap_init: At 3FFE0440 len 00003AE0 (14 KiB): D/IRAM
I (4549) heap_init: At 3FFE4350 len 0001BCB0 (111 KiB): D/IRAM
I (4552) heap_init: At 4008B004 len 00014FFC (83 KiB): IRAM
I (4621) cpu_start: Pro cpu start user code
I (1499) spi_flash: detected chip: gd
I (1511) spi_flash: flash io: dio
W (1516) spi_flash: Detected size(4096k) larger than the size in the binary image header(2048k). Using the size in the binary image header.
I (1517) cpu_start: Starting scheduler on PRO CPU.
I (10) cpu_start: Starting scheduler on APP CPU.
I (1727) system_api: Base MAC address is not set
I (1727) system_api: read default base MAC address from EFUSE
I (1747) esp_eth.netif.glue: 00:00:00:00:00:03
I (1747) esp_eth.netif.glue: ethernet attached to netif
I (1757) example_connect: Waiting for IP
I (4727) esp_netif_handlers: eth ip: 10.0.2.15, mask: 255.255.255.0, gw: 10.0.2.2
I (4727) example_connect: Got IP event!
I (4737) example_connect: Connected to Ethernet
I (4737) example_connect: IPv4 address: 10.0.2.15
I (4747) example: Socket created
I (4767) example: Socket bound, port 3333
I (4777) example: Socket listening
```

ON NEW TERMINAL: 
```
$ emu eport --id 1  
AND TYPE
HI FROM ESP32 DEVICE NUMBER 1 (press enter)
``` 

ON NEW TERMINAL: 
$ emu eport --id 2 
AND TYPE
HI FROM ESP32 DEVICE NUMBER 2 (press enter)
``` 

WHEN CONNECTED TO SOCKET ON PORT 3333, emu monitor output will be updated for both ESP32 devices:
```
I (11686) example: Socket accepted ip address: 172.18.0.1
```

on browser enter `http://localhost:8000/data` and response is:
```json
{"input data from ESP32": "['HI FROM ESP 32 DEVICE NUMBER 1', 'HI FROM ESP 32 DEVICE NUMBER 2']"}
```
