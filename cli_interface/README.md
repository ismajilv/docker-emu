# EMU IoT Lab Environment CLI (Command Line Interface)

## Setup `emu` cli
cli uses python's subprocess module, to manage containers with docker client. The Docker daemon always runs as the root user, and if you run
cli without sudo privilege, `emu` will ask for `sudo` password. So it is preferable, to add your `$USER` to `docker` group. 
Please have a look [here](https://docs.docker.com/engine/install/linux-postinstall/) to add your `$USER` to `docker` group.

You could get some dependencies missing warning when running emu cli, it's due to `espressif` environment is not activated or wasn't installed properly. 

Install with:
```
$ python3 -m pip install --editable .
```
## Usage of CLI


```
$ emu --help
Usage: emu [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  flash    Same as idf.py flash
  log      ['esp32', 'raspberry_pi'] log one of the device logs
  monitor  Same as idf.py monitor
  restart  Restart IoT lab environment
  ssh      SSH into raspbian
  start    Start IoT lab environment
  stop     Stop IoT lab environment
```