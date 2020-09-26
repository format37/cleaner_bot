import pandas as pd
	
def cleaner_bot_unauthorized():
	return 'unauthorized'

def cleaner_bot_stats():
	df = pd.read_csv('data.csv')
	df = df.drop(['accounts'],axis = 1)
	df = df.set_index('Пользователи')
	heat_map = sns.heatmap(df, annot=True, cmap="YlGnBu")
	fig = heat_map.get_figure()
	filepath = "/home/format37_gmail_com/projects/cleaner_bot/images/heat_map.png"
	fig.savefig(filepath)
	return filepath