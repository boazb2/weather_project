import pandas as pd
import mysql.connector
from mysql.connector import Error
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters

# Create an empty DataFrame to store user data
df = pd.DataFrame(columns=['Username', 'First Name', 'Last Name', 'Email'])

# Define conversation states
USERNAME, FIRST_NAME, LAST_NAME, EMAIL = range(4)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Please enter your username.")
    return USERNAME

def handle_username(update, context):
    username = update.message.text

    # Save the username in the DataFrame
    df.loc[update.effective_user.id, 'Username'] = username

    # Ask for the user's first name
    context.bot.send_message(chat_id=update.effective_chat.id, text="Please enter your first name.")
    return FIRST_NAME

def handle_first_name(update, context):
    first_name = update.message.text

    # Save the first name in the DataFrame
    df.loc[update.effective_user.id, 'First Name'] = first_name

    # Ask for the user's last name
    context.bot.send_message(chat_id=update.effective_chat.id, text="Please enter your last name.")
    return LAST_NAME

def handle_last_name(update, context):
    last_name = update.message.text

    # Save the last name in the DataFrame
    df.loc[update.effective_user.id, 'Last Name'] = last_name

    # Ask for the user's email name
    context.bot.send_message(chat_id=update.effective_chat.id, text="Please enter you email")
    return EMAIL

def handle_email(update, context):
    email = update.message.text

    # Save the city name in the DataFrame
    df.loc[update.effective_user.id, 'Email'] = email

    # Inform the user that the data has been stored
    context.bot.send_message(chat_id=update.effective_chat.id, text="Thank you! Your data has been stored.")

 
    sql_insert_to_user = f"Insert into users (user_name,first_name,last_name,email) values ('{str(df['Username'].values[0])}','{str(df['First Name'].values[0])}','{str(df['Last Name'].values[0])}','{str(df['Email'].values[0])}')"
    print(sql_insert_to_user)

    conn = mysql.connector.connect(
    host='cnt7-naya-cdh63',
    user='nifi',
    password='NayaPass1!',
    database='weather_db'
)

    cursor = conn.cursor()
    cursor.execute(sql_insert_to_user)
    conn.commit()
    
    return ConversationHandler.END

def cancel(update, context):
    # Cancel the conversation
    context.bot.send_message(chat_id=update.effective_chat.id, text="The conversation has been cancelled.")
    return ConversationHandler.END

def main():
    updater = Updater(token="5993334898:AAHCOt1GTVEW3_0FY-wEWmyMvnt71VceloM", use_context=True)
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            USERNAME: [MessageHandler(Filters.text & (~Filters.command), handle_username)],
            FIRST_NAME: [MessageHandler(Filters.text & (~Filters.command), handle_first_name)],
            LAST_NAME: [MessageHandler(Filters.text & (~Filters.command), handle_last_name)],
            EMAIL: [MessageHandler(Filters.text & (~Filters.command), handle_email)],
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dispatcher.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
