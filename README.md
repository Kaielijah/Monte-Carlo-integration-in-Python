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


#### IMPORTANT
While inside the virtual environment, 
Use pip without ```sudo``` to install packages
To deactivate the environment, run: ```deactivate```

# Monte-Carlo-integration-in-Python
### Monte Carlo integration in Python - Question1


Monte Carlo integration is an application of the law of large numbers. Consider the integral
𝐼 = ∫ sin⁡(𝑥)
𝑥+𝑐𝑜𝑠2
⁡(𝑥) 𝑑𝑥
1
0.
1) Explain how one can evaluate 𝐼 numerically using Monte Carlo integration. Write detailed
steps.
2) Implement the numerical integration in Part 1) 1000 times using 𝑛 = 200⁡sample points and
find an appropriate way to justify the accuracy of your numerical results.
3) Instead of the uniform (0,1) distribution often used in Monte Carlo integration, one can generate
a random sample of size 𝑛 from a distribution with the pdf
𝑓 𝑋(𝑥) = 2𝑥 for 𝑥⁡ ∈ [0, 1]. (1)
State how to evaluate 𝐼⁡using the sample points from this distribution.
4) Implement the numerical integration in Part 3) 1000 times with sample size 𝑛 = 200. Evaluate
the accuracy.
5) Compare two sets of 1000 estimates of 𝐼 obtained by methods Parts 2) and 4), respectively,
using appropriate statistical measures. Which numerical integration method do you prefer and
why?  
Note: For implementation of numerical integrations in parts 2) and 4), you are required to write an
R or Python code (or other computer languages that you are familiar with), which should be
included in your answers together with the relevant computer outcomes.
a. To generate a size-200 random sample (i.e., 200 random numbers) from a distribution, say
Uniform(0,1), in R, you can use
sample<-runif(200, min=0, max=1) 
b. To generate random numbers from a distribution in (1), you need to use the probability
transform as follows. Suppose that 𝐹 𝑋(𝑥) is the cdf of the distribution of random variable 𝑋,
Let 𝑌 = 𝐹 𝑋(𝑋). Then 𝑌~𝑈𝑛𝑖𝑓𝑜𝑟𝑚(0, 1). To generate random numbers of 𝑋, we first
generate random numbers 𝑦1,
⋯
, 𝑦𝑛 for 𝑌 from uniform(0, 1), and then random numbers for
X are obtained by 𝑥𝑖 = 𝐹 𝑋
−1(𝑦𝑖) for 𝑖 = 1,
⋯
, 𝑛.
