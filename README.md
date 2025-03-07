# Terminal-Helper
An AI tool that you can use inside the terminal to get help with commands and errors


## Installation & Setup
1. Clone this repository 
```bash
git clone https://github.com/Outdatedcandy92/Thelper.git
```
2. cd into the repository
```bash 
cd Thelper
```
3. Install requirements
```bash
pip install -r requirements.txt
```
4. Make `thelper` executeable 
```bash
chmod +x thelper
```
4. Move the folder to a folder where you won't accidentally remove it. (Could be Documents or Applications folder)

## Add thelper to path
### For Linux and Mac

1. Check which shell you're using
```bash
echo $SHELL
```
2. Add folder to path
```bash
nano ~/.zshrc  # For Zsh
# or
nano ~/.bash_profile  # For Bash

```
3. Add this to your file
```bash
export PATH="$HOME/path_to/your_project_folder:$PATH"
```

### For Windows

1. Press Windows + S and search for Environment Variables.
2. Click Edit the system environment variables.
3. In the System Properties window, click Environment Variables.
4. Under User variables, select the Path variable and click Edit....
4. Click New and add the folder where thelper.bat is located (e.g., C:\Users\YourUsername\path_to\your_project_folder).
6. Click OK to close all windows.


## Usage

1. Run thelper to setup
```bash
> thelper
```
This will run the setup process for you  to get the API key go to [this link](https://ai.google.dev/gemini-api/docs/api-key).  
Complete the inital setup process

### Arguments


```bash
thelper -h #help command
thelper <your question> #Ask AI about your problem
thelper -i #Initlize setup again
thelper -s #Prints current settings
thelper -e #uses the copied error message and sends it to the Ai
```
