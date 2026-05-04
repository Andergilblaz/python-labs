
monthConversions = {
    "jan":"January",
    "feb":"February",
    "mar":"March",
    "apr":"April",
    "may":"May",
    "jun":"June",
    "jul":"July",
    "aug":"August",
    "sep":"September",
    "oct":"October",
    "nov":"November",
    "dec":"December"
}

print(monthConversions["feb"])

# With this, we can put an error message
print(monthConversions.get("luv", "Not a valid key"))