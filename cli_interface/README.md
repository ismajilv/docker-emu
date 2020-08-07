# EMU IoT Lab Environment CLI (Command Line Interface)

## Setup `emu` cli
cli uses python's subprocess module, to manage containers with docker client. The Docker daemon always runs as the root user, and if you run
cli without sudo privilege, `emu` will ask for `sudo` password. So it is preferable, to add your `$USER` to `docker` group. 
Please have a look [here](https://docs.docker.com/engine/install/linux-postinstall/) to add your `$USER` to `docker` group.

Please use `python3` to setup emu cli and note that you could get some dependencies missing warning when running emu cli, it's due to `espressif` environment is not activated or wasn't installed properly. 

Install with:
```
$ pip3 install -r requirements.txt
$ python3 -m pip install --editable .
```
## Usage of CLI


```
$ emu --help
Usage: emu [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  eport    Get port information of ESP32, option: --id n
  esocket  Connect to socket port of ESP32, option: --id n
  flash    Same as idf.py flash, option: --id n
  log      ['esp32 --id [1 to n]', 'raspberry_pi'] device logs
  monitor  Same as idf.py monitor, option: --id n
  restart  Restart IoT lab environment
  rgpio    See raspberry pi gpio state
  ssh      SSH into raspbian
  start    Start IoT lab environment, option: --scale-esp32 n
  stop     Stop IoT lab environment
```
