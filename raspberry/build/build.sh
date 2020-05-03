#!/bin/bash

# constants
RPI_QEMU_KERNEL=kernel-qemu-4.9.59-stretch
RPI_QEMU_KERNEL_COMMIT=813a28ec2ccaf7fc1380f61283b5e74f8d675de5
RASPBIAN_IMAGE=2018-06-27-raspbian-stretch-lite

# urls
RASPBIAN_IMAGE_URL=http://director.downloads.raspberrypi.org/raspbian_lite/images/raspbian_lite-2018-06-29/
RASPBIAN_QEMU_KERNEL_URL=https://raw.githubusercontent.com/dhruvvyas90/qemu-rpi-kernel

# downloads
set -x 
curl -O $RASPBIAN_IMAGE_URL/$RASPBIAN_IMAGE.zip
curl $RASPBIAN_QEMU_KERNEL_URL/$RPI_QEMU_KERNEL_COMMIT/$RPI_QEMU_KERNEL > kernel-qemu-stretch
curl -O $RASPBIAN_QEMU_KERNEL_URL/$RPI_QEMU_KERNEL_COMMIT/versatile-pb.dtb

# run
unzip $RASPBIAN_IMAGE.zip
rm $RASPBIAN_IMAGE.zip
qemu-img convert -f raw -O qcow2 $RASPBIAN_IMAGE.img $RASPBIAN_IMAGE.qcow2
rm $RASPBIAN_IMAGE.img
qemu-img resize $RASPBIAN_IMAGE.qcow2 +2G
guestfish --rw -m /dev/sda1 -a $RASPBIAN_IMAGE.qcow2 write /ssh ""
