FROM fedora
LABEL maintainer="security@lists.fedoraproject.org"
ENV PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

RUN useradd -c 'enum4linux' -m -s /sbin/nologin enum4linux
RUN dnf upgrade -y && \
    dnf install -y \
        samba-client \
        which \
        perl \
        perl-Data-Dumper \
        git \
        bzip2 \
        openldap-clients \
        samba-common-tools && \
    cd /tmp && \
    curl -o polenum-0.2.tar.bz2 https://labs.portcullis.co.uk/download/polenum-0.2.tar.bz2 && \
    git clone https://github.com/portcullislabs/enum4linux.git && \
    mv enum4linux/enum4linux.pl /usr/bin/enum4linux && \
    rm -rf enum4linux/.git && \
    mv enum4linux /usr/share/enum4linux && \
    tar -xjf polenum-0.2.tar.bz2 && \
    mv polenum-0.2/polenum.py /usr/bin/polenum.py && \
    mv polenum-0.2 /usr/share/polenum && \
    dnf erase -y \
        git \
        bzip2 && \
    dnf clean all 
USER enum4linux
ENTRYPOINT [ "enum4linux" ]
CMD [ "-h" ]