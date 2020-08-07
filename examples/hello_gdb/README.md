# Hello GDB Example

Starts a FreeRTOS task to print "Hello World" and also demonstrate usage of GDB with qemu.

ESP32
 - Connect GDB to target on remote port 1234

How to run:
```
Inisde examples/hello_gdb/esp32 folder
$ emu start   # Starts 1 instance of Raspberry Pi and 1 instance of ESP32
$ emu flash --id 1
$ emu monitor --id 1
```
You should see the output on idf.py monitor:
```
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
I (199) boot: ESP-IDF v4.2-dev-1303-gcd4fa46f5 2nd stage bootloader
I (214) boot: compile time 21:08:26
I (217) boot: chip revision: 0
I (220) boot.esp32: SPI Speed      : 40MHz
I (221) boot.esp32: SPI Mode       : DIO
I (222) boot.esp32: SPI Flash Size : 2MB
I (228) boot: Enabling RNG early entropy source...
I (235) boot: Partition Table:
I (235) boot: ## Label            Usage          Type ST Offset   Length
I (236) boot:  0 nvs              WiFi data        01 02 00009000 00006000
I (245) boot:  1 phy_init         RF data          01 01 0000f000 00001000
I (246) boot:  2 factory          factory app      00 00 00010000 00100000
I (251) boot: End of partition table
I (254) esp_image: segment 0: paddr=0x00010020 vaddr=0x3f400020 size=0x05aec ( 23276) map
I (276) esp_image: segment 1: paddr=0x00015b14 vaddr=0x3ffb0000 size=0x021dc (  8668) load
I (289) esp_image: segment 2: paddr=0x00017cf8 vaddr=0x40080000 size=0x00404 (  1028) load
I (298) esp_image: segment 3: paddr=0x00018104 vaddr=0x40080404 size=0x07f14 ( 32532) load
I (323) esp_image: segment 4: paddr=0x00020020 vaddr=0x400d0020 size=0x12fac ( 77740) map
I (379) esp_image: segment 5: paddr=0x00032fd4 vaddr=0x40088318 size=0x01a3c (  6716) load
I (401) boot: Loaded app from partition at offset 0x10000
I (402) boot: Disabling RNG early entropy source...
I (410) cpu_start: Pro cpu up.
I (410) cpu_start: Application information:
I (411) cpu_start: Project name:     hello-world
I (411) cpu_start: App version:      1
I (412) cpu_start: Compile time:     May 25 2020 21:08:09
I (412) cpu_start: ELF file SHA256:  7cb60c7700db4fb0...
I (413) cpu_start: ESP-IDF:          v4.2-dev-1303-gcd4fa46f5
I (413) cpu_start: Starting app cpu, entry point is 0x40081270
I (1960) cpu_start: App cpu up.
I (2597) heap_init: Initializing. RAM available for dynamic allocation:
I (2606) heap_init: At 3FFAE6E0 len 00001920 (6 KiB): DRAM
I (2610) heap_init: At 3FFB2A20 len 0002D5E0 (181 KiB): DRAM
I (2613) heap_init: At 3FFE0440 len 00003AE0 (14 KiB): D/IRAM
I (2616) heap_init: At 3FFE4350 len 0001BCB0 (111 KiB): D/IRAM
I (2619) heap_init: At 40089D54 len 000162AC (88 KiB): IRAM
I (2629) cpu_start: Pro cpu start user code
I (810) spi_flash: detected chip: gd
I (827) spi_flash: flash io: dio
W (831) spi_flash: Detected size(4096k) larger than the size in the binary image header(2048k). Using the size in the binary image header.
I (832) cpu_start: Starting scheduler on PRO CPU.
I (0) cpu_start: Starting scheduler on APP CPU.
Hello world!
This is esp32 chip with 2 CPU cores, WiFi/BT/BLE, silicon revision 0, 2MB external flash
Free heap: 299556
Restarting in 10 seconds...
Restarting in 9 seconds...
Restarting in 8 seconds...
Restarting in 7 seconds...
Restarting in 6 seconds...
Restarting in 5 seconds...
Restarting in 4 seconds...
Restarting in 3 seconds...
Restarting in 2 seconds...
Restarting in 1 seconds...
Restarting in 0 seconds...
Restarting now.
```

And then open new terminal insiede docker-emu/examples/hello_gdb/esp32/ while emu monitor is running and run:
```
$ emu eport --id 1     # Get the GDB port and update in below command
$ xtensa-esp32-elf-gdb build/hello-world.elf -ex "target remote :{GDB_PORT}" -ex "monitor system_reset" -ex "tb app_main" -ex "c"
GNU gdb (crosstool-NG esp-2020r1) 8.1.0.20180627-git
Copyright (C) 2018 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "--host=x86_64-build_pc-linux-gnu --target=xtensa-esp32-elf".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from build/hello-world.elf...done.
Remote debugging using :1234
0x400e2bca in esp_pm_impl_waiti () at /home/ismajilv/esp/esp-idf/esp-idf-4.2/components/esp32/pm_esp32.c:484
484         asm("waiti 0");
Temporary breakpoint 1 at 0x400d2a2c: file ../main/hello_world_main.c, line 17.
Continuing.

Thread 1 hit Temporary breakpoint 1, app_main () at ../main/hello_world_main.c:17
17      {

AND TERMINAL OUTPUT WILL BE
 (178748) heap_init: Initializing. RAM available for dynamic allocation:
I (178754) heap_init: At 3FFAE6E0 len 00001920 (6 KiB): DRAM
I (178756) heap_init: At 3FFB2A20 len 0002D5E0 (181 KiB): DRAM
I (178759) heap_init: At 3FFE0440 len 00003AE0 (14 KiB): D/IRAM
I (178762) heap_init: At 3FFE4350 len 0001BCB0 (111 KiB): D/IRAM
I (178792) heap_init: At 40089D54 len 000162AC (88 KiB): IRAM
I (178798) cpu_start: Pro cpu start user code
I (23865) spi_flash: detected chip: gd
I (23870) spi_flash: flash io: dio
W (23886) spi_flash: Detected size(4096k) larger than the size in the binary image header(2048k). Using the size in the binary image header.
I (23887) cpu_start: Starting scheduler on PRO CPU.
I (0) cpu_start: Starting scheduler on APP CPU.
```

In GDB press `c` to continue and idf.py monitor output will be updated accordingly
