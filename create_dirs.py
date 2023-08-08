from pathlib import Path
from datetime import datetime
from datetime import timedelta

basedir = '/Users/cameron/Desktop'

trees = ["ech", "ech_raw", "rf", "rf_raw", "nbi", "nbi_raw", "bias", "bias_raw", "diag", "diag_raw", "misc", "misc_raw"]

# Get today's date
today = datetime.now()

# Calculate the last day of the current year
end_of_year = datetime(today.year, 12, 31)

# Generate a list of datetime objects
date_list = []
current_date = today

while current_date <= end_of_year:
    date_list.append(current_date)
    current_date += timedelta(days=1)

# Print the list of datetime objects
for date in date_list:

	for tree in trees:


		#year = date.strftime("%y")

		Path(f'{basedir}/{date.strftime("%y")}/{date.month:02d}/{date.day:02d}/{tree}').mkdir(parents=True, exist_ok=True)