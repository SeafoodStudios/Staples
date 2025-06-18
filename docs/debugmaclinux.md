# If Staples is not working on a MacOS or Linux, follow these steps.
1. You may not have Python 3.11 installed. To fix this, run this command (fill in your path).

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
2. Run this command to ensure Staples works.
```
staples runstring "[{{{[[[[[{{{[[{[[{{[{[[{[{{[{{{[[{{{[{[[[[{[{[[[[[{[[[{[[{[{[[{{[{{{[{[[[{{[[[[{[{{{[[[[[{{[{{[[[{{[[{[{[{{{[[{{[[{[[[[[[{[{[{{{[{{[{{{{[{{{[[{[[{{[{[{{[{{{[[{{[[{[[[[{[[{[[[{[[[{[{[[{}]]}]}]]]}]]]}]]}]]]]}]]}}]]}}}]}}]}]}}]]}]]}}}]}}}}]}}]}}}]}]}]]]]]]}]]}}]]}}}]}]}]]}}]]]}}]}}]]]]]}}}]}]]]]}}]]]}]}}}]}}]]}]}]]}]]]}]]]]]}]}]]]]}]}}}]]}}}]}}]}]]}]}}]]}]]}}}]]]]]}}}]"
```
If it prints "Staples Works!" or something like that, your fine!
