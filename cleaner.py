import unicodedata
import pandas as pd
import argparse
import sys


def without_accents(text):
    decomposed = unicodedata.normalize("NFD", text)
    no_marks = "".join(c for c in decomposed if not unicodedata.combining(c))
    return no_marks.casefold()


def clean_data(df, sort_by):
    df = df.dropna(how="all")
    df = df.drop_duplicates()
    df = df.sort_values(by=sort_by, key=lambda col: col.astype(str).map(without_accents))
    df = df.reset_index(drop=True)
    return df


def main():
    parser = argparse.ArgumentParser(description="Καθαρισμός αρχείου Excel")
    parser.add_argument("input_file", help="το Excel που θα καθαριστεί")
    parser.add_argument("-o", "--output", default="clean_data.xlsx",
                        help="όνομα του νέου αρχείου")
    parser.add_argument("-s", "--sort-by",
                        help="στήλη ταξινόμησης (αν λείπει, η πρώτη στήλη)")
    args = parser.parse_args()

    try:
        df = pd.read_excel(args.input_file)
    except FileNotFoundError:
        sys.exit(f"Σφάλμα: δεν βρέθηκε το αρχείο '{args.input_file}'")

    print("Before:", df.shape)

    sort_by = args.sort_by or df.columns[0]
    if sort_by not in df.columns:
        available = ", ".join(str(c) for c in df.columns)
        sys.exit(f"Σφάλμα: δεν υπάρχει στήλη '{sort_by}'. Διαθέσιμες: {available}")

    df = clean_data(df, sort_by=sort_by)
    print("After:", df.shape)

    try:
        df.to_excel(args.output, index=False)
    except PermissionError:
        sys.exit(f"Σφάλμα: κλείσε το '{args.output}' στο Excel και ξανατρέξε")

    print(f"Το {args.output} δημιουργήθηκε!")


if __name__ == "__main__":
    main()