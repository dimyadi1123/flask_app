from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# Pesan-pesan default Puja Kerang Ajaib
pesan_puja_kerang_ajaib = [
    "Makan patty itu spongebob",
    "Berdansalah, Patrick",
    "Hati-hati dengan Plankton",
    "Jangan lupa pergi ke Krusty Krab",
    "Cari Krabby Patty yang hilang",
    "Spongebob adalah koki terbaik di Bikini Bottom",
    "Patrick adalah teman yang unik",
    "Squidward selalu kesal",
    "Sandy suka olahraga air",
    "Mr. Krabs sangat pelit"
]

@app.route('/')
def beranda():
    random_pesan = random.choice(pesan_puja_kerang_ajaib)
    return render_template('index.html', pesan=random_pesan)

@app.route('/input_nama', methods=['GET', 'POST'])
def input_nama():
    pesan_selamat_datang = None

    if request.method == 'POST':
        nama = request.form.get('nama')
        pesan_selamat_datang = f"Selamat datang, {nama}, di Puja Kerang Ajaib!"
        return render_template('input_nama.html', pesan_selamat_datang=pesan_selamat_datang, nama=nama)

    return render_template('input_nama.html', pesan_selamat_datang=pesan_selamat_datang)

@app.route('/puja_kerang_ajaib', methods=['GET'])
def puja_kerang_ajaib():
    nama = request.args.get('nama')
    random_pesan = random.choice(pesan_puja_kerang_ajaib)
    return render_template('puja_kerang_ajaib.html', nama=nama, pesan=random_pesan)

if __name__ == '__main__':
    app.run(debug=True)
