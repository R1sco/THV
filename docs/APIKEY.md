# Dokumentasi API Key

Aplikasi THV (True Heart Voice) menggunakan API Key untuk mengamankan endpoint. Berikut panduan penggunaan:

## 1. Mendapatkan API Key
API Key dihasilkan saat konfigurasi pertama dan disimpan di file `.env`:

```dotenv
API_KEY=(Buat random key)
```

## 2. Header yang Digunakan
Setiap request ke endpoint yang dilindungi perlu menyertakan header:

```
X-API-Key: <API_KEY>
```

## 3. Menggunakan di Swagger UI
1. Buka `/docs` di browser
2. Klik tombol **Authorize**
3. Masukkan API Key di field `X-API-Key` dan klik **Authorize**
4. Tes endpoint seperti biasa

## 4. Contoh Menggunakan curl
```bash
curl -X POST http://localhost:8000/api/upload \
  -H "X-API-Key: <API_KEY>" \
  -F "file=@/path/to/audio.mp3"
```

## 5. Contoh Menggunakan Postman
- Tambahkan header:
  - **Key**: `X-API-Key`
  - **Value**: `<API_KEY>`
- Pilih method `POST` dan URL `http://localhost:8000/api/upload`
- Di tab **Body**, pilih `form-data` dan field `file` untuk upload

## 6. Tips Keamanan
- Simpan API Key dengan aman, jangan di-commit ke repositori
- Gunakan HTTPS di produksi
- Ganti API Key secara berkala jika diperlukan