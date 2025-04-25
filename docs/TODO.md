<!-- File: TODO.md -->
# TODO List Proyek THV (True Heart Voice)

## 📋 Prioritas MVP (Q2 2025)
- [🔴 Critical] Backend FastAPI:  
  - [x] Endpoint upload audio & metadata  
  - [x] Integrasi penyimpanan lokal  
  (25 Apr – 29 Apr)
- [🔴 Critical] Frontend Next.js:  
  - Implementasi perekam audio + share link  
  (29 Apr – 1 May)
- [🟠 Important] Auth & Anonimitas:  
  - Magic Link (Auth0) + middleware validasi  
  (1 May – 3 May)
- [🟢 Nice-to-have] Speech-to-text integration  
  (4 May – 6 May)

## 🗓️ Timeline Keseluruhan
- **Apr 2025**  
  - Setup FastAPI, Next.js  
  - Basic UI perekam + upload
- **Mei 2025**  
  - Auth & rate-limiting  
  - CI/CD (GitHub Actions)  
- **Jun 2025**  
  - Monitoring (Sentry/Prometheus)  
  - Testing & dokumentasi akhir

## ✅ Tugas Lainnya
- [ ] HTTPS + CSP di Nginx  
- [ ] Backup & log rotation  
- [ ] Unit/E2E tests  
- [ ] CONTRIBUTING.md & CODE_OF_CONDUCT.md

## 1. Frontend

- [ ] Linting & formatting (ESLint + Prettier)
- [ ] Responsiveness & aksesibilitas dasar (ARIA, keyboard navigation)
- [ ] Env var untuk base-URL back-end

## 2. Back-end (FastAPI)

- [x] Endpoint upload audio & metadata
- [x] Integrasi penyimpanan lokal
- [x] Validasi & pydantic schemas untuk request/response
- [x] Rate-limiting (fastapi-throttle) agar anon link tidak disalahgunakan (5 req per 60 detik)
- [ ] Swagger & ReDoc otomatis (default FastAPI, pastikan security scheme ditambah bila pakai Auth)
- [x] Unit-test dengan PyTest

## 3. Storage & Media

- [x] Persiapkan direktori lokal `uploads/` untuk menyimpan file audio  
- [x] Implementasi penyimpanan file audio di disk pada service FastAPI  
- [o] Script cron / background task untuk cleanup file lama (>3 hari)  
- [x] Env var untuk path direktori penyimpanan audio

## 4. DevOps

- [x] Environment variables (.env + python-dotenv)
- [x] Backup rutin DB 
- [x] Log rotation di VM (logrotate)
- [x] Health-check endpoint + systemd watchdog untuk FastAPI service

## 5. Security & Compliance

- [ ] HTTPS redirect enforcement
- [ ] Content-Security-Policy header di Nginx
- [ ] GDPR / kebijakan privasi (karena data suara)

## 6. Monitoring

- [ ] Alerting (Grafana/Prometheus alertmanager atau Azure Monitor)
- [ ] Uptime Robot / StatusCake sederhana

## 7. Testing

- [ ] Integration test (FastAPI TestClient)
- [ ] Front-end E2E (Playwright/Cypress)
- [ ] Load test ringan (k6)

## 8. Dokumentasi & Project Hygiene

- [ ] CONTRIBUTING.md & CODE_OF_CONDUCT.md
- [ ] Versi API & changelog (keep-a-changelog)
- [ ] Update README badges (build status, license)