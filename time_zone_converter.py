import streamlit as st
from datetime import datetime
import pytz

# Title of the app
st.title("🌍 UK to Pakistan Time Converter")

# Input for current time in UK
current_time_uk = datetime.now(pytz.timezone('Europe/London'))
st.write(f"Current time in UK (London): {current_time_uk.strftime('%Y-%m-%d %H:%M:%S')}")

# Convert current UK time to Pakistan time
current_time_pk = current_time_uk.astimezone(pytz.timezone('Asia/Karachi'))
st.write(f"Current time in Pakistan (Karachi): {current_time_pk.strftime('%Y-%m-%d %H:%M:%S')}")

# Optional input to manually input the UK time
st.subheader("Convert a Specific UK Time to Pakistan Time")
input_time = st.time_input("Select a time (in UK time zone):", current_time_uk.time())
input_date = st.date_input("Select a date (in UK time zone):", current_time_uk.date())

# Combine the selected date and time
input_datetime_uk = datetime.combine(input_date, input_time)
input_datetime_uk = pytz.timezone('Europe/London').localize(input_datetime_uk)

# Convert the manually entered time to Pakistan time
converted_time_pk = input_datetime_uk.astimezone(pytz.timezone('Asia/Karachi'))
st.write(f"Converted time in Pakistan (Karachi): {converted_time_pk.strftime('%Y-%m-%d %H:%M:%S')}")
