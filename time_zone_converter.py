import streamlit as st
from datetime import datetime
import pytz

# Title of the app
st.title("🌍 UK to Pakistan Time Converter")

# Input for current UK time
st.subheader("Enter a Specific UK Time")

# Allow user to input UK time
input_time = st.time_input("Select a time (in UK time zone):")
input_date = st.date_input("Select a date (in UK time zone):")

# Combine the selected date and time into a datetime object
if input_time and input_date:
    input_datetime_uk = datetime.combine(input_date, input_time)
    input_datetime_uk = pytz.timezone('Europe/London').localize(input_datetime_uk)

    # Button to convert time
    if st.button("Convert to Pakistan Time"):
        # Convert the UK time to Pakistan time
        converted_time_pk = input_datetime_uk.astimezone(pytz.timezone('Asia/Karachi'))
        st.write(f"Converted time in Pakistan (Karachi): {converted_time_pk.strftime('%Y-%m-%d %H:%M:%S')}")
