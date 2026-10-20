# Anleitung: Vorschau, Domain und Änderungen

## 1. Vorschau über GitHub Pages einschalten (einmalig)

Die fertige Website liegt im Ordner `docs/`. GitHub Pages veröffentlicht diesen Ordner direkt aus dem Branch `main`.

1. Pull Request auf GitHub mergen, damit `docs/` auf `main` liegt.
2. Im Repository auf **Settings → Pages** gehen.
3. Bei **Build and deployment → Source**: „Deploy from a branch“ wählen.
4. Bei **Branch**: `main` und Ordner `/docs` wählen, dann **Save**.
5. Nach ein bis zwei Minuten ist die Seite erreichbar unter
   **https://eliyah-kernseite.github.io/NFC-Guide-/**
   (englische Version: …/NFC-Guide-/en/).

Jeder neue Commit auf `main`, der `docs/` ändert, wird automatisch neu veröffentlicht.

## 2. Domain kadirsells.de und www richtig einrichten

Ziel: Es gibt nur **eine** Adresse, `https://kadirsells.de`. Wer `www.kadirsells.de` eintippt, wird per 301 dorthin umgeleitet.
Stand 20.10.2026: `kadirsells.de` zeigt noch auf Lovable, `www.kadirsells.de` ist gar nicht erreichbar.

### Variante A: Neue Seite über GitHub Pages (empfohlen, wenn die neue Seite live gehen soll)

Beim Domain-Anbieter (dort, wo kadirsells.de registriert ist) die DNS-Einträge so setzen:

| Typ | Name | Wert |
| --- | --- | --- |
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| AAAA | @ | 2606:50c0:8000::153 |
| AAAA | @ | 2606:50c0:8001::153 |
| AAAA | @ | 2606:50c0:8002::153 |
| AAAA | @ | 2606:50c0:8003::153 |
| CNAME | www | eliyah-kernseite.github.io |

Alte A-/CNAME-Einträge, die auf Lovable zeigen, vorher löschen.
Dann in **Settings → Pages → Custom domain** `kadirsells.de` eintragen, speichern und, sobald es angeboten wird, **Enforce HTTPS** anhaken.
GitHub leitet `www.kadirsells.de` dann automatisch auf `kadirsells.de` um.

Achtung: Ab dem Umzug zeigt die Domain die neue Seite und nicht mehr Lovable. Vorher die Vorschau prüfen.

### Variante B: Seite bleibt bei Lovable

In Lovable unter **Settings → Domains** zusätzlich `www.kadirsells.de` hinzufügen, den angezeigten DNS-Eintrag beim Domain-Anbieter setzen und `kadirsells.de` als Hauptdomain markieren. Dann muss in `tools/content.py` der Abschnitt „Hosting“ der Datenschutzerklärung wieder auf Lovable umgestellt werden.

### Danach: Google Search Console

1. https://search.google.com/search-console öffnen, Property „Domain“ mit `kadirsells.de` anlegen, per DNS-TXT-Eintrag bestätigen.
2. Unter **Sitemaps** `https://kadirsells.de/sitemap.xml` einreichen.
3. Startseite per **URL-Prüfung** zur Indexierung anfordern.

## 3. Texte ändern

Alle Texte stehen in `tools/content.py` (Deutsch und Englisch nebeneinander).
Nach einer Änderung einmal `python3 tools/build_site.py` ausführen, dann sind die Seiten in `docs/` neu gebaut.
Dafür braucht es Python 3 mit Pillow (`pip install pillow`). Wer am iPad arbeitet, kann mir die Änderung einfach schreiben.

## 4. Was Kadir noch prüfen oder erledigen muss

- **Rechtstexte absegnen lassen**: Die Texte sind nach bestem Wissen erstellt, ersetzen aber keine Rechtsberatung. Vor dem Livegang von einem Anwalt oder Rechtstexte-Dienst prüfen lassen.
- **Streichpreise im Digistore24-Checkout**: Dort steht 49,99 € → 29,99 € bzw. 19,99 € → 13,99 €. Ein Streichpreis ist nur erlaubt, wenn das Produkt vorher wirklich zu diesem Preis verkauft wurde (§ 11 PAngV). Sonst in Digistore24 entfernen.
- **Widerrufsverzicht im Checkout**: In Digistore24 prüfen, dass die Zustimmung zum vorzeitigen Erlöschen des Widerrufsrechts bei digitalen Inhalten aktiv ist. Die eigene Checkbox auf der Kaufseite wurde entfernt, weil nur die Zustimmung bei Digistore24 zählt.
- **Updates des Guides**: Die Kaufseite verspricht „spätere Updates inklusive“. Das muss auch wirklich passieren (z. B. über Digistore24 oder per E-Mail an die Käufer).
- **Telefon**: Der Satz „Telefon in Einrichtung“ wurde gestrichen. Als zweiter Kontaktweg ist Instagram-DM angegeben. Eine eigene Adresse wie kontakt@kadirsells.de wäre professioneller und datenschutzrechtlich besser als Gmail.
- **Privatadresse im Impressum**: Klären, ob sie dort stehen soll. Alternative ist eine ladungsfähige Geschäftsadresse (Impressum-Service).
