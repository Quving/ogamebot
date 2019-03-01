FROM python:3.6

MAINTAINER vinh-ngu@hotmail.com
ENV DOCKER_VERSION 18.06.1~ce~3-0~debian

# Install docker
RUN apt update && \
	apt install -y  \
	    apt-transport-https \
	    ca-certificates \
	    curl \
	    gnupg2 \
	    software-properties-common \
            nginx

RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -
RUN add-apt-repository \
	   "deb [arch=amd64] https://download.docker.com/linux/debian \
	   $(lsb_release -cs) \
	   stable"
RUN apt-get update && \
	apt-get install -y docker-ce=${DOCKER_VERSION}

WORKDIR /app
ADD . .
RUN pip install -r requirements.txt

# Forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

RUN chmod u+x entrypoint.sh
CMD ["bash","entrypoint.sh"]
