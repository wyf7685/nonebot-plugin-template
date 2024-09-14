<div align="center">
  <a href="https://v2.nonebot.dev/store">
    <img src="https://raw.githubusercontent.com/wyf7685/wyf7685/main/assets/NoneBotPlugin.svg" width="300" alt="logo">
  </a>
</div>

<div align="center">

# nonebot-plugin-template

_✨ NoneBot 插件简单描述 ✨_

[![license](https://img.shields.io/github/license/owner/nonebot-plugin-template.svg)](./LICENSE)
[![pypi](https://img.shields.io/pypi/v/nonebot-plugin-template?logo=python&logoColor=edb641)](https://pypi.python.org/pypi/nonebot-plugin-template)
[![python](https://img.shields.io/badge/python-3.10+-blue?logo=python&logoColor=edb641)](https://www.python.org/)

[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![isort](https://img.shields.io/badge/%20imports-isort-%231674b1)](https://pycqa.github.io/isort/)
[![black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pyright](https://img.shields.io/badge/types-pyright-797952.svg?logo=python&logoColor=edb641)](https://github.com/Microsoft/pyright)

[![pre-commit](https://results.pre-commit.ci/badge/github/owner/nonebot-plugin-template/master.svg)](https://results.pre-commit.ci/latest/github/owner/nonebot-plugin-template/master)
[![pyright](https://github.com/owner/nonebot-plugin-template/actions/workflows/pyright.yml/badge.svg?branch=master&event=push)](https://github.com/owner/nonebot-plugin-template/actions/workflows/pyright.yml)
[![publish](https://github.com/owner/nonebot-plugin-template/actions/workflows/pypi-publish.yml/badge.svg)](https://github.com/owner/nonebot-plugin-template/actions/workflows/pypi-publish.yml)

</div>

这是一个 nonebot2 插件项目的模板库, 你可以直接使用本模板创建你的 nonebot2 插件项目的仓库

模板使用 [`uv`](https://github.com/astral-sh/uv) 进行依赖管理，使用 [`pyright`](https://github.com/microsoft/pyright) 进行代码检查

### 模板使用

- 点击仓库中的 "Use this template" 按钮, 输入仓库名与描述, 点击 " Create repository from template" 创建仓库
- 全局替换 `owner` 为你的 Github 用户名
- 全局替换 `nonebot-plugin-template` 为你的插件包名
- 重命名 `nonebot_plugin_template` 文件夹为你的插件导入名
- 全局替换 `nonebot_plugin_template` 为你的插件导入名
- 在 `pyproject.toml` 中修改 `[project]` 部分的信息
- 前往 [这里](https://github.com/settings/installations/53369898) 配置 pre-commit cli
- 执行 `uv lock` 和 `uv sync` 锁定依赖版本并创建虚拟环境

<details>
<summary>触发发布工作流</summary>

插件模板使用 [Trusted Publisher](https://docs.pypi.org/trusted-publishers/) 发布模块到 PyPI，使用工作流前需要根据 [文档](https://docs.pypi.org/trusted-publishers/creating-a-project-through-oidc/) 在 PyPI 上进行相关配置

从本地推送任意 tag 即可触发。

tag 格式: `v{x}.{y}.{z}`

创建 tag:

    git tag <tag_name>

推送本地所有 tag:

    git push origin --tags

</details><br/>

<details>
<summary>配置本地调试</summary>

插件模板提供了基于 `VS Code` 的调试配置，使用 `OneBot V11` 适配器 + [`Matcha`](https://github.com/A-kirami/matcha) 进行本地调试

- 创建 `.env` 文件，根据 [文档](https://nonebot.dev/docs/appendices/config) 填写 Nonebot 配置项
- 安装并配置 [`Matcha`](https://github.com/A-kirami/matcha)
- 在 `VS Code` 中按下 `F5` 开始调试

<details>
<summary>.env 配置参考</summary>

```env
DRIVER=~fastapi
LOG_LEVEL=DEBUG
SUPERUSERS=[]
COMMAND_START=["/"]
COMMAND_SEP=["."]

# adapter-onebot-v11
HOST=0.0.0.0
PORT=8080

# nonebot-plugin-template
# 添加你的配置项...
```

</details>

</details>

## 📖 介绍

这里是插件的详细介绍部分

## 💿 安装

<details open>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-template

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

```sh
pip install nonebot-plugin-template
```

</details>
<details>
<summary>pdm</summary>

```sh
pdm add nonebot-plugin-template
```

</details>
<details>
<summary>poetry</summary>

```sh
poetry add nonebot-plugin-template
```

</details>
<details>
<summary>conda</summary>

```sh
conda install nonebot-plugin-template
```

</details>
<details>
<summary>uv</summary>

```sh
uv add nonebot-plugin-template
```

</details>

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot_plugin_template"]

</details>

## ⚙️ 配置

在 nonebot2 项目的`.env`文件中添加下表中的必填配置

|  配置项  | 必填 | 默认值 |   说明   |
| :------: | :--: | :----: | :------: |
| 配置项 1 |  是  |   无   | 配置说明 |
| 配置项 2 |  否  |   无   | 配置说明 |

## 🎉 使用

### 指令表

|  指令  | 权限 | 需要@ | 范围 |   说明   |
| :----: | :--: | :---: | :--: | :------: |
| 指令 1 | 主人 |  否   | 私聊 | 指令说明 |
| 指令 2 | 群员 |  是   | 群聊 | 指令说明 |

## 💡 鸣谢

- (可能的鸣谢清单)

## 📝 更新日志

<details>
<summary>更新日志</summary>

- 2024.09.14 v0.1.0

  - 插件模板
  - 更新日志

</details>
