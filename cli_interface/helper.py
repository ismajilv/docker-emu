import subprocess


def get_raspberry_pi_device_id():
    id = subprocess.run(
        ["sudo", "docker", "ps", "-aqf", "name=docker-emu_raspberry-service"],
        stdout=subprocess.PIPE,
    )

    return id.stdout.decode().strip() if id else None


def get_esp32_device_id(device_id: str):
    id = subprocess.run(
        ["sudo", "docker", "ps", "-aqf", "name=docker-emu_esp32_" + device_id],
        stdout=subprocess.PIPE,
    )

    return id.stdout.decode().strip() if id else None


def get_esp32_port(device_id: str, type: str):
    id = get_esp32_device_id(device_id)
    if not id:
        return

    if type in ["flash", "monitor"]:
        address = subprocess.run(
            ["sudo", "docker", "port", id, "5555/tcp"], stdout=subprocess.PIPE,
        )
    elif type == "socket":
        address = subprocess.run(
            ["sudo", "docker", "port", id, "3333/tcp"], stdout=subprocess.PIPE,
        )
    elif type == "gdb":
        address = subprocess.run(
            ["sudo", "docker", "port", id, "1234/tcp"], stdout=subprocess.PIPE,
        )
    else:
        return None

    return address.stdout.decode().split(":")[1].strip() if id else None
