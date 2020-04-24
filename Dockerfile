FROM ubuntu:18.04

WORKDIR /root

RUN set -x \
    && apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        xz-utils libpixman-1-0 libpng16-16 libjpeg8 libglib2.0 \
        busybox \
        curl \
        qemu \
        libguestfs-tools \
        unzip \
        linux-image-generic:amd64 \
        netcat \
        sshpass \
        expect \
    && rm -rf /var/lib/apt/lists/

COPY scripts /usr/local/bin/

RUN bash /usr/local/bin/raspberry_and_esp32.sh

EXPOSE 2222 5555 6666

HEALTHCHECK CMD ["nc", "-z", "-w5", "localhost", "2222"]

CMD nohup qemu-system-arm -kernel kernel-qemu-stretch -append "root=/dev/sda2 rootfstype=ext4 rw" -hda raspbian-lite-small.qcow2 -serial tcp::6666,server -cpu arm1176 -m 256 -machine versatilepb -no-reboot -dtb versatile-pb.dtb -nographic -net "user,hostfwd=tcp::2222-:22,hostfwd=tcp::1883-:1883" -net nic 2>/dev/null & ./qemu-system-xtensa/qemu-system-xtensa -nographic -machine esp32 -drive file=flash_image.bin,if=mtd,format=raw -echr 0x02 -serial tcp::5555,server -nic user,model=open_eth
