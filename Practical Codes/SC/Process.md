
# macOS / Linux

## 1) Select the correct Python interpreter in VS Code

1. Open Command Palette: `Cmd+Shift+P`
2. Run: `Python: Select Interpreter`
3. Pick the interpreter for your project (ideally the one inside your virtual environment, e.g., `.../venv/bin/python`).

## 2) (Optional but recommended) Create and activate a virtual environment

```bash
# In your project folder
python3 -m venv venv
source venv/bin/activate
```

Verify the prompt shows `(venv)`.

## 3) Install required packages in that interpreter/env

```bash
pip install numpy matplotlib scikit-learn
pip install torch torchvision torchaudio
pip install scikit-fuzzy
pip install --upgrade pip

```

## 4) Verify installs

```bash
python -m pip show numpy matplotlib scikit-learn
```

## 5) Test imports

```bash
python -c "import numpy, matplotlib, sklearn; print('All imports OK!')"
```

## 6) If warnings persist in VS Code

* Re-run `Python: Select Interpreter` and choose the `venv` path.
* Reload window: `Cmd+Shift+P` → `Developer: Reload Window`.
* Ensure the workspace setting isn’t overriding the interpreter:

  * `.vscode/settings.json` should not point to a different Python path.

---

# Windows

## 1) Select the correct Python interpreter in VS Code

1. Open Command Palette: `Ctrl+Shift+P`
2. Run: `Python: Select Interpreter`
3. Choose your project interpreter (ideally the one in `venv\Scripts\python.exe`).

## 2) (Optional but recommended) Create and activate a virtual environment

```powershell
# In your project folder (PowerShell)
python -m venv venv
venv\Scripts\activate
```

You should see `(venv)` in the prompt.

## 3) Install required packages

```powershell
pip install numpy matplotlib scikit-learn
```

## 4) Verify installs

```powershell
python -m pip show numpy matplotlib scikit-learn
```

## 5) Test imports

```powershell
python -c "import numpy, matplotlib, sklearn; print('All imports OK!')"
```

## 6) If warnings persist in VS Code

* Re-run `Python: Select Interpreter` and pick `.\venv\Scripts\python.exe`.
* Reload window: `Ctrl+Shift+P` → `Developer: Reload Window`.
* Check `.vscode\settings.json` for an incorrect `python.defaultInterpreterPath` or `python.pythonPath`.

Got it 👍 — on **Windows**, if you sometimes get **execution / module / permission errors** while running `torch`, `torchvision`, or `skfuzzy` in VS Code or CMD, here’s a **complete set of commands and fixes** you can safely use.


## **7) Fix “execution policy” errors (PowerShell)**

If you get something like

> “Execution of scripts is disabled on this system”

Run PowerShell **as Administrator** and execute:

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then restart VS Code or your terminal.

---