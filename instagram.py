import instaloader
import re

bot = instaloader.Instaloader()

conta = instaloader.Profile.from_username(bot.context, 'jonnypaiva')

print("Nome de usuario:", conta.username)
print("ID: ", conta.userid)
print("NUmero de posts:", conta.mediacount)
num_seg = conta.followers
seguindo = conta.followees
print("Numero de Seguidores:", num_seg)
print("Contas que sigo:", seguindo)
print("Bio: ", conta.biography)
print("URL: ", conta.external_url)
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", conta.biography)
print(emails)

top_five = instaloader.TopSearchResults(bot.context,'uniateneu')

print(top_five.get_profiles())

i = 0
for contas in top_five.get_profiles():
    i += 1
    print(i, ":", contas)

i = 0
for hashtag in top_five.get_hashtags():
    i += 1
    print(i, ":", hashtag)

print(top_five.get_locations())


if num_seg > 10000:
    print("Habilitado")