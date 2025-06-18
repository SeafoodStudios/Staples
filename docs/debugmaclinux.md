# If Staples is not working on a MacOS or Linux, follow these steps.
1. You may not have a "zshrc" file, so please run this again:
```
pip3 install --user staples_lang --upgrade && \
if ! grep -qxF 'export PATH="$HOME/Library/Python/3.11/bin:$HOME/.local/bin:/Library/Frameworks/Python.framework/Versions/3.11/bin:/usr/local/bin:/opt/homebrew/bin:/usr/bin:$PATH"' ~/.zshrc; then \
  echo 'export PATH="$HOME/Library/Python/3.11/bin:$HOME/.local/bin:/Library/Frameworks/Python.framework/Versions/3.11/bin:/usr/local/bin:/opt/homebrew/bin:/usr/bin:$PATH"' >> ~/.zshrc; \
fi && source ~/.zshrc
```
2. You may not have Python 3.11 installed. To fix this, you can either run this command (fill in your path) or [download Python 3.11](https://www.python.org/downloads/release/python-3111/).

For MacOS:
```
echo 'export PATH="$HOME/Library/Python/3.13/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```
For Linux:
```
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```
3. Run this command to ensure Staples works.
```
staples runstring "[{{{[[[[[{{{[[{[[{{[{[[{[{{[{{{[[{{{[{[[[[{[{[[[[[{[[[{[[{[{[[{{[{{{[{[[[{{[[[[{[{{{[[[[[{{[{{[[[{{[[{[{[{{{[[{{[[{[[[[[[{[{[{{{[{{[{{{{[{{{[[{[[{{[{[{{[{{{[[{{[[{[[[[{[[{[[[{[[[{[{[[{}]]}]}]]]}]]]}]]}]]]]}]]}}]]}}}]}}]}]}}]]}]]}}}]}}}}]}}]}}}]}]}]]]]]]}]]}}]]}}}]}]}]]}}]]]}}]}}]]]]]}}}]}]]]]}}]]]}]}}}]}}]]}]}]]}]]]}]]]]]}]}]]]]}]}}}]]}}}]}}]}]]}]}}]]}]]}}}]]]]]}}}]"
```
If it prints "Staples Works!" or something like that, your fine! If it still does not work, please debug with an AI.
