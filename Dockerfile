FROM gijzelaerr/snap7
ADD . /
RUN cd /paho-mqtt-1.5.1/ && python3 setup.py install
CMD cd / && python3 main.py