import streamlit as st
from datetime import datetime
import pytz

# Title of the app
st.title("🌍 Time Zone Converter")

# Instructions for users
st.subheader("Instructions")
st.write("1. Select the date and time you want to convert.")
st.write("2. Choose the source country (where the time is currently).")
st.write("3. Select the target country (where you want to know the time).")
st.write("4. Click the 'Convert' button to see the converted time.")

# Allow user to input time and date
input_time = st.time_input("Select a time:")
input_date = st.date_input("Select a date:")

# Comprehensive list of time zones for various countries
timezones_dict = {
    "Afghanistan": "Asia/Kabul",
    "Albania": "Europe/Tirane",
    "Algeria": "Africa/Algiers",
    # ... [rest of the countries]
    "United Kingdom": "Europe/London",
    "United States (Eastern)": "America/New_York",
    # Add more countries as needed
}

# Dropdown for selecting source time zone
selected_source_country = st.selectbox("Select source country:", list(timezones_dict.keys()))
selected_source_timezone = timezones_dict[selected_source_country]

# Display current time in the source time zone
current_time_source = datetime.now(pytz.timezone(selected_source_timezone))
st.write(f"Current time in {selected_source_country}: {current_time_source.strftime('%Y-%m-%d %H:%M:%S')}")

# Dropdown for selecting target time zone
selected_target_country = st.selectbox("Select target country:", list(timezones_dict.keys()))
selected_target_timezone = timezones_dict[selected_target_country]

# Display current time in the target time zone
current_time_target = datetime.now(pytz.timezone(selected_target_timezone))
st.write(f"Current time in {selected_target_country}: {current_time_target.strftime('%Y-%m-%d %H:%M:%S')}")

# Combine the selected date and time into a datetime object
if input_time and input_date:
    input_datetime = datetime.combine(input_date, input_time)
    source_timezone = pytz.timezone(selected_source_timezone)
    input_datetime_source = source_timezone.localize(input_datetime)

    # Button to convert time
    if st.button("Convert"):
        # Convert the input time to the selected target time zone
        converted_time = input_datetime_source.astimezone(pytz.timezone(selected_target_timezone))
        st.write(f"Converted time in {selected_target_country}: {converted_time.strftime('%Y-%m-%d %H:%M:%S')}")
else:
    st.warning("Please select both date and time to convert.")
