import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
day_df = pd.read_csv("day.csv")
hour_df = pd.read_csv("hour.csv")

# Preprocessing
day_df['dteday'] = pd.to_datetime(day_df['dteday'])
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])
day_df['season'] = day_df['season'].astype('category')
day_df['weathersit'] = day_df['weathersit'].astype('category')

# Set title for the dashboard
st.title("🚴‍♂️ Dashboard Analisis Penyewaan Sepeda")
st.subheader("Analisis Data Penyewaan Sepeda Berdasarkan Faktor Cuaca dan Waktu")

# Sidebar for navigation
st.sidebar.title("Navigasi")
page = st.sidebar.radio("Pilih Halaman:", ["🔍 Exploratory Data Analysis", "🌤️ Analisis Cuaca", "📈 Pola Penyewaan", "📚 Kesimpulan"])

# Page: Exploratory Data Analysis
if page == "🔍 Exploratory Data Analysis":
    st.header("🔍 Exploratory Data Analysis")
    st.write("Bagian ini menampilkan analisis awal data untuk memahami karakteristik dataset harian (day_df) dan per jam (hour_df).")

    # Statistik Deskriptif - day_df
    st.subheader("Statistik Deskriptif - Dataset Harian (day_df)")
    st.write("Ringkasan statistik untuk variabel utama dalam dataset harian:")
    st.write(day_df[['temp', 'hum', 'windspeed', 'cnt']].describe())

    # Statistik Deskriptif - hour_df
    st.subheader("Statistik Deskriptif - Dataset Per Jam (hour_df)")
    st.write("Ringkasan statistik untuk variabel utama dalam dataset per jam:")
    st.write(hour_df[['temp', 'hum', 'windspeed', 'cnt']].describe())

    # Distribusi Jumlah Penyewaan - day_df
    st.subheader("Distribusi Jumlah Penyewaan - Dataset Harian")
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    sns.histplot(day_df['cnt'], bins=30, kde=True, ax=ax1)
    ax1.set_title('Distribusi Jumlah Penyewaan Sepeda (Harian)', fontsize=14)
    ax1.set_xlabel('Jumlah Penyewaan', fontsize=12)
    ax1.set_ylabel('Frekuensi', fontsize=12)
    st.pyplot(fig1)

    # Distribusi Jumlah Penyewaan - hour_df
    st.subheader("Distribusi Jumlah Penyewaan - Dataset Per Jam")
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    sns.histplot(hour_df['cnt'], bins=30, kde=True, ax=ax2)
    ax2.set_title('Distribusi Jumlah Penyewaan Sepeda (Per Jam)', fontsize=14)
    ax2.set_xlabel('Jumlah Penyewaan', fontsize=12)
    ax2.set_ylabel('Frekuensi', fontsize=12)
    st.pyplot(fig2)

