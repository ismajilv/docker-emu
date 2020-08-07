# Raspberry Pi GPIO sample application

This example shows how to use Raspberry PI GPIO subsytem with IoT Lab Environment.

Raspberry Pi
 - Deploy simple C application that changes PIN to input/output and changes voltages to HIGH/LOW using wiringPi
 - View the `loop.c` file presented in the directory to see more abou it

How to run:
```
Inisde examples/raspberry_gpip/raspberry folder
$ emu start     # Starts 1 instance of Raspberry Pi and 1 instance of ESP32
$ emu rgpio     # In separate terminal to see gpio outputs
$ cd ../raspberry
$ ansible-playbook -i ../../../ansible/inventory/hosts setup.yml
```
With `emu rgpio` you should see this output:
```
        Func    LVL     Output
GPIO0   In      0       0
GPIO1   In      0       0
GPIO2   In      0       0
GPIO3   In      0       0
GPIO4   In      0       0
GPIO5   In      0       0
GPIO6   In      0       0
GPIO7   In      0       0
```

And when ansible script finished, raspberry pi GPIOs output should change starting from GPIO 00:
```
        Func    LVL     Output
GPIO0   In      0       0
GPIO1   In      0       0
GPIO2   In      0       0
GPIO3   In      0       0
GPIO4   In      0       0
GPIO5   In      0       0
GPIO6   In      0       0
GPIO7   In      0       0

        Func    LVL     Output
GPIO0   Out     0       0
GPIO1   In      0       0
GPIO2   In      0       0
GPIO3   In      0       0
GPIO4   In      0       0
GPIO5   In      0       0
GPIO6   In      0       0
GPIO7   In      0       0

        Func    LVL     Output
GPIO0   Out     0       1
GPIO1   In      0       0
GPIO2   In      0       0
GPIO3   In      0       0
GPIO4   In      0       0
GPIO5   In      0       0
GPIO6   In      0       0
GPIO7   In      0       0

        Func    LVL     Output
GPIO0   Out     0       0
GPIO1   In      0       0
GPIO2   In      0       0
GPIO3   In      0       0
GPIO4   In      0       0
GPIO5   In      0       0
GPIO6   In      0       0
GPIO7   In      0       0

        Func    LVL     Output
GPIO0   In      0       0
GPIO1   In      0       0
GPIO2   In      0       0
GPIO3   In      0       0
GPIO4   In      0       0
GPIO5   In      0       0
GPIO6   In      0       0
GPIO7   In      0       0

        Func    LVL     Output
GPIO0   In      0       0
GPIO1   Out     0       0
GPIO2   In      0       0
GPIO3   In      0       0
GPIO4   In      0       0
GPIO5   In      0       0
GPIO6   In      0       0
GPIO7   In      0       0

...
```