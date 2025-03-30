FROM public.ecr.aws/docker/library/python:3.13-bullseye as base
ARG USERNAME=user
ARG GROUPNAME=user
ARG UID=1000
ARG GID=1000
RUN apt-get update && apt-get install -y curl
RUN groupadd -g $GID $GROUPNAME && \
    useradd -m -s /bin/bash -u $UID -g $GID $USERNAME

USER $USERNAME
WORKDIR /home/$USERNAME/app
ENV PYTHONUNBUFFERED=1
ENV POETRY_VIRTUALENVS_CREATE=false

RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH /home/$USERNAME/.local/bin:$PATH

FROM base as develop

FROM base as production
COPY . .
RUN poetry install --group webapi
