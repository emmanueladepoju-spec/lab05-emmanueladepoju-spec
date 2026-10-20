
import argparse
import csv


def main():
    parser = argparse.ArgumentParser(
        description="Print CSV rows matching a column value."
    )
    parser.add_argument("filename", help="the CSV file to search")
    parser.add_argument("column", help="the column name")
    parser.add_argument("value", help="the value to match")

    args = parser.parse_args()

    with open(args.filename, newline="") as file:
        reader = csv.reader(file)
        rows = list(reader)

    header = rows[0]
    column_index = header.index(args.column)

    for row in rows[1:]:
        if row[column_index] == args.value:
            print(",".join(row))


if __name__ == "__main__":
    main()
