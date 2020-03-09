#!/bin/bash

RPI_QEMU_KERNEL=kernel-qemu-4.9.59-stretch
RPI_QEMU_KERNEL_COMMIT=813a28ec2ccaf7fc1380f61283b5e74f8d675de5
RASPBIAN_IMAGE=2018-06-27-raspbian-stretch-lite
RASPBIAN_IMAGE_URL=http://director.downloads.raspberrypi.org/raspbian_lite/images/raspbian_lite-2018-06-29/

set -x 
curl -O $RASPBIAN_IMAGE_URL/$RASPBIAN_IMAGE.zip
unzip $RASPBIAN_IMAGE.zip
rm $RASPBIAN_IMAGE.zip
curl https://raw.githubusercontent.com/dhruvvyas90/qemu-rpi-kernel/$RPI_QEMU_KERNEL_COMMIT/$RPI_QEMU_KERNEL > kernel-qemu-stretch
curl -O https://raw.githubusercontent.com/dhruvvyas90/qemu-rpi-kernel/$RPI_QEMU_KERNEL_COMMIT/versatile-pb.dtb
