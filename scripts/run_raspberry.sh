#!/usr/bin/expect -f

set timeout -1

spawn qemu-system-arm -kernel kernel-qemu-stretch -append "root=/dev/sda2 rootfstype=ext4 rw" -hda raspbian-lite.qcow2 -cpu arm1176 -m 256 -machine versatilepb -no-reboot -dtb versatile-pb.dtb -nographic -net "user,hostfwd=tcp::2222-:22,hostfwd=tcp::2333-:2333" -net nic

expect "raspberrypi login: "
send "pi\r"

expect "Password: "
send "raspberry\r"

expect "# "