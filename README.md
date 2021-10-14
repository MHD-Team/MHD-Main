# MHD-Scanner
[![GitHub last commit](https://img.shields.io/github/last-commit/MHD-Team/MHD-Main?logo=github&logoColor=success)](https://github.com/MHD-Team/MHD-Main/commits/main)
[![GitHub commit activity](https://img.shields.io/github/commit-activity/m/MHD-Team/MHD-Main?logo=github&logoColor=blue)](https://github.com/MHD-Team/MHD-Main/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/MHD-Team/MHD-Main?logo=github&logoColor=blue)](https://github.com/MHD-Team/MHD-Main)
[![Github language count](https://img.shields.io/github/languages/count/MHD-Team/MHD-Main?logo=github&logoColor=blue)](https://github.com/MHD-Team/MHD-Main)
[![Discord](https://img.shields.io/discord/897766520476827669?logo=discord)](https://discord.com/channels/897766520476827669/897766520476827672)
[![Code Style](https://img.shields.io/badge/code%20style-black-black?logo=python&logoColor=black)](https://github.com/psf/black)

[**German Version**](https://github.com/MHD-Team/MHD-Main/blob/main/README_German.md)

<sup>This project was originally made for <a href="https://jugendhackt.org/events/berlin/">Jugend hackt Berlin</a> by <a href="https://github.com/orgs/MHD-Team/people/Tams-Tams">Math</a>, <a href="https://github.com/orgs/MHD-Team/people/Nino6781">Nino6781</a>, <a href="https://github.com/orgs/MHD-Team/people/Joshuawwolf">joshua</a> and Farhan.</sup>

<details>
    <summary><span style="cursor:pointer;color:blue;text-decoration:underline;">Table of Contents</span></summary>
    <ul>
        <li>1.0 <a href="#10-installing">Installing</a></li>
        <li>2.0 <a href="#20-contributing">Contributing</a></li>
        <li>3.0 <a href="#30-troubleshooting">Troubleshooting</a>
            <ul>
                <li>3.1 <a href="#31-installation-errors">Installation Errors</a></li>
                <li>3.2 <a href="#32-other-errors">Other Errors</a></li>
            </ul>
        </li>
        <li>4.0 <a href="#40-reference">Reference</a></li>
    </ul>
</details>


<br>

With the MHD-Scanner, you can get points and play games by buying Groceries which expired just a few days ago. Thus you encourage people to buy food which isn't spoiled, but Supermarkets still dispose, because not enough people are buying it. It's a Win-Win Situation, both for the people, who can play games and for the environment.

---

## 1.0 Installing
The first step is to install python. This project probably needs python 3.5+, it was created with python 3.7. But you can install the latest version of python (currently 3.10.0).  
[Download Python](https://www.python.org/downloads/)  
**Don't forget to tick "Add Python to PATH", "Add Python to environment variables" and "pip"**  

To check if python's installed, open your terminal and type `python -V`.  
If you get an error, go to [Troubleshooting](#13-troubleshooting).

Now check if pip's installed. Type `pip -h` in the terminal.  
If you get an error, go to [Troubleshooting](#13-troubleshooting).

OPTIONAL: Because this project needs a lot of modules from pip, we recommend you to use a [Virtual Environment](https://www.section.io/engineering-education/introduction-to-virtual-environments-and-dependency-managers/). (make sure you are in the main directory)  

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



Great! Now install the modules from requirements.txt:
```bash
pip install -r requirements.txt
```

Now you can run the program with
```bash
python app.py
```

That's it! You did it! Now deactivate the venv:

Windows:
```
.\env\Scripts\deactivate.bat
```

Linux/Mac:
```bash
deactivate
```



**If you want to run the project again, here are the steps:**  
1. **Activate the venv:**  
	Windows:
	```
	.\env\Scripts\activate
	```

	Linux/Mac:
	```bash
	activate
	```

2. **Run the project**  
	```bash
	python app.py
	```

3. **Deactivate the venv**  
	Windows:
	```
	.\env\Scripts\deactivate.bat
	```

	Linux/Mac:
	```bash
	deactivate
	```

## 2.0 Contributing
We always welcome contributions. If you have any ideas or suggestions, please [post an issue](https://github.com/MHD-Team/MHD-Main/issues/new) first with the tag enhancement. If you want to solve an issue, please leave a comment that you've been working on it. If you have made changes yourself, make a new branch and make a [pull request](https://github.com/MHD-Team/MHD-Main/compare) and wait for one of the owners/members to merge it.

## 3.0 Troubleshooting

### 3.1 Installation Errors
**`'python' is not recognized as an internal or external command,
operable program or batch file.`**  
That means you haven't installed python correctly, or it's not in the PATH variable.  

Try:

- `python3 -V`
- `py -V`
- `python [PYTHONVERSION.PYTHONVERSION]` e.g. `python 3.10`

If both commands doen't work, try to uninstall python and install it with the [instructions above](#11-installing).

**`'pip' is not recognized as an internal or external command,
operable program or batch file.`**  
That means you haven't installed pip when you installed python, or it's not in the PATH variable.  

Try:

- `pip3 -V`
- `pip -V`

If both commands don't work, [install pip](https://pip.pypa.io/en/stable/installation/).

### 3.1 Other errors
If you have any other errors, program or installing errors we didn't mention, don't hesitate to [open an issue](https://github.com/MHD-Team/MHD-Main/issues/new) with the tag bug.
Or write an e-mail to mhd.team[at]outlook.de

---

# 3.0 Reference
Github: https://github.com/MHD-Team  
License: https://github.com/MHD-Team/MHD-Main/blob/main/LICENSE  
Discord: https://discord.com/channels/897766520476827669/897766520476827672  
Jugend Hackt: https://jugendhackt.org/  