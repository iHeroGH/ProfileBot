from typing import List
from uuid import UUID
from collections import defaultdict

from discord import Embed

from cogs.utils.profiles.field import Field


class Profile(object):

    all_profiles = {}
    all_guilds = defaultdict(dict)

    def __init__(self, profile_id:UUID, colour:int, guild_id:int, verification_channel_id:int, name:str):
        self.profile_id = profile_id 
        self.colour = colour
        self.guild_id = guild_id
        self.verification_channel_id = verification_channel_id
        self.name = name

        self.all_profiles[self.profile_id] = self
        self.all_guilds[self.guild_id][self.name] = self

    @property
    def fields(self) -> List[Field]:
        '''Returns a list of cogs.utils.profiles.fields.Field objects for this particular profile'''

        return sorted(Field.all_profile_fields.get(self.profile_id), key=lambda x: x.index)