\# Excel Cleaner



Πρόγραμμα Python που καθαρίζει αυτόματα αρχεία Excel.



\## Τι κάνει



\- Αφαιρεί τις εντελώς κενές γραμμές

\- Εντοπίζει και αφαιρεί τις διπλότυπες εγγραφές

\- Ταξινομεί τα δεδομένα με βάση μια στήλη (σωστά και με ελληνικούς τόνους)

\- Εξάγει ένα νέο, καθαρό αρχείο Excel (το αρχικό δεν αλλάζει)



\## Εγκατάσταση



```bash

git clone https://github.com/giansygkounas-source/excel-cleaner.git

cd excel-cleaner

python -m venv venv

venv\\Scripts\\activate

pip install -r requirements.txt

```



(Σε Mac/Linux η ενεργοποίηση είναι `source venv/bin/activate`.)



\## Χρήση



```bash

python cleaner.py data.xlsx

```



Προαιρετικές παράμετροι:



| Παράμετρος | Τι κάνει | Προεπιλογή |

|---|---|---|

| `-o`, `--output` | όνομα του νέου αρχείου | `clean\_data.xlsx` |

| `-s`, `--sort-by` | στήλη ταξινόμησης | η πρώτη στήλη |



Παράδειγμα:



```bash

python cleaner.py data.xlsx -s Πόλη -o by\_city.xlsx

```



\## Παράδειγμα



Το `data.xlsx` έχει 9 γραμμές: 2 κενές και 2 διπλότυπες. Μετά τον καθαρισμό μένουν 5.



\## Τεχνολογίες



Python, pandas, openpyxl

