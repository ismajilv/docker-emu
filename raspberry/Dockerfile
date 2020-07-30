FROM ubuntu:16.04

WORKDIR /root

RUN set -x \
    && apt-get update --fix-missing \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        xz-utils libpixman-1-0 libpng16-16 libjpeg8 libglib2.0 \
        busybox \
        curl \
        qemu \
        libguestfs-tools \
        unzip \
        linux-image-generic:amd64 \
        netcat \
        wget \
    && rm -rf /var/lib/apt/lists/

COPY build/ /usr/local/bin/

COPY image/2016-05-27-raspbian-jessie-lite.img.zip ./

RUN bash /usr/local/bin/build.sh

EXPOSE 2222 8000

HEALTHCHECK CMD ["nc", "-z", "-w5", "localhost", "2222"]

CMD /usr/local/bin/qemu-system-arm -kernel kernel-qemu-4.4.13-jessie -cpu arm1176 -m 256 -M versatilepb -no-reboot -append "root=/dev/sda2 rootfstype=ext4 rw" -drive file=2016-05-27-raspbian-jessie-lite.img,format=raw -nographic -net "user,hostfwd=tcp::2222-:22,hostfwd=tcp::8000-:8000" -net nic 