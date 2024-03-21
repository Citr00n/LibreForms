FROM ubuntu:latest
LABEL authors="citro"

ENTRYPOINT ["top", "-b"]