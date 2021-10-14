# MHD-Scanner
[![GitHub last commit](https://img.shields.io/github/last-commit/MHD-Team/MHD-Main?logo=github&logoColor=success)](https://github.com/MHD-Team/MHD-Main/commits/main)
[![GitHub commit activity](https://img.shields.io/github/commit-activity/m/MHD-Team/MHD-Main?logo=github&logoColor=blue)](https://github.com/MHD-Team/MHD-Main/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/MHD-Team/MHD-Main?logo=github&logoColor=blue)](https://github.com/MHD-Team/MHD-Main)
[![Github language count](https://img.shields.io/github/languages/count/MHD-Team/MHD-Main?logo=github&logoColor=blue)](https://github.com/MHD-Team/MHD-Main)
[![Discord](https://img.shields.io/discord/897766520476827669?logo=discord&color=7289d9)](https://discord.com/channels/897766520476827669/897766520476827672)
[![Code Style](https://img.shields.io/badge/code%20style-black-black?logo=python&logoColor=black)](https://github.com/psf/black)

[**English Version**](https://github.com/MHD-Team/MHD-Main/blob/main/README.md)

<sup>Dieses Projekt wurde ursprünglich für <a href="https://jugendhackt.org/events/berlin/">Jugend hackt Berlin</a> von <a href="https://github.com/orgs/MHD-Team/people/Tams-Tams">Math</a>, <a href="https://github.com/orgs/MHD-Team/people/Nino6781">Nino6781</a>, <a href="https://github.com/orgs/MHD-Team/people/Joshuawwolf">joshua</a> und Farhan erstellt.</sup>

<details>
    <summary><span style="cursor:pointer;color:blue;text-decoration:underline;">Table of Contents</span></summary>
    <ul>
        <li>1.0 <a href="#10-installation">Installation</a></li>
        <li>2.0 <a href="#20-mitmachen">Mitmachen</a></li>
        <li>3.0 <a href="#30-fehlerbehebung">Fehlerbehebung</a>
            <ul>
                <li>3.1 <a href="#31-fehler-bei-der-installation">Fehler bei der Installation</a></li>
                <li>3.2 <a href="#32-andere-fehler">Andere Fehler</a></li>
            </ul>
        </li>
        <li>4.0 <a href="#40-links">Links</a></li>
    </ul>
</details>

<br>


Mit dem MHD-Scanner kannst du Punkte bekommen und Spiele spielen, indem du Lebensmittel kaufst, die erst vor ein paar Tagen abgelaufen sind. So ermutigst du die Leute dazu, Lebensmittel zu kaufen, die noch nicht verdorben sind, aber von den Supermärkten trotzdem entsorgt werden, weil nicht genug Leute sie kaufen. Das ist eine Win-Win-Situation, sowohl für die Menschen, die spielen können, als auch für die Umwelt.

---

## 1.0 Installation
Der erste Schritt ist die Installation von python. Dieses Projekt benötigt wahrscheinlich python 3.5+, es wurde mit python 3.7 erstellt. Du kannst aber die neueste Version von Python installieren (derzeit 3.10.0).  
[Python herunterladen](https://www.python.org/downloads/)  
**Vergiss nicht, "Add Python to PATH", "Add Python to environment variables" und "pip"** anzukreuzen.  

Um zu überprüfen, ob Python installiert ist, öffne dein Terminal und geben Sie `python -V` ein.  
Wenn du einen Fehler erhältst, gehe zu [Fehlerbehebung](#30-fehlerbehebung).

Prüfe nun, ob pip installiert ist. Gib `pip -h` in das Terminal ein.  
Wenn du eine Fehlermeldung erhältst, gehe zu [Fehlerbehebung](#30-fehlerbehebung).

OPTIONAL: Da dieses Projekt viele Module von pip benötigt, empfehlen wir dich, eine [Virtual Environment](https://www.section.io/engineering-education/introduction-to-virtual-environments-and-dependency-managers/) zu verwenden. (stelle sicher, dass du dich im Hauptverzeichnis befindest)  

Windows:
```
python -m venv env
.\env\Scripts\activate
```

Linux/Mac:
```bash
python3 -m venv env
source env/bin/activate
```

Super! Installiere nun die Module aus der Datei requirements.txt:
```bash
pip install -r requirements.txt
```

Jetzt kannst du das Programm ausführen mit
```bash
python app.py
```

Das war's! Sie haben es geschafft! Deaktiviere nun den venv:

Windows:
```
.env\Scripts\deactivate.bat
```

Linux/Mac:
```bash
deactivate
```



**Wenn du das Projekt erneut starten willst, sind hier die Schritte:**  
1. **Aktivieren Sie den venv:**  
	Windows:
	```
	.venv\Scripts\activate
	```

	Linux/Mac:
	```bash
	activate
	```

2. **Das Projekt starten**  
	```bash
	python app.py
	```

3. **Deaktiviere das venv**  
	Windows:
	```
	\env\Scripts\deactivate.bat
	```

	Linux/Mac:
	```bash
	deactivate
	```

## 2.0 Mitmachen
Wir freuen uns immer über Beiträge. Wenn du irgendwelche Ideen oder Vorschläge hast, schreibe bitte zuerst einen [issue](https://github.com/MHD-Team/MHD-Main/issues/new) mit dem Tag enhancement. Wenn du ein Problem lösen willst, hinterlasse bitte einen Kommentar, dass du daran arbeitest. Wenn du selbst Änderungen vorgenommen hast, erstelle einen neuen branch und stelle einen [pull request](https://github.com/MHD-Team/MHD-Main/compare) und warte darauf, dass einer der Eigentümer/Mitglieder ihn zusammenführt.

## 3.0 Fehlerbehebung

### 3.1 Fehler bei der Installation
**`''python' is not recognized as an internal or external command,
operable program or batch file.`**  
Das bedeutet, dass Python nicht korrekt installiert ist oder dass es nicht in der PATH-Variable enthalten ist.  

Versuche:

- `python3 -V`
- `py -V`
- `python [PYTHONVERSION.PYTHONVERSION]` z.B. `python 3.10`

Wenn beide Befehle nicht funktionieren, versuche Python zu deinstallieren und wieder mit der [Anleitung oben zu installieren](#11-installing).

**`'pip' is not recognized as an internal or external command,
operable program or batch file.`**  
Das bedeutet, dass du pip nicht installiert hast, als du Python installiert hast, oder es nicht in der PATH-Variable ist.  

Versuche:

- `pip3 -V`
- `pip -V`

Wenn beide Befehle nicht funktionieren, [installiere pip](https://pip.pypa.io/en/stable/installation/).

### 3.2 Andere Fehler
Wenn du andere Fehler, Programm- oder Installationsfehler hast, die wir nicht erwähnt haben, zögere nicht, [ein Problem](https://github.com/MHD-Team/MHD-Main/issues/new) mit dem Tag bug zu öffnen.
Oder schreiben Sie eine E-Mail an mhd.team[at]outlook.de

---

# 4.0 Links
Github: https://github.com/MHD-Team  
Lizenz: https://github.com/MHD-Team/MHD-Main/blob/main/LICENSE  
Discord: https://discord.com/channels/897766520476827669/897766520476827672  
Jugend Hackt: https://jugendhackt.org/ 