# hash:sha256:080f535c73fcf75dcde68775aa219e0491fb237a1f8cb23b47b1092925890a52
FROM registry.codeocean.com/codeocean/miniconda3:4.7.10-python3.7-ubuntu18.04

ARG DEBIAN_FRONTEND=noninteractive

RUN conda install -y \
        matplotlib==3.1.1 \
    && conda clean -ya

RUN pip install -U --no-cache-dir \
    opencv-contrib-python-headless==4.1.1.26

COPY postInstall /
RUN /postInstall
