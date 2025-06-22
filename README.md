# Staples
Staples is an esoteric language that consists of four characters. This language is built on top of Python, and obfuscates it. Its syntax is binary text, except the hard bracket is zero and the curly bracket is one (facing right). Also, a checksum is required. This is done by copying the the code, reversing it, and making it the opposite bracket (facing left).

## Quickstart
Staples can be installed using this command (**Python 3.11 is required**, so if you don't have it installed, install it [here](https://www.python.org/downloads/release/python-3111/).):

For MacOS (You want to run this in a ZSH terminal. If Staples is not running, debug with [these instructions](https://github.com/SeafoodStudios/Staples/blob/main/docs/debugmaclinux.md).):
```
pip3 install --user staples_lang --upgrade && \
if ! grep -qxF 'export PATH="$HOME/Library/Python/3.11/bin:$HOME/.local/bin:/Library/Frameworks/Python.framework/Versions/3.11/bin:/usr/local/bin:/opt/homebrew/bin:/usr/bin:$PATH"' ~/.zshrc; then \
  echo 'export PATH="$HOME/Library/Python/3.11/bin:$HOME/.local/bin:/Library/Frameworks/Python.framework/Versions/3.11/bin:/usr/local/bin:/opt/homebrew/bin:/usr/bin:$PATH"' >> ~/.zshrc; \
fi && source ~/.zshrc
```
For Linux (really simple.):
```
pip3 install staples_lang
```
For Windows (Not tested, but should work.):
```
pip3 install staples_lang; 
$p='C:\Python311\Scripts'; 
if (Test-Path $p) { 
  if (-not ($env:Path.Split(';') -contains $p)) { 
    [Environment]::SetEnvironmentVariable('Path', $env:Path + ';' + $p, 'User'); 
    Write-Output "Added $p to User PATH. Restart your terminal." 
  } else { 
    Write-Output "$p is already in PATH." 
  } 
} else { 
  Write-Output "$p does not exist." 
}
```
For occasional updating of Staples, use this command (it should work for Windows, Linux and MacOS):
```
pip3 install staples_lang --upgrade
```
An average Staples string looks like this (Notice the comments, which will not throw syntax errors, and will be ignored. Anything that is not in the standard Staples syntax is considered a comment.):
```
[{{{#you can have a comment here#[[[[[{{{[[{[[{{[{[[{[{{[{{{[[{{{[{[[[[{[{[[[[[{[[[{[[{[[{[[[[{{[[{[{[{{[{{[[[{{[{{[[[{{[{{{{[[{[[[[[[{[{[{{{[{{[{{{{[{{{[[{[[{{[{{[[[{{[[{[[[[{[[[[{[[{[[[{[[[{[{[[{}]]}]}]]]}]]#or here#]}]]}]]]]}]]]]}]]}}]]]}}]}}]]}]]}}}]}}}}]#everywhere!#}}]}}}]}]}]]]]]]}]]}}}}]}}]]]}}]}}]]]}}]}}]}]}]]}}]]]]}]]}]]}]]]}]]]]]}]}]]]]}]}}}]]}}}]}}]}]]}]}}]]}]]}}}]]]]]}}}]
```
Staples can be used using a variety of self-explanatory commands (A common syntax error is when you include an extra space, because the interpreter cannot read that.):

Runfile runs the file path (the file has to be raw Staples code) you provided.
```
staples runfile '/Desktop/file.py.staples/'
```
Compilefile reads the Python file path you provide and creates a new file that ends with ".staples" that contains the raw Staples code.
```
staples compilefile '/Desktop/file.py/'
```
Runstring straight up runs the Staples code string you provide.
```
staples runstring '[{{{[[[[[{{{[[{[[{{[{[[{[{{[{{{[[{{{[{[[[[{[{[[[[[{[[[{[[{[[{[[[[{{[[{[{[{{[{{[[[{{[{{[[[{{[{{{{[[{[[[[[[{[{[{{{[{{[{{{{[{{{[[{[[{{[{{[[[{{[[{[[[[{[[[[{[[{[[[{[[[{[{[[{}]]}]}]]]}]]]}]]}]]]]}]]]]}]]}}]]]}}]}}]]}]]}}}]}}}}]}}]}}}]}]}]]]]]]}]]}}}}]}}]]]}}]}}]]]}}]}}]}]}]]}}]]]]}]]}]]}]]]}]]]]]}]}]]]]}]}}}]]}}}]}}]}]]}]}}]]}]]}}}]]]]]}}}]'
```
Compilestring takes the Python code you input as a string, converts it to raw Staples code and prints it.
```
staples compilestring 'print("Hello World!")'
```
Running this command opens the Staples shell. Please keep in mind that the larger the string, the less likely the shell will run it due to shell issues. To prevent this, please run your commands using the "staples runstring" command outside of the shell, because the shell is mainly for testing purposes.
```
staples
```

## Resources

Here are some Staples examples: 

[Dodge Game Code](https://raw.githubusercontent.com/SeafoodStudios/Staples/refs/heads/main/examples/dodge.py.staples)

[Snake Game Code](https://raw.githubusercontent.com/SeafoodStudios/Staples/refs/heads/main/examples/snake.py.staples)

[Fibonacci Sequence Code](https://raw.githubusercontent.com/SeafoodStudios/Staples/refs/heads/main/examples/fibonacci.py.staples)


<img width="200" alt="OutputExample1" src="https://github.com/user-attachments/assets/d06bf9ec-d659-4a68-a575-3fd1fb0f22b5" />

<img width="200" alt="OutputExample2" src="https://github.com/user-attachments/assets/50107c92-e983-4cb0-84a1-2adf204b8e6e" />

<img width="500" alt="OutputExample3" src="https://github.com/user-attachments/assets/69762ed9-4e38-416a-8de0-04018fa48feb" />

Here is a syntax dictionary to ensure ease of use (Paste it into a TXT file, if you want.):

[Syntax Dictionary Link](https://raw.githubusercontent.com/SeafoodStudios/Staples/refs/heads/main/static/staples_dictionary.txt)

## Thanks!
**Please don't run any untrusted Staples code.** Staples is also Turing complete. You can have proof [here](https://raw.githubusercontent.com/SeafoodStudios/Staples/refs/heads/main/static/proof-of-turing-completeness.staples). Thanks for using Staples!

You can also find Staples on [Esolangs.org](https://esolangs.org/wiki/Staples).
