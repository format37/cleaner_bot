import pandas as pd
import seaborn as sns

def cleaner_bot_alert(user_id,script_path):
	#script_path = '/home/format37_gmail_com/projects/cleaner_bot/'
	#df_full = pd.read_csv(script_path+'data.csv')
	return 'u '+str(user_id)#str(id) in [str(i) for i in df_full.account_id.to_list()]

def cleaner_bot_user_authorized(user_id,script_path):
	#script_path = '/home/format37_gmail_com/projects/cleaner_bot/'
	df_full = pd.read_csv(script_path+'data.csv')		
	return str(user_id) in [str(i) for i in df_full.account_id.to_list()]

def cleaner_bot_stat(script_path):
	#script_path = '/home/format37_gmail_com/projects/cleaner_bot/'
	df_full = pd.read_csv(script_path+'data.csv')
	df = pd.DataFrame()
	df['user']=df_full['user']
	df['Посуда']=df_full['Посуда']
	df['Мусор']=df_full['Мусор']
	df['Туалет']=df_full['Туалет']
	df = df.set_index('user')
	heat_map = sns.heatmap(df, annot=True, cmap="YlGnBu")
	fig = heat_map.get_figure()	
	filepath = script_path+"images/heat_map.png"
	fig.savefig(filepath)
	return filepath