# Page: Analisis Cuaca
elif page == "🌤️ Analisis Cuaca":
    st.header("Analisis Pengaruh Faktor Cuaca terhadap Penyewaan Sepeda")
    
    # Tabel rata-rata penyewaan berdasarkan kondisi cuaca
    st.subheader("Tabel Rata-rata Penyewaan Berdasarkan Kondisi Cuaca")
    weather_avg = day_df.groupby('weathersit')['cnt'].mean().reset_index()
    weather_avg.columns = ['Kondisi Cuaca (1=Cerah, 2=Berkabut, 3=Hujan)', 'Rata-rata Penyewaan']
    st.write(weather_avg)

    # Scatter plot suhu vs jumlah penyewaan
    st.subheader("Hubungan Suhu terhadap Penyewaan Sepeda")
    fig3, ax3 = plt.subplots(figsize=(10, 6))
    sns.regplot(data=day_df, x='temp', y='cnt', scatter_kws={'alpha':0.5}, line_kws={'color':'red'}, ax=ax3)
    ax3.set_title('Hubungan Suhu terhadap Penyewaan Sepeda', fontsize=14)
    ax3.set_xlabel('Suhu (Normalisasi)', fontsize=12)
    ax3.set_ylabel('Jumlah Penyewaan', fontsize=12)
    st.pyplot(fig3)

    # Scatter plot kelembaban vs jumlah penyewaan
    st.subheader("Hubungan Kelembaban terhadap Penyewaan Sepeda")
    fig4, ax4 = plt.subplots(figsize=(10, 6))
    sns.regplot(data=day_df, x='hum', y='cnt', scatter_kws={'alpha':0.5}, line_kws={'color':'blue'}, ax=ax4)
    ax4.set_title('Hubungan Kelembaban terhadap Penyewaan Sepeda', fontsize=14)
    ax4.set_xlabel('Kelembaban (Normalisasi)', fontsize=12)
    ax4.set_ylabel('Jumlah Penyewaan', fontsize=12)
    st.pyplot(fig4)

    # Scatter plot kecepatan angin vs jumlah penyewaan
    st.subheader("Hubungan Kecepatan Angin terhadap Penyewaan Sepeda")
    fig5, ax5 = plt.subplots(figsize=(10, 6))
    sns.regplot(data=day_df, x='windspeed', y='cnt', scatter_kws={'alpha':0.5}, line_kws={'color':'green'}, ax=ax5)
    ax5.set_title('Hubungan Kecepatan Angin terhadap Penyewaan Sepeda', fontsize=14)
    ax5.set_xlabel('Kecepatan Angin (Normalisasi)', fontsize=12)
    ax5.set_ylabel('Jumlah Penyewaan', fontsize=12)
    st.pyplot(fig5)

    # Box plot kondisi cuaca
    st.subheader("Pengaruh Kondisi Cuaca terhadap Penyewaan Sepeda")
    fig6, ax6 = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=day_df, x='weathersit', y='cnt', ax=ax6)
    ax6.set_title('Pengaruh Kondisi Cuaca terhadap Penyewaan Sepeda', fontsize=14)
    ax6.set_xlabel('Kondisi Cuaca (1=Cerah, 2=Berkabut, 3=Hujan)', fontsize=12)
    ax6.set_ylabel('Jumlah Penyewaan', fontsize=12)
    st.pyplot(fig6)

    # Heatmap korelasi
    st.subheader("Korelasi Faktor Cuaca terhadap Penyewaan")
    fig7, ax7 = plt.subplots(figsize=(10, 6))
    sns.heatmap(day_df[['temp', 'hum', 'windspeed', 'cnt']].corr(), annot=True, cmap='coolwarm', ax=ax7)
    ax7.set_title('Korelasi Faktor Cuaca terhadap Penyewaan Sepeda', fontsize=14)
    st.pyplot(fig7)

