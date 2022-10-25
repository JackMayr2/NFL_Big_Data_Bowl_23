import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

lis1 = api.competitions_list(search='nfl-big-data-bowl-2023')
api.competition_download_files('nfl-big-data-bowl-2023')
kaggle.unzip
# open in finder, then unzip and folders will be in the correct place
# yuhhhh