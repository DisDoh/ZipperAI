import numpy as np
import matplotlib.pyplot as plt
import pickle
import os


def _96qjfekr(_ae55pvlx, _z712cr33, _d616f16f, _cmlv7ss5, _d3vlvrj2,
    _0on05jtt, _ygev9bqs, _9xgknamm, _nbezaug4, _znmke9p0=0.95, _7d7fnsog=
    0.999, _npzlspek=1e-08, _0w1zm54e=1):
    _zwggc3q3 = _znmke9p0 * _d3vlvrj2 + (1 - _znmke9p0) * _d616f16f
    _w5g791dz = _7d7fnsog * _0on05jtt + (1 - _7d7fnsog) * _d616f16f ** 2
    _z1j6fdol = _znmke9p0 * _ygev9bqs + (1 - _znmke9p0) * _cmlv7ss5
    _z4tiuzsl = _7d7fnsog * _9xgknamm + (1 - _7d7fnsog) * _cmlv7ss5 ** 2
    _zuiov7m9 = _f6njlryl / (1 - _znmke9p0 ** _0w1zm54e)
    _shd9diy1 = _x8kxk8tl / (1 - _7d7fnsog ** _0w1zm54e)
    _q8jofdi5 = _vu1j9z60 / (1 - _znmke9p0 ** _0w1zm54e)
    _8zj1f0qc = _1cq43fhq / (1 - _7d7fnsog ** _0w1zm54e)
    _ae55pvlx -= _nbezaug4 * _ak0906v6 / (_2rbxays2.sqrt(_toocwpno) + _npzlspek
        )
    _z712cr33 -= _nbezaug4 * _or2y37pj / (_2rbxays2.sqrt(_tccswbun) + _npzlspek
        )
    return _ae55pvlx, _z712cr33, _f6njlryl, _x8kxk8tl, _vu1j9z60, _1cq43fhq


class _fohnt96v:

    def __init__(_pugufvye, _3u7ptv3l, _jlll0i23):
        _pugufvye.activation_function = _3u7ptv3l
        _pugufvye.activation_derivative = _jlll0i23
        _pugufvye.input = None

    def _luqtitbl(_pugufvye, _3adniqst):
        _pugufvye.input = _3adniqst
        return _pugufvye.activation_function(_3adniqst)

    def _efdjddpv(_pugufvye, _aptj22f9):
        return _aptj22f9 * _pugufvye.activation_derivative(_pugufvye.input)


def _9pq7d4rf(_jlnmkzhy):
    if _5jksjq5h.path.exists(_jlnmkzhy):
        with open(_jlnmkzhy, 'rb') as _ab9gc0fo:
            _ugq81low = _n8tmii0q.load(_ab9gc0fo)
            _tipdx9uw = _r1cvz77m['model']
            _ry7f06cx = _r1cvz77m['x_train']
            _6pfj7h6k = _r1cvz77m['x_val']
            return _5a7fb5rs, _ulonowk0, _61vuxlal
    return None, None, None


def _xa7yai3e(_5a7fb5rs, _ulonowk0, _61vuxlal, _jlnmkzhy):
    _ugq81low = {'model': _5a7fb5rs, 'x_train': _ulonowk0, 'x_val': _61vuxlal}
    with open(_jlnmkzhy, 'wb') as _ab9gc0fo:
        _n8tmii0q.dump(_r1cvz77m, _ab9gc0fo)


def _vyhbkdsh(_5lwig7oy):
    return 1 / (1 + _2rbxays2.exp(-_5lwig7oy))


def _pm05e8d7(_5lwig7oy):
    """ Compute sigmoid for x avoiding overflow. """
    return _2rbxays2.where(_5lwig7oy >= 0, 1 / (1 + _2rbxays2.exp(-
        _5lwig7oy)), _2rbxays2.exp(_5lwig7oy) / (1 + _2rbxays2.exp(_5lwig7oy)))


def _zic4bnsh(_7pew8bde):
    return _7pew8bde * (1 - _7pew8bde)


