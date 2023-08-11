from flask import Flask, redirect, render_template, jsonify
import random
import os

app = Flask(__name__)
sample_flag = ('BKSEC{t00_f4st_rjght?}', 'BKSEC{w3_l0v3_sp33d}', 'BKSEC{rac1ng_b0y_1n_hust}', 'BKSEC{fl4sk_1s_k1nd4_vu1n3rabl3}',
               'BKSEC{h0w_ab0ut_m1gr4te_to_dj4ng0}', 'BKSEC{h3r3_1s_th4_FL4G_subm1t_pls!!!}', "BKSEC{san1ty_ch3ck}", 'BKSEC{w3b_3xpl0it4t10n}', 'BKSEC{https://youtu.be/dQw4w9WgXcQ}', 'BKSEC{1_h0p3_th1s_is_n0t_t00_e4sy}', 'BKSEC{1s_n0dejs_a_h0t_t0p1c}', 'BKSEC{CVE-2021-44228}')


@app.route('/')
def start_point():
    return render_template('index.html')


@app.route('/3cst4sy')
def mdma():
    return redirect('/B')


@app.route('/B')
def B():
    return redirect('/K')


@app.route('/K')
def K():
    return redirect('/S')

@app.route('/S')
def S():
    return redirect('/E')


@app.route('/E')
def E():
    return redirect('/C')


@app.route('/C')
def C():
    return redirect('/{')


@app.route('/{')
def opening_curly_brackets():
    return redirect('/9')


@app.route('/9')
def nine():
    return redirect('/3')


@app.route('/3')
def three():
    return redirect('/t')


@app.route('/t')
def t():
    return redirect('/_')


@app.route('/_')
def underscore():
    return redirect('/h')


@app.route('/h')
def h():
    return redirect('/1')


@app.route('/1')
def one():
    return redirect('/g')


@app.route('/g')
def g():
    return redirect('/H')


@app.route('/H')
def H():
    return redirect('/-')


@app.route('/-')
def hyphen():
    return redirect('/y')


@app.route('/y')
def y():
    return redirect('/e')


@app.route('/e')
def e():
    return redirect('/T')


@app.route('/T')
def T():
    return redirect('/}')


@app.route('/}')
def closing_curly_brackets():
    return redirect('/api/viewflag')


@app.route('/api/viewflag')
def int3r3st1ng_api():
    for flag in random.choices(sample_flag):
        return jsonify({'FL4G': flag})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ['PORT'], debug=False)
