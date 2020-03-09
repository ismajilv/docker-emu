FROM debian:stretch-slim

WORKDIR /root

RUN set -x \
    && apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        busybox \
        curl \
        qemu \
        libguestfs-tools \
        unzip \
        linux-image-amd64 \
        netcat \
    && rm -rf /var/lib/apt/lists/

COPY scripts /usr/local/bin/

RUN bash /usr/local/bin/download.sh

RUN bash /usr/local/bin/run.sh

EXPOSE 2222

HEALTHCHECK CMD ["nc", "-z", "-w5", "localhost", "2222"]

CMD ["qemu-system-arm", "-kernel", "kernel-qemu-stretch", "-append", "root=/dev/sda2 rootfstype=ext4 rw'", "-hda", "raspbian-lite.qcow2", "-cpu", "arm1176", "-m", "256", "-machine", "versatilepb", "-no-reboot", "-dtb", "versatile-pb.dtb", "-nographic", "-net", "user,hostfwd=tcp::2222-:22", "-net", "nic"]
 