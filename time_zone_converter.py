import streamlit as st
from datetime import datetime
import pytz

# Add background image (ensure the URL is accessible)
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://example.com/path-to-your-background-image.jpg');  /* Replace with a valid URL */
        background-size: cover;
        background-position: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title of the app
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🌍 Time Zone Converter</h1>", unsafe_allow_html=True)

# Instructions for users
st.markdown("<h3 style='color: #555;'>Instructions</h3>", unsafe_allow_html=True)
st.write("1. Select the date and time you want to convert. 🗓️")
st.write("2. Choose the source country (where the time is currently). 🌍")
st.write("3. Select the target country (where you want to know the time). 🕒")
st.write("4. Click the 'Convert' button to see the converted time. 🔄")

# Allow user to input time and date
input_time = st.slider("Select a time:", value=datetime.now().time(), format="HH:mm")
input_date = st.date_input("Select a date:")

# Comprehensive list of time zones for various countries
timezones_dict = {
    "Afghanistan": "Asia/Kabul",
    "Albania": "Europe/Tirane",
    "Algeria": "Africa/Algiers",
    "Andorra": "Europe/Andorra",
    "Angola": "Africa/Luanda",
    "Antigua and Barbuda": "America/Antigua",
    "Argentina": "America/Argentina/Buenos_Aires",
    "Armenia": "Asia/Yerevan",
    "Australia (Adelaide)": "Australia/Adelaide",
    "Australia (Brisbane)": "Australia/Brisbane",
    "Australia (Melbourne)": "Australia/Melbourne",
    "Australia (Perth)": "Australia/Perth",
    "Australia (Sydney)": "Australia/Sydney",
    "Austria": "Europe/Vienna",
    "Azerbaijan": "Asia/Baku",
    "Bahamas": "America/Nassau",
    "Bahrain": "Asia/Bahrain",
    "Bangladesh": "Asia/Dhaka",
    "Barbados": "America/Barbados",
    "Belarus": "Europe/Minsk",
    "Belgium": "Europe/Brussels",
    "Belize": "America/Belize",
    "Benin": "Africa/Porto-Novo",
    "Bhutan": "Asia/Thimphu",
    "Bolivia": "America/La_Paz",
    "Bosnia and Herzegovina": "Europe/Sarajevo",
    "Botswana": "Africa/Gaborone",
    "Brazil (Brasília)": "America/Brasilia",
    "Brazil (São Paulo)": "America/Sao_Paulo",
    "Brunei": "Asia/Brunei",
    "Bulgaria": "Europe/Sofia",
    "Burkina Faso": "Africa/Ouagadougou",
    "Burundi": "Africa/Bujumbura",
    "Cabo Verde": "Atlantic/Cape_Verde",
    "Cambodia": "Asia/Phnom_Penh",
    "Cameroon": "Africa/Douala",
    "Canada (Atlantic)": "America/Halifax",
    "Canada (Central)": "America/Winnipeg",
    "Canada (Eastern)": "America/Toronto",
    "Canada (Mountain)": "America/Edmonton",
    "Canada (Pacific)": "America/Vancouver",
    "Chile": "America/Santiago",
    "China": "Asia/Shanghai",
    "Colombia": "America/Bogota",
    "Comoros": "Indian/Comoro",
    "Congo (Congo-Brazzaville)": "Africa/Brazzaville",
    "Congo (Democratic Republic of the)": "Africa/Kinshasa",
    "Costa Rica": "America/Costa_Rica",
    "Croatia": "Europe/Zagreb",
    "Cuba": "America/Havana",
    "Cyprus": "Asia/Nicosia",
    "Czech Republic": "Europe/Prague",
    "Denmark": "Europe/Copenhagen",
    "Djibouti": "Africa/Djibouti",
    "Dominica": "America/Dominica",
    "Dominican Republic": "America/Santo_Domingo",
    "Ecuador": "America/Guayaquil",
    "Egypt": "Africa/Cairo",
    "El Salvador": "America/El_Salvador",
    "Equatorial Guinea": "Africa/Malabo",
    "Eritrea": "Africa/Asmera",
    "Estonia": "Europe/Tallinn",
    "Eswatini": "Africa/Mbabane",
    "Ethiopia": "Africa/Addis_Ababa",
    "Fiji": "Pacific/Fiji",
    "Finland": "Europe/Helsinki",
    "France": "Europe/Paris",
    "Gabon": "Africa/Libreville",
    "Gambia": "Africa/Banjul",
    "Georgia": "Asia/Tbilisi",
    "Germany": "Europe/Berlin",
    "Ghana": "Africa/Accra",
    "Greece": "Europe/Athens",
    "Grenada": "America/Grenada",
    "Guatemala": "America/Guatemala",
    "Guinea": "Africa/Conakry",
    "Guinea-Bissau": "Africa/Bissau",
    "Guyana": "America/Guyana",
    "Haiti": "America/Port-au-Prince",
    "Honduras": "America/Tegucigalpa",
    "Hungary": "Europe/Budapest",
    "Iceland": "Atlantic/Reykjavik",
    "India": "Asia/Kolkata",
    "Indonesia (Bali)": "Asia/Ubud",
    "Indonesia (Jakarta)": "Asia/Jakarta",
    "Iran": "Asia/Tehran",
    "Iraq": "Asia/Baghdad",
    "Ireland": "Europe/Dublin",
    "Israel": "Asia/Jerusalem",
    "Italy": "Europe/Rome",
    "Jamaica": "America/Jamaica",
    "Japan": "Asia/Tokyo",
    "Jordan": "Asia/Amman",
    "Kazakhstan (Almaty)": "Asia/Almaty",
    "Kazakhstan (Nur-Sultan)": "Asia/Nur-Sultan",
    "Kenya": "Africa/Nairobi",
    "Kiribati": "Pacific/Tarawa",
    "Kuwait": "Asia/Kuwait",
    "Kyrgyzstan": "Asia/Bishkek",
    "Laos": "Asia/Vientiane",
    "Latvia": "Europe/Riga",
    "Lebanon": "Asia/Beirut",
    "Lesotho": "Africa/Maseru",
    "Liberia": "Africa/Monrovia",
    "Libya": "Africa/Tripoli",
    "Liechtenstein": "Europe/Vaduz",
    "Lithuania": "Europe/Vilnius",
    "Luxembourg": "Europe/Luxembourg",
    "Madagascar": "Indian/Antananarivo",
    "Malawi": "Africa/Blantyre",
    "Malaysia": "Asia/Kuala_Lumpur",
    "Maldives": "Asia/Male",
    "Mali": "Africa/Bamako",
    "Malta": "Europe/Valletta",
    "Marshall Islands": "Pacific/Majuro",
    "Mauritania": "Africa/Nouakchott",
    "Mauritius": "Indian/Mauritius",
    "Mexico (Central)": "America/Mexico_City",
    "Mexico (Pacific)": "America/Tijuana",
    "Micronesia": "Pacific/Chuuk",
    "Moldova": "Europe/Chisinau",
    "Monaco": "Europe/Monaco",
    "Mongolia (Ulaanbaatar)": "Asia/Ulaanbaatar",
    "Mongolia (Hovd)": "Asia/Hovd",
    "Montenegro": "Europe/Podgorica",
    "Morocco": "Africa/Casablanca",
    "Mozambique": "Africa/Maputo",
    "Myanmar": "Asia/Yangon",
    "Namibia": "Africa/Windhoek",
    "Nauru": "Pacific/Nauru",
    "Nepal": "Asia/Kathmandu",
    "Netherlands": "Europe/Amsterdam",
    "New Zealand (Auckland)": "Pacific/Auckland",
    "New Zealand (Wellington)": "Pacific/Wellington",
    "Nicaragua": "America/Managua",
    "Niger": "Africa/Niamey",
    "Nigeria": "Africa/Lagos",
    "North Macedonia": "Europe/Skopje",
    "Norway": "Europe/Oslo",
    "Oman": "Asia/Muscat",
    "Pakistan": "Asia/Karachi",
    "Palau": "Pacific/Palau",
    "Panama": "America/Panama",
    "Papua New Guinea": "Pacific/Port_Moresby",
    "Paraguay": "America/Asuncion",
    "Peru": "America/Lima",
    "Philippines": "Asia/Manila",
    "Poland": "Europe/Warsaw",
    "Portugal": "Europe/Lisbon",
    "Qatar": "Asia/Qatar",
    "Romania": "Europe/Bucharest",
    "Russia (Moscow)": "Europe/Moscow",
    "Russia (Siberia)": "Asia/Krasnoyarsk",
    "Rwanda": "Africa/Kigali",
    "Saint Kitts and Nevis": "America/St_Kitts",
    "Saint Lucia": "America/St_Lucia",
    "Saint Vincent and the Grenadines": "America/St_Vincent",
    "Samoa": "Pacific/Apia",
    "San Marino": "Europe/San_Marino",
    "Sao Tome and Principe": "Africa/Sao_Tome",
    "Saudi Arabia": "Asia/Riyadh",
    "Senegal": "Africa/Dakar",
    "Serbia": "Europe/Belgrade",
    "Seychelles": "Indian/Mahe",
    "Sierra Leone": "Africa/Freetown",
    "Singapore": "Asia/Singapore",
    "Slovakia": "Europe/Bratislava",
    "Slovenia": "Europe/Ljubljana",
    "Solomon Islands": "Pacific/Guadalcanal",
    "Somalia": "Africa/Mogadishu",
    "South Africa": "Africa/Johannesburg",
    "South Korea": "Asia/Seoul",
    "South Sudan": "Africa/Juba",
    "Spain": "Europe/Madrid",
    "Sri Lanka": "Asia/Colombo",
    "Sudan": "Africa/Khartoum",
    "Suriname": "America/Paramaribo",
    "Sweden": "Europe/Stockholm",
    "Switzerland": "Europe/Zurich",
    "Syria": "Asia/Damascus",
    "Taiwan": "Asia/Taipei",
    "Tajikistan": "Asia/Dushanbe",
    "Tanzania": "Africa/Dar_es_Salaam",
    "Thailand": "Asia/Bangkok",
    "Timor-Leste": "Asia/Dili",
    "Togo": "Africa/Lome",
    "Tonga": "Pacific/Tongatapu",
    "Trinidad and Tobago": "America/Port_of_Spain",
    "Tunisia": "Africa/Tunis",
    "Turkey": "Europe/Istanbul",
    "Turkmenistan": "Asia/Ashgabat",
    "Tuvalu": "Pacific/Funafuti",
    "Uganda": "Africa/Kampala",
    "Ukraine": "Europe/Kiev",
    "United Arab Emirates": "Asia/Dubai",
    "United Kingdom": "Europe/London",
    "United States (Alaska)": "America/Anchorage",
    "United States (Central)": "America/Chicago",
    "United States (Eastern)": "America/New_York",
    "United States (Mountain)": "America/Denver",
    "United States (Pacific)": "America/Los_Angeles",
    "Uruguay": "America/Montevideo",
    "Uzbekistan": "Asia/Tashkent",
    "Vanuatu": "Pacific/Efate",
    "Vatican City": "Europe/Vatican",
    "Venezuela": "America/Caracas",
    "Vietnam": "Asia/Ho_Chi_Minh",
    "Yemen": "Asia/Aden",
    "Zambia": "Africa/Lusaka",
    "Zimbabwe": "Africa/Harare"
}

# Select source and target countries
source_country = st.selectbox("Select the source country:", list(timezones_dict.keys()))
target_country = st.selectbox("Select the target country:", list(timezones_dict.keys()))

# Convert button
if st.button("Convert"):
    source_tz = pytz.timezone(timezones_dict[source_country])
    target_tz = pytz.timezone(timezones_dict[target_country])

    # Get the current date and time in the source timezone
    source_datetime = datetime.combine(input_date, input_time)
    source_datetime = source_tz.localize(source_datetime)

    # Convert to the target timezone
    target_datetime = source_datetime.astimezone(target_tz)

    # Display results
    st.markdown("<h3 style='color: #4CAF50;'>Converted Time</h3>", unsafe_allow_html=True)
    st.write(f"Original Time in **{source_country}**: {source_datetime.strftime('%Y-%m-%d %H:%M:%S')}")
    st.write(f"Converted Time in **{target_country}**: {target_datetime.strftime('%Y-%m-%d %H:%M:%S')}")
