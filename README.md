# Task 1 - Analisis Data CRM dengan PostgreSQL dan Docker

Proyek ini menggunakan Docker untuk menjalankan database PostgreSQL dan skrip ETL Python untuk memuat dan menganalisis data CRM.

## Cara Menjalankan

1.  **Prasyarat:** Pastikan Anda telah menginstal Docker dan Docker Compose.
2.  **Tempatkan Data:** Letakkan file `CRMEvents.csv` dan `CRMCallCenterLogs.csv` di dalam folder `data/`.
3.  **Jalankan Kontainer:** Buka terminal di direktori root `task-1/` dan jalankan perintah:
    ```bash
    docker-compose up --build
    ```
4.  **Verifikasi:** Skrip ETL akan berjalan secara otomatis, memuat data ke database. Anda dapat terhubung ke database di `localhost:5432` menggunakan kredensial di `docker-compose.yml` untuk menjalankan kueri dari `sql/analysis.sql`.


# Task 2 - Dashboard Analisis Pinjaman dengan Plotly Dash

Proyek ini menjalankan aplikasi web interaktif untuk visualisasi data LuxuryLoanPortfolio menggunakan Dash dan Docker.

## Cara Menjalankan

1.  **Prasyarat:** Pastikan Docker dan Docker Compose terinstal.
2.  **Tempatkan Data:** Letakkan `LuxuryLoanPortfolio.csv` di folder `dashboard/data/`.
3.  **Jalankan Aplikasi:** Buka terminal di direktori root `task-2/` dan jalankan:
    ```bash
    docker-compose up --build
    ```
4.  **Akses Dashboard:** Buka browser Anda dan navigasi ke `http://localhost:8050`.

# Task 3 - 5
Link: https://docs.google.com/document/d/1HM4RptSqEH37o_LS57ZmiNpcmuoLLepJqoM8VvGNCFM/edit?usp=sharing