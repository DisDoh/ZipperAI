import numpy as np
import matplotlib.pyplot as plt
import pickle
import os


def _shvemzridx(_wuqsotblyy, _mccusrinfo, _ziespkanhc, _xogmqujnoh,
    _eintfairdb, _srkzfzobwk, _srhuedgjue, _qihmllxnqv, _fzbbanksws,
    _zafgupcdpu=0.95, _kdebfmpili=0.999, _xcibrfegyr=1e-08, _xhtlvuuanq=1):
    _izmjkngxhl = _zafgupcdpu * _eintfairdb + (1 - _zafgupcdpu) * _ziespkanhc
    _zicnuwtfsn = _kdebfmpili * _srkzfzobwk + (1 - _kdebfmpili
        ) * _ziespkanhc ** 2
    _bspifxzzyg = _zafgupcdpu * _srhuedgjue + (1 - _zafgupcdpu) * _xogmqujnoh
    _lxncfeaowh = _kdebfmpili * _qihmllxnqv + (1 - _kdebfmpili
        ) * _xogmqujnoh ** 2
    _wygjiuiujq = _vimibwiset / (1 - _zafgupcdpu ** _xhtlvuuanq)
    _inwrogkmme = _dedmhcjiad / (1 - _kdebfmpili ** _xhtlvuuanq)
    _kdfkvpxqiq = _vxkfsnvgwq / (1 - _zafgupcdpu ** _xhtlvuuanq)
    _ajdmyyttjo = _ahtinfnbms / (1 - _kdebfmpili ** _xhtlvuuanq)
    _wuqsotblyy -= _fzbbanksws * _nrfejpyxut / (_uujlgzqxdl.sqrt(
        _acjdbtvgqu) + _xcibrfegyr)
    _mccusrinfo -= _fzbbanksws * _jvrbzfodpg / (_uujlgzqxdl.sqrt(
        _wwpbtdpyvp) + _xcibrfegyr)
    return (_wuqsotblyy, _mccusrinfo, _vimibwiset, _dedmhcjiad, _vxkfsnvgwq,
        _ahtinfnbms)


class _vppyjaxwwv:

    def __init__(_qvptvszkyx, _uotchwemvm, _qroagucgzs):
        _qvptvszkyx.activation_function = _uotchwemvm
        _qvptvszkyx.activation_derivative = _qroagucgzs
        _qvptvszkyx.input = None

    def _sqaiejqqyu(_qvptvszkyx, _qbhtbbhses):
        _qvptvszkyx.input = _qbhtbbhses
        return _qvptvszkyx.activation_function(_qbhtbbhses)

    def _ixentbkzvk(_qvptvszkyx, _raxbuinmqp):
        return _raxbuinmqp * _qvptvszkyx.activation_derivative(_qvptvszkyx.
            input)


def _xpgwmmpjvj(_dxsfvuedak):
    if _ihshtncdju.path.exists(_dxsfvuedak):
        with _ptwpkzuhmb(_dxsfvuedak, 'rb') as _rtdssbylrf:
            _ysvlgpecab = _urmobamona.load(_rtdssbylrf)
            _mjqcbkiaev = _urocjlpqun['model']
            _ewrwwfsgdn = _urocjlpqun['x_train']
            _efmritnvyl = _urocjlpqun['x_val']
            return _inblsauurb, _jshujtkdof, _qjtzoiuzfg
    return None, None, None


def _cmbuxpcpik(_inblsauurb, _jshujtkdof, _qjtzoiuzfg, _dxsfvuedak):
    _ysvlgpecab = {'model': _inblsauurb, 'x_train': _jshujtkdof, 'x_val':
        _qjtzoiuzfg}
    with _ptwpkzuhmb(_dxsfvuedak, 'wb') as _rtdssbylrf:
        _urmobamona.dump(_urocjlpqun, _rtdssbylrf)


def _jfcvioduri(_idnerrvhym):
    return 1 / (1 + _uujlgzqxdl.exp(-_idnerrvhym))


def _awavpgesle(_idnerrvhym):
    """ Compute sigmoid for x avoiding overflow. """
    return _uujlgzqxdl.where(_idnerrvhym >= 0, 1 / (1 + _uujlgzqxdl.exp(-
        _idnerrvhym)), _uujlgzqxdl.exp(_idnerrvhym) / (1 + _uujlgzqxdl.exp(
        _idnerrvhym)))


def _tzwtiowszw(_pujlanclyj):
    return _pujlanclyj * (1 - _pujlanclyj)


def _euqwekfqro(_idnerrvhym):
    return _uujlgzqxdl.maximum(0, _idnerrvhym)


