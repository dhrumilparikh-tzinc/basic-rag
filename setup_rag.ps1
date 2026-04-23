$python = ".\.venv\Scripts\python.exe"
$psql = "C:\Program Files\PostgreSQL\18\bin\psql.exe"
$envFile = ".\.env"

Write-Host "STEP 1: Checking virtual environment" -ForegroundColor Cyan
if (-not (Test-Path $python)) {
    Write-Host "STEP 1 ERROR: .venv\Scripts\python.exe was not found." -ForegroundColor Red
    exit 1
}
Write-Host "STEP 1 SUCCESS: Virtual environment found" -ForegroundColor Green

Write-Host "`nSTEP 2: Checking .env file" -ForegroundColor Cyan
if (-not (Test-Path $envFile)) {
    Write-Host "STEP 2 ERROR: .env not found. Copy .env.example to .env and fill in real values first." -ForegroundColor Red
    exit 1
}
Write-Host "STEP 2 SUCCESS: .env file found" -ForegroundColor Green

Write-Host "`nSTEP 3: Checking psql" -ForegroundColor Cyan
if (-not (Test-Path $psql)) {
    Write-Host "STEP 3 ERROR: psql.exe not found at $psql" -ForegroundColor Red
    exit 1
}
Write-Host "STEP 3 SUCCESS: psql found" -ForegroundColor Green

Write-Host "`nSTEP 4: Creating PostgreSQL database if needed" -ForegroundColor Cyan
& $psql -U postgres -c "CREATE DATABASE basic_rag;" 2>&1
if ($LASTEXITCODE -eq 0) {
    Write-Host "STEP 4 SUCCESS: Database created" -ForegroundColor Green
} else {
    Write-Host "STEP 4 INFO: Database may already exist or authentication may be required" -ForegroundColor Yellow
}

Write-Host "`nSTEP 5: Initializing tables" -ForegroundColor Cyan
& $python -m scripts.init_db
if ($LASTEXITCODE -eq 0) {
    Write-Host "STEP 5 SUCCESS: Database initialized" -ForegroundColor Green
} else {
    Write-Host "STEP 5 ERROR: Database initialization failed" -ForegroundColor Red
}

Write-Host "`nSTEP 6: Building FAISS index" -ForegroundColor Cyan
& $python -m scripts.build_index
if ($LASTEXITCODE -eq 0) {
    Write-Host "STEP 6 SUCCESS: FAISS index built" -ForegroundColor Green
} else {
    Write-Host "STEP 6 ERROR: FAISS build failed" -ForegroundColor Red
}

Write-Host "`nSTEP 7: Run the app manually with .\.venv\Scripts\python.exe app.py" -ForegroundColor Cyan
