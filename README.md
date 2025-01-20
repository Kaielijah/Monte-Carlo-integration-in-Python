# Step 1 - Setting up environment 
### Check Dependencies versions install Dependencies:
1.	Homebrew
- Install: ```/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"```
- Check version: ```brew –version```
    - ```Homebrew 4.4.8```

2.	Python3
- ```python3 –version```  
    - Python 3.13.0
- ```brew install python```

3.	pip Python package manager
- ```pip3 –version```
    - ```pip 24.2 from /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/pip (python 3.13)```
- Install: ```python3 -m ensurepip --default-pip```

4. Pyenv - For Managing Multiple Python Versions (Optional)
- Check version: ```pyenv –version```
- Install:	```brew install pyenv```

5. Virtualenv - For Managing Virtual Environments (Optional)
- Check Version: ```pip3 install virtualenv```
- Install: ```pip3 install virtualenv```

6. Jupyter Notebook (Optional)
- Check Version: ``` jupyter --version```
- Install: ```pip3 install jupyter```

7. Essential Python Packages
- Run virtual env: ```source venv/bin/activate  # Reactivate the virtual environment if not already active
pip install --upgrade pip setuptools wheel```

8. Matplotlib - For plotting graph
- Install: ```pip install matplotlib```

9. ZSH system check (Optional) Depends on system . 
- Ensure python Points to python3: ```which python3 which pip3 echo $PATH```
    - Open .zshrc in a text editor: ```nano ~/.zshrc```
    - Add this line at the bottom: ```alias python="python3"```
    - Save the file (press CTRL + X, then Y, then Enter).
- source ~/.zshrc

10. Terminal commands to create local folder
- ```cd desktop/[folder]```
- ```mkdir ~/python-projects```
- ```cd ~/python-projects```
- ```python3 -m venv venv```
- ```source venv/bin/activate``` 
    - This is to activates virtual environment

11. Create Python file in VS with terminal
- ```touch main.py``` or create file 
- This is to open the file: ```code main.py```
- VS Terminal: ```python3 main.py``` 
    - This is to run the script in terminal to generate output
- Example of installing Python packages in env: ```pip install numpy pandas requests```
- Check the packages installed: ```pip list```

12. Pending to install Machine Learning (Future)
- Install: ``` pip install scikit-learn``` 


***Pro-tip: Always activate your virtual environment before running Python scripts: ```source venv/bin/activate```***


####IMPORTANT: While inside the virtual environment:  
Use pip without sudo to install packages:  
To deactivate the environment, run: ```deactivate```

# Monte-Carlo-integration-in-Python
### Monte Carlo integration in Python - Question1



