import nonebot
from nonebot.adapters.onebot.v11 import Adapter as OB11Adapter

nonebot.init()
driver = nonebot.get_driver()
driver.register_adapter(OB11Adapter)
nonebot.load_plugin("nonebot_plugin_template")

if __name__ == "__main__":
    nonebot.run()