def _1xak0qod(_5lwig7oy):
    return _2rbxays2.maximum(0, _5lwig7oy)


def _8qjkhg53(_5lwig7oy):
    return _2rbxays2.where(_5lwig7oy <= 0, 0, 1)


def _bu00yx2v(_5lwig7oy):
    return _5lwig7oy * 0.5 * (1 + _2rbxays2.tanh(_2rbxays2.sqrt(2 /
        _2rbxays2.pi) * (_5lwig7oy + 0.044715 * _2rbxays2.power(_5lwig7oy, 3)))
        )


def _kxor5nrd(_5lwig7oy):
    return 0.5 * (1 + _2rbxays2.tanh(_2rbxays2.sqrt(2 / _2rbxays2.pi) * (
        _5lwig7oy + 0.044715 * _2rbxays2.power(_5lwig7oy, 3)))
        ) + 0.5 * _5lwig7oy * (1 - _2rbxays2.tanh(_2rbxays2.sqrt(2 /
        _2rbxays2.pi) * (_5lwig7oy + 0.044715 * _2rbxays2.power(_5lwig7oy, 3)))
        ) * (1 + _2rbxays2.sqrt(2 / _2rbxays2.pi) * (0.044715 * _2rbxays2.
        power(_5lwig7oy, 3) + 3 * 0.044715 * _2rbxays2.power(_5lwig7oy, 2)))


def _6v2uih7f(_5lwig7oy, _wadqctj1, _7qmqmffs, _npzlspek=1e-05):
    _vhfgkerb = _2rbxays2.mean(_5lwig7oy, axis=0, keepdims=True)
    _fun7yu9t = _2rbxays2.var(_5lwig7oy, axis=0, keepdims=True)
    _zgezd5es = (_5lwig7oy - _tz5obj4k) / _2rbxays2.sqrt(_t8fno1ut + _npzlspek)
    return _wadqctj1 * _sgbl78kd + _7qmqmffs, _sgbl78kd, _tz5obj4k, _t8fno1ut


def _47nq1x1w(_7lhymu9u):
    return _2rbxays2.unpackbits(_2rbxays2.frombuffer(_7lhymu9u, dtype=
        _2rbxays2.uint8))


def _oikd25a8(_14nqfmyr, _q4k4znkc):
    _km9gbup2 = []
    _aeg2vkoq = 0
    for _qvw2krm1 in _q4k4znkc:
        _dn9gsp4i.append(_14nqfmyr[_50gwbwel:_50gwbwel + _qvw2krm1])
        _50gwbwel += _qvw2krm1
    return _2rbxays2.concatenate(_dn9gsp4i)


def _kh63uvrf(_liycthav, _bwlqirpi):
    _6pkgs103 = len(_liycthav) // _bwlqirpi
    _eqs6kube = len(_liycthav) % _bwlqirpi
    _g3srrvda = [_liycthav[_x8bg9s8g * _bwlqirpi:(_x8bg9s8g + 1) *
        _bwlqirpi] for _x8bg9s8g in range(_plxfw1c9)]
    if _dxww3sgb > 0:
        _5fcd7qjq = _liycthav[-_dxww3sgb:]
        _0ljcbsjd = _2rbxays2.pad(_y7isj0cz, (0, _bwlqirpi - _dxww3sgb),
            mode='constant', constant_values=0)
        _d9ks1sof.append(_7b7dnmdm)
    return _d9ks1sof


import os
import numpy as np
import matplotlib.pyplot as plt


