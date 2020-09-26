import pandas as pd
import seaborn as sns
	
def cleaner_bot_unauthorized():
	return 'unauthorized'

def cleaner_bot_stats():
	df_full = pd.read_csv('data.csv')
	df = pd.DataFrame()
	df['user']=df_full['user']
	df['Посуда']=df_full['Посуда']
	df['Мусор']=df_full['Мусор']
	df['Туалет']=df_full['Туалет']
	df = df.set_index('user')
	heat_map = sns.heatmap(df, annot=True, cmap="YlGnBu")
	fig = heat_map.get_figure()	
	filepath = "/home/format37_gmail_com/projects/cleaner_bot/images/heat_map.png"
	fig.savefig(filepath)
	return filepath