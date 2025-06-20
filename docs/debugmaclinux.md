# If Staples is not working on a MacOS or Linux, follow these steps.
Please note that there is a chance it is working, even if it throws an error. You can confirm it by running this command to ensure Staples works. If it prints "Staples Works!" or something like that, your fine!
> [!TIP]
> Our PIP package is called "staples_lang", so beware of typosquatting!
```
staples runstring "[{{{[[[[[{{{[[{[[{{[{[[{[{{[{{{[[{{{[{[[[[{[{[[[[[{[[[{[[{[{[[{{[{{{[{[[[{{[[[[{[{{{[[[[[{{[{{[[[{{[[{[{[{{{[[{{[[{[[[[[[{[{[{{{[{{[{{{{[{{{[[{[[{{[{[{{[{{{[[{{[[{[[[[{[[{[[[{[[[{[{[[{}]]}]}]]]}]]]}]]}]]]]}]]}}]]}}}]}}]}]}}]]}]]}}}]}}}}]}}]}}}]}]}]]]]]]}]]}}]]}}}]}]}]]}}]]]}}]}}]]]]]}}}]}]]]]}}]]]}]}}}]}}]]}]}]]}]]]}]]]]]}]}]]]]}]}}}]]}}}]}}]}]]}]}}]]}]]}}}]]]]]}}}]"
```
1. You may not have a "zshrc" file, so please run this again:
```
pip3 install --user staples_lang --upgrade && \
if ! grep -qxF 'export PATH="$HOME/Library/Python/3.11/bin:$HOME/.local/bin:/Library/Frameworks/Python.framework/Versions/3.11/bin:/usr/local/bin:/opt/homebrew/bin:/usr/bin:$PATH"' ~/.zshrc; then \
  echo 'export PATH="$HOME/Library/Python/3.11/bin:$HOME/.local/bin:/Library/Frameworks/Python.framework/Versions/3.11/bin:/usr/local/bin:/opt/homebrew/bin:/usr/bin:$PATH"' >> ~/.zshrc; \
fi && source ~/.zshrc
```
2. If you are still experiencing issues, you may not have Python 3.11 installed. To fix this, you can either run this command (fill in your path) or [follow the instructions](https://github.com/SeafoodStudios/Staples) on the main page carefully, because it provides a Python installation link (if you scroll to the bottom of the provided Python page; it may be hidden).

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