def _vmpga3fv(_ulonowk0, _61vuxlal, _hsrg4c5u, _ywmls647, _x4o2osvz,
    _j48s2seo, _8ns74nsd, _7n9ncavs, _8hstcpyg, _ga931zn8, _ykppr6jz,
    _yjl6myik, _7xej2iii, _wwgtibt6, _8k1sv9fu, _whar6eno, _u8fabpay,
    _znmke9p0, _wqjsjezj, _7d7fnsog, _nbezaug4, _ppwdeuds, _cfx5bqfb,
    _j966tonp, _pdcdwx10, _xpx430uw, _kjar8gtu, _859hmpd9, _zsne1b4y,
    _ri8cxzgg, _tjb1nspp, _kwcn698p, _zpdmpolk, _p4vsdct4, _youjlr2m,
    _g31rl632, _cm1upws9, _wwzfv98d, _0jbzemj5, _ihsw1cem, _bs41kygs,
    _hl73zvm1, _bgtnuanm, _qsa34oh4, _bv93h48z, _6jxz523b):
    _7ajvkkai = []
    _cd90nowt = []
    for _3mm4vabn in range(_ppwdeuds):
        _yk7y6mfm = _kxj6jtot(_2rbxays2.dot(_ulonowk0, _hsrg4c5u) + _ywmls647)
        _jxky5g69, _n2ozrv6g, _n2ozrv6g, _n2ozrv6g = _91yd08nc(_70su5vfm,
            _8k1sv9fu, _whar6eno)
        _va8541eq = _kxj6jtot(_2rbxays2.dot(_jxky5g69, _x4o2osvz) + _j48s2seo)
        _7ar6o3cg, _n2ozrv6g, _n2ozrv6g, _n2ozrv6g = _91yd08nc(_oxagpakh,
            _u8fabpay, _znmke9p0)
        _jd4iqrgy = _2rbxays2.round(_kxj6jtot(_2rbxays2.dot(_7ar6o3cg,
            _8ns74nsd) + _7n9ncavs))
        _luwb6xic, _n2ozrv6g, _n2ozrv6g, _n2ozrv6g = _91yd08nc(_fz6cj3o6,
            _wqjsjezj, _7d7fnsog)
        _8iq8ht4d = _kxj6jtot(_2rbxays2.dot(_luwb6xic, _8hstcpyg) + _ga931zn8)
        _epkjwc1e = _kxj6jtot(_2rbxays2.dot(_i6n9lip4, _ykppr6jz) + _yjl6myik)
        _inw7sy3r = _kxj6jtot(_2rbxays2.dot(_syp4s65d, _7xej2iii) + _wwgtibt6)
        _4bz14g9h = _2rbxays2.mean(_2rbxays2.abs(_ulonowk0 - _6k2sgpvg))
        _rpxd9wx7.append(_ykcodioy)
        _m9a358lp = _kxj6jtot(_2rbxays2.dot(_61vuxlal, _hsrg4c5u) + _ywmls647)
        _pbrwlu11, _n2ozrv6g, _n2ozrv6g, _n2ozrv6g = _91yd08nc(_xm3m9kj1,
            _8k1sv9fu, _whar6eno)
        _knkvfsm6 = _kxj6jtot(_2rbxays2.dot(_pbrwlu11, _x4o2osvz) + _j48s2seo)
        _hwaxalev, _n2ozrv6g, _n2ozrv6g, _n2ozrv6g = _91yd08nc(_2vv7nvhh,
            _u8fabpay, _znmke9p0)
        _pdiqr1zt = _2rbxays2.round(_kxj6jtot(_2rbxays2.dot(_hwaxalev,
            _8ns74nsd) + _7n9ncavs))
        _ctg218i6, _n2ozrv6g, _n2ozrv6g, _n2ozrv6g = _91yd08nc(_79uaylv5,
            _wqjsjezj, _7d7fnsog)
        _160p8zdv = _kxj6jtot(_2rbxays2.dot(_ctg218i6, _8hstcpyg) + _ga931zn8)
        _sfx6tf7k = _kxj6jtot(_2rbxays2.dot(_bg7k8qmf, _ykppr6jz) + _yjl6myik)
        _8vagafdu = _kxj6jtot(_2rbxays2.dot(_fg307ooj, _7xej2iii) + _wwgtibt6)
        _t1m9fdff = _2rbxays2.mean(_2rbxays2.abs(_61vuxlal - _bjk3k6sv))
        _xvhxfy7i.append(_3o3eq5hx)
        _b39gdfkm = _ulonowk0 - _6k2sgpvg
        _t238hj8q = _lse1p3hv * _2ys52gro(_6k2sgpvg)
        _dl2zmcww = _wv93yt7k.dot(_7xej2iii.T)
        _wum5yll6 = _4rhmaem7 * _2ys52gro(_syp4s65d)
        _80j8jsty = _obh4oixb.dot(_ykppr6jz.T)
        _tnweo4d8 = _f3m60r6s * _2ys52gro(_i6n9lip4)
        _q56qcgid = _0y48s5du.dot(_8hstcpyg.T)
        _dutiq3ov = _lavxvmht * _2ys52gro(_fz6cj3o6)
        _7nzyj6jt = _2x4nzncz.dot(_8ns74nsd.T)
        _gshy6d08 = _ei5cm72k * _2ys52gro(_oxagpakh)
        _rpbg2kfo = _oonjdwmn.dot(_x4o2osvz.T)
        _nbk9z5xs = _dd5pvb7a * _2ys52gro(_70su5vfm)
        _7xej2iii += _syp4s65d.T.dot(_wv93yt7k) * _nbezaug4
        _wwgtibt6 += _2rbxays2.sum(_wv93yt7k, axis=0) * _nbezaug4
        _ykppr6jz += _i6n9lip4.T.dot(_obh4oixb) * _nbezaug4
        _yjl6myik += _2rbxays2.sum(_obh4oixb, axis=0) * _nbezaug4
        _8hstcpyg += _fz6cj3o6.T.dot(_0y48s5du) * _nbezaug4
        _ga931zn8 += _2rbxays2.sum(_0y48s5du, axis=0) * _nbezaug4
        _8ns74nsd += _oxagpakh.T.dot(_2x4nzncz) * _nbezaug4
        _7n9ncavs += _2rbxays2.sum(_2x4nzncz, axis=0) * _nbezaug4
        _x4o2osvz += _70su5vfm.T.dot(_oonjdwmn) * _nbezaug4
        _j48s2seo += _2rbxays2.sum(_oonjdwmn, axis=0) * _nbezaug4
        _hsrg4c5u += _ulonowk0.T.dot(_9temkbck) * _nbezaug4
        _ywmls647 += _2rbxays2.sum(_9temkbck, axis=0) * _nbezaug4
        _bcrnr0ge = _2rbxays2.round(_bjk3k6sv) == _61vuxlal
        _hdn3sh6s = _2rbxays2.mean(_mcmc0a0l)
        if _3mm4vabn % 100 == 0:
            print(
                f'Epoch {_3mm4vabn}: Training Loss: {_ykcodioy}, Validation Loss: {_3o3eq5hx}, Accuracy: {_4kpc5tz8 * 100:.6f}%'
                )
            _tipdx9uw = {'encoder_weights0': _hsrg4c5u, 'encoder_bias0':
                _ywmls647, 'encoder_weights1': _x4o2osvz, 'encoder_bias1':
                _j48s2seo, 'encoder_weights2': _8ns74nsd, 'encoder_bias2':
                _7n9ncavs, 'decoder_weights1': _8hstcpyg, 'decoder_bias1':
                _ga931zn8, 'decoder_weights2': _ykppr6jz, 'decoder_bias2':
                _yjl6myik, 'decoder_weights3': _7xej2iii, 'decoder_bias3':
                _wwgtibt6, 'm_encoder_weights0': _cfx5bqfb,
                'v_encoder_weights0': _j966tonp, 'm_encoder_bias0':
                _pdcdwx10, 'v_encoder_bias0': _xpx430uw,
                'm_encoder_weights1': _kjar8gtu, 'v_encoder_weights1':
                _859hmpd9, 'm_encoder_bias1': _zsne1b4y, 'v_encoder_bias1':
                _ri8cxzgg, 'm_encoder_weights2': _tjb1nspp,
                'v_encoder_weights2': _kwcn698p, 'm_encoder_bias2':
                _zpdmpolk, 'v_encoder_bias2': _p4vsdct4,
                'm_decoder_weights1': _youjlr2m, 'v_decoder_weights1':
                _g31rl632, 'm_decoder_bias1': _cm1upws9, 'v_decoder_bias1':
                _wwzfv98d, 'm_decoder_weights2': _0jbzemj5,
                'v_decoder_weights2': _ihsw1cem, 'm_decoder_bias2':
                _bs41kygs, 'v_decoder_bias2': _hl73zvm1,
                'm_decoder_weights3': _bgtnuanm, 'v_decoder_weights3':
                _qsa34oh4, 'm_decoder_bias3': _bv93h48z, 'v_decoder_bias3':
                _6jxz523b}
            _um9n0o52(_5a7fb5rs, _ulonowk0, _61vuxlal, 'autoencoder_model.pkl')
            _26x6f69o.close('all')
            _26x6f69o.figure(figsize=(5, 5))
            _26x6f69o.plot(_rpxd9wx7, label='Training Loss')
            _26x6f69o.plot(_xvhxfy7i, label='Validation Loss')
            _26x6f69o.xlabel('Epoch')
            _26x6f69o.ylabel('Loss')
            _26x6f69o.title('Training and Validation Losses')
            _26x6f69o.legend()
            _26x6f69o.show()
            if _2rbxays2.array_equal(_ulonowk0, _2rbxays2.round(_6k2sgpvg)):
                print(
                    f'Original data equals reconstructed data rounded at epoch {_3mm4vabn}. Stopping training.'
                    )
                break


