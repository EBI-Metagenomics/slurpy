FROM ubuntu:noble AS base
LABEL authors="mgnify team"

RUN groupadd -r slurm
RUN useradd -rm -d /home/slurm -s /bin/bash -g slurm -G sudo slurm
RUN mkdir -p /home/slurm && chown -R slurm:slurm /home/slurm
RUN useradd -rms /bin/bash munge
RUN useradd -M -r -s /usr/sbin/nologin -U slurmrestd

RUN apt -y update && apt -y upgrade && apt -y install curl nano wget zip bzip2 rsync build-essential

RUN apt -y install python3-pip python-is-python3

RUN apt -y install sudo gosu netcat-traditional

RUN apt-get install -y \
    libmunge-dev \
    munge \
    libcurl4-openssl-dev \
    libhttp-parser-dev \
    libjson-c-dev \
    libyaml-dev \
    libjwt-dev \
    libmariadb-dev \
    libmariadb-dev-compat \
    lua5.4 \
    pkgconf \
    dbus

ARG SLURM_VERSION=24.11.6
RUN curl -sL https://download.schedmd.com/slurm/slurm-${SLURM_VERSION}.tar.bz2 | tar -xj
RUN cd slurm-${SLURM_VERSION} && \
    ./configure --sysconfdir=/etc/slurm && \
    make install -j16

COPY configs/slurm.conf /etc/slurm/slurm.conf
COPY configs/slurmdbd.conf /etc/slurm/slurmdbd.conf
COPY configs/cgroup.conf /etc/slurm/cgroup.conf
RUN chmod 600 /etc/slurm/slurmdbd.conf
RUN chown -R slurm:slurm /etc/slurm/

RUN mkdir -p /run/munge && chown -R munge /run/munge
RUN mkdir -p /var/run/slurm && chown -R slurm:slurm /var/run/slurm
RUN mkdir -p /var/log/slurm && chown -R slurm:slurm /var/log/slurm
RUN mkdir -p /var/spool/slurmctld && chown -R slurm:slurm /var/spool/slurmctld
RUN mkdir -p /var/spool/slurmd && chown -R slurm:slurm /var/spool/slurmd

# Setup jwt key - generate random 256-bit key
RUN dd if=/dev/random of=/var/spool/slurmctld/jwt_hs256.key bs=32 count=1
RUN chown slurm:slurm /var/spool/slurmctld/jwt_hs256.key
RUN chmod 0600 /var/spool/slurmctld/jwt_hs256.key


# DBD + Ctl + Worker + REST in a single container
COPY entrypoints/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