# Page: Pola Penyewaan
elif page == "📈 Pola Penyewaan":
    st.header("Pola Penyewaan Sepeda Berdasarkan Waktu")
    
    # Tabel Waktu Puncak Penyewaan Sepeda dalam Sehari
    st.subheader("Tabel Waktu Puncak Penyewaan Sepeda dalam Sehari")
    hour_df['day_type'] = hour_df['workingday'].map({1: 'Hari Kerja', 0: 'Akhir Pekan/Libur'})
    hourly_rentals = hour_df.groupby(['hr', 'day_type'])['cnt'].mean().reset_index()
    hourly_rentals.columns = ['Jam', 'Tipe Hari', 'Rata-rata Penyewaan']
    st.write("Tabel menunjukkan rata-rata penyewaan per jam untuk hari kerja dan akhir pekan/libur:")
    st.write(hourly_rentals)

    # Line plot pola penyewaan dalam sehari
    st.subheader("Visualisasi Waktu Puncak Penyewaan Sepeda dalam Sehari")
    fig8, ax8 = plt.subplots(figsize=(12, 6))
    sns.lineplot(data=hourly_rentals, x='Jam', y='Rata-rata Penyewaan', hue='Tipe Hari', marker='o', ax=ax8)
    ax8.set_title('Pola Penyewaan Sepeda dalam Sehari', fontsize=14)
    ax8.set_xlabel('Jam', fontsize=12)
    ax8.set_ylabel('Rata-rata Penyewaan Sepeda', fontsize=12)
    ax8.set_xticks(range(0, 24))
    ax8.legend(title='Tipe Hari')
    ax8.grid(True)
    st.pyplot(fig8)

    # Wawasan Waktu Puncak
    st.subheader("Wawasan Waktu Puncak Penyewaan Sepeda")
    st.write("""
    - **Hari Kerja**: Puncak penyewaan terjadi pada jam **08:00** (pagi, commuting ke tempat kerja) dan **17:00-18:00** (sore, pulang kerja), dengan nilai rata-rata tertinggi mendekati 500-525 penyewaan.
    - **Akhir Pekan/Libur**: Puncak terjadi di siang hingga sore (**12:00-16:00**), dengan nilai rata-rata lebih rendah (sekitar 200-300), menunjukkan penggunaan untuk rekreasi.
    """)

    # Tabel Pola Penyewaan Harian Berdasarkan Hari Kerja dan Akhir Pekan
    st.subheader("Tabel Pola Penyewaan Harian")
    daily_pattern = day_df.groupby('workingday')['cnt'].agg(['mean', 'min', 'max']).reset_index()
    daily_pattern.columns = ['Hari Kerja (1=Ya, 0=Tidak)', 'Rata-rata Penyewaan', 'Penyewaan Minimum', 'Penyewaan Maksimum']
    st.write("Tabel menunjukkan statistik penyewaan harian untuk hari kerja dan akhir pekan:")
    st.write(daily_pattern)

    # Box plot perbandingan hari kerja vs akhir pekan
    st.subheader("Visualisasi Pola Penyewaan Harian: Hari Kerja vs Akhir Pekan")
    fig9, ax9 = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=day_df, x='workingday', y='cnt', ax=ax9)
    ax9.set_title('Perbandingan Penyewaan: Hari Kerja vs Akhir Pekan', fontsize=14)
    ax9.set_xlabel('Hari Kerja (1=Ya, 0=Tidak)', fontsize=12)
    ax9.set_ylabel('Jumlah Penyewaan', fontsize=12)
    st.pyplot(fig9)

    # Wawasan Pola Penyewaan Harian
    st.subheader("Wawasan Pola Penyewaan Harian")
    st.write("""
    - **Rata-rata Penyewaan**: Hari kerja sedikit lebih tinggi (sekitar 4584.8) dibandingkan akhir pekan (sekitar 4330.2), mungkin karena penggunaan rutin untuk commuting.
    - **Variasi**: Hari kerja memiliki penyewaan minimum yang sangat rendah (22), menunjukkan adanya hari dengan anomali (misalnya cuaca buruk), sementara akhir pekan lebih konsisten (minimum 605).
    - **Maksimum**: Kedua tipe hari memiliki nilai maksimum yang tinggi (8714 untuk akhir pekan dan 8362 untuk hari kerja), menunjukkan potensi penyewaan besar pada kondisi optimal.
    - **Distribusi**: Hari kerja memiliki variasi lebih besar (kotak lebih lebar pada box plot), sedangkan akhir pekan lebih konsisten dengan kemungkinan lebih banyak outlier rendah.
    """)

    # Tabel Pengaruh Cuaca pada Waktu Puncak
    st.subheader("Tabel Pengaruh Cuaca pada Waktu Puncak Penyewaan Sepeda")
    hourly_weather = hour_df.groupby(['hr', 'day_type', 'weathersit'])['cnt'].mean().reset_index()
    hourly_weather.columns = ['Jam', 'Tipe Hari', 'Kondisi Cuaca (1=Cerah, 2=Berkabut, 3=Hujan)', 'Rata-rata Penyewaan']
    st.write("Tabel ini menunjukkan rata-rata penyewaan per jam berdasarkan tipe hari dan kondisi cuaca:")
    st.write(hourly_weather)

    # Wawasan Pengaruh Cuaca pada Waktu Puncak
    st.subheader("Wawasan Pengaruh Cuaca pada Waktu Puncak")
    st.write("""
    - **Hari Kerja**: Puncak jam 08:00 dan 17:00 sangat dipengaruhi cuaca. Cuaca cerah meningkatkan penyewaan (sekitar 400-600), sedangkan hujan menurunkannya drastis (sekitar 150-300).
    - **Akhir Pekan**: Puncak siang (14:00) menurun signifikan saat hujan (dari sekitar 350 ke 100), menunjukkan aktivitas rekreasi sensitif terhadap cuaca.
    """)

    # Tabel Pengaruh Cuaca pada Pola Harian
    st.subheader("Tabel Pengaruh Cuaca pada Pola Penyewaan Harian")
    daily_weather = day_df.groupby(['workingday', 'weathersit'])['cnt'].mean().reset_index()
    daily_weather.columns = ['Hari Kerja (1=Ya, 0=Tidak)', 'Kondisi Cuaca (1=Cerah, 2=Berkabut, 3=Hujan)', 'Rata-rata Penyewaan']
    st.write("Tabel ini menunjukkan rata-rata penyewaan harian berdasarkan tipe hari dan kondisi cuaca:")
    st.write(daily_weather)

    # Wawasan Pengaruh Cuaca pada Pola Harian
    st.subheader("Wawasan Pengaruh Cuaca pada Pola Harian")
    st.write("""
    - **Hari Kerja**: Cuaca cerah meningkatkan penyewaan harian (sekitar 5100), sedangkan hujan menurunkannya (sekitar 2500).
    - **Akhir Pekan**: Pola serupa, dengan cuaca cerah (sekitar 4800) jauh lebih tinggi dari hujan (sekitar 2000), menegaskan preferensi pengguna untuk cuaca baik.
    """)

