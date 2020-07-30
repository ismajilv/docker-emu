# Limitations of the emulated IoT system
- Peripherals such as I2C, GPIO, SPI not working but UART can be implemented in a way described here for ESP32: [echo](./examples/echo)
- GPIO is working for Raspberry Pi, see example: [raspberry_gpio](./examples/raspberry_gpio)
- Emulated ethernet establish connection between `ESP32` and `Raspberry Pi`, not WiFi
- Configuring `Raspberry Pi` emulation with `ansible` takes considerably more time than real experience