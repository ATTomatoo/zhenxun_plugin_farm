from nonebot import get_driver
from nonebot.plugin import PluginMetadata

from zhenxun.configs.utils import Command, PluginExtraData, RegisterConfig
from zhenxun.services.log import logger
from zhenxun.utils.message import MessageUtils

from .command import diuse_farm, diuse_register, reclamation
from .config import g_pJsonManager
from .database import g_pSqlManager
from .farm.farm import g_pFarmManager
from .farm.shop import g_pShopManager
from .request import g_pRequestManager

__plugin_meta__ = PluginMetadata(
    name="真寻农场",
    description="快乐的农场时光",
    usage="""
    你也要种地?
    指令：
        at 开通农场
        我的农场
        我的农场币
        种子商店 [页数]
        购买种子 [作物/种子名称] [数量]
        我的种子
        播种 [作物/种子名称] [数量]
        收获
        铲除
        我的作物
        出售作物 [作物/种子名称] [数量]
        偷菜 at
        开垦
        购买农场币 [数量] 数量为消耗金币的数量
    """.strip(),
    extra=PluginExtraData(
        author="Art_Sakura",
        version="1.0",
        commands=[Command(command="我的农场")],
        menu_type="群内小游戏",
        configs=[
            RegisterConfig(
                key="兑换倍数",
                value="2",
                help="金币兑换农场币的倍数 默认值为: 2倍",
                default_value="2",
            ),
            RegisterConfig(
                key="手续费",
                value="0.2",
                help="金币兑换农场币的手续费 默认值为: 0.2 实际意义为20%手续费",
                default_value="0.2",
            ),
            RegisterConfig(
                key="服务地址",
                value="http://diuse.work",
                help="签到、交易行、活动等服务器地址",
                default_value="http://diuse.work",
            )
        ]
    ).to_dict(),
)
driver = get_driver()


# 构造函数
@driver.on_startup
async def start():
    # 初始化数据库
    await g_pSqlManager.init()

    # 初始化读取Json
    await g_pJsonManager.init()

# 析构函数
@driver.on_shutdown
async def shutdown():
    await g_pSqlManager.cleanup()
