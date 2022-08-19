import sys
import json
import os
# from vnpy_ctp.gateway import ctp_gateway

sys.path.append('/home/main_server/futures/vnpy')
from vnpy.event import EventEngine
from vnpy.trader.engine import MainEngine
from vnpy.trader.ui import MainWindow, create_qapp

sys.path.append('/home/main_server/futures/vnpy_ctp')
from vnpy_ctp import CtpGateway


def main():
    """主入口函数"""
    # qapp = create_qapp()

    name = 'ctp_gateway'
    event_engine = EventEngine()
    main_engine = MainEngine(event_engine)
    main_engine.add_gateway(CtpGateway, name)

    get = main_engine.get_gateway(name)

    print(os.path.abspath('.'))
    # read json config
    json_file = '/home/main_server/futures/vnpy_ctp/script/account.json'
    fp = open(json_file)
    json_data = json.load(fp)

    main_engine.connect(json_data, "CTP")

    print("ddd")

    # main_window = MainWindow(main_engine, event_engine)
    # main_window.showMaximized()

    # qapp.exec()


if __name__ == "__main__":
    main()
