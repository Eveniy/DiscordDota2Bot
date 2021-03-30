import requests

account_id = '2347811093'  # 859432337  #234781093

class GetAccountInfo (object):
    def __init__(self, account_id):
        self.accID = str(account_id)

    def get_profile(self):
        return requests.get(f'https://api.opendota.com/api/players/{self.accID}').json()

    def get_matches(self):
        return [i for i in requests.get(f'https://api.opendota.com/api/players/{self.accID}/matches').json() if i['game_mode'] == 22]

    def get_winrate(self):
        if self.get_profile()['tracked_until'] != None:
            res = requests.get(f'https://api.opendota.com/api/players/{self.accID}/wl').json()
            print(res)
            win = res['win']
            allmatch = res['win'] + res['lose']
            return f'Винрейт равен {round(win/allmatch, 2) * 100}%'
        else:
            return f'Аккаунт с номером {self.accID} не найден!'

    # def check_profile

print(GetAccountInfo(account_id).get_profile())