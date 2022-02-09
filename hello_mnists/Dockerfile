FROM  nvidia/cuda:11.3.1-cudnn8-devel-ubuntu20.04

# Change default shell.
SHELL ["/bin/bash", "-c"]

ENV DEBIAN_FRONTEND=noninteractive
ENV LANG C.UTF-8

# Install Python & Pip.
RUN apt-get update && apt-get install --no-install-recommends -y \
    python3.9 \
    python3.9-distutils \
    curl && \
    apt-get -o Dpkg::Options::="--force-confmiss" install --reinstall -y netbase
RUN ln -s $(which python3.9) /usr/local/bin/python3
RUN ln -s $(which python3.9) /usr/local/bin/python
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py \
    && python get-pip.py && rm -rf get-pip.py
RUN python -m pip --no-cache-dir install --upgrade \
    pip \
    setuptools \
    wheel && \
    pip install --no-cache-dir torch==1.10.1+cu113 torchvision==0.11.2+cu113 torchaudio==0.10.1+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html && \
    pip install --no-cache-dir pytorch-lightning==1.5.1 torchviz --upgrade

# Tell Tensorflow where to find CUDA.
ENV LD_LIBRARY_PATH /usr/local/cuda/lib64:$LD_LIBRARY_PATH
RUN ln -s /usr/local/cuda/lib64/stubs/libcuda.so /usr/local/cuda/lib64/stubs/libcuda.so.1 \
    && echo "/usr/local/cuda/lib64/stubs" > /etc/ld.so.conf.d/z-cuda-stubs.conf \
    && ldconfig

# Prepare the current project.
WORKDIR /gridai/project
COPY . .
RUN python -m pip install --no-cache-dir -r requirements.txt