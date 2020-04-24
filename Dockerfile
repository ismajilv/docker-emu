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

COPY files .

COPY scripts /usr/local/bin/

RUN bash /usr/local/bin/raspberry.sh

RUN chmod a+x qemu-system-xtensa/qemu-system-xtensa

EXPOSE 1234 2222

HEALTHCHECK CMD ["nc", "-z", "-w5", "localhost", "2222"]

# RUN expect /usr/local/bin/run_raspberry.sh

# RUN ["apt-get install", "python3-pip"]

CMD ["qemu-system-arm", "-kernel", "kernel-qemu-stretch", "-append", "root=/dev/sda2 rootfstype=ext4 rw'", "-hda", "raspbian-lite.qcow2", "-cpu", "arm1176", "-m", "256", "-machine", "versatilepb", "-no-reboot", "-dtb", "versatile-pb.dtb", "-nographic", "-net", "user,hostfwd=tcp::2222-:22,hostfwd=tcp::2333-:2333", "-net", "nic"]
 
# CMD ["qemu-system-xtensa/qemu-system-xtensa", "-nographic", "-M", "esp32", "-drive", "file=esp32flash.bin,if=mtd,format=raw", "-s", "-S"]