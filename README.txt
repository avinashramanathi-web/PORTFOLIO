# Ramanathi Avinash — Portfolio
## HOW TO RUN IN VISUAL STUDIO CODE (STEP BY STEP)

==============================================
STEP 1 — EXTRACT THE ZIP
==============================================
1. Right-click "portfolio2.zip"
2. Click "Extract All"
3. Choose your Desktop
4. Click "Extract"
You will see a folder called "portfolio2" on Desktop.

==============================================
STEP 2 — OPEN IN VS CODE
==============================================
1. Open Visual Studio Code
2. Click "File" in top menu
3. Click "Open Folder"
4. Go to Desktop → Select "portfolio2" folder
5. Click "Select Folder"
You will see all files on the left side panel.

==============================================
STEP 3 — OPEN THE TERMINAL IN VS CODE
==============================================
1. In VS Code, click "Terminal" in the top menu
2. Click "New Terminal"
A black panel will open at the bottom of VS Code.

==============================================
STEP 4 — INSTALL FLASK (only once)
==============================================
In the terminal, type this and press Enter:

    pip install flask

Wait for it to finish. You will see "Successfully installed flask".

==============================================
STEP 5 — RUN THE WEBSITE
==============================================
In the terminal, type this and press Enter:

    python app.py

You will see this message:
    Portfolio running at: http://localhost:5000

==============================================
STEP 6 — OPEN IN BROWSER
==============================================
1. Open Google Chrome
2. In the address bar, type:
       http://localhost:5000
3. Press Enter
Your portfolio website will open!

==============================================
STEP 7 — STOP THE SERVER
==============================================
When you want to stop, go back to VS Code terminal
and press:  Ctrl + C

==============================================
EVERY TIME YOU WANT TO OPEN YOUR PORTFOLIO:
==============================================
1. Open VS Code
2. Open Terminal (Terminal → New Terminal)
3. Type:  python app.py
4. Open Chrome → http://localhost:5000

==============================================
FOLDER STRUCTURE:
==============================================
portfolio2/
├── app.py                    ← Python Flask backend
├── README.txt                ← This file
├── templates/
│   └── index.html            ← Your website
└── static/
    └── files/
        ├── profile.png       ← Your photo
        ├── resume.pdf        ← Your CV
        ├── intern_*.pdf      ← Internship certificates
        └── cert_*.pdf/png    ← Course certificates

==============================================
IF YOU SEE ANY ERROR:
==============================================
Error: "pip is not recognized"
→ Try: py -m pip install flask

Error: "python is not recognized"
→ Try: py app.py

Error: "Address already in use"
→ Close other terminals and try again
