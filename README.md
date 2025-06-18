# Staples
Staples is a esoteric language that consists of four characters. This language is built on top of Python, and obfuscates it. Its syntax is binary text, except the hard bracket is zero and the curly bracket is one (facing right). Also, a checksum is required. This is done by copying the the code, reversing it, and making it the opposite bracket (facing left).

## Quickstart
Staples can be installed using this command (**Python 3.11 is required**, so if you don't have it installed, install it [here](https://www.python.org/downloads/).):

For MacOS and Linux (You want to run this in a ZSH terminal):
```
pip3 install staples_lang && if [ -d "/Library/Frameworks/Python.framework/Versions/3.13/bin" ]; then grep -qxF 'export PATH="/Library/Frameworks/Python.framework/Versions/3.13/bin:$PATH"' ~/.zshrc || echo 'export PATH="/Library/Frameworks/Python.framework/Versions/3.13/bin:$PATH"' >> ~/.zshrc && source ~/.zshrc; fi
```
For Windows (Not tested, but should work.):
```
pip3 install staples_lang; $p='C:\Python313\Scripts'; if (Test-Path $p) { if (-not ($env:Path.Split(';') -contains $p)) { [Environment]::SetEnvironmentVariable('Path', $env:Path + ';' + $p, 'User'); Write-Output "Added $p to User PATH. Restart your terminal." } else { Write-Output "$p is already in PATH." } } else { Write-Output "$p does not exist." }
```
To update Staples, use this command (should work for MacOS, Linux and Windows):
```
pip3 install staples_lang --upgrade
```
Staples can be used using a variety of self-explanatory commands (A common syntax error is when you include an extra space, because the interpreter cannot read that.):
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

## Resources

Here are some Staples examples: 

[Dodge Game Code](https://raw.githubusercontent.com/SeafoodStudios/Staples/refs/heads/main/examples/dodge.py.staples)

[Snake Game Code](https://raw.githubusercontent.com/SeafoodStudios/Staples/refs/heads/main/examples/snake.py.staples)

[Fibonacci Sequence Code](https://raw.githubusercontent.com/SeafoodStudios/Staples/refs/heads/main/examples/fibonacci.py.staples)


<img width="200" alt="OutputExample1" src="https://github.com/user-attachments/assets/d06bf9ec-d659-4a68-a575-3fd1fb0f22b5" />

<img width="200" alt="OutputExample2" src="https://github.com/user-attachments/assets/50107c92-e983-4cb0-84a1-2adf204b8e6e" />


Here is a syntax dictionary to ensure ease of use (Paste it into a TXT file, if you want.):

[Syntax Dictionary Link](https://raw.githubusercontent.com/SeafoodStudios/Staples/refs/heads/main/static/staples_dictionary.txt)

## Thanks!
**Please don't run any untrusted Staples code.** Thanks for using Staples!

You can also find Staples on [Esolangs.org](https://esolangs.org/wiki/Staples).
