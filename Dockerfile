FROM jenkins/jenkins

USER root
RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y  make build-essential libssl-dev zlib1g-dev
RUN apt-get install -y libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm
RUN apt-get install -y libncurses5-dev  libncursesw5-dev xz-utils tk-dev
RUN curl -O https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tar.xz
RUN tar -xf Python-3.7.3.tar.xz
RUN cd Python-3.7.3 && ls && ./configure --enable-optimizations && make && make altinstall
RUN python3.7 --version
RUN apt install -y python3-pip
RUN pip3 --version
RUN PATH=$PATH:/Python-3.7.3/
RUN apt install -y libcurl4-openssl-dev libssl-dev python3-dev
RUN pip3 install pfurl