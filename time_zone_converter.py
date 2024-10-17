
import streamlit as st
from datetime import datetime
import pytz

# Title of the app
st.title("🌍 Time Zone Converter")

# Input for current time (automatically uses UK time as default)
current_time_uk = datetime.now(pytz.timezone('Europe/London'))
st.write(f"Current time in UK (London): {current_time_uk.strftime('%Y-%m-%d %H:%M:%S')}")

# Get user input for time zone selection
timezones = pytz.all_timezones
selected_timezone = st.selectbox("Select target time zone:", timezones)

# Display current time in the selected time zone
if selected_timezone:
    target_time = datetime.now(pytz.timezone(selected_timezone))
    st.write(f"Current time in {selected_timezone}: {target_time.strftime('%Y-%m-%d %H:%M:%S')}")

# Optional input to manually input the time to convert
st.subheader("Convert a Specific Time")
input_time = st.time_input("Select a time (in UK time zone):", current_time_uk.time())
input_date = st.date_input("Select a date (in UK time zone):", current_time_uk.date())

# Combine the selected date and time
input_datetime = datetime.combine(input_date, input_time)
input_datetime_uk = pytz.timezone('Europe/London').localize(input_datetime)

# Convert the manually entered time to the selected time zone
if selected_timezone:
    converted_time = input_datetime_uk.astimezone(pytz.timezone(selected_timezone))
    st.write(f"Converted time in {selected_timezone}: {converted_time.strftime('%Y-%m-%d %H:%M:%S')}")
