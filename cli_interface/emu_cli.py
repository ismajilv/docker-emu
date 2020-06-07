import click
import time
import subprocess
from subprocess import PIPE, STDOUT, DEVNULL
from helper import get_device_id


@click.group()
def cli():
    pass


@cli.command(help="Start IoT lab environment")
def start():
    subprocess.Popen(
        ["sudo", "docker-compose", "up"], stdin=PIPE, stdout=DEVNULL, stderr=STDOUT
    )
    click.echo("IoT lab started. ESP32 and Raspberry Pi are running!")


@cli.command(help="Stop IoT lab environment")
def stop():
    esp32_id = get_device_id("esp32")
    subprocess.run(
        ["sudo", "docker", "rm", "-f", esp32_id], stdout=DEVNULL, stderr=STDOUT,
    )

    raspberry_pi_id = get_device_id("raspberry_pi")
    subprocess.run(
        ["sudo", "docker", "rm", "-f", raspberry_pi_id], stdout=DEVNULL, stderr=STDOUT,
    )
    click.echo("IoT lab environment stopped!")


@cli.command(help="Restart IoT lab environment")
@click.pass_context
def restart(context):
    context.invoke(stop)
    context.invoke(start)


@cli.command(help="['esp32', 'raspberry_pi'] log one of the device logs")
@click.argument("device")
def log(device):
    if device in ["esp32", "raspberry_pi"]:
        device_id = get_device_id(device)
        subprocess.run(["sudo", "docker", "logs", device_id])
    else:

        click.echo("Please provide one of [esp32, raspberry_pi]")


@cli.command(help="Same as idf.py flash")
def flash():
    esp32_id = get_device_id("esp32")
    subprocess.run(
        [
            "sudo",
            "docker",
            "exec",
            esp32_id,
            "bash",
            "-c",
            "pkill -f qemu-system-xtensa",
        ],
        stdout=DEVNULL,
        stderr=STDOUT,
    )
    subprocess.Popen(
        [
            "sudo",
            "docker",
            "exec",
            esp32_id,
            "bash",
            "-c",
            "./qemu-system-xtensa/qemu-system-xtensa -nographic -machine esp32 -drive file=flash_image.bin,if=mtd,format=raw -global driver=esp32.gpio,property=strap_mode,value=0x0f -echr 0x02 -serial tcp::5555,server -nic user,model=open_eth,id=lo0,hostfwd=tcp::3333-:3333 -gdb tcp::1234",
        ],
        stdout=DEVNULL,
        stderr=STDOUT,
    )
    subprocess.run(["idf.py", "flash", "-p", "socket://localhost:5555"])
    print("Flashed successfully!")


@cli.command(help="Same as idf.py monitor")
def monitor():
    esp32_id = get_device_id("esp32")
    subprocess.run(
        [
            "sudo",
            "docker",
            "exec",
            esp32_id,
            "bash",
            "-c",
            "killall qemu-system-xtensa",
        ]
    )
    subprocess.Popen(
        [
            "sudo",
            "docker",
            "exec",
            esp32_id,
            "bash",
            "-c",
            "./qemu-system-xtensa/qemu-system-xtensa -nographic -machine esp32 -drive file=flash_image.bin,if=mtd,format=raw -echr 0x02 -serial tcp::5555,server -nic user,model=open_eth,id=lo0,hostfwd=tcp::3333-:3333 -gdb tcp::1234",
        ],
        stdout=DEVNULL,
        stderr=STDOUT,
    )
    subprocess.run(["idf.py", "monitor", "-p", "socket://localhost:5555"])


@cli.command(help="SSH into raspbian")
def ssh():
    subprocess.run(["ssh", "-p", "2222", "-o", "UserKnownHostsFile=/dev/null", "-o", "StrictHostKeyChecking=no", "pi@localhost"])