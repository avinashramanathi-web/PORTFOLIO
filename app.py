from flask import Flask, render_template, send_from_directory, request, jsonify
import os

app = Flask(__name__)

# ── All downloadable files ──────────────────────────────────────────
FILES = {
    "resume":                  ("resume.pdf",                   "Ramanathi_Avinash_Resume.pdf"),
    "intern_techoctanet":      ("intern_techoctanet.pdf",       "TechOctaNet_Python_Internship.pdf"),
    "intern_ecotech":          ("intern_ecotech.pdf",           "Ecotech_FullStack_Internship.pdf"),
    "intern_codtech":          ("intern_codtech.pdf",           "Codtech_AI_Internship.pdf"),
    "cert_tcs_ion":            ("cert_tcs_ion.pdf",             "TCS_ION_IT_Primer_Certificate.pdf"),
    "cert_powerbi":            ("cert_powerbi.pdf",             "PowerBI_UniAthena_Certificate.pdf"),
    "cert_codtech":            ("cert_codtech.pdf",             "Codtech_Certificate.pdf"),
    "cert_guvi_hcl":           ("cert_guvi_hcl.jpg",           "GUVI_HCL_UIUX_Certificate.jpg"),
    "cert_skillected_reactjs": ("cert_skillected_reactjs.png",  "SkillEcted_ReactJS_Certificate.png"),
    "cert_skillected_movie":   ("cert_skillected_movie.png",    "SkillEcted_MovieApp_Certificate.png"),
    "cert_skillected_fullstack":("cert_skillected_fullstack.png","SkillEcted_FullStack_Certificate.png"),
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/download/<key>")
def download(key):
    if key not in FILES:
        return jsonify({"error": "File not found"}), 404
    filename, download_name = FILES[key]
    return send_from_directory(
        os.path.join(app.root_path, "static", "files"),
        filename,
        as_attachment=True,
        download_name=download_name
    )

@app.route("/contact", methods=["POST"])
def contact():
    data = request.get_json()
    name    = data.get("name", "").strip()
    email   = data.get("email", "").strip()
    mobile  = data.get("mobile", "").strip()
    subject = data.get("subject", "").strip()
    message = data.get("message", "").strip()

    if not all([name, email, message]):
        return jsonify({"success": False, "error": "Name, email and message are required."}), 400

    print(f"\n New Contact Message")
    print(f"   From   : {name} <{email}>")
    print(f"   Mobile : {mobile}")
    print(f"   Subject: {subject}")
    print(f"   Message: {message}\n")

    return jsonify({"success": True, "message": "Message received! I'll get back to you soon."})

if __name__ == "__main__":
    print("\n Portfolio running at: http://localhost:5000\n")
    app.run(debug=True, port=5000)
