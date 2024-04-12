FROM ubuntu:latest
LABEL authors="citr0n"

ENTRYPOINT ["top", "-b"]