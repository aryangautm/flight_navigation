import csv


def convert_dat_to_csv(dat_file, csv_file):
    columns = [
        "id",
        "name",
        "city",
        "country",
        "iata",
        "icao",
        "latitude",
        "longitude",
        "altitude",
        "timezone",
        "dst",
        "database",
        "type",
        "source",
    ]
    with open(dat_file, "r") as f:
        with open(csv_file, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(columns)
            for line in f:
                # Split the line by comma, while considering quoted fields
                row = [field.strip('"') for field in csv.reader([line]).__next__()]
                # Check if the number of columns exceeds 14
                if len(row) > 14:
                    print("Warning: Row has more than 14 columns.")
                # Write the row to CSV file
                writer.writerow(row)


# Example usage:
dat_file = "airports.dat"
csv_file = "airports.csv"
convert_dat_to_csv(dat_file, csv_file)
print("Conversion complete!")
