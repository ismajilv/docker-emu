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
    && rm -rf /var/lib/apt/lists/

COPY build/build.sh /usr/local/bin/

RUN bash /usr/local/bin/build.sh

EXPOSE 2222 6666

HEALTHCHECK CMD ["nc", "-z", "-w5", "localhost", "2222"]

CMD qemu-system-arm -kernel kernel-qemu-stretch -append "root=/dev/sda2 rootfstype=ext4 rw" -hda 2018-06-27-raspbian-stretch-lite.qcow2 -serial tcp::6666,server -cpu arm1176 -m 256 -machine versatilepb -no-reboot -dtb versatile-pb.dtb -nographic -net "user,hostfwd=tcp::2222-:22,hostfwd=tcp::1883-:1883" -net nic 
