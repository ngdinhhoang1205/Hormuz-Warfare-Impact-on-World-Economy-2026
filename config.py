# Updated country_dict with English labels
country_dict = {
    # ==========================================
    # 1. SOUTHEAST ASIA (ASEAN)
    # ==========================================
    "VN": "Viet Nam",                      # Chọn phiên bản chuẩn ISO chính thức
    "TH": "Thailand",
    "SG": "Singapore", 
    "ID": "Indonesia",
    "MY": "Malaysia",
    "PH": "Philippines",
    "BN": "Brunei",
    "KH": "Cambodia",
    "LA": "Laos",
    "MM": "Myanmar",
    "TL": "Timor-Leste",

    # ==========================================
    # 2. EUROPE (Eurozone & Major Economies)
    # ==========================================
    "DE": "Germany",
    "FR": "France",
    "IT": "Italy",
    "ES": "Spain",
    "NL": "Netherlands",
    "GB": "United Kingdom",
    "BE": "Belgium",
    "AT": "Austria",
    "PT": "Portugal",
    "GR": "Greece",
    "FI": "Finland",
    "IE": "Ireland",
    "DK": "Denmark",
    "SE": "Sweden",
    "PL": "Poland",
    "CZ": "Czechia",
    "RO": "Romania",
    "HU": "Hungary",
    "VA": "Holy See (Vatican City State)",  # Tên đầy đủ hơn
    "UA": "Ukraine",
    "TR": "Türkiye",                       # Tên chính thức mới
    "XK": "Kosovo, Republic of",

    # ==========================================
    # 3. AMERICAS (North & South America)
    # ==========================================
    "US": "United States",
    "CA": "Canada",
    "MX": "Mexico",
    "BR": "Brazil",
    "AR": "Argentina",
    "CO": "Colombia",
    "SR": "Suriname",
    "SV": "El Salvador",
    "SX": "Sint Maarten (Dutch part)",
    "TT": "Trinidad and Tobago",
    "UY": "Uruguay",
    "VC": "Saint Vincent and the Grenadines",
    "VE": "Venezuela, Bolivarian Republic", # Tên đầy đủ hơn

    # ==========================================
    # 4. MIDDLE EAST & CENTRAL ASIA
    # ==========================================
    "SA": "Saudi Arabia", 
    "AE": "UAE",          
    "QA": "Qatar",
    "KW": "Kuwait",
    "OM": "Oman",
    "BH": "Bahrain",
    "IQ": "Iraq",
    "SY": "Syrian Arab Republic",           # Tên đầy đủ hơn
    "TJ": "Tajikistan",
    "TM": "Turkmenistan",
    "UZ": "Uzbekistan",
    "YE": "Yemen",

    # ==========================================
    # 5. AFRICA
    # ==========================================
    "SN": "Senegal",
    "SO": "Somalia",
    "SS": "South Sudan",
    "SZ": "Eswatini",
    "TD": "Chad",
    "TG": "Togo",
    "TN": "Tunisia",
    "TZ": "Tanzania, United Republic of",  # Tên đầy đủ hơn
    "UG": "Uganda",
    "ZA": "South Africa",
    "ZM": "Zambia",
    "ZW": "Zimbabwe",

    # ==========================================
    # 6. OCEANIA & OTHERS / REGIONAL
    # ==========================================
    "TO": "Tonga",
    "TV": "Tuvalu",
    "VU": "Vanuatu",
    "WS": "Samoa",
    "ST": "Sao Tome and Principe",
    "SUH": "Former U.S.S.R.",
    "U2": "Euro Area (Member States and Institutions of the Euro Area) changing composition"
}


country_dict_3_char = {
    # ==========================================
    # 1. SOUTHEAST ASIA (ASEAN)
    # ==========================================
    "VNM": "Southeast Asia (Vietnam)",
    "THA": "Southeast Asia (Thailand)",
    "SGP": "Southeast Asia (Singapore)", 
    "IDN": "Southeast Asia (Indonesia)",
    "MYS": "Southeast Asia (Malaysia)",
    "PHL": "Southeast Asia (Philippines)",
    "BRN": "Southeast Asia (Brunei)",
    "KHM": "Southeast Asia (Cambodia)",
    "LAO": "Southeast Asia (Laos)",
    "MMR": "Southeast Asia (Myanmar)",
    "TLS": "Southeast Asia (Timor-Leste)",

    # ==========================================
    # 2. EUROPE (Eurozone & Major Economies)
    # ==========================================
    "DEU": "Europe (Germany)",
    "FRA": "Europe (France)",
    "ITA": "Europe (Italy)",
    "ESP": "Europe (Spain)",
    "NLD": "Europe (Netherlands)",
    "GBR": "Europe (United Kingdom)",
    "BEL": "Europe (Belgium)",
    "AUT": "Europe (Austria)",
    "PRT": "Europe (Portugal)",
    "GRC": "Europe (Greece)",
    "FIN": "Europe (Finland)",
    "IRL": "Europe (Ireland)",
    "DNK": "Europe (Denmark)",
    "SWE": "Europe (Sweden)",
    "POL": "Europe (Poland)",
    "CZE": "Europe (Czechia)",
    "ROU": "Europe (Romania)",
    "HUN": "Europe (Hungary)",

    # ==========================================
    # 3. AMERICAS (North & South America)
    # ==========================================
    "USA": "Americas (United States)",
    "CAN": "Americas (Canada)",
    "MEX": "Americas (Mexico)",
    "BRA": "Americas (Brazil)",
    "ARG": "Americas (Argentina)",
    "COL": "Americas (Colombia)",

    # ==========================================
    # 4. MIDDLE EAST (Strait of Hormuz Region)
    # ==========================================
    "SAU": "Middle East (Saudi Arabia)", 
    "ARE": "Middle East (UAE)",          
    "QAT": "Middle East (Qatar)",
    "KWT": "Middle East (Kuwait)",
    "OMN": "Middle East (Oman)",
    "BHR": "Middle East (Bahrain)",
    "IRQ": "Middle East (Iraq)"
}




us_economy_metrics = {
    'CPI_All_Items': 'CPIAUCSL',         # Monthly
    'Unemployment_Rate': 'UNRATE',       # Monthly
    'Total_Nonfarm_Payrolls': 'PAYEMS',  # Monthly
    'Real_GDP': 'GDPC1',                 # Quarterly
    'Manufacturing_Investment': 'C307RX1Q020SBEA' # Quarterly
}