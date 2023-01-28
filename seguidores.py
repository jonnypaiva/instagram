import instaloader

import pandas as pd

bot = instaloader.Instaloader()
bot.login(user="html_e_css", passwd="knn1056c")
#insira os dados da conta para realizar a pesquisa
conta = instaloader.Profile.from_username(bot.context, "php.arretado")
'''
seguidores = []
for seguidor in conta.get_followers():
   seguidores.append([seguidor.username, seguidor.followers, seguidor.followees
                      seguidor.mediacount]) 
'''

seguidores = [seguidor.username for seguidor in conta.get_followers()]

seguidores_df = pd.DataFrame(seguidores)

seguidores_df.to_csv('seguidores.csv', sep=";")

seguindos = [seguindo.username for seguindo in conta.get_followees()]

seguindos_df = pd.DataFrame(seguindos)

seguindos_df.to_csv('seguindos.csv', sep=";")