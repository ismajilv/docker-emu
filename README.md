
# docker-emu

This docker image runs QEMU system emulation for Raspbian Stretch Lite. 
It will let you run Raspbian as if it was running on an actual Raspberry PI. 

## Usage

SSH is enabled on port `2222`. The username is `pi` and the password is `raspberry`. 

To run the container:

`docker run -it -p 2222:2222 --privileged ismajilv/docker-emu`

To connect with SSH:

`ssh -p 2222 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no pi@localhost`

qemu-system-arm -kernel kernel-qemu-stretch -append root=/dev/sda2 rootfstype=ext4 rw' -hda raspbian-lite.qcow2 -cpu arm1176 -m 256 -machine versatilepb -no-reboot -dtb versatile-pb.dtb -nographic -net user,hostfwd=tcp::2222-:22,hostfwd=tcp::2333-:2333 -net nic
