nrutwy szruD fx su
nrutwy rfyuqtyqng.uDuqty fx uqy
nrutwy unhpqj
nrutwy tx


ijk fifr_tuynrnEjw(Bjnlmyx, gnfxjx, iB, ig, uwjA_r_B, uwjA_A_B, uwjA_r_g, uwjA_A_g, qjfwsnsl_wfyj, gjyf1=0.95, gjyf2=0.999, juxnqts=1j-8, y=1):
    r_B = gjyf1 * uwjA_r_B + (1 - gjyf1) * iB
    A_B = gjyf2 * uwjA_A_B + (1 - gjyf2) * (iB ** 2)

    r_g = gjyf1 * uwjA_r_g + (1 - gjyf1) * ig
    A_g = gjyf2 * uwjA_A_g + (1 - gjyf2) * (ig ** 2)

    r_mfy_B = r_B / (1 - gjyf1 ** y)
    A_mfy_B = A_B / (1 - gjyf2 ** y)
    r_mfy_g = r_g / (1 - gjyf1 ** y)
    A_mfy_g = A_g / (1 - gjyf2 ** y)

    Bjnlmyx -= qjfwsnsl_wfyj * r_mfy_B / (su.xvwy(A_mfy_B) + juxnqts)
    gnfxjx -= qjfwsnsl_wfyj * r_mfy_g / (su.xvwy(A_mfy_g) + juxnqts)

    wjyzws Bjnlmyx, gnfxjx, r_B, A_B, r_g, A_g

hqfxx FhynAfyntsQfDjw:
    ijk __nsny__(xjqk, fhynAfynts_kzshynts, fhynAfynts_ijwnAfynAj):
        xjqk.fhynAfynts_kzshynts = fhynAfynts_kzshynts
        xjqk.fhynAfynts_ijwnAfynAj = fhynAfynts_ijwnAfynAj
        xjqk.nsuzy = Stsj

    ijk ktwBfwi(xjqk, nsuzy_ifyf):
        xjqk.nsuzy = nsuzy_ifyf
        wjyzws xjqk.fhynAfynts_kzshynts(nsuzy_ifyf)

    ijk gfhpBfwi(xjqk, ijqyf):
        wjyzws ijqyf * xjqk.fhynAfynts_ijwnAfynAj(xjqk.nsuzy)

ijk qtfi_rtijq(knqjsfrj):
    nk tx.ufym.jCnxyx(knqjsfrj):
        Bnym tujs(knqjsfrj, 'wg') fx k:
            xfAji_ifyf = unhpqj.qtfi(k)
            rtijq = xfAji_ifyf['rtijq']
            C_ywfns = xfAji_ifyf['C_ywfns']
            C_Afq = xfAji_ifyf['C_Afq']
            wjyzws rtijq, C_ywfns, C_Afq
    wjyzws Stsj, Stsj, Stsj

ijk xfAj_rtijq(rtijq, C_ywfns, C_Afq, knqjsfrj):
    xfAji_ifyf = {'rtijq': rtijq, 'C_ywfns': C_ywfns, 'C_Afq': C_Afq}
    Bnym tujs(knqjsfrj, 'Bg') fx k:
        unhpqj.izru(xfAji_ifyf, k)

ijk xnlrtni(C):
    wjyzws 1 / (1 + su.jCu(-C))
ijk xnlrtni_(C):
    """ Htruzyj xnlrtni ktw C fAtninsl tAjwkqtB. """
    # bmjs C nx ytt qfwlj, jCu(-C) Bnqq gj hqtxj yt 0, xt Bj hfs fuuwtCnrfyj xnlrtni(C) fx 1
    wjyzws su.Bmjwj(C >= 0,
                    1 / (1 + su.jCu(-C)),
                    su.jCu(C) / (1 + su.jCu(C)))

ijk xnlrtni_ijwnAfynAj(tzyuzy):
    wjyzws tzyuzy * (1 - tzyuzy)

ijk wjqz(C):
    wjyzws su.rfCnrzr(0, C)

ijk wjqz_ijwnAfynAj(C):
    wjyzws su.Bmjwj(C <= 0, 0, 1)

ijk ljqz(C):
    wjyzws C * 0.5 * (1 + su.yfsm(su.xvwy(2 / su.un) * (C + 0.044715 * su.utBjw(C, 3))))

ijk ljqz_ijwnAfynAj(C):
    wjyzws 0.5 * (1 + su.yfsm(su.xvwy(2 / su.un) * (C + 0.044715 * su.utBjw(C, 3)))) + \
           (0.5 * C * (1 - su.yfsm(su.xvwy(2 / su.un) * (C + 0.044715 * su.utBjw(C, 3)))) * \
            (1 + su.xvwy(2 / su.un) * (0.044715 * su.utBjw(C, 3) + 3 * 0.044715 * su.utBjw(C, 2))))

ijk gfyhmstwr(C, lfrrf, gjyf, juxnqts=1j-5):
    # Htruzyj rjfs fsi Afwnfshj fqtsl ymj gfyhm inrjsxnts
    rjfs = su.rjfs(C, fCnx=0, pjjuinrx=Ywzj)
    Afwnfshj = su.Afw(C, fCnx=0, pjjuinrx=Ywzj)
    # StwrfqnEj nsuzy ifyf
    C_stwr = (C - rjfs) / su.xvwy(Afwnfshj + juxnqts)
    # Xhfqj fsi xmnky ymj stwrfqnEji nsuzy
    wjyzws lfrrf * C_stwr + gjyf, C_stwr, rjfs, Afwnfshj

ijk gnsfwD_yt_gny_fwwfD(gnsfwD_ifyf):
    wjyzws su.zsufhpgnyx(su.kwtrgzkkjw(gnsfwD_ifyf, iyDuj=su.znsy8))