def _g5xhuigk():
    _lazattis = 8200
    _mt8cj9lk = 8
    _bxbek4cg = 0.8
    _xdyolsaz = 0.0001
    _lu5gjgqu = 100000
    _nhytzkos = 8
    _tvxhnzbs = _2rbxays2.random.randint(0, 2, size=(_ztlb6fru, _lep1j1ep))
    _0fhxx7si = int(_ztlb6fru * _cj1w00gt)
    _ry7f06cx = _82ee2xf9[:_sefg6p6w]
    _6pfj7h6k = _82ee2xf9[_sefg6p6w:]
    _e1wk0tjc = _lep1j1ep
    _jjnkggnn = 64
    _6j0ssfjy = 32
    _j7hw1c0v = 8 * 2
    _e24yukj8 = 32
    _vimkl2f5 = 64
    _yghs212t = _h2iis1g0
    if _5jksjq5h.path.exists('autoencoder_model.pkl'):
        _5a7fb5rs, _ulonowk0, _61vuxlal = _uvjjie1z('autoencoder_model.pkl')
        _u55l3j2y = _5a7fb5rs['encoder_weights0']
        _cq9lpwb9 = _5a7fb5rs['encoder_bias0']
        _mv8ljfe6 = _5a7fb5rs['encoder_weights1']
        _ocrdkyio = _5a7fb5rs['encoder_bias1']
        _6pupwei9 = _5a7fb5rs['encoder_weights2']
        _ip7a93ce = _5a7fb5rs['encoder_bias2']
        _g7aqywip = _5a7fb5rs['decoder_weights1']
        _ywjycn40 = _5a7fb5rs['decoder_bias1']
        _cj4xds6p = _5a7fb5rs['decoder_weights2']
        _0qkrlcpz = _5a7fb5rs['decoder_bias2']
        _0qogbmii = _5a7fb5rs['decoder_weights3']
        _b0nwphrq = _5a7fb5rs['decoder_bias3']
        _zbgllygu = _5a7fb5rs['m_encoder_weights0']
        _4r6ate7f = _5a7fb5rs['v_encoder_weights0']
        _2nojgbk7 = _5a7fb5rs['m_encoder_bias0']
        _ti6kly4p = _5a7fb5rs['v_encoder_bias0']
        _7qod695t = _5a7fb5rs['m_encoder_weights1']
        _6rztbuoj = _5a7fb5rs['v_encoder_weights1']
        _5n5nrdox = _5a7fb5rs['m_encoder_bias1']
        _vcd5rwmq = _5a7fb5rs['v_encoder_bias1']
        _9xyusz2c = _5a7fb5rs['m_encoder_weights2']
        _dppu3ags = _5a7fb5rs['v_encoder_weights2']
        _9xihrulf = _5a7fb5rs['m_encoder_bias2']
        _0xgu9wif = _5a7fb5rs['v_encoder_bias2']
        _kblcnebm = _5a7fb5rs['m_decoder_weights1']
        _oyvgok4k = _5a7fb5rs['v_decoder_weights1']
        _6e1i0npf = _5a7fb5rs['m_decoder_bias1']
        _1uw902uu = _5a7fb5rs['v_decoder_bias1']
        _h1xqby04 = _5a7fb5rs['m_decoder_weights2']
        _3br7lm2x = _5a7fb5rs['v_decoder_weights2']
        _ltz8igow = _5a7fb5rs['m_decoder_bias2']
        _gv58c1p0 = _5a7fb5rs['v_decoder_bias2']
        _xdf89w5n = _5a7fb5rs['m_decoder_weights3']
        _j9i2ekqk = _5a7fb5rs['v_decoder_weights3']
        _qgm4v52b = _5a7fb5rs['m_decoder_bias3']
        _5t0g76sn = _5a7fb5rs['v_decoder_bias3']
    else:
        _u55l3j2y = _2rbxays2.random.randn(_h2iis1g0, _yan2ljvq)
        _cq9lpwb9 = _2rbxays2.zeros(_yan2ljvq)
        _mv8ljfe6 = _2rbxays2.random.randn(_yan2ljvq, _t779jpdb)
        _ocrdkyio = _2rbxays2.zeros(_t779jpdb)
        _6pupwei9 = _2rbxays2.random.randn(_t779jpdb, _7353ucgk)
        _ip7a93ce = _2rbxays2.zeros(_7353ucgk)
        _g7aqywip = _2rbxays2.random.randn(_7353ucgk, _8imuvdki)
        _ywjycn40 = _2rbxays2.zeros(_8imuvdki)
        _cj4xds6p = _2rbxays2.random.randn(_8imuvdki, _zaa0ii0r)
        _0qkrlcpz = _2rbxays2.zeros(_zaa0ii0r)
        _0qogbmii = _2rbxays2.random.randn(_zaa0ii0r, _1fs09t5b)
        _b0nwphrq = _2rbxays2.zeros(_1fs09t5b)
        _zbgllygu = _2rbxays2.zeros_like(_hsrg4c5u)
        _4r6ate7f = _2rbxays2.zeros_like(_hsrg4c5u)
        _2nojgbk7 = _2rbxays2.zeros_like(_ywmls647)
        _ti6kly4p = _2rbxays2.zeros_like(_ywmls647)
        _7qod695t = _2rbxays2.zeros_like(_x4o2osvz)
        _6rztbuoj = _2rbxays2.zeros_like(_x4o2osvz)
        _5n5nrdox = _2rbxays2.zeros_like(_j48s2seo)
        _vcd5rwmq = _2rbxays2.zeros_like(_j48s2seo)
        _9xyusz2c = _2rbxays2.zeros_like(_8ns74nsd)
        _dppu3ags = _2rbxays2.zeros_like(_8ns74nsd)
        _9xihrulf = _2rbxays2.zeros_like(_7n9ncavs)
        _0xgu9wif = _2rbxays2.zeros_like(_7n9ncavs)
        _kblcnebm = _2rbxays2.zeros_like(_8hstcpyg)
        _oyvgok4k = _2rbxays2.zeros_like(_8hstcpyg)
        _6e1i0npf = _2rbxays2.zeros_like(_ga931zn8)
        _1uw902uu = _2rbxays2.zeros_like(_ga931zn8)
        _h1xqby04 = _2rbxays2.zeros_like(_ykppr6jz)
        _3br7lm2x = _2rbxays2.zeros_like(_ykppr6jz)
        _ltz8igow = _2rbxays2.zeros_like(_yjl6myik)
        _gv58c1p0 = _2rbxays2.zeros_like(_yjl6myik)
        _xdf89w5n = _2rbxays2.zeros_like(_7xej2iii)
        _j9i2ekqk = _2rbxays2.zeros_like(_7xej2iii)
        _qgm4v52b = _2rbxays2.zeros_like(_wwgtibt6)
        _5t0g76sn = _2rbxays2.zeros_like(_wwgtibt6)
    _gav9brk0 = _2rbxays2.ones(_yan2ljvq)
    _52odzqum = _2rbxays2.zeros(_yan2ljvq)
    _sqs7rkpb = _2rbxays2.ones(_t779jpdb)
    _h4ctchu6 = _2rbxays2.zeros(_t779jpdb)
    _tcygjxnw = _2rbxays2.ones(_7353ucgk)
    _58d212i9 = _2rbxays2.zeros(_7353ucgk)
    _1xx78zho(_ulonowk0, _61vuxlal, _hsrg4c5u, _ywmls647, _x4o2osvz,
        _j48s2seo, _8ns74nsd, _7n9ncavs, _8hstcpyg, _ga931zn8, _ykppr6jz,
        _yjl6myik, _7xej2iii, _wwgtibt6, _8k1sv9fu, _whar6eno, _u8fabpay,
        _znmke9p0, _wqjsjezj, _7d7fnsog, _nbezaug4, _ppwdeuds, _cfx5bqfb,
        _j966tonp, _pdcdwx10, _xpx430uw, _kjar8gtu, _859hmpd9, _zsne1b4y,
        _ri8cxzgg, _tjb1nspp, _kwcn698p, _zpdmpolk, _p4vsdct4, _youjlr2m,
        _g31rl632, _cm1upws9, _wwzfv98d, _0jbzemj5, _ihsw1cem, _bs41kygs,
        _hl73zvm1, _bgtnuanm, _qsa34oh4, _bv93h48z, _6jxz523b)
    _tipdx9uw = {'encoder_weights0': _hsrg4c5u, 'encoder_bias0': _ywmls647,
        'encoder_weights1': _x4o2osvz, 'encoder_bias1': _j48s2seo,
        'encoder_weights2': _8ns74nsd, 'encoder_bias2': _7n9ncavs,
        'decoder_weights1': _8hstcpyg, 'decoder_bias1': _ga931zn8,
        'decoder_weights2': _ykppr6jz, 'decoder_bias2': _yjl6myik,
        'decoder_weights3': _7xej2iii, 'decoder_bias3': _wwgtibt6,
        'm_encoder_weights0': _cfx5bqfb, 'v_encoder_weights0': _j966tonp,
        'm_encoder_bias0': _pdcdwx10, 'v_encoder_bias0': _xpx430uw,
        'm_encoder_weights1': _kjar8gtu, 'v_encoder_weights1': _859hmpd9,
        'm_encoder_bias1': _zsne1b4y, 'v_encoder_bias1': _ri8cxzgg,
        'm_encoder_weights2': _tjb1nspp, 'v_encoder_weights2': _kwcn698p,
        'm_encoder_bias2': _zpdmpolk, 'v_encoder_bias2': _p4vsdct4,
        'm_decoder_weights1': _youjlr2m, 'v_decoder_weights1': _g31rl632,
        'm_decoder_bias1': _cm1upws9, 'v_decoder_bias1': _wwzfv98d,
        'm_decoder_weights2': _0jbzemj5, 'v_decoder_weights2': _ihsw1cem,
        'm_decoder_bias2': _bs41kygs, 'v_decoder_bias2': _hl73zvm1,
        'm_decoder_weights3': _bgtnuanm, 'v_decoder_weights3': _qsa34oh4,
        'm_decoder_bias3': _bv93h48z, 'v_decoder_bias3': _6jxz523b}
    _um9n0o52(_5a7fb5rs, _ulonowk0, _61vuxlal, 'autoencoder_model.pkl')
    _n9je4hc5 = 'test'
    with open(_7ik1cxlx, 'rb') as _ab9gc0fo:
        _5w5czjol = _ab9gc0fo.read()
    _8vyi2lzy = _8mi44eu6(_7lhymu9u)
    _w4q3rg5c = _28v3uojf(_oc39rzbq, _bwlqirpi)
    _50vpg186 = []
    _2i0dhmog = []
    for _x8bg9s8g, _nwbmv2ru in enumerate(_u7ohyl2e):
        _xiz9dc0m = _2rbxays2.array(list(_nwbmv2ru), dtype=_2rbxays2.uint8)
        _xiz9dc0m = _2rbxays2.expand_dims(_nwbmv2ru, axis=0)
        _knkvfsm6 = _kxj6jtot(_2rbxays2.dot(_nwbmv2ru, _x4o2osvz) + _j48s2seo)
        _pdiqr1zt = _kxj6jtot(_2rbxays2.dot(_2vv7nvhh, _8ns74nsd) + _7n9ncavs)
        _4iby8hv3 = _79uaylv5
        _160p8zdv = _kxj6jtot(_2rbxays2.dot(_ff2sjzw5, _8hstcpyg) + _ga931zn8)
        _8vagafdu = _kxj6jtot(_2rbxays2.dot(_bg7k8qmf, _ykppr6jz) + _yjl6myik)
        _dtwyif5e = _bjk3k6sv
        print(f'{_x8bg9s8g}/{len(_u7ohyl2e)}')
        _dtwyif5e = _d2z95fh1(_qy2idhdg.squeeze(), [8])
        _14nqfmyr.append(_qy2idhdg)
        _q4k4znkc.append(len(_nwbmv2ru[0]))
    _lu50yg4v = _2rbxays2.array(_14nqfmyr)
    _qxddbjxt = _k16w3w63.astype(_2rbxays2.float64)
    _zcm5hr4j = _p0wz5tkd.tobytes()
    with open(f'{_7ik1cxlx}.AIZip', 'wb') as _mxmhrzjy:
        _mxmhrzjy.write(_07ytpmpo)
    _n9je4hc5 = f'{_7ik1cxlx}.AIZip'
    if _7ik1cxlx and _7ik1cxlx.endswith('.AIZip'):
        with open(_7ik1cxlx, 'rb') as _mxmhrzjy:
            _zcm5hr4j = _mxmhrzjy.read()
        _qxddbjxt = _2rbxays2.frombuffer(_07ytpmpo, dtype=_2rbxays2.float64)
        _m8t70bjz = 4
        _6pkgs103 = len(_p0wz5tkd) // _3g4oi8xd
        _lu50yg4v = _p0wz5tkd[:_plxfw1c9 * _3g4oi8xd].reshape((_plxfw1c9,
            _3g4oi8xd))
        _bff9iq32 = []
        _50vpg186 = []
        for _x8bg9s8g, _nwbmv2ru in enumerate(_k16w3w63):
            _xiz9dc0m = _2rbxays2.expand_dims(_nwbmv2ru, axis=0)
            _160p8zdv = _kxj6jtot(_2rbxays2.dot(_nwbmv2ru, _8hstcpyg) +
                _ga931zn8)
            _8vagafdu = _kxj6jtot(_2rbxays2.dot(_bg7k8qmf, _ykppr6jz) +
                _yjl6myik)
            _dtwyif5e = _bjk3k6sv
            print(f'{_x8bg9s8g}/{len(_k16w3w63)}')
            _dtwyif5e = _d2z95fh1(_qy2idhdg.squeeze(), [8])
            _14nqfmyr.append(_qy2idhdg)
        _50vpg186 = _2rbxays2.round(_14nqfmyr, 0)
        _50vpg186 = _14nqfmyr.astype(_2rbxays2.uint8)
        _50vpg186 = [''.join(map(str, map(int, _4i4no6yh))) for _4i4no6yh in
            _14nqfmyr]
        _xpibj236 = [_w1dt3wo6(_4i4no6yh, 8) for _4i4no6yh in _14nqfmyr]
        _wskkz6c9 = bytearray([int(_4i4no6yh, 2) for _pini1lo1 in _qo6hbvu8 for
            _4i4no6yh in _pini1lo1])
        with open(_7ik1cxlx[:-6], 'wb') as _mxmhrzjy:
            _mxmhrzjy.write(_6mwmgsbr)


if __name__ == '__main__':
    _3pgv4b5t()
