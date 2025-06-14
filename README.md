# Staples
Staples is a esoteric language that consists of four characters. This language is built on top of Python, and obfuscates it. Its syntax is binary text, except the hard bracket is zero and the curly bracket is one (facing right). Also, a checksum is required. This is done by copying the the code, reversing it, and making it the opposite bracket (facing left).

## Quickstart
Staples can be installed using this command (Python 3.11 is required, so if you don't have it installed, install it [here](https://www.python.org/ftp/python/3.13.5/python-3.13.5-macos11.pkg). Also, you want to run this in a ZSH terminal):
```
pip3 install staples_lang
echo 'export PATH="/Library/Frameworks/Python.framework/Versions/3.13/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```
Staples can be used using a variety of self-explanatory commands:
```
staples runfile <file_path>
```
```
staples compilefile <file_path>
```
```
staples runstring <staples_code_as_a_string>
```
```
staples compilestring <python_code_as_a_string>
```
In case you don't understand, running the file runs Staples code and compiling converts Python to Staples.
Here's an example of Staples: [https://raw.githubusercontent.com/SeafoodStudios/Staples/refs/heads/main/examples/dodge.py.staples](https://raw.githubusercontent.com/SeafoodStudios/Staples/refs/heads/main/examples/dodge.py.staples)

<img width="200" alt="OutputExample" src="https://github.com/user-attachments/assets/d06bf9ec-d659-4a68-a575-3fd1fb0f22b5" />
[<img width="500" alt="CodeExample" src="https://github.com/user-attachments/assets/1c087de8-03f7-4151-8f77-cad8452a32f7" />
](https://raw.githubusercontent.com/SeafoodStudios/Staples/refs/heads/main/examples/dodge.py.staples)

## Thanks!
Please don't run any untrusted Staples code. Thanks for using Staples!
