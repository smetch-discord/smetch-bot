from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase, AsyncIOMotorCollection
from datetime import datetime


class InfractionClient:
    '''
    Class which enables interaction with the MongoDB database for infractions it has pre-defined methods:
    1. `insert_infraction`
    2. `insert_mute`
    3. `expire_mute`
    '''

    def __init__(self, uri: str) -> None:
        self.client: AsyncIOMotorClient = AsyncIOMotorClient(uri)
        self.database: AsyncIOMotorDatabase = self.client.SMETCH
        self.collection: AsyncIOMotorCollection = self.database.infractions

    async def get_next_id(self) -> int:
        number_of_documents: int = await self.collection.count({})
        return number_of_documents

    async def insert_infraction(self, type_: str, moderator_id: int, banned_id: int, reason: str) -> None:
        next_id: int = await self.get_next_id()
        await self.collection.insert_one(
            {
                '_id': next_id,
                'mod': moderator_id,
                'type': type_,
                'date': datetime.now(),
                'reason': reason,
                'user': banned_id
            }
        )
        return
