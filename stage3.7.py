#Virtual Environments & pip

#venv setup
#Installing packages

#1. What is a Virtual Environment?
#A virtual environment is an isolated Python environment where you can 
#install packages separately from your system-wide Python.

#| Without Virtual Env         | With Virtual Env                            |
#| --------------------------- | ------------------------------------------- |
#| Risk of package conflicts   | Isolated packages per project               |
#| System Python gets polluted | Clean and controlled environment            |
#| Hard to reproduce           | Reproducible setups with `requirements.txt` |

#2. Setting Up with venv

#Navigate to your project folder: cd my_project
#Create a virtual environment: python -m venv venv (venv is the name of the environment folder (can be any name).)
#Activate the virtual environment: 	venv\Scripts\activate
#You’ll see the environment name in your terminal:(venv) C:\Users\chetan\my_project>
#Deactivate when done:deactivate

#3. Installing Packages with pip
#pip install requests

#| Command                  | Purpose                                  |
#| ------------------------ | ---------------------------------------- |
#| `pip install flask`      | Install Flask                            |
#| `pip uninstall requests` | Remove a package                         |
#| `pip list`               | Show installed packages                  |
#| `pip freeze`             | List installed packages (exact versions) |
#| `pip show pandas`        | Show package details                     |

#4. Using requirements.txt

#Save your dependencies:pip freeze > requirements.txt
#Reinstall everything later:pip install -r requirements.txt

#5. Best Practices & Troubleshooting

#| Tip                                                 | Why                                       |
#| --------------------------------------------------- | ----------------------------------------- |
#| Always use `venv` for new projects                  | Avoid package conflicts                   |
#| Use `requirements.txt`                              | Ensures easy install on other systems     |
#| Commit `requirements.txt`, not `venv/`              | `venv/` is OS-specific and large          |
#| Use `pip install --upgrade <package>`               | Keep libraries up-to-date                 |
#| VS Code: select interpreter from `.venv/bin/python` | Ensures your editor uses the right Python |

#Full Example
# Create folder
mkdir my_project && cd my_project

# Create venv
python -m venv venv

# Activate
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install packages
pip install requests flask

# Save packages
pip freeze > requirements.txt

# Deactivate when done
deactivate
