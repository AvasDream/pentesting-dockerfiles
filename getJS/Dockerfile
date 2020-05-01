FROM golang:latest

RUN apt update &&\
    go get -u github.com/003random/getJS

ENTRYPOINT [ "getJS" ]