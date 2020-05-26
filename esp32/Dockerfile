FROM ubuntu:18.04

ARG GDB

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

COPY build/qemu-system-xtensa ./

EXPOSE 1234 3333 5555

CMD ./qemu-system-xtensa/qemu-system-xtensa -nographic -machine esp32 -drive file=./mount/flash_image.bin,if=mtd,format=raw -echr 0x02 -serial tcp::5555,server -nic user,model=open_eth,id=lo0,hostfwd=tcp::3333-:3333 `if [ $GDB = TRUE ]; then echo "-s -S"; fi`
