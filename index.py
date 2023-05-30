import discord
from discord.ext import commands

# Configuração do bot
TOKEN = 'seu_token_de_autenticação_do_discord'
PREFIXO = '!'

# Criação do bot
bot = commands.Bot(command_prefix=PREFIXO)

# Evento de inicialização do bot
@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user.name}')
    print('------')

# Comando para obter informações de um membro
@bot.command()
async def info(ctx, member: discord.Member):
    # Obtém informações do membro
    nome = member.name
    apelido = member.nick
    id = member.id
    status = member.status
    jogo = member.activity.name if member.activity else 'Nenhum'
    cargo_principal = member.top_role.name
    data_criacao = member.created_at
    data_entrada = member.joined_at

    # Formatação da resposta
    resposta = f'**Informações de {nome}:**\n'
    resposta += f'Apelido: {apelido}\n' if apelido else ''
    resposta += f'ID: {id}\n'
    resposta += f'Status: {status}\n'
    resposta += f'Jogo: {jogo}\n'
    resposta += f'Cargo Principal: {cargo_principal}\n'
    resposta += f'Data de Criação: {data_criacao}\n'
    resposta += f'Data de Entrada: {data_entrada}\n'

    # Envia a resposta no canal onde o comando foi executado
    await ctx.send(resposta)

# Execução do bot
bot.run(TOKEN)