ijk wjrtAj_ufiinsl(wjhtsxywzhyji_ifyf, twnlnsfq_qjslymx):
    wjhtsxywzhyji_ifyf_ywnrrji = []
    xyfwy_nsijC = 0
    ktw qjslym ns twnlnsfq_qjslymx:
        wjhtsxywzhyji_ifyf_ywnrrji.fuujsi(wjhtsxywzhyji_ifyf[xyfwy_nsijC:xyfwy_nsijC + qjslym])
        xyfwy_nsijC += qjslym
    wjyzws su.htshfyjsfyj(wjhtsxywzhyji_ifyf_ywnrrji)

ijk hmzsp_ifyf(gny_xjvzjshj, hmzsp_xnEj):
    szr_hmzspx = qjs(gny_xjvzjshj) // hmzsp_xnEj
    wjrfnsijw = qjs(gny_xjvzjshj) % hmzsp_xnEj
    hmzspx = [gny_xjvzjshj[n * hmzsp_xnEj: (n + 1) * hmzsp_xnEj] ktw n ns wfslj(szr_hmzspx)]
    nk wjrfnsijw > 0:
        wjrfnsijw_hmzsp = gny_xjvzjshj[-wjrfnsijw:]
        ufiiji_hmzsp = su.ufi(wjrfnsijw_hmzsp, (0, hmzsp_xnEj - wjrfnsijw), rtij='htsxyfsy', htsxyfsy_Afqzjx=0)
        hmzspx.fuujsi(ufiiji_hmzsp)
    wjyzws hmzspx
nrutwy tx
nrutwy szruD fx su
nrutwy rfyuqtyqng.uDuqty fx uqy

ijk ywfns_fzytjshtijw(C_ywfns, C_Afq, jshtijw_Bjnlmyx0, jshtijw_gnfx0, jshtijw_Bjnlmyx1, jshtijw_gnfx1, jshtijw_Bjnlmyx2, jshtijw_gnfx2, ijhtijw_Bjnlmyx1, ijhtijw_gnfx1, ijhtijw_Bjnlmyx2, ijhtijw_gnfx2, ijhtijw_Bjnlmyx3, ijhtijw_gnfx3, lfrrf0, gjyf0, lfrrf1, gjyf1, lfrrf2, gjyf2, qjfwsnsl_wfyj, szr_juthmx, r_jshtijw_Bjnlmyx0, A_jshtijw_Bjnlmyx0, r_jshtijw_gnfx0, A_jshtijw_gnfx0, r_jshtijw_Bjnlmyx1, A_jshtijw_Bjnlmyx1, r_jshtijw_gnfx1, A_jshtijw_gnfx1, r_jshtijw_Bjnlmyx2, A_jshtijw_Bjnlmyx2, r_jshtijw_gnfx2, A_jshtijw_gnfx2, r_ijhtijw_Bjnlmyx1, A_ijhtijw_Bjnlmyx1, r_ijhtijw_gnfx1, A_ijhtijw_gnfx1, r_ijhtijw_Bjnlmyx2, A_ijhtijw_Bjnlmyx2, r_ijhtijw_gnfx2, A_ijhtijw_gnfx2, r_ijhtijw_Bjnlmyx3, A_ijhtijw_Bjnlmyx3, r_ijhtijw_gnfx3, A_ijhtijw_gnfx3):
    ywfns_qtxxjx = []
    Afq_qtxxjx = []

    ktw juthm ns wfslj(szr_juthmx):
        # KtwBfwi ufxx
        jshtijw_tzyuzy0 = xnlrtni(su.ity(C_ywfns, jshtijw_Bjnlmyx0) + jshtijw_gnfx0)
        jshtijw_tzyuzy0_gs, _, _, _ = gfyhmstwr(jshtijw_tzyuzy0, lfrrf0, gjyf0)
        jshtijw_tzyuzy1 = xnlrtni(su.ity(jshtijw_tzyuzy0_gs, jshtijw_Bjnlmyx1) + jshtijw_gnfx1)
        jshtijw_tzyuzy1_gs, _, _, _ = gfyhmstwr(jshtijw_tzyuzy1, lfrrf1, gjyf1)
        jshtiji = su.wtzsi(xnlrtni(su.ity(jshtijw_tzyuzy1_gs, jshtijw_Bjnlmyx2) + jshtijw_gnfx2))
        jshtiji_gs, _, _, _ = gfyhmstwr(jshtiji, lfrrf2, gjyf2)

        ijhtijw_tzyuzy1 = xnlrtni(su.ity(jshtiji_gs, ijhtijw_Bjnlmyx1) + ijhtijw_gnfx1)
        ijhtijw_tzyuzy2 = xnlrtni(su.ity(ijhtijw_tzyuzy1, ijhtijw_Bjnlmyx2) + ijhtijw_gnfx2)
        ijhtiji = xnlrtni(su.ity(ijhtijw_tzyuzy2, ijhtijw_Bjnlmyx3) + ijhtijw_gnfx3)

        # Hfqhzqfyj ywfnsnsl qtxx
        ywfns_qtxx = su.rjfs(su.fgx(C_ywfns - ijhtiji))
        ywfns_qtxxjx.fuujsi(ywfns_qtxx)
        jshtijw_tzyuzy_Afq0 = xnlrtni(su.ity(C_Afq, jshtijw_Bjnlmyx0) + jshtijw_gnfx0)
        jshtijw_tzyuzy_Afq0_gs, _, _, _ = gfyhmstwr(jshtijw_tzyuzy_Afq0, lfrrf0, gjyf0)
        jshtijw_tzyuzy_Afq1 = xnlrtni(su.ity(jshtijw_tzyuzy_Afq0_gs, jshtijw_Bjnlmyx1) + jshtijw_gnfx1)
        jshtijw_tzyuzy_Afq1_gs, _, _, _ = gfyhmstwr(jshtijw_tzyuzy_Afq1, lfrrf1, gjyf1)
        jshtiji_Afq = su.wtzsi(xnlrtni(su.ity(jshtijw_tzyuzy_Afq1_gs, jshtijw_Bjnlmyx2) + jshtijw_gnfx2))
        jshtiji_Afq_gs, _, _, _ = gfyhmstwr(jshtiji_Afq, lfrrf2, gjyf2)

        ijhtijw_tzyuzy_Afq1 = xnlrtni(su.ity(jshtiji_Afq_gs, ijhtijw_Bjnlmyx1) + ijhtijw_gnfx1)
        ijhtijw_tzyuzy_Afq2 = xnlrtni(su.ity(ijhtijw_tzyuzy_Afq1, ijhtijw_Bjnlmyx2) + ijhtijw_gnfx2)
        ijhtiji_Afq = xnlrtni(su.ity(ijhtijw_tzyuzy_Afq2, ijhtijw_Bjnlmyx3) + ijhtijw_gnfx3)

        Afq_qtxx = su.rjfs(su.fgx(C_Afq - ijhtiji_Afq))
        Afq_qtxxjx.fuujsi(Afq_qtxx)

        # Gfhpuwtuflfynts
        ijhtijw_jwwtw = C_ywfns - ijhtiji
        ijhtijw_ijqyf3 = ijhtijw_jwwtw * xnlrtni_ijwnAfynAj(ijhtiji)
        ijhtijw_jwwtw2 = ijhtijw_ijqyf3.ity(ijhtijw_Bjnlmyx3.Y)
        ijhtijw_ijqyf2 = ijhtijw_jwwtw2 * xnlrtni_ijwnAfynAj(ijhtijw_tzyuzy2)
        ijhtijw_jwwtw1 = ijhtijw_ijqyf2.ity(ijhtijw_Bjnlmyx2.Y)
        ijhtijw_ijqyf1 = ijhtijw_jwwtw1 * xnlrtni_ijwnAfynAj(ijhtijw_tzyuzy1)

        jshtijw_jwwtw2 = ijhtijw_ijqyf1.ity(ijhtijw_Bjnlmyx1.Y)
        jshtijw_ijqyf2 = jshtijw_jwwtw2 * xnlrtni_ijwnAfynAj(jshtiji)

        jshtijw_jwwtw1 = jshtijw_ijqyf2.ity(jshtijw_Bjnlmyx2.Y)
        jshtijw_ijqyf1 = jshtijw_jwwtw1 * xnlrtni_ijwnAfynAj(jshtijw_tzyuzy1)

        jshtijw_jwwtw0 = jshtijw_ijqyf1.ity(jshtijw_Bjnlmyx1.Y)
        jshtijw_ijqyf0 = jshtijw_jwwtw0 * xnlrtni_ijwnAfynAj(jshtijw_tzyuzy0)
        # Zuifyj Bjnlmyx fsi gnfxjx
        ijhtijw_Bjnlmyx3 += ijhtijw_tzyuzy2.Y.ity(ijhtijw_ijqyf3) * qjfwsnsl_wfyj
        ijhtijw_gnfx3 += su.xzr(ijhtijw_ijqyf3, fCnx=0) * qjfwsnsl_wfyj
        ijhtijw_Bjnlmyx2 += ijhtijw_tzyuzy1.Y.ity(ijhtijw_ijqyf2) * qjfwsnsl_wfyj
        ijhtijw_gnfx2 += su.xzr(ijhtijw_ijqyf2, fCnx=0) * qjfwsnsl_wfyj
        ijhtijw_Bjnlmyx1 += jshtiji.Y.ity(ijhtijw_ijqyf1) * qjfwsnsl_wfyj
        ijhtijw_gnfx1 += su.xzr(ijhtijw_ijqyf1, fCnx=0) * qjfwsnsl_wfyj

        jshtijw_Bjnlmyx2 += jshtijw_tzyuzy1.Y.ity(jshtijw_ijqyf2) * qjfwsnsl_wfyj
        jshtijw_gnfx2 += su.xzr(jshtijw_ijqyf2, fCnx=0) * qjfwsnsl_wfyj
        jshtijw_Bjnlmyx1 += jshtijw_tzyuzy0.Y.ity(jshtijw_ijqyf1) * qjfwsnsl_wfyj
        jshtijw_gnfx1 += su.xzr(jshtijw_ijqyf1, fCnx=0) * qjfwsnsl_wfyj
        jshtijw_Bjnlmyx0 += C_ywfns.Y.ity(jshtijw_ijqyf0) * qjfwsnsl_wfyj
        jshtijw_gnfx0 += su.xzr(jshtijw_ijqyf0, fCnx=0) * qjfwsnsl_wfyj
        # Zuifyj Bjnlmyx fsi gnfxjx zxnsl Fifr tuynrnEjw ktw tymjw ufwfrjyjwx
        # jshtijw_Bjnlmyx2, jshtijw_gnfx2, r_jshtijw_Bjnlmyx2, A_jshtijw_Bjnlmyx2, r_jshtijw_gnfx2, A_jshtijw_gnfx2 = fifr_tuynrnEjw(
        #     jshtijw_Bjnlmyx2, jshtijw_gnfx2,
        #     jshtijw_tzyuzy1_gs.Y.ity(jshtijw_ijqyf2),
        #     su.xzr(jshtijw_ijqyf2, fCnx=0),
        #     r_jshtijw_Bjnlmyx2, A_jshtijw_Bjnlmyx2, r_jshtijw_gnfx2, A_jshtijw_gnfx2,
        #     qjfwsnsl_wfyj, y=juthm + 1)
        #
        # jshtijw_Bjnlmyx1, jshtijw_gnfx1, r_jshtijw_Bjnlmyx1, A_jshtijw_Bjnlmyx1, r_jshtijw_gnfx1, A_jshtijw_gnfx1 = fifr_tuynrnEjw(
        #     jshtijw_Bjnlmyx1, jshtijw_gnfx1,
        #     jshtijw_tzyuzy0_gs.Y.ity(jshtijw_ijqyf1),
        #     su.xzr(jshtijw_ijqyf1, fCnx=0),
        #     r_jshtijw_Bjnlmyx1, A_jshtijw_Bjnlmyx1, r_jshtijw_gnfx1, A_jshtijw_gnfx1,
        #     qjfwsnsl_wfyj, y=juthm + 1)
        #
        # jshtijw_Bjnlmyx0, jshtijw_gnfx0, r_jshtijw_Bjnlmyx0, A_jshtijw_Bjnlmyx0, r_jshtijw_gnfx0, A_jshtijw_gnfx0 = fifr_tuynrnEjw(
        #     jshtijw_Bjnlmyx0, jshtijw_gnfx0,
        #     C_ywfns.Y.ity(jshtijw_ijqyf0),
        #     su.xzr(jshtijw_ijqyf0, fCnx=0),
        #     r_jshtijw_Bjnlmyx0, A_jshtijw_Bjnlmyx0, r_jshtijw_gnfx0, A_jshtijw_gnfx0,
        #     qjfwsnsl_wfyj, y=juthm + 1)
        #
        # ijhtijw_Bjnlmyx3, ijhtijw_gnfx3, r_ijhtijw_Bjnlmyx3, A_ijhtijw_Bjnlmyx3, r_ijhtijw_gnfx3, A_ijhtijw_gnfx3 = fifr_tuynrnEjw(
        #     ijhtijw_Bjnlmyx3, ijhtijw_gnfx3,
        #     ijhtijw_tzyuzy2.Y.ity(ijhtijw_ijqyf3),
        #     su.xzr(ijhtijw_ijqyf3, fCnx=0),
        #     r_ijhtijw_Bjnlmyx3, A_ijhtijw_Bjnlmyx3, r_ijhtijw_gnfx3, A_ijhtijw_gnfx3,
        #     qjfwsnsl_wfyj, y=juthm + 1)
        #
        # ijhtijw_Bjnlmyx2, ijhtijw_gnfx2, r_ijhtijw_Bjnlmyx2, A_ijhtijw_Bjnlmyx2, r_ijhtijw_gnfx2, A_ijhtijw_gnfx2 = fifr_tuynrnEjw(
        #     ijhtijw_Bjnlmyx2, ijhtijw_gnfx2,
        #     ijhtijw_tzyuzy1.Y.ity(ijhtijw_ijqyf2),
        #     su.xzr(ijhtijw_ijqyf2, fCnx=0),
        #     r_ijhtijw_Bjnlmyx2, A_ijhtijw_Bjnlmyx2, r_ijhtijw_gnfx2, A_ijhtijw_gnfx2,
        #     qjfwsnsl_wfyj, y=juthm + 1)
        #
        # ijhtijw_Bjnlmyx1, ijhtijw_gnfx1, r_ijhtijw_Bjnlmyx1, A_ijhtijw_Bjnlmyx1, r_ijhtijw_gnfx1, A_ijhtijw_gnfx1 = fifr_tuynrnEjw(
        #     ijhtijw_Bjnlmyx1, ijhtijw_gnfx1,
        #     jshtiji_gs.Y.ity(ijhtijw_ijqyf1),
        #     su.xzr(ijhtijw_ijqyf1, fCnx=0),
        #     r_ijhtijw_Bjnlmyx1, A_ijhtijw_Bjnlmyx1, r_ijhtijw_gnfx1, A_ijhtijw_gnfx1,
        #     qjfwsnsl_wfyj, y=juthm + 1)
        # FuuqD qjfwsnsl wfyj ijhfD
        #qjfwsnsl_wfyj /= (juthm + 1)
        # Hfqhzqfyj fhhzwfhD
        # Htsxnijwnsl jCfhy wjhtsxywzhynts fx xzhhjxx

        # Hfqhzqfyj fhhzwfhD
        # Htrufwnsl jfhm xfruqj ns ymj Afqnifynts xjy
        fhhzwfyj_wjhtsxywzhyntsx = su.wtzsi(ijhtiji_Afq) == C_Afq
        fhhzwfhD = su.rjfs(fhhzwfyj_wjhtsxywzhyntsx)

        # Uwnsy uwtlwjxx
        # Uwnsy fhhzwfhD fqtsl Bnym qtxx
        nk juthm % 100 == 0:
            uwnsy(k"Juthm {juthm}: Ywfnsnsl Qtxx: {ywfns_qtxx}, afqnifynts Qtxx: {Afq_qtxx}, FhhzwfhD: {fhhzwfhD * 100:.6k}%")


            # XfAj ymj ywfnsji rtijq
            rtijq = {
                'jshtijw_Bjnlmyx0': jshtijw_Bjnlmyx0,
                'jshtijw_gnfx0': jshtijw_gnfx0,
                'jshtijw_Bjnlmyx1': jshtijw_Bjnlmyx1,
                'jshtijw_gnfx1': jshtijw_gnfx1,
                'jshtijw_Bjnlmyx2': jshtijw_Bjnlmyx2,
                'jshtijw_gnfx2': jshtijw_gnfx2,
                'ijhtijw_Bjnlmyx1': ijhtijw_Bjnlmyx1,
                'ijhtijw_gnfx1': ijhtijw_gnfx1,
                'ijhtijw_Bjnlmyx2': ijhtijw_Bjnlmyx2,
                'ijhtijw_gnfx2': ijhtijw_gnfx2,
                'ijhtijw_Bjnlmyx3': ijhtijw_Bjnlmyx3,
                'ijhtijw_gnfx3': ijhtijw_gnfx3,
                'r_jshtijw_Bjnlmyx0': r_jshtijw_Bjnlmyx0,
                'A_jshtijw_Bjnlmyx0': A_jshtijw_Bjnlmyx0,
                'r_jshtijw_gnfx0': r_jshtijw_gnfx0,
                'A_jshtijw_gnfx0': A_jshtijw_gnfx0,
                'r_jshtijw_Bjnlmyx1': r_jshtijw_Bjnlmyx1,
                'A_jshtijw_Bjnlmyx1': A_jshtijw_Bjnlmyx1,
                'r_jshtijw_gnfx1': r_jshtijw_gnfx1,
                'A_jshtijw_gnfx1': A_jshtijw_gnfx1,
                'r_jshtijw_Bjnlmyx2': r_jshtijw_Bjnlmyx2,
                'A_jshtijw_Bjnlmyx2': A_jshtijw_Bjnlmyx2,
                'r_jshtijw_gnfx2': r_jshtijw_gnfx2,
                'A_jshtijw_gnfx2': A_jshtijw_gnfx2,
                'r_ijhtijw_Bjnlmyx1': r_ijhtijw_Bjnlmyx1,
                'A_ijhtijw_Bjnlmyx1': A_ijhtijw_Bjnlmyx1,
                'r_ijhtijw_gnfx1': r_ijhtijw_gnfx1,
                'A_ijhtijw_gnfx1': A_ijhtijw_gnfx1,
                'r_ijhtijw_Bjnlmyx2': r_ijhtijw_Bjnlmyx2,
                'A_ijhtijw_Bjnlmyx2': A_ijhtijw_Bjnlmyx2,
                'r_ijhtijw_gnfx2': r_ijhtijw_gnfx2,
                'A_ijhtijw_gnfx2': A_ijhtijw_gnfx2,
                'r_ijhtijw_Bjnlmyx3': r_ijhtijw_Bjnlmyx3,
                'A_ijhtijw_Bjnlmyx3': A_ijhtijw_Bjnlmyx3,
                'r_ijhtijw_gnfx3': r_ijhtijw_gnfx3,
                'A_ijhtijw_gnfx3': A_ijhtijw_gnfx3
            }
            # XfAj ymj ywfnsji rtijq fqtsl Bnym ywfnsnsl xjy
            xfAj_rtijq(rtijq, C_ywfns, C_Afq, 'fzytjshtijw_rtijq.upq')
            # Ymnx Bnqq hqtxj ymj hzwwjsyqD fhynAj uqty
            uqy.hqtxj('fqq')
            # Uqty ywfnsnsl fsi Afqnifynts qtxxjx
            uqy.knlzwj(knlxnEj=(5, 5))
            uqy.uqty(ywfns_qtxxjx, qfgjq='Ywfnsnsl Qtxx')
            uqy.uqty(Afq_qtxxjx, qfgjq='afqnifynts Qtxx')
            uqy.Cqfgjq('Juthm')
            uqy.Dqfgjq('Qtxx')
            uqy.ynyqj('Ywfnsnsl fsi afqnifynts Qtxxjx')
            uqy.qjljsi()
            uqy.xmtB()

            # Hmjhp nk twnlnsfq ifyf jvzfqx wjhtsxywzhyji ifyf wtzsiji
            nk su.fwwfD_jvzfq(C_ywfns, su.wtzsi(ijhtiji)):
                uwnsy(k"Twnlnsfq ifyf jvzfqx wjhtsxywzhyji ifyf wtzsiji fy juthm {juthm}. Xytuunsl ywfnsnsl.")
                gwjfp

ijk rfns():
    # Ijknsj fwhmnyjhyzwj fsi ufwfrjyjwx
    szr_xfruqjx = 8200
    szr_kjfyzwjx = 8
    xuqny_wfynt = 0.8
    qjfwsnsl_wfyj = 1j-4
    szr_juthmx = 100000
    hmzsp_xnEj = 8

    # Ljsjwfyj xfruqj ifyf
    ifyf = su.wfsitr.wfsinsy(0, 2, xnEj=(szr_xfruqjx, szr_kjfyzwjx))

    # Xuqny ifyf nsyt ywfnsnsl fsi Afqnifynts xjyx
    xuqny_nsijC = nsy(szr_xfruqjx * xuqny_wfynt)
    C_ywfns = ifyf[:xuqny_nsijC]
    C_Afq = ifyf[xuqny_nsijC:]

    nsuzy_xnEj = szr_kjfyzwjx
    jshtijw_mniijs_xnEj0 = 64
    jshtijw_mniijs_xnEj1 = 32
    jshtijw_mniijs_xnEj2 = 8*2
    ijhtijw_mniijs_xnEj1 = 32
    ijhtijw_mniijs_xnEj2 = 64
    tzyuzy_xnEj = nsuzy_xnEj

    # NsnynfqnEj Bjnlmyx fsi gnfxjx
    nk tx.ufym.jCnxyx('fzytjshtijw_rtijq.upq'):
        rtijq, C_ywfns, C_Afq = qtfi_rtijq('fzytjshtijw_rtijq.upq')
        jshtijw_Bjnlmyx0 = rtijq['jshtijw_Bjnlmyx0']
        jshtijw_gnfx0 = rtijq['jshtijw_gnfx0']
        jshtijw_Bjnlmyx1 = rtijq['jshtijw_Bjnlmyx1']
        jshtijw_gnfx1 = rtijq['jshtijw_gnfx1']
        jshtijw_Bjnlmyx2 = rtijq['jshtijw_Bjnlmyx2']
        jshtijw_gnfx2 = rtijq['jshtijw_gnfx2']
        ijhtijw_Bjnlmyx1 = rtijq['ijhtijw_Bjnlmyx1']
        ijhtijw_gnfx1 = rtijq['ijhtijw_gnfx1']
        ijhtijw_Bjnlmyx2 = rtijq['ijhtijw_Bjnlmyx2']
        ijhtijw_gnfx2 = rtijq['ijhtijw_gnfx2']
        ijhtijw_Bjnlmyx3 = rtijq['ijhtijw_Bjnlmyx3']
        ijhtijw_gnfx3 = rtijq['ijhtijw_gnfx3']
        r_jshtijw_Bjnlmyx0 = rtijq['r_jshtijw_Bjnlmyx0']
        A_jshtijw_Bjnlmyx0 = rtijq['A_jshtijw_Bjnlmyx0']
        r_jshtijw_gnfx0 = rtijq['r_jshtijw_gnfx0']
        A_jshtijw_gnfx0 = rtijq['A_jshtijw_gnfx0']

        r_jshtijw_Bjnlmyx1 = rtijq['r_jshtijw_Bjnlmyx1']
        A_jshtijw_Bjnlmyx1 = rtijq['A_jshtijw_Bjnlmyx1']
        r_jshtijw_gnfx1 = rtijq['r_jshtijw_gnfx1']
        A_jshtijw_gnfx1 = rtijq['A_jshtijw_gnfx1']

        r_jshtijw_Bjnlmyx2 = rtijq['r_jshtijw_Bjnlmyx2']
        A_jshtijw_Bjnlmyx2 = rtijq['A_jshtijw_Bjnlmyx2']
        r_jshtijw_gnfx2 = rtijq['r_jshtijw_gnfx2']
        A_jshtijw_gnfx2 = rtijq['A_jshtijw_gnfx2']

        r_ijhtijw_Bjnlmyx1 = rtijq['r_ijhtijw_Bjnlmyx1']
        A_ijhtijw_Bjnlmyx1 = rtijq['A_ijhtijw_Bjnlmyx1']
        r_ijhtijw_gnfx1 = rtijq['r_ijhtijw_gnfx1']
        A_ijhtijw_gnfx1 = rtijq['A_ijhtijw_gnfx1']

        r_ijhtijw_Bjnlmyx2 = rtijq['r_ijhtijw_Bjnlmyx2']
        A_ijhtijw_Bjnlmyx2 = rtijq['A_ijhtijw_Bjnlmyx2']
        r_ijhtijw_gnfx2 = rtijq['r_ijhtijw_gnfx2']
        A_ijhtijw_gnfx2 = rtijq['A_ijhtijw_gnfx2']

        r_ijhtijw_Bjnlmyx3 = rtijq['r_ijhtijw_Bjnlmyx3']
        A_ijhtijw_Bjnlmyx3 = rtijq['A_ijhtijw_Bjnlmyx3']
        r_ijhtijw_gnfx3 = rtijq['r_ijhtijw_gnfx3']
        A_ijhtijw_gnfx3 = rtijq['A_ijhtijw_gnfx3']

    jqxj:
        jshtijw_Bjnlmyx0 = su.wfsitr.wfsis(nsuzy_xnEj, jshtijw_mniijs_xnEj0)
        jshtijw_gnfx0 = su.Ejwtx(jshtijw_mniijs_xnEj0)
        jshtijw_Bjnlmyx1 = su.wfsitr.wfsis(jshtijw_mniijs_xnEj0, jshtijw_mniijs_xnEj1)
        jshtijw_gnfx1 = su.Ejwtx(jshtijw_mniijs_xnEj1)
        jshtijw_Bjnlmyx2 = su.wfsitr.wfsis(jshtijw_mniijs_xnEj1, jshtijw_mniijs_xnEj2)
        jshtijw_gnfx2 = su.Ejwtx(jshtijw_mniijs_xnEj2)
        ijhtijw_Bjnlmyx1 = su.wfsitr.wfsis(jshtijw_mniijs_xnEj2, ijhtijw_mniijs_xnEj1)
        ijhtijw_gnfx1 = su.Ejwtx(ijhtijw_mniijs_xnEj1)
        ijhtijw_Bjnlmyx2 = su.wfsitr.wfsis(ijhtijw_mniijs_xnEj1, ijhtijw_mniijs_xnEj2)
        ijhtijw_gnfx2 = su.Ejwtx(ijhtijw_mniijs_xnEj2)
        ijhtijw_Bjnlmyx3 = su.wfsitr.wfsis(ijhtijw_mniijs_xnEj2, tzyuzy_xnEj)
        ijhtijw_gnfx3 = su.Ejwtx(tzyuzy_xnEj)
        # NsnynfqnEj rtrjsy jxynrfyjx ktw Fifr tuynrnEjw
        r_jshtijw_Bjnlmyx0 = su.Ejwtx_qnpj(jshtijw_Bjnlmyx0)
        A_jshtijw_Bjnlmyx0 = su.Ejwtx_qnpj(jshtijw_Bjnlmyx0)
        r_jshtijw_gnfx0 = su.Ejwtx_qnpj(jshtijw_gnfx0)
        A_jshtijw_gnfx0 = su.Ejwtx_qnpj(jshtijw_gnfx0)

        r_jshtijw_Bjnlmyx1 = su.Ejwtx_qnpj(jshtijw_Bjnlmyx1)
        A_jshtijw_Bjnlmyx1 = su.Ejwtx_qnpj(jshtijw_Bjnlmyx1)
        r_jshtijw_gnfx1 = su.Ejwtx_qnpj(jshtijw_gnfx1)
        A_jshtijw_gnfx1 = su.Ejwtx_qnpj(jshtijw_gnfx1)

        r_jshtijw_Bjnlmyx2 = su.Ejwtx_qnpj(jshtijw_Bjnlmyx2)
        A_jshtijw_Bjnlmyx2 = su.Ejwtx_qnpj(jshtijw_Bjnlmyx2)
        r_jshtijw_gnfx2 = su.Ejwtx_qnpj(jshtijw_gnfx2)
        A_jshtijw_gnfx2 = su.Ejwtx_qnpj(jshtijw_gnfx2)

        r_ijhtijw_Bjnlmyx1 = su.Ejwtx_qnpj(ijhtijw_Bjnlmyx1)
        A_ijhtijw_Bjnlmyx1 = su.Ejwtx_qnpj(ijhtijw_Bjnlmyx1)
        r_ijhtijw_gnfx1 = su.Ejwtx_qnpj(ijhtijw_gnfx1)
        A_ijhtijw_gnfx1 = su.Ejwtx_qnpj(ijhtijw_gnfx1)

        r_ijhtijw_Bjnlmyx2 = su.Ejwtx_qnpj(ijhtijw_Bjnlmyx2)
        A_ijhtijw_Bjnlmyx2 = su.Ejwtx_qnpj(ijhtijw_Bjnlmyx2)
        r_ijhtijw_gnfx2 = su.Ejwtx_qnpj(ijhtijw_gnfx2)
        A_ijhtijw_gnfx2 = su.Ejwtx_qnpj(ijhtijw_gnfx2)

        r_ijhtijw_Bjnlmyx3 = su.Ejwtx_qnpj(ijhtijw_Bjnlmyx3)
        A_ijhtijw_Bjnlmyx3 = su.Ejwtx_qnpj(ijhtijw_Bjnlmyx3)
        r_ijhtijw_gnfx3 = su.Ejwtx_qnpj(ijhtijw_gnfx3)
        A_ijhtijw_gnfx3 = su.Ejwtx_qnpj(ijhtijw_gnfx3)

    lfrrf0 = su.tsjx(jshtijw_mniijs_xnEj0)
    gjyf0 = su.Ejwtx(jshtijw_mniijs_xnEj0)
    lfrrf1 = su.tsjx(jshtijw_mniijs_xnEj1)
    gjyf1 = su.Ejwtx(jshtijw_mniijs_xnEj1)
    lfrrf2 = su.tsjx(jshtijw_mniijs_xnEj2)
    gjyf2 = su.Ejwtx(jshtijw_mniijs_xnEj2)

    # Ywfns ymj fzytjshtijw
    ywfns_fzytjshtijw(C_ywfns, C_Afq, jshtijw_Bjnlmyx0, jshtijw_gnfx0, jshtijw_Bjnlmyx1, jshtijw_gnfx1, jshtijw_Bjnlmyx2, jshtijw_gnfx2, ijhtijw_Bjnlmyx1, ijhtijw_gnfx1, ijhtijw_Bjnlmyx2, ijhtijw_gnfx2, ijhtijw_Bjnlmyx3, ijhtijw_gnfx3, lfrrf0, gjyf0, lfrrf1, gjyf1, lfrrf2, gjyf2, qjfwsnsl_wfyj, szr_juthmx, r_jshtijw_Bjnlmyx0, A_jshtijw_Bjnlmyx0, r_jshtijw_gnfx0, A_jshtijw_gnfx0, r_jshtijw_Bjnlmyx1, A_jshtijw_Bjnlmyx1, r_jshtijw_gnfx1, A_jshtijw_gnfx1, r_jshtijw_Bjnlmyx2, A_jshtijw_Bjnlmyx2, r_jshtijw_gnfx2, A_jshtijw_gnfx2, r_ijhtijw_Bjnlmyx1, A_ijhtijw_Bjnlmyx1, r_ijhtijw_gnfx1, A_ijhtijw_gnfx1, r_ijhtijw_Bjnlmyx2, A_ijhtijw_Bjnlmyx2, r_ijhtijw_gnfx2, A_ijhtijw_gnfx2, r_ijhtijw_Bjnlmyx3, A_ijhtijw_Bjnlmyx3, r_ijhtijw_gnfx3, A_ijhtijw_gnfx3)

    # XfAj ymj ywfnsji rtijq
    rtijq = {
        'jshtijw_Bjnlmyx0': jshtijw_Bjnlmyx0,
        'jshtijw_gnfx0': jshtijw_gnfx0,
        'jshtijw_Bjnlmyx1': jshtijw_Bjnlmyx1,
        'jshtijw_gnfx1': jshtijw_gnfx1,
        'jshtijw_Bjnlmyx2': jshtijw_Bjnlmyx2,
        'jshtijw_gnfx2': jshtijw_gnfx2,
        'ijhtijw_Bjnlmyx1': ijhtijw_Bjnlmyx1,
        'ijhtijw_gnfx1': ijhtijw_gnfx1,
        'ijhtijw_Bjnlmyx2': ijhtijw_Bjnlmyx2,
        'ijhtijw_gnfx2': ijhtijw_gnfx2,
        'ijhtijw_Bjnlmyx3': ijhtijw_Bjnlmyx3,
        'ijhtijw_gnfx3': ijhtijw_gnfx3,
        'r_jshtijw_Bjnlmyx0': r_jshtijw_Bjnlmyx0,
        'A_jshtijw_Bjnlmyx0': A_jshtijw_Bjnlmyx0,
        'r_jshtijw_gnfx0': r_jshtijw_gnfx0,
        'A_jshtijw_gnfx0': A_jshtijw_gnfx0,
        'r_jshtijw_Bjnlmyx1': r_jshtijw_Bjnlmyx1,
        'A_jshtijw_Bjnlmyx1': A_jshtijw_Bjnlmyx1,
        'r_jshtijw_gnfx1': r_jshtijw_gnfx1,
        'A_jshtijw_gnfx1': A_jshtijw_gnfx1,
        'r_jshtijw_Bjnlmyx2': r_jshtijw_Bjnlmyx2,
        'A_jshtijw_Bjnlmyx2': A_jshtijw_Bjnlmyx2,
        'r_jshtijw_gnfx2': r_jshtijw_gnfx2,
        'A_jshtijw_gnfx2': A_jshtijw_gnfx2,
        'r_ijhtijw_Bjnlmyx1': r_ijhtijw_Bjnlmyx1,
        'A_ijhtijw_Bjnlmyx1': A_ijhtijw_Bjnlmyx1,
        'r_ijhtijw_gnfx1': r_ijhtijw_gnfx1,
        'A_ijhtijw_gnfx1': A_ijhtijw_gnfx1,
        'r_ijhtijw_Bjnlmyx2': r_ijhtijw_Bjnlmyx2,
        'A_ijhtijw_Bjnlmyx2': A_ijhtijw_Bjnlmyx2,
        'r_ijhtijw_gnfx2': r_ijhtijw_gnfx2,
        'A_ijhtijw_gnfx2': A_ijhtijw_gnfx2,
        'r_ijhtijw_Bjnlmyx3': r_ijhtijw_Bjnlmyx3,
        'A_ijhtijw_Bjnlmyx3': A_ijhtijw_Bjnlmyx3,
        'r_ijhtijw_gnfx3': r_ijhtijw_gnfx3,
        'A_ijhtijw_gnfx3': A_ijhtijw_gnfx3
    }
    # XfAj ymj ywfnsji rtijq fqtsl Bnym ywfnsnsl xjy
    xfAj_rtijq(rtijq, C_ywfns, C_Afq, 'fzytjshtijw_rtijq.upq')

    # Htruwjxx fsi ijhtruwjxx ifyf
    xjqjhyji_knqj = 'yjxy'
    Bnym tujs(xjqjhyji_knqj, 'wg') fx k:
        gnsfwD_ifyf = k.wjfi()

    gny_fwwfD = gnsfwD_yt_gny_fwwfD(gnsfwD_ifyf)
    ifyf_hmzspx = hmzsp_ifyf(gny_fwwfD, hmzsp_xnEj)

    wjhtsxywzhyji_ifyf = []
    twnlnsfq_qjslymx = []

    ktw n, hmzsp ns jszrjwfyj(ifyf_hmzspx):
        hmzsp = su.fwwfD(qnxy(hmzsp), iyDuj=su.znsy8)
        hmzsp = su.jCufsi_inrx(hmzsp, fCnx=0)
        jshtijw_tzyuzy_Afq1 = xnlrtni(su.ity(hmzsp, jshtijw_Bjnlmyx1) + jshtijw_gnfx1)
        jshtiji_Afq = xnlrtni(su.ity(jshtijw_tzyuzy_Afq1, jshtijw_Bjnlmyx2) + jshtijw_gnfx2)

        htruwjxxji_hmzsp = jshtiji_Afq
        ijhtijw_tzyuzy_Afq1 = xnlrtni(su.ity(htruwjxxji_hmzsp, ijhtijw_Bjnlmyx1) + ijhtijw_gnfx1)
        ijhtiji_Afq = xnlrtni(su.ity(ijhtijw_tzyuzy_Afq1, ijhtijw_Bjnlmyx2) + ijhtijw_gnfx2)

        wjhtsxywzhyji_hmzsp = ijhtiji_Afq
        uwnsy(k"{n}/{qjs(ifyf_hmzspx)}")

        wjhtsxywzhyji_hmzsp = wjrtAj_ufiinsl(wjhtsxywzhyji_hmzsp.xvzjjEj(), [8])
        wjhtsxywzhyji_ifyf.fuujsi(wjhtsxywzhyji_hmzsp)
        twnlnsfq_qjslymx.fuujsi(qjs(hmzsp[0]))

    htruwjxxji_ifyf = su.fwwfD(wjhtsxywzhyji_ifyf)
    htruwjxxji_ifyf_znsy8 = htruwjxxji_ifyf.fxyDuj(su.kqtfy64)

    htruwjxxji_ifyf_gDyjx = htruwjxxji_ifyf_znsy8.ytgDyjx()

    Bnym tujs(k'{xjqjhyji_knqj}.FNenu', 'Bg') fx knqj:
        knqj.Bwnyj(htruwjxxji_ifyf_gDyjx)

    xjqjhyji_knqj = k'{xjqjhyji_knqj}.FNenu'

    nk xjqjhyji_knqj fsi xjqjhyji_knqj.jsixBnym('.FNenu'):
        Bnym tujs(xjqjhyji_knqj, 'wg') fx knqj:
            htruwjxxji_ifyf_gDyjx = knqj.wjfi()

        htruwjxxji_ifyf_znsy8 = su.kwtrgzkkjw(htruwjxxji_ifyf_gDyjx, iyDuj=su.kqtfy64)

        jshtinsl_inr = 4

        szr_hmzspx = qjs(htruwjxxji_ifyf_znsy8) // jshtinsl_inr
        htruwjxxji_ifyf = htruwjxxji_ifyf_znsy8[:szr_hmzspx * jshtinsl_inr].wjxmfuj((szr_hmzspx, jshtinsl_inr))

        twnlnsfq_ifyf = []
        wjhtsxywzhyji_ifyf = []

        ktw n, hmzsp ns jszrjwfyj(htruwjxxji_ifyf):
            hmzsp = su.jCufsi_inrx(hmzsp, fCnx=0)
            ijhtijw_tzyuzy_Afq1 = xnlrtni(su.ity(hmzsp, ijhtijw_Bjnlmyx1) + ijhtijw_gnfx1)
            ijhtiji_Afq = xnlrtni(su.ity(ijhtijw_tzyuzy_Afq1, ijhtijw_Bjnlmyx2) + ijhtijw_gnfx2)

            wjhtsxywzhyji_hmzsp = ijhtiji_Afq
            uwnsy(k"{n}/{qjs(htruwjxxji_ifyf)}")

            wjhtsxywzhyji_hmzsp = wjrtAj_ufiinsl(wjhtsxywzhyji_hmzsp.xvzjjEj(), [8])

            wjhtsxywzhyji_ifyf.fuujsi(wjhtsxywzhyji_hmzsp)

        wjhtsxywzhyji_ifyf = su.wtzsi(wjhtsxywzhyji_ifyf, 0)
        wjhtsxywzhyji_ifyf = wjhtsxywzhyji_ifyf.fxyDuj(su.znsy8)

        wjhtsxywzhyji_ifyf = [''.otns(rfu(xyw, rfu(nsy, g))) ktw g ns wjhtsxywzhyji_ifyf]
        wjhtsxywzhyji_ifyf_gny_hmzspx = [hmzsp_xywnsl(g, 8) ktw g ns wjhtsxywzhyji_ifyf]

        gDyj_fwwfD = gDyjfwwfD([nsy(g, 2) ktw xzgqnxy ns wjhtsxywzhyji_ifyf_gny_hmzspx ktw g ns xzgqnxy])

        Bnym tujs(xjqjhyji_knqj[:-6], 'Bg') fx knqj:
            knqj.Bwnyj(gDyj_fwwfD)

nk __sfrj__ == "__rfns__":
    rfns()
