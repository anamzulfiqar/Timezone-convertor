import streamlit as st
from datetime import datetime
import pytz

# Title of the app
st.title("🌍 Time Zone Converter")

# User input for the time to convert
st.subheader("Enter a Specific Time to Convert")

# Allow user to input time and date
input_time = st.time_input("Select a time:")
input_date = st.date_input("Select a date:")

# Dropdown for selecting source time zone
source_timezones = pytz.all_timezones
selected_source_timezone = st.selectbox("Select source time zone:", source_timezones)

# Dropdown for selecting target time zone
target_timezones = pytz.all_timezones
selected_target_timezone = st.selectbox("Select target time zone:", target_timezones)

# Combine the selected date and time into a datetime object
if input_time and input_date:
    input_datetime = datetime.combine(input_date, input_time)
    source_timezone = pytz.timezone(selected_source_timezone)
    input_datetime_source = source_timezone.localize(input_datetime)

    # Button to convert time
    if st.button("Convert"):
        # Convert the input time to the selected target time zone
        converted_time = input_datetime_source.astimezone(pytz.timezone(selected_target_timezone))
        st.write(f"Converted time in {selected_target_timezone}: {converted_time.strftime('%Y-%m-%d %H:%M:%S')}")
