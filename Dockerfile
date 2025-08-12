FROM ubuntu:latest
RUN apt-get update && apt-get install -y \
    vim \
    git \
    curl \
    net-tools
WORKDIR /app
EXPOSE 8000
RUN curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -o \
    /tmp/miniconda.sh && \
    /bin/bash /tmp/miniconda.sh -b -p /opt/miniconda && \
    rm /tmp/miniconda.sh
ENV PATH="/opt/miniconda/bin:${PATH}"
RUN conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/main
RUN conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/r
RUN conda update -n base -c defaults conda
RUN conda install -c conda-forge -c omnia \
    fastapi \
    foyer \
    python=3.12.0 \
    mbuild=0.18.0
ADD tools /app/tools
ADD main.py /app
CMD fastapi run main.py
