import json
from pathlib import Path

from zhenxun.configs.path_config import DATA_PATH
from zhenxun.services.log import logger

g_sDBPath = DATA_PATH / "farm_db"
g_sDBFilePath = DATA_PATH / "farm_db/farm.db"

g_sResourcePath = Path(__file__).resolve().parent / "resource"

class CJsonManager:
    def __init__(self):
        self.m_pItem = {}
        self.m_pPlant = {}
        self.m_pLevel = {}
        self.m_pSoil = {}

    async def init(self) -> bool:
        if not await self.initItem():
            return False

        if not await self.initPlant():
            return False

        if not await self.initLevel():
            return False

        if not await self.initSoil():
            return False

        return True

    async def initItem(self) -> bool:
        current_file_path = Path(__file__)

        try:
            with open(
                current_file_path.resolve().parent / "config/item.json",
                encoding="utf-8",
            ) as file:
                self.m_pItem = json.load(file)

                return True
        except FileNotFoundError:
            logger.warning("item.json 打开失败")
            return False
        except json.JSONDecodeError as e:
            logger.warning(f"item.json JSON格式错误: {e}")
            return False

    async def initPlant(self) -> bool:
        current_file_path = Path(__file__)

        try:
            with open(
                current_file_path.resolve().parent / "config/plant.json",
                encoding="utf-8",
            ) as file:
                self.m_pPlant = json.load(file)

                return True
        except FileNotFoundError:
            logger.warning("plant.json 打开失败")
            return False
        except json.JSONDecodeError as e:
            logger.warning(f"plant.json JSON格式错误: {e}")
            return False

    async def initLevel(self) -> bool:
        current_file_path = Path(__file__)

        try:
            with open(
                current_file_path.resolve().parent / "config/level.json",
                encoding="utf-8",
            ) as file:
                self.m_pLevel = json.load(file)

                return True
        except FileNotFoundError:
            logger.warning("level.json 打开失败")
            return False
        except json.JSONDecodeError as e:
            logger.warning(f"level.json JSON格式错误: {e}")
            return False

    async def initSoil(self) -> bool:
        current_file_path = Path(__file__)

        try:
            with open(
                current_file_path.resolve().parent / "config/soil.json",
                encoding="utf-8",
            ) as file:
                self.m_pSoil = json.load(file)

                return True
        except FileNotFoundError:
            logger.warning("soil.json 打开失败")
            return False
        except json.JSONDecodeError as e:
            logger.warning(f"soil.json JSON格式错误: {e}")
            return False

g_pJsonManager = CJsonManager()
