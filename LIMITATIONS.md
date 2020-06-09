# Limitations of the emulated IoT system
- Peripherals such as I2C, GPIO, SPI not working but UART can be implemented in a way described here: https://github.com/ismajilv/docker-emu/tree/dev/examples/echo
- Emulated ethernet establish connection between `ESP32` and `Raspberry Pi`, not WiFi
- Configuring `Raspberry Pi` emulation with `ansible` takes considerably more time than real experience