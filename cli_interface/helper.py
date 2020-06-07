import subprocess


def get_device_id(device):
    id = None
    if device == "esp32":
        id = subprocess.run(
            ["sudo", "docker", "ps", "-aqf", "name=docker-emu_esp32"],
            stdout=subprocess.PIPE,
        )
    elif device == "raspberry_pi":
        id = subprocess.run(
            ["sudo", "docker", "ps", "-aqf", "name=docker-emu_raspberry-service"],
            stdout=subprocess.PIPE,
        )

    return id.stdout.decode().strip() if id else None
