import discord

''' FOR REFERENCE
embed=discord.Embed(title=title)
embed.set_thumbnail(url=iconurl)
embed.add_field(name=boldTitle, value=messageContent, inline=False)
embed.set_footer(text=footerMessage)
await ctx.send(embed=embed)
'''

class EmbedCreator:
    footerMessage = 'Powered by UoA Esports.'

    def __init__(self, title='None', boldTitle='None', values='', footer=footerMessage):
        self.embed=discord.Embed(title=title, color=0x0dd5d9)
        self.embed.add_field(name=boldTitle, value=values, inline=False)
        self.embed.set_footer(text=footer)
    
    def set_thumbnail(self, thumbnail_url):
        self.embed.set_thumbnail(url=thumbnail_url)
    
    def get_embed(self):
        return self.embed
        
