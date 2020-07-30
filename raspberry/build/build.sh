#!/bin/bash

# constants
RPI_QEMU_KERNEL=kernel-qemu-4.4.13-jessie
RPI_QEMU_KERNEL_COMMIT=aecfbd4275963e3be1ddf1ad361a905ce518e797

# urls
RASPBIAN_QEMU_KERNEL_URL=https://github.com/dhruvvyas90/qemu-rpi-kernel/blob/

# downloads
set -x 
wget -O $RPI_QEMU_KERNEL $RASPBIAN_QEMU_KERNEL_URL/$RPI_QEMU_KERNEL_COMMIT/$RPI_QEMU_KERNEL?raw=true


# unzip
unzip 2016-05-27-raspbian-jessie-lite.img.zip
rm 2016-05-27-raspbian-jessie-lite.img.zip
