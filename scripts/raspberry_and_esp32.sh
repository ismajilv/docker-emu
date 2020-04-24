#!/bin/bash

# Downloads pre-built:
# - flash_image.bin : esp32 bin file with mqtt client 
# - qemu-system-xtensa/qemu-system-xtensa : qemu file to start esp32 emulation
# - raspbian-lite-small.qcow2 : qcow2 file that has mosquitto broker

RPI_QEMU_KERNEL=kernel-qemu-4.9.59-stretch
RPI_QEMU_KERNEL_COMMIT=813a28ec2ccaf7fc1380f61283b5e74f8d675de5
DOCKER_EMU_URL=https://www.dropbox.com/sh/e71mzurg42qnrha/AACb_gYygq7fKqhUJ-RFMdEHa?dl=1/
DOCKER_EMU_FOLDER=mqtt-docker
RASPBIAN_IMAGE=raspbian-lite-small

set -x 
curl -L $DOCKER_EMU_FOLDER $DOCKER_EMU_URL > $DOCKER_EMU_FOLDER.zip
unzip $DOCKER_EMU_FOLDER.zip
rm $DOCKER_EMU_FOLDER.zip
curl https://raw.githubusercontent.com/dhruvvyas90/qemu-rpi-kernel/$RPI_QEMU_KERNEL_COMMIT/$RPI_QEMU_KERNEL > kernel-qemu-stretch
curl -O https://raw.githubusercontent.com/dhruvvyas90/qemu-rpi-kernel/$RPI_QEMU_KERNEL_COMMIT/versatile-pb.dtb

qemu-img resize $RASPBIAN_IMAGE.qcow2 +2G
guestfish --rw -m /dev/sda1 -a $RASPBIAN_IMAGE.qcow2 write /ssh ""
