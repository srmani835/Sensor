import pandas as pd

df=pd.read_csv('/content/mobile_events_2020.csv',sep=';')

df.sample(5)

"""Question_1:

What is the percentage of sessions with an inevention to buy a scooter?

"""

df.info()

df['event_name'].unique()

vechileselected_auto=df[df['event_name']=='Scooter Selected - Auto'].count()
vechileselected_user=df[df['event_name']=='Scooter Selected - User'].count()

vechileselected=vechileselected_auto+vechileselected_user

vechileselected_auto

vechileselected_auto.to_excel('vechileselected_auto.xlsx')

vechileselected_user

total_vechile_selected=vechileselected/df.count()

total_vechile_selected_value=total_vechile_selected['anonymous_id']

print(f"The percentage of  sessions with an inevention to buy a scooter is {total_vechile_selected_value*100}")

"""Question_2:

The percentage of sessions with a sucessfull booking
"""

#df_vechile_pay_user=df[ | (df.event_name=='Qr Scanner - Scanned Succeeded')]
#df_vechile_pay_auto=df[(df.event_name=='Vehicle Selected - Auto') | (df.event_name=='Qr Scanner - Scanned Succeeded')]
df_scan=df[df['event_name']=='Qr Scanner - Scanned Succeeded']
df_select_user_scan=df[df['event_name']=='Scooter Selected - User']
df_select_auto_scan=df[df['event_name']=='Scooter Selected - Auto']

df_select_user_scan.merge(df_select_auto_scan, on='anonymous_id', how='inner').count()

df_select_user_scan.count()

df_inner_user = pd.merge(df_scan, df_select_user_scan, on='context_device_id', how='inner')

df_scan  #4927

df_inner_user.count()

df_inner_auto = pd.merge(df_scan, df_select_auto_scan, on='context_device_id', how='inner')

df_inner_auto.count()

total_payment=df_inner_user.count()+df_inner_auto.count()
total_payment_made=total_payment

total_payment_made

percentage_of_sucessfull_booking=(total_payment_made)/(vechileselected)

print(f"percentage of sucessfull booking {percentage_of_sucessfull_booking*100}")

"""Question_3:

What determines you to book?
"""

vechileselected_user_context=df[df['event_name']=='Scooter Selected - User']['context_device_id']
vechileselected_user_context

df.head()

"""The features values like when List Of Payment Shown and  Paypal Dialogue - Okay Pressed and Qr Scanner - Scanned Succeeded"""



"""Question_4:

What determines sucessfull booking:

When the user procedd to List of Payment page and sucessfully payment processing.
"""