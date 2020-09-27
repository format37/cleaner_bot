import pandas as pd
import seaborn as sns
import os

def cleaner_bot_counter_plus(account_id,script_path,task):
	df_full = pd.read_csv(script_path+'data.csv')
	current_value = int(df_full[df_full.account_id==account_id][task])
	df_full.loc[(df_full.account_id==account_id),task]=current_value+1
	df_full.to_csv(script_path+'data.csv',index = None)
	return task+' +1'

def cleaner_bot_alert(script_path,task):	
	df_full				= pd.read_csv(script_path+'data.csv')
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
	heat_map		= sns.heatmap(df, annot=True, cmap="YlGnBu", cbar = False)
	# clear ++
	fig				= heat_map.get_figure()	
	fig.clf()
	# clear --
	fig 			= heat_map.get_figure()	
	image_path = script_path+'images/heat_map.png'	
	#if os.path.exists(image_path):
	#	os.remove(image_path)
	fig.savefig(image_path)
	return image_path

def cleaner_bot_user_authorized(account_id,script_path):
	df_full = pd.read_csv(script_path+'data.csv')		
	return str(account_id) in [str(i) for i in df_full.account_id.to_list()]