# Page: Kesimpulan
elif page == "📚 Kesimpulan":
    st.header("Kesimpulan Analisis")
    st.write("Berdasarkan analisis data penyewaan sepeda, berikut adalah temuan utama:")
    st.write("1. **Pengaruh Faktor Cuaca terhadap Penyewaan Sepeda**:")
    st.write("   - **Suhu**: Terdapat korelasi positif yang kuat. Semakin tinggi suhu (dalam batas nyaman), semakin banyak penyewaan sepeda.")
    st.write("   - **Kelembaban**: Korelasi negatif. Kelembaban tinggi cenderung mengurangi minat penyewaan sepeda.")
    st.write("   - **Kecepatan Angin**: Pengaruhnya relatif kecil, tetapi kecepatan angin tinggi sedikit menurunkan jumlah penyewaan.")
    st.write("   - **Kondisi Cuaca**: Hari cerah (weathersit=1) memiliki penyewaan tertinggi, diikuti berkabut (2), dan hujan (3) dengan jumlah terendah.")
    st.write("2. **Pola Penyewaan Sepeda dalam Sehari dan Perbandingan Hari Kerja vs Akhir Pekan**:")
    st.write("   - **Hari Kerja**: Pola penyewaan menunjukkan dua puncak utama pada jam 08:00 (pagi) dan 17:00-18:00 (sore), mencerminkan penggunaan untuk commuting.")
    st.write("   - **Akhir Pekan/Libur**: Pola lebih merata dengan puncak di siang hingga sore (12:00-16:00), menunjukkan penggunaan untuk rekreasi.")
    st.write("   - Secara keseluruhan, hari kerja memiliki variasi penyewaan yang lebih besar dibandingkan akhir pekan.")

# Footer
st.write("---")
st.sidebar.write("**Informasi Kontak:**")
st.sidebar.write("Nama: Damianus Christopher Samosir")
st.sidebar.write("Email: christophersamosir@gmail.com")
st.sidebar.write("ID Dicoding: mc189d5y0821")