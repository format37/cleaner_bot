import pandas as pd
import seaborn as sns

def cleaner_bot_alert(user_id,task):	
	df_full				= pd.read_csv('data.csv')
	df					= pd.DataFrame()
	df['user']			= df_full['user']
	df['account_name']	= df_full['account_name']
	df['account_id']	= df_full['account_id']
	df[task]			= df_full[task]
	min_count			= df[task].min()
	actual_users		= df[df[task]==min_count]
	message_string 		= ''
	for a_name in actual_users.account_name:
		message_string += a_name + ' '
	message_string 		+= task
	return message_string

def cleaner_bot_stat(script_path):
	df_full			= pd.read_csv(script_path+'data.csv')
	df				= pd.DataFrame()
	df['user']		= df_full['user']
	df['посуда']	= df_full['посуда']
	df['мусор']		= df_full['мусор']
	df['туалет']	= df_full['туалет']
	df 				= df.set_index('user')
	heat_map		= sns.heatmap(df, annot=True, cmap="YlGnBu")
	fig				= heat_map.get_figure()	
	filepath		= script_path+"images/heat_map.png"
	fig.savefig(filepath)
	return filepath

def cleaner_bot_user_authorized(user_id,script_path):
	df_full = pd.read_csv(script_path+'data.csv')		
	return str(user_id) in [str(i) for i in df_full.account_id.to_list()]