def _yodevmtagl(_idnerrvhym):
    return _uujlgzqxdl.where(_idnerrvhym <= 0, 0, 1)


def _hjgopkxjaf(_idnerrvhym):
    return _idnerrvhym * 0.5 * (1 + _uujlgzqxdl.tanh(_uujlgzqxdl.sqrt(2 /
        _uujlgzqxdl.pi) * (_idnerrvhym + 0.044715 * _uujlgzqxdl.power(
        _idnerrvhym, 3))))


def _jjgpsnyhdp(_idnerrvhym):
    return 0.5 * (1 + _uujlgzqxdl.tanh(_uujlgzqxdl.sqrt(2 / _uujlgzqxdl.pi) *
        (_idnerrvhym + 0.044715 * _uujlgzqxdl.power(_idnerrvhym, 3)))
        ) + 0.5 * _idnerrvhym * (1 - _uujlgzqxdl.tanh(_uujlgzqxdl.sqrt(2 /
        _uujlgzqxdl.pi) * (_idnerrvhym + 0.044715 * _uujlgzqxdl.power(
        _idnerrvhym, 3)))) * (1 + _uujlgzqxdl.sqrt(2 / _uujlgzqxdl.pi) * (
        0.044715 * _uujlgzqxdl.power(_idnerrvhym, 3) + 3 * 0.044715 *
        _uujlgzqxdl.power(_idnerrvhym, 2)))


def _vyqlyqtjkn(_idnerrvhym, _xmzkmsunow, _rrlqezdzze, _xcibrfegyr=1e-05):
    _jkhcuvjfuj = _uujlgzqxdl.mean(_idnerrvhym, axis=0, keepdims=True)
    _oyyqzzixre = _uujlgzqxdl.var(_idnerrvhym, axis=0, keepdims=True)
    _fmdlkfsfzd = (_idnerrvhym - _gnhjpcffaq) / _uujlgzqxdl.sqrt(
        _lnkyznpdme + _xcibrfegyr)
    return (_xmzkmsunow * _ynsevigfmi + _rrlqezdzze, _ynsevigfmi,
        _gnhjpcffaq, _lnkyznpdme)


def _pkdotbwbfx(_vsfrikuume):
    return _uujlgzqxdl.unpackbits(_uujlgzqxdl.frombuffer(_vsfrikuume, dtype
        =_uujlgzqxdl.uint8))


def _stunzkpdpl(_rtdmhqsibm, _fnjjgrrwqk):
    _dhhteqwwiq = []
    _amiggrczen = 0
    for _mjgoydjeyk in _fnjjgrrwqk:
        _frvfjutfwi.append(_rtdmhqsibm[_dnggykhath:_dnggykhath + _mjgoydjeyk])
        _dnggykhath += _mjgoydjeyk
    return _uujlgzqxdl.concatenate(_frvfjutfwi)


def _owvggsuuah(_fkirfilttd, _rygwxquibk):
    _whonojyyqk = _tuootdetym(_fkirfilttd) // _rygwxquibk
    _yzmtgqxvgt = _tuootdetym(_fkirfilttd) % _rygwxquibk
    _uicwfppmvk = [_fkirfilttd[_zqdpprjnft * _rygwxquibk:(_zqdpprjnft + 1) *
        _rygwxquibk] for _zqdpprjnft in _ehijdsdomz(_bqvinlbqmm)]
    if _sleorqlrlo > 0:
        _hdofqjgpxo = _fkirfilttd[-_sleorqlrlo:]
        _vhjfyjeqji = _uujlgzqxdl.pad(_vbjpnkvpun, (0, _rygwxquibk -
            _sleorqlrlo), mode='constant', constant_values=0)
        _hjauwpuggk.append(_dfmucswfox)
    return _hjauwpuggk


import os
import numpy as np
import matplotlib.pyplot as plt


def _ubspayccpx(_jshujtkdof, _qjtzoiuzfg, _mvmetuiitk, _arukmygqav,
    _waaffaruba, _joznnxxoit, _pepwqxmqgh, _vllmkxbjzn, _ptmitmtyee,
    _hivazfomgh, _bsatzgcyds, _rnrpmmfrpq, _knmfcaqymu, _sbgmpwdmzt,
    _gqcirrmrxk, _vqlwrbzjnj, _fyldvigioz, _zafgupcdpu, _vlqnbomkjn,
    _kdebfmpili, _fzbbanksws, _qywlikboax, _dqaijjrkqq, _epozzgbfks,
    _tfqazmnkbz, _ymnasmirlx, _jdpaldnwrd, _hyargxrzyk, _yzhhpjohbj,
    _mmipnaipfg, _ldwtdzktxi, _yyewstrpls, _wpbiqnwypa, _zuknygrpsf,
    _giyufdaflm, _dubiqdhmun, _mixsteqhyf, _gfemwmvtpm, _bitfjvmktf,
    _yrpagnckvc, _ullujimozc, _waupouckqu, _azejortcom, _hgvptmvcit,
    _vxfussfyoe, _etttwtwcfu):
    _ogiuxwtwnv = []
    _iebreivwdt = []
    for _yerkyvdcwc in _ehijdsdomz(_qywlikboax):
        _ngpispjyan = _wgstjbvqxv(_uujlgzqxdl.dot(_jshujtkdof, _mvmetuiitk) +
            _arukmygqav)
        _nixfybroqz, _ysoewvmdac, _ysoewvmdac, _ysoewvmdac = _kbwpqrjspt(
            _otvtzcxfus, _gqcirrmrxk, _vqlwrbzjnj)
        _lmsccuhrgq = _wgstjbvqxv(_uujlgzqxdl.dot(_nixfybroqz, _waaffaruba) +
            _joznnxxoit)
        _mgydvsubsa, _ysoewvmdac, _ysoewvmdac, _ysoewvmdac = _kbwpqrjspt(
            _qtzmmclivt, _fyldvigioz, _zafgupcdpu)
        _ffthislmsx = _uujlgzqxdl.round(_wgstjbvqxv(_uujlgzqxdl.dot(
            _mgydvsubsa, _pepwqxmqgh) + _vllmkxbjzn))
        _dixtmfaean, _ysoewvmdac, _ysoewvmdac, _ysoewvmdac = _kbwpqrjspt(
            _zkcvmijfsr, _vlqnbomkjn, _kdebfmpili)
        _ijjungaaif = _wgstjbvqxv(_uujlgzqxdl.dot(_dixtmfaean, _ptmitmtyee) +
            _hivazfomgh)
        _vfmijnzfgu = _wgstjbvqxv(_uujlgzqxdl.dot(_rehxrclshm, _bsatzgcyds) +
            _rnrpmmfrpq)
        _phaydpisna = _wgstjbvqxv(_uujlgzqxdl.dot(_cwwohvtpco, _knmfcaqymu) +
            _sbgmpwdmzt)
        _wzesyqdmbb = _uujlgzqxdl.mean(_uujlgzqxdl.abs(_jshujtkdof -
            _kfmtlartqh))
        _nlyywriozj.append(_zfvjpadhex)
        _eckzlnowqs = _wgstjbvqxv(_uujlgzqxdl.dot(_qjtzoiuzfg, _mvmetuiitk) +
            _arukmygqav)
        _zaettvtyfm, _ysoewvmdac, _ysoewvmdac, _ysoewvmdac = _kbwpqrjspt(
            _ccsetuvaoi, _gqcirrmrxk, _vqlwrbzjnj)
        _teyvsksdes = _wgstjbvqxv(_uujlgzqxdl.dot(_zaettvtyfm, _waaffaruba) +
            _joznnxxoit)
        _jmdznujlcz, _ysoewvmdac, _ysoewvmdac, _ysoewvmdac = _kbwpqrjspt(
            _voosoiisem, _fyldvigioz, _zafgupcdpu)
        _pwoulgwfuk = _uujlgzqxdl.round(_wgstjbvqxv(_uujlgzqxdl.dot(
            _jmdznujlcz, _pepwqxmqgh) + _vllmkxbjzn))
        _xsveshtqlk, _ysoewvmdac, _ysoewvmdac, _ysoewvmdac = _kbwpqrjspt(
            _zwdhnkbhau, _vlqnbomkjn, _kdebfmpili)
        _hlceungfnf = _wgstjbvqxv(_uujlgzqxdl.dot(_xsveshtqlk, _ptmitmtyee) +
            _hivazfomgh)
        _gwwcsugloe = _wgstjbvqxv(_uujlgzqxdl.dot(_vdnvkepgcf, _bsatzgcyds) +
            _rnrpmmfrpq)
        _haqawzavqv = _wgstjbvqxv(_uujlgzqxdl.dot(_ljcvmhxjvl, _knmfcaqymu) +
            _sbgmpwdmzt)
        _amvmpuwraq = _uujlgzqxdl.mean(_uujlgzqxdl.abs(_qjtzoiuzfg -
            _fsryaoqlfu))
        _upwjtvkstj.append(_xkyqzhmaso)
        _bcznnvvbpd = _jshujtkdof - _kfmtlartqh
        _wjpbkroadh = _agvbvhutvq * _ajymesalgr(_kfmtlartqh)
        _njdaubxhbf = _hoalupmegv.dot(_knmfcaqymu.T)
        _nnmbpotrac = _ofauthkyqr * _ajymesalgr(_cwwohvtpco)
        _aiocoarent = _luvbthurvg.dot(_bsatzgcyds.T)
        _jwxxbirqoj = _ipbjsancnl * _ajymesalgr(_rehxrclshm)
        _twnpxrscfm = _zgqobwnlpu.dot(_ptmitmtyee.T)
        _akjrjydxow = _mmumhffkjl * _ajymesalgr(_zkcvmijfsr)
        _qlmeydbzwp = _bsxuoixvqt.dot(_pepwqxmqgh.T)
        _utyjdpdyzq = _vgpbnciauf * _ajymesalgr(_qtzmmclivt)
        _hmhwcguvvv = _vsovzdzjyo.dot(_waaffaruba.T)
        _aavibolgyu = _qfiexzzcep * _ajymesalgr(_otvtzcxfus)
        _knmfcaqymu += _cwwohvtpco.T.dot(_hoalupmegv) * _fzbbanksws
        _sbgmpwdmzt += _uujlgzqxdl.sum(_hoalupmegv, axis=0) * _fzbbanksws
        _bsatzgcyds += _rehxrclshm.T.dot(_luvbthurvg) * _fzbbanksws
        _rnrpmmfrpq += _uujlgzqxdl.sum(_luvbthurvg, axis=0) * _fzbbanksws
        _ptmitmtyee += _zkcvmijfsr.T.dot(_zgqobwnlpu) * _fzbbanksws
        _hivazfomgh += _uujlgzqxdl.sum(_zgqobwnlpu, axis=0) * _fzbbanksws
        _pepwqxmqgh += _qtzmmclivt.T.dot(_bsxuoixvqt) * _fzbbanksws
        _vllmkxbjzn += _uujlgzqxdl.sum(_bsxuoixvqt, axis=0) * _fzbbanksws
        _waaffaruba += _otvtzcxfus.T.dot(_vsovzdzjyo) * _fzbbanksws
        _joznnxxoit += _uujlgzqxdl.sum(_vsovzdzjyo, axis=0) * _fzbbanksws
        _mvmetuiitk += _jshujtkdof.T.dot(_ssjnzqavax) * _fzbbanksws
        _arukmygqav += _uujlgzqxdl.sum(_ssjnzqavax, axis=0) * _fzbbanksws
        _pksclkyoko = _uujlgzqxdl.round(_fsryaoqlfu) == _qjtzoiuzfg
        _yznqedchti = _uujlgzqxdl.mean(_kddcbrpxde)
        if _yerkyvdcwc % 100 == 0:
            _lhknjbxdlf(
                f'Epoch {_yerkyvdcwc}: Training Loss: {_zfvjpadhex}, Validation Loss: {_xkyqzhmaso}, Accuracy: {_ozcsispcyc * 100:.6f}%'
                )
            _mjqcbkiaev = {'encoder_weights0': _mvmetuiitk, 'encoder_bias0':
                _arukmygqav, 'encoder_weights1': _waaffaruba,
                'encoder_bias1': _joznnxxoit, 'encoder_weights2':
                _pepwqxmqgh, 'encoder_bias2': _vllmkxbjzn,
                'decoder_weights1': _ptmitmtyee, 'decoder_bias1':
                _hivazfomgh, 'decoder_weights2': _bsatzgcyds,
                'decoder_bias2': _rnrpmmfrpq, 'decoder_weights3':
                _knmfcaqymu, 'decoder_bias3': _sbgmpwdmzt,
                'm_encoder_weights0': _dqaijjrkqq, 'v_encoder_weights0':
                _epozzgbfks, 'm_encoder_bias0': _tfqazmnkbz,
                'v_encoder_bias0': _ymnasmirlx, 'm_encoder_weights1':
                _jdpaldnwrd, 'v_encoder_weights1': _hyargxrzyk,
                'm_encoder_bias1': _yzhhpjohbj, 'v_encoder_bias1':
                _mmipnaipfg, 'm_encoder_weights2': _ldwtdzktxi,
                'v_encoder_weights2': _yyewstrpls, 'm_encoder_bias2':
                _wpbiqnwypa, 'v_encoder_bias2': _zuknygrpsf,
                'm_decoder_weights1': _giyufdaflm, 'v_decoder_weights1':
                _dubiqdhmun, 'm_decoder_bias1': _mixsteqhyf,
                'v_decoder_bias1': _gfemwmvtpm, 'm_decoder_weights2':
                _bitfjvmktf, 'v_decoder_weights2': _yrpagnckvc,
                'm_decoder_bias2': _ullujimozc, 'v_decoder_bias2':
                _waupouckqu, 'm_decoder_weights3': _azejortcom,
                'v_decoder_weights3': _hgvptmvcit, 'm_decoder_bias3':
                _vxfussfyoe, 'v_decoder_bias3': _etttwtwcfu}
            _stebftiujl(_inblsauurb, _jshujtkdof, _qjtzoiuzfg,
                'autoencoder_model.pkl')
            _gxittfbbdp.close('all')
            _gxittfbbdp.figure(figsize=(5, 5))
            _gxittfbbdp.plot(_nlyywriozj, label='Training Loss')
            _gxittfbbdp.plot(_upwjtvkstj, label='Validation Loss')
            _gxittfbbdp.xlabel('Epoch')
            _gxittfbbdp.ylabel('Loss')
            _gxittfbbdp.title('Training and Validation Losses')
            _gxittfbbdp.legend()
            _gxittfbbdp.show()
            if _uujlgzqxdl.array_equal(_jshujtkdof, _uujlgzqxdl.round(
                _kfmtlartqh)):
                _lhknjbxdlf(
                    f'Original data equals reconstructed data rounded at epoch {_yerkyvdcwc}. Stopping training.'
                    )
                break


def _nwrjawlrqs():
    _bvvkhvjirr = 8200
    _glzsqxnvmj = 8
    _qjjrehmpsg = 0.8
    _tdhcbyncds = 0.0001
    _zltmkagiws = 100000
    _mffhakayor = 8
    _ggjnqlkdre = _uujlgzqxdl.random.randint(0, 2, size=(_aivjamxjkn,
        _mulubdjrri))
    _qxwdbyssdn = _iraygzuyqy(_aivjamxjkn * _yucyhfegym)
    _ewrwwfsgdn = _jgiiotcpjl[:_pzdsrwrwie]
    _efmritnvyl = _jgiiotcpjl[_pzdsrwrwie:]
    _gjsuxqfdaq = _mulubdjrri
    _drkjrcchxd = 64
    _ckrmodghss = 32
    _gkptozeniz = 8 * 2
    _tlcxlnpvgn = 32
    _kdkdwaxlpd = 64
    _qdbnvztwak = _xteuhkhjoa
    if _ihshtncdju.path.exists('autoencoder_model.pkl'):
        _inblsauurb, _jshujtkdof, _qjtzoiuzfg = _hirowbsbph(
            'autoencoder_model.pkl')
        _bhvrnmarzt = _inblsauurb['encoder_weights0']
        _tarlqptzke = _inblsauurb['encoder_bias0']
        _rsjcnzkdgw = _inblsauurb['encoder_weights1']
        _rfoiogyndl = _inblsauurb['encoder_bias1']
        _xugmutlfph = _inblsauurb['encoder_weights2']
        _gkgpfcgsqu = _inblsauurb['encoder_bias2']
        _lkwpshqvnh = _inblsauurb['decoder_weights1']
        _yyeslkdpsc = _inblsauurb['decoder_bias1']
        _cglardqywt = _inblsauurb['decoder_weights2']
        _hkjrterlxg = _inblsauurb['decoder_bias2']
        _awidqjknfi = _inblsauurb['decoder_weights3']
        _myeedqlxjx = _inblsauurb['decoder_bias3']
        _qndwfwxoiv = _inblsauurb['m_encoder_weights0']
        _tffhjkgpfd = _inblsauurb['v_encoder_weights0']
        _wmmryqcnjz = _inblsauurb['m_encoder_bias0']
        _ylrjsonnlw = _inblsauurb['v_encoder_bias0']
        _kcolmtmdjp = _inblsauurb['m_encoder_weights1']
        _exhozudpzl = _inblsauurb['v_encoder_weights1']
        _rxpiglsoap = _inblsauurb['m_encoder_bias1']
        _ykmzrcxnfg = _inblsauurb['v_encoder_bias1']
        _fjsduwxjgo = _inblsauurb['m_encoder_weights2']
        _kmdrjlhrzx = _inblsauurb['v_encoder_weights2']
        _mnicmlckrz = _inblsauurb['m_encoder_bias2']
        _rruzkmbqye = _inblsauurb['v_encoder_bias2']
        _fizksklvof = _inblsauurb['m_decoder_weights1']
        _itgtxicusk = _inblsauurb['v_decoder_weights1']
        _rqbqyxdiar = _inblsauurb['m_decoder_bias1']
        _tnicxtjeus = _inblsauurb['v_decoder_bias1']
        _rdnrnntgnw = _inblsauurb['m_decoder_weights2']
        _grzqgrntvb = _inblsauurb['v_decoder_weights2']
        _kqxbmsrqnh = _inblsauurb['m_decoder_bias2']
        _mpsftnchev = _inblsauurb['v_decoder_bias2']
        _jvpmgpnzxj = _inblsauurb['m_decoder_weights3']
        _puyrjnhjbq = _inblsauurb['v_decoder_weights3']
        _julgfnqtms = _inblsauurb['m_decoder_bias3']
        _kdknjvzjtt = _inblsauurb['v_decoder_bias3']
    else:
        _bhvrnmarzt = _uujlgzqxdl.random.randn(_xteuhkhjoa, _hxnvuwhxpp)
        _tarlqptzke = _uujlgzqxdl.zeros(_hxnvuwhxpp)
        _rsjcnzkdgw = _uujlgzqxdl.random.randn(_hxnvuwhxpp, _hmztufedrn)
        _rfoiogyndl = _uujlgzqxdl.zeros(_hmztufedrn)
        _xugmutlfph = _uujlgzqxdl.random.randn(_hmztufedrn, _slapznuriv)
        _gkgpfcgsqu = _uujlgzqxdl.zeros(_slapznuriv)
        _lkwpshqvnh = _uujlgzqxdl.random.randn(_slapznuriv, _zllqgtpncz)
        _yyeslkdpsc = _uujlgzqxdl.zeros(_zllqgtpncz)
        _cglardqywt = _uujlgzqxdl.random.randn(_zllqgtpncz, _ybydxfxnjc)
        _hkjrterlxg = _uujlgzqxdl.zeros(_ybydxfxnjc)
        _awidqjknfi = _uujlgzqxdl.random.randn(_ybydxfxnjc, _miqowevgad)
        _myeedqlxjx = _uujlgzqxdl.zeros(_miqowevgad)
        _qndwfwxoiv = _uujlgzqxdl.zeros_like(_mvmetuiitk)
        _tffhjkgpfd = _uujlgzqxdl.zeros_like(_mvmetuiitk)
        _wmmryqcnjz = _uujlgzqxdl.zeros_like(_arukmygqav)
        _ylrjsonnlw = _uujlgzqxdl.zeros_like(_arukmygqav)
        _kcolmtmdjp = _uujlgzqxdl.zeros_like(_waaffaruba)
        _exhozudpzl = _uujlgzqxdl.zeros_like(_waaffaruba)
        _rxpiglsoap = _uujlgzqxdl.zeros_like(_joznnxxoit)
        _ykmzrcxnfg = _uujlgzqxdl.zeros_like(_joznnxxoit)
        _fjsduwxjgo = _uujlgzqxdl.zeros_like(_pepwqxmqgh)
        _kmdrjlhrzx = _uujlgzqxdl.zeros_like(_pepwqxmqgh)
        _mnicmlckrz = _uujlgzqxdl.zeros_like(_vllmkxbjzn)
        _rruzkmbqye = _uujlgzqxdl.zeros_like(_vllmkxbjzn)
        _fizksklvof = _uujlgzqxdl.zeros_like(_ptmitmtyee)
        _itgtxicusk = _uujlgzqxdl.zeros_like(_ptmitmtyee)
        _rqbqyxdiar = _uujlgzqxdl.zeros_like(_hivazfomgh)
        _tnicxtjeus = _uujlgzqxdl.zeros_like(_hivazfomgh)
        _rdnrnntgnw = _uujlgzqxdl.zeros_like(_bsatzgcyds)
        _grzqgrntvb = _uujlgzqxdl.zeros_like(_bsatzgcyds)
        _kqxbmsrqnh = _uujlgzqxdl.zeros_like(_rnrpmmfrpq)
        _mpsftnchev = _uujlgzqxdl.zeros_like(_rnrpmmfrpq)
        _jvpmgpnzxj = _uujlgzqxdl.zeros_like(_knmfcaqymu)
        _puyrjnhjbq = _uujlgzqxdl.zeros_like(_knmfcaqymu)
        _julgfnqtms = _uujlgzqxdl.zeros_like(_sbgmpwdmzt)
        _kdknjvzjtt = _uujlgzqxdl.zeros_like(_sbgmpwdmzt)
    _qneygtljci = _uujlgzqxdl.ones(_hxnvuwhxpp)
    _kqbzqugohx = _uujlgzqxdl.zeros(_hxnvuwhxpp)
    _gxqmiefrpg = _uujlgzqxdl.ones(_hmztufedrn)
    _rrmdeciyhp = _uujlgzqxdl.zeros(_hmztufedrn)
    _mrzooxwzbq = _uujlgzqxdl.ones(_slapznuriv)
    _nxfbkfbqdc = _uujlgzqxdl.zeros(_slapznuriv)
    _gravumnsqf(_jshujtkdof, _qjtzoiuzfg, _mvmetuiitk, _arukmygqav,
        _waaffaruba, _joznnxxoit, _pepwqxmqgh, _vllmkxbjzn, _ptmitmtyee,
        _hivazfomgh, _bsatzgcyds, _rnrpmmfrpq, _knmfcaqymu, _sbgmpwdmzt,
        _gqcirrmrxk, _vqlwrbzjnj, _fyldvigioz, _zafgupcdpu, _vlqnbomkjn,
        _kdebfmpili, _fzbbanksws, _qywlikboax, _dqaijjrkqq, _epozzgbfks,
        _tfqazmnkbz, _ymnasmirlx, _jdpaldnwrd, _hyargxrzyk, _yzhhpjohbj,
        _mmipnaipfg, _ldwtdzktxi, _yyewstrpls, _wpbiqnwypa, _zuknygrpsf,
        _giyufdaflm, _dubiqdhmun, _mixsteqhyf, _gfemwmvtpm, _bitfjvmktf,
        _yrpagnckvc, _ullujimozc, _waupouckqu, _azejortcom, _hgvptmvcit,
        _vxfussfyoe, _etttwtwcfu)
    _mjqcbkiaev = {'encoder_weights0': _mvmetuiitk, 'encoder_bias0':
        _arukmygqav, 'encoder_weights1': _waaffaruba, 'encoder_bias1':
        _joznnxxoit, 'encoder_weights2': _pepwqxmqgh, 'encoder_bias2':
        _vllmkxbjzn, 'decoder_weights1': _ptmitmtyee, 'decoder_bias1':
        _hivazfomgh, 'decoder_weights2': _bsatzgcyds, 'decoder_bias2':
        _rnrpmmfrpq, 'decoder_weights3': _knmfcaqymu, 'decoder_bias3':
        _sbgmpwdmzt, 'm_encoder_weights0': _dqaijjrkqq,
        'v_encoder_weights0': _epozzgbfks, 'm_encoder_bias0': _tfqazmnkbz,
        'v_encoder_bias0': _ymnasmirlx, 'm_encoder_weights1': _jdpaldnwrd,
        'v_encoder_weights1': _hyargxrzyk, 'm_encoder_bias1': _yzhhpjohbj,
        'v_encoder_bias1': _mmipnaipfg, 'm_encoder_weights2': _ldwtdzktxi,
        'v_encoder_weights2': _yyewstrpls, 'm_encoder_bias2': _wpbiqnwypa,
        'v_encoder_bias2': _zuknygrpsf, 'm_decoder_weights1': _giyufdaflm,
        'v_decoder_weights1': _dubiqdhmun, 'm_decoder_bias1': _mixsteqhyf,
        'v_decoder_bias1': _gfemwmvtpm, 'm_decoder_weights2': _bitfjvmktf,
        'v_decoder_weights2': _yrpagnckvc, 'm_decoder_bias2': _ullujimozc,
        'v_decoder_bias2': _waupouckqu, 'm_decoder_weights3': _azejortcom,
        'v_decoder_weights3': _hgvptmvcit, 'm_decoder_bias3': _vxfussfyoe,
        'v_decoder_bias3': _etttwtwcfu}
    _stebftiujl(_inblsauurb, _jshujtkdof, _qjtzoiuzfg, 'autoencoder_model.pkl')
    _fnnthsjezw = 'test'
    with _ptwpkzuhmb(_hyugiplohi, 'rb') as _rtdssbylrf:
        _audaayzedf = _rtdssbylrf.read()
    _wfxyigaxbl = _dfbrdbnprx(_vsfrikuume)
    _aspdfhljsg = _xklxwdlpbf(_svzgtjavxv, _rygwxquibk)
    _xueukkrdaf = []
    _kgumoylqhx = []
    for _zqdpprjnft, _zsvczpdjam in _dwqoeaxrgf(_lqgplffvud):
        _nwunjdhpls = _uujlgzqxdl.array(_qyjxxjezjd(_zsvczpdjam), dtype=
            _uujlgzqxdl.uint8)
        _nwunjdhpls = _uujlgzqxdl.expand_dims(_zsvczpdjam, axis=0)
        _teyvsksdes = _wgstjbvqxv(_uujlgzqxdl.dot(_zsvczpdjam, _waaffaruba) +
            _joznnxxoit)
        _pwoulgwfuk = _wgstjbvqxv(_uujlgzqxdl.dot(_voosoiisem, _pepwqxmqgh) +
            _vllmkxbjzn)
        _nwvcsvxlza = _zwdhnkbhau
        _hlceungfnf = _wgstjbvqxv(_uujlgzqxdl.dot(_ihccktdauw, _ptmitmtyee) +
            _hivazfomgh)
        _haqawzavqv = _wgstjbvqxv(_uujlgzqxdl.dot(_vdnvkepgcf, _bsatzgcyds) +
            _rnrpmmfrpq)
        _peimdoewht = _fsryaoqlfu
        _lhknjbxdlf(f'{_zqdpprjnft}/{_tuootdetym(_lqgplffvud)}')
        _peimdoewht = _tecbvuuexz(_xplnpiumkv.squeeze(), [8])
        _rtdmhqsibm.append(_xplnpiumkv)
        _fnjjgrrwqk.append(_tuootdetym(_zsvczpdjam[0]))
    _wqhkceedqq = _uujlgzqxdl.array(_rtdmhqsibm)
    _inepbttcad = _bbqdkgotwj.astype(_uujlgzqxdl.float64)
    _kesgfmswsk = _bjgkinyqkg.tobytes()
    with _ptwpkzuhmb(f'{_hyugiplohi}.AIZip', 'wb') as _mgddkuvvkg:
        _mgddkuvvkg.write(_lgcmustddp)
    _fnnthsjezw = f'{_hyugiplohi}.AIZip'
    if _hyugiplohi and _hyugiplohi.endswith('.AIZip'):
        with _ptwpkzuhmb(_hyugiplohi, 'rb') as _mgddkuvvkg:
            _kesgfmswsk = _mgddkuvvkg.read()
        _inepbttcad = _uujlgzqxdl.frombuffer(_lgcmustddp, dtype=_uujlgzqxdl
            .float64)
        _rtmbqpfpif = 4
        _whonojyyqk = _tuootdetym(_bjgkinyqkg) // _uuhxmncwcn
        _wqhkceedqq = _bjgkinyqkg[:_bqvinlbqmm * _uuhxmncwcn].reshape((
            _bqvinlbqmm, _uuhxmncwcn))
        _ilhgcnqylo = []
        _xueukkrdaf = []
        for _zqdpprjnft, _zsvczpdjam in _dwqoeaxrgf(_bbqdkgotwj):
            _nwunjdhpls = _uujlgzqxdl.expand_dims(_zsvczpdjam, axis=0)
            _hlceungfnf = _wgstjbvqxv(_uujlgzqxdl.dot(_zsvczpdjam,
                _ptmitmtyee) + _hivazfomgh)
            _haqawzavqv = _wgstjbvqxv(_uujlgzqxdl.dot(_vdnvkepgcf,
                _bsatzgcyds) + _rnrpmmfrpq)
            _peimdoewht = _fsryaoqlfu
            _lhknjbxdlf(f'{_zqdpprjnft}/{_tuootdetym(_bbqdkgotwj)}')
            _peimdoewht = _tecbvuuexz(_xplnpiumkv.squeeze(), [8])
            _rtdmhqsibm.append(_xplnpiumkv)
        _xueukkrdaf = _uujlgzqxdl.round(_rtdmhqsibm, 0)
        _xueukkrdaf = _rtdmhqsibm.astype(_uujlgzqxdl.uint8)
        _xueukkrdaf = [''.join(_lwlyobcfef(_khxreyoqrr, _lwlyobcfef(
            _gcapapmlcc, _jkuddlbvnv))) for _jkuddlbvnv in _rtdmhqsibm]
        _mxmuowolhz = [_ypjjjfudms(_jkuddlbvnv, 8) for _jkuddlbvnv in
            _rtdmhqsibm]
        _qndzypijwt = _fxaermgcyu([_iraygzuyqy(_jkuddlbvnv, 2) for
            _cibdyelfor in _ahywaovcfc for _jkuddlbvnv in _cibdyelfor])
        with _ptwpkzuhmb(_hyugiplohi[:-6], 'wb') as _mgddkuvvkg:
            _mgddkuvvkg.write(_hlzoostdnu)


if _rjljvaydqs == '__main__':
    _ipizkvuody()
