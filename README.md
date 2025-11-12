<<<<<<< HEAD 
##  Project Overview

This project demonstrates a **complete MLOps pipeline** — from data tracking to model versioning — using:

* **FastAPI** for serving the ML model
* **DVC (Data Version Control)** for data and model management
* **Google Cloud Storage (GCS)** as the DVC remote backend
* **GitHub Actions** for CI/CD automation

Your repo structure looks like this:

```
MLOps_CI_CD/
│
├── data/                 # Contains data files (tracked by DVC)
│   ├── data.csv.dvc
│
├── model/                # Contains model artifacts
│   ├── model.joblib.dvc
│
├── src/                  # Your training, evaluation, and API code
│
├── main.py               # FastAPI entry point
│
├── dvc.yaml              # DVC pipeline stages (data → train → evaluate)
├── .dvc/                 # DVC internal cache
├── requirements.txt
├── .github/workflows/    # CI/CD workflows
│   ├── ci.yml
│
└── README.md
```

---

## ⚙️ Step 1: Environment Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/MLOps_CI_CD.git
cd MLOps_CI_CD
```

### 2️⃣ Create and Activate Virtual Environment

```bash
python3 -m venv .env
source .env/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📦 Step 2: Initialize DVC

If it’s your first time setting up locally:

```bash
dvc init
```

This creates the `.dvc/` directory and basic config.

---

## ☁️ Step 3: Connect DVC to Google Cloud Storage (Remote Storage)

### 1️⃣ Authenticate Google Cloud

Make sure you’re logged into your Google Cloud account:

```bash
gcloud auth login
```

### 2️⃣ Verify your active account:

```bash
gcloud auth list
```

If not active, set your account:

```bash
gcloud config set account <your-email>
```

### 3️⃣ Create a GCS bucket (only once):

```bash
gsutil mb -l ASIA-SOUTH1 gs://mlops-dvc-bucket/
```

### 4️⃣ Configure your DVC remote:

```bash
dvc remote add -d myremote gs://mlops-dvc-bucket
```

### 5️⃣ Install Google Cloud support for DVC:

```bash
pip install dvc-gs
```

### 6️⃣ Push your data and model to GCS:

```bash
dvc push
```

✅ This will upload your tracked data (`data.csv`) and model (`model.joblib`) to the GCS bucket.

---

## 🧩 Step 4: GitHub Integration

### 1️⃣ Commit the DVC configuration

```bash
git add .dvc/config data.dvc model.dvc
git commit -m "Configured DVC with Google Cloud remote"
git push origin dev
```

### 2️⃣ Store Google credentials securely

Go to **GitHub → Repository → Settings → Secrets and variables → Actions → New repository secret**
Add the following:

| Secret Name  | Description                                        |
| ------------ | -------------------------------------------------- |
| `GCP_SA_KEY` | Your Google Cloud service account JSON key content |
| `DVC_REMOTE` | The name of your DVC remote (e.g., `myremote`)     |

---

## 🚀 Step 5: Configure GitHub Workflow (CI/CD)

Inside `.github/workflows/ci.yml` — your file should contain:

```yaml
name: CI Pipeline

on:
  push:
    branches:
      - dev
      - main

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repo
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.10"

      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install dvc-gs

      - name: Authenticate GCP
        uses: google-github-actions/auth@v2
        with:
          credentials_json: ${{ secrets.GCP_SA_KEY }}

      - name: Configure DVC Remote
        run: dvc remote default ${{ secrets.DVC_REMOTE }}

      - name: Pull Data and Model from DVC Remote
        run: dvc pull

      - name: Run Tests
        run: pytest tests/

      - name: Run FastAPI (Optional - for test)
        run: uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

---

## 🧠 Step 6: How the Workflow Works

Here’s what happens when you push your code:

| Step                     | Description                                                       |
| ------------------------ | ----------------------------------------------------------------- |
| **Checkout**             | GitHub pulls your repository                                      |
| **Set up Python**        | Installs the right Python version                                 |
| **Install dependencies** | Installs libraries + DVC backend                                  |
| **Authenticate GCP**     | Connects GitHub runner to Google Cloud using your service account |
| **Pull Data/Model**      | Downloads data and model artifacts from GCS                       |
| **Run Tests**            | Executes tests to verify model/data integrity                     |
| **(Optional)**           | Runs FastAPI app if needed                                        |

---

## ✅ Step 7: Common Commands Reference

| Command                      | Description                           |
| ---------------------------- | ------------------------------------- |
| `dvc add data/data.csv`      | Track a new dataset                   |
| `dvc add model/model.joblib` | Track a new model artifact            |
| `dvc push`                   | Push tracked data to remote           |
| `dvc pull`                   | Pull data/model from remote           |
| `dvc status`                 | Check if local and remote are in sync |
| `dvc repro`                  | Run the full ML pipeline              |
| `dvc remote list`            | Show configured remotes               |

---

## 📈 Step 8: When You Add New Data or Model

Every time you retrain the model or update data:

```bash
dvc add data/new_data.csv
dvc add model/new_model.joblib
git add data.dvc model.dvc
git commit -m "Updated data and model"
dvc push
git push origin dev
```

Your workflow will automatically:

* Fetch the latest model/data from GCS
* Re-run tests
* Deploy or validate the build

---



=======
>>>>>>> 5125f68 (Initial setup with CI and tests updated)
