# XD Token Cracker

This is a tool for checking the validity of Telegram API tokens. It can be used to verify if a given Telegram bot token is correct and active.


## Features

1. *Check the validity of a Telegram bot token*
2. *Simple and easy-to-use command-line interface*
3. *Ability to check tokens from inside the file*
3. *Registers the correct tokens in a file*
4. *Provide feedback on whether the token is valid or invalid*


## Installation

To use this tool, you'll need to have Python 3 installed on your system. You can then install the required dependencies using pip:
```
pip install -r requirements.txt
```


## Usage

1. First, we run the script file:
```
python XD_TC.py
```

2. We select the crack part

3. Now we execute our command


## Input parameters for the command:

1. t_in  : Name of the file containing the token list (*txt format*) 
1. t_out : Name of the output file for valid tokens (*txt format*)


## Example

```
t_in=tokenlist.txt-t_out=output.txt
```
This command tells the tool that you have a file named tokenlist.txt containing the token list, and the output will be a file named output.txt created automatically.

<span style="color:red">Remember to separate parameters with (-)</span>


## Developers

- [Hojjat Jahanpour](https://github.com/hojjatjh)
- [XD Team](https://github.com/XD-tm)



## License

This project is licensed under the MIT License.
