from nonebot.plugin import PluginMetadata

from .config import Config

__version__ = "0.1.0"
__plugin_meta__ = PluginMetadata(
    name="nonebot-plugin-template",
    description="Nonebot2 插件模板",
    usage="使用方法",
    type="application",
    homepage="https://github.com/owner/nonebot-plugin-template",
    config=Config,
    supported_adapters=None,
    extra={"author": "owner"},
)
