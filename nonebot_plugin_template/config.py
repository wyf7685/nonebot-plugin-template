from nonebot import get_plugin_config
from pydantic import BaseModel


class PluginConfig(BaseModel): ...


class Config(BaseModel):
    template: PluginConfig = PluginConfig()


plugin_config = get_plugin_config(Config).template
