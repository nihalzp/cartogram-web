FROM python:3.7-stretch

COPY ./internal/requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

COPY ./internal /root/internal
COPY ./data /root/data

ENV CARTOGRAM_DATA_DIR=/root/data
ENV CARTOGRAM_LOCAL_DOCKERIZED=TRUE
ENV CARTOGRAM_EXE=
ENV CARTOGRAM_COLOR=#aaaaaa

ARG CARTOGRAM_VERSION=devel
ENV CARTOGRAM_VERSION $CARTOGRAM_VERSION

EXPOSE 5000
WORKDIR /root/internal
CMD ["sh", "-c", "python -c \"import web; web.db.create_all()\" && python web.py"]