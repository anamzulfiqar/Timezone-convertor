import streamlit as st
from datetime import datetime
import pytz

# Set page config
st.set_page_config(page_title="🌍 Time Zone Converter", page_icon="🌍")

# Title of the app with some styling
st.title("🌍 Time Zone Converter")
st.markdown("""
    <style>
    .title {
        text-align: center;
        color: #4B0082;
        font-size: 2.5em;
    }
    </style>
""", unsafe_allow_html=True)

# Subheader for user input
st.subheader("Enter a Specific Time to Convert")

# Allow user to input time and date
input_time = st.time_input("Select a time:")
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
    "Russia (Yekaterinburg)": "Asia/Yekaterinburg",
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
    "Tanzania": "Africa/Dodoma",
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
    "Ukraine": "Europe/Kyiv",
    "United Arab Emirates": "Asia/Dubai",
    "United Kingdom": "Europe/London",
    "United States (Eastern)": "America/New_York",
    "United States (Central)": "America/Chicago",
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

# Create two select boxes for choosing countries
source_country = st.selectbox("Select Source Country", list(timezones_dict.keys()))
target_country = st.selectbox("Select Target Country", list(timezones_dict.keys()))

# Button to convert time
if st.button("Convert Time"):
    if input_time and input_date:
        # Combine date and time into a datetime object
        source_time = datetime.combine(input_date, input_time)
        
        # Get the corresponding timezone for the selected countries
        source_timezone = pytz.timezone(timezones_dict[source_country])
        target_timezone = pytz.timezone(timezones_dict[target_country])
        
        # Localize the source time and convert it to the target timezone
        localized_time = source_timezone.localize(source_time)
        converted_time = localized_time.astimezone(target_timezone)
        
        # Display the converted time
        st.success(f"Converted Time in {target_country}: {converted_time.strftime('%Y-%m-%d %H:%M:%S')}")

# Footer for app information
st.markdown("""
    <style>
    .footer {
        text-align: center;
        font-size: 1em;
        color: #808080;
    }
    </style>
    <div class="footer">Created by [Anam Zulfiqar]</div>
""", unsafe_allow_html=True)
