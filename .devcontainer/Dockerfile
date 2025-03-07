FROM python:3.11-slim

# Install sudo and curl
RUN apt update && \
    apt install -y sudo curl

# Create a non-root user
ARG USERNAME=nonroot
RUN groupadd --gid 1000 $USERNAME && \
    useradd --uid 1000 --gid 1000 -m $USERNAME
ENV PATH="/home/${USERNAME}/.local/bin:${PATH}"
USER $USERNAME

# Upgrade pip and install PDM
RUN pip install --upgrade pip pdm

# Set working directory and install dependencies using PDM
COPY --chown=nonroot:1000 . /tmp/src
WORKDIR /tmp/src
RUN pdm install