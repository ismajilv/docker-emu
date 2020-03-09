#!/bin/bash

RASPBIAN_IMAGE=2018-06-27-raspbian-stretch-lite

set -x
qemu-img convert -f raw -O qcow2 $RASPBIAN_IMAGE.img raspbian-lite.qcow2
rm $RASPBIAN_IMAGE.img
qemu-img resize raspbian-lite.qcow2 +2G
guestfish --rw -m /dev/sda1 -a raspbian-lite.qcow2 write /ssh ""
