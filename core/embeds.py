import datetime, random
from discord import Embed, Color

class Embeds:
    def __init__(self, message):
        self.message = message

    def success(self, **kwargs):
        embed = Embed(
            description=self.message,
            color=Color.green()
        )
        for i in kwargs:
            embed.add_field(name=i.replace("_", " "), value=kwargs[i])
        return embed

    def error(self, **kwargs):
        embed = Embed(
            description=self.message,
            color=Color.red()
        )
        for i in kwargs:
            embed.add_field(name=i.replace("_", " "), value=kwargs[i])
        return embed

    def warn(self, **kwargs):
        embed = Embed(
            description=self.message,
            color=Color.orange()
        )
        for i in kwargs:
            embed.add_field(name=i.replace("_", " "), value=kwargs[i])
        return embed

class DMMessage:
    def __init__(self, message):
        self.message = message
    
    def papyrusMessage(self):
        files = None
        if len(self.message.attachments):
            files = '\n'.join([i.url for i in self.message.attachments])
        
        return (self.message.content if self.message.content else "") + (f"\n{files}" if files else "")
    
    def userEmbed(self):
        embed = Embed(
            description=self.message.content,
            color=Color.red(),
            timestamp=datetime.datetime.utcnow()
        )

        embed.set_author(name=str(self.message.author), icon_url=self.message.author.avatar_url_as(static_format="png"))

        if self.message.attachments:
            embed.set_image(url=self.message.attachments[0].url)
            embed.add_field(name="Attachments", value=', '.join([f'[{file.filename}]({file.url})' for file in self.message.attachments]))

        return embed