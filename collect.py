#!/usr/bin/python
# -*- coding: UTF-8 -*-
import logging
import devinfo
import idesk

logging.basicConfig(level=logging.ERROR)


def dev_install():
    # 获取设备配置信息
    _desk_id = devinfo.get_desk_number()
    _plc_ip = devinfo.get_plc_ip(_desk_id)

    _client = idesk.iDesk(_plc_ip,
                          0,
                          1,
                          devinfo.get_time_config()['reconnect'],
                          devinfo.get_time_config()['telemetry'],
                          _desk_id)
    logging.info("dev : %s installed !" + str(_desk_id))
    _client.start()
