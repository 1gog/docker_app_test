FROM centos:7
RUN yum install -y epel-release && yum install -y bzip2 python3-pip.noarch && pip3 install flask
RUN mkdir -p /opt/app
WORKDIR /opt/app
COPY main.py /opt/app
COPY requirements.txt /opt/app/
RUN pip3 install -r /opt/app/requirements.txt
EXPOSE 5000
CMD ["python3", "/opt/app/main.py"]
