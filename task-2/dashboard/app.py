import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Inisialisasi aplikasi Dash
app = dash.Dash(__name__)
server = app.server

# --- Memuat dan Membersihkan Data ---
df = pd.read_csv('data/LuxuryLoanPortfolio.csv')

# Konversi kolom ke tipe numerik, menangani error dengan mengubahnya menjadi NaN
numeric_cols = ['funded_amount', 'property value', 'interest rate percent', 'payments']
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Hapus baris dengan data numerik yang kosong untuk analisis
df.dropna(subset=numeric_cols, inplace=True)

# --- Membuat Visualisasi ---

# 1. Bar Chart: Rata-rata Suku Bunga Berdasarkan Durasi Pinjaman
df_interest_by_duration = df.groupby('duration years')['interest rate percent'].mean().reset_index()
fig_bar = px.bar(
    df_interest_by_duration,
    x='duration years',
    y='interest rate percent',
    title='Rata-rata Suku Bunga vs. Durasi Pinjaman',
    labels={'duration years': 'Durasi (Tahun)', 'interest rate percent': 'Rata-rata Suku Bunga (%)'}
)

# 2. Scatter Plot: Nilai Properti vs. Jumlah Pinjaman
fig_scatter = px.scatter(
    df,
    x='property value',
    y='funded_amount',
    title='Nilai Properti vs. Jumlah Pinjaman',
    labels={'property value': 'Nilai Properti ($)', 'funded_amount': 'Jumlah Pinjaman ($)'},
    hover_data=['firstname', 'lastname']
)

# 3. Histogram: Distribusi Jumlah Pinjaman
fig_hist = px.histogram(
    df,
    x='funded_amount',
    title='Distribusi Jumlah Pinjaman',
    labels={'funded_amount': 'Jumlah Pinjaman ($)'},
    nbins=50
)

# --- Mendefinisikan Layout Aplikasi ---
app.layout = html.Div(children=[
    html.H1(children='Dashboard Analisis Luxury Loan Portfolio'),

    dcc.Graph(
        id='interest-rate-by-duration-chart',
        figure=fig_bar
    ),

    dcc.Graph(
        id='property-vs-funded-chart',
        figure=fig_scatter
    ),

    dcc.Graph(
        id='funded-amount-distribution-chart',
        figure=fig_hist
    )
])

if __name__ == '__main__':
    # '0.0.0.0' agar bisa diakses dari luar kontainer
    app.run(debug=True, host='0.0.0.0', port=8050)