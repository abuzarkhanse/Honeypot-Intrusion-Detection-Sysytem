import geoip2.database
import pandas as pd

# Load honeypot CSV
df = pd.read_csv('honeypot_logs.csv')

# Load GeoIP database
reader = geoip2.database.Reader('GeoLite2-City_20250429/GeoLite2-City.mmdb')

# Look up country by IP
countries = []
for ip in df['ip']:
    try:
        response = reader.city(ip)
        country = response.country.name
    except:
        country = "Unknown"
    countries.append(country)

# Add country to dataframe
df['country'] = countries

# Save new CSV with country info
df.to_csv('honeypot_logs_geo.csv', index=False)
print("[+] GeoIP lookup complete. File saved as honeypot_logs_geo.csv")

