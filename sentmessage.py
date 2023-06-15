from telegram.ext import Updater

# Define your notify_user function
def notify_user(bot, df, user_id):
    # Tell the user about df
    bot.send_message(chat_id=user_id, text="Something important happened! Here is the data:\n\n{}".format(df))
    

def main(p_user_id,p_tk,p_df):
    # Set up your updater and dispatcher as before
    updater = Updater(token=p_tk, use_context=True)
    dispatcher = updater.dispatcher

    # Your code to detect the important event and get the relevant data and user ID
    df = p_df
    user_id = p_user_id  # Replace with the desired user's chat ID

   
    # Start the bot
    updater.start_polling()
    updater.idle()

 # Call the notify_user function with the relevant parameters
    notify_user(updater.bot, df, user_id)
