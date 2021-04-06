from typing import Any
from motor.motor_asyncio import AsyncIOMotorClient
from discord import Member
from datetime import datetime


class Database:

    def __init__(self, uri: str) -> None:
        self.client = AsyncIOMotorClient(uri)
        self.database = self.client.SMETCH
        self.infractions_collection = self.database.punishments
        return

    async def add_infraction(self, type_: str, moderator: Member, user: Member, reason: str) -> None:
        current_time: datetime = datetime.utcnow()
        id: int = await self.get_next_infraction_id()
        infraction = {
            '_id': id,
            'type': type_,
            'moderator': moderator.id,
            'user': user.id,
            'reason': reason,
            'date': current_time
        }
        await self.infractions_collection.insert_one(infraction)
        return

    async def get_infractions(self, **filter: dict[str, Any]) -> list:
        infractions: list = []
        for infraction in self.infractions_collection.find(filter):
            infractions.append(infraction)
        return infraction

    async def get_next_infraction_id(self) -> int:
        '''
        Returns what the ID of the next infraction should be.
        It does this by counting how many documents are in the collection.
        '''
        next_id: int = await self.infractions_collection.count_documents({})
        return next_id
