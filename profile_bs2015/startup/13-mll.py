from ophyd.controls import EpicsMotor, PVPositioner, PseudoPositioner

ssx = EpicsMotor('XF:03IDC-ES{Ppmac:1-ssx}Mtr', name='ssx')
ssy = EpicsMotor('XF:03IDC-ES{Ppmac:1-ssy}Mtr', name='ssy')
ssz = EpicsMotor('XF:03IDC-ES{Ppmac:1-ssz}Mtr', name='ssz')

sth = EpicsMotor('XF:03IDC-ES{ANC350:1-Ax:0}Mtr', name='sth')
# anc1m1 = EpicsMotor('XF:03IDC-ES{ANC350:1-Ax:1}Mtr', name='anc1m1')
hth = EpicsMotor('XF:03IDC-ES{ANC350:1-Ax:2}Mtr', name='hth')
# anc350_ssx = EpicsMotor('XF:03IDC-ES{ANC350:1-Ax:3}Mtr', name='anc350_ssx')
# anc350_ssy = EpicsMotor('XF:03IDC-ES{ANC350:1-Ax:4}Mtr', name='anc350_ssy')
# anc350_ssz = EpicsMotor('XF:03IDC-ES{ANC350:1-Ax:5}Mtr', name='anc350_ssz')

vx = EpicsMotor('XF:03IDC-ES{ANC350:2-Ax:0}Mtr', name='vx')
vy = EpicsMotor('XF:03IDC-ES{ANC350:2-Ax:1}Mtr', name='vy')
vz = EpicsMotor('XF:03IDC-ES{ANC350:2-Ax:2}Mtr', name='vz')
vchi = EpicsMotor('XF:03IDC-ES{ANC350:2-Ax:4}Mtr', name='vchi')
vth = EpicsMotor('XF:03IDC-ES{ANC350:2-Ax:3}Mtr', name='vth')
hx = EpicsMotor('XF:03IDC-ES{ANC350:2-Ax:5}Mtr', name='hx')
sy = EpicsMotor('XF:03IDC-ES{ANC350:3-Ax:0}Mtr', name='sy')
sx1 = EpicsMotor('XF:03IDC-ES{ANC350:3-Ax:1}Mtr', name='sx1')
sz = EpicsMotor('XF:03IDC-ES{ANC350:3-Ax:2}Mtr', name='sz')
sz1 = EpicsMotor('XF:03IDC-ES{ANC350:3-Ax:3}Mtr', name='sz1')
hy = EpicsMotor('XF:03IDC-ES{ANC350:4-Ax:0}Mtr', name='hy')
hz = EpicsMotor('XF:03IDC-ES{ANC350:4-Ax:1}Mtr', name='hz')
osax = EpicsMotor('XF:03IDC-ES{ANC350:4-Ax:2}Mtr', name='osax')
osay = EpicsMotor('XF:03IDC-ES{ANC350:4-Ax:3}Mtr', name='osay')
osaz = EpicsMotor('XF:03IDC-ES{ANC350:4-Ax:4}Mtr', name='osaz')
sx = EpicsMotor('XF:03IDC-ES{ANC350:4-Ax:5}Mtr', name='sx')
bsx = EpicsMotor('XF:03IDC-ES{ANC350:5-Ax:0}Mtr', name='bsx')
bsy = EpicsMotor('XF:03IDC-ES{ANC350:5-Ax:1}Mtr', name='bsy')

# anc5m2 = EpicsMotor('XF:03IDC-ES{ANC350:5-Ax:2}Mtr', name='anc5m2')
# anc5m3 = EpicsMotor('XF:03IDC-ES{ANC350:5-Ax:3}Mtr', name='anc5m3')
# anc5m4 = EpicsMotor('XF:03IDC-ES{ANC350:5-Ax:4}Mtr', name='anc5m4')
# anc5m5 = EpicsMotor('XF:03IDC-ES{ANC350:5-Ax:5}Mtr', name='anc5m5')
# anc6m0 = EpicsMotor('XF:03IDC-ES{ANC350:6-Ax:0}Mtr', name='anc6m0')
# anc6m1 = EpicsMotor('XF:03IDC-ES{ANC350:6-Ax:1}Mtr', name='anc6m1')
# anc6m2 = EpicsMotor('XF:03IDC-ES{ANC350:6-Ax:2}Mtr', name='anc6m2')
# anc6m3 = EpicsMotor('XF:03IDC-ES{ANC350:6-Ax:3}Mtr', name='anc6m3')
# anc6m4 = EpicsMotor('XF:03IDC-ES{ANC350:6-Ax:4}Mtr', name='anc6m4')
# anc6m5 = EpicsMotor('XF:03IDC-ES{ANC350:6-Ax:5}Mtr', name='anc6m5')
# anc7m0 = EpicsMotor('XF:03IDC-ES{ANC350:7-Ax:0}Mtr', name='anc7m0')
# anc7m1 = EpicsMotor('XF:03IDC-ES{ANC350:7-Ax:1}Mtr', name='anc7m1')
# anc7m2 = EpicsMotor('XF:03IDC-ES{ANC350:7-Ax:2}Mtr', name='anc7m2')

_xz_angle = 15. * pi / 180.


def _pssxz_rev(ssx=None, ssz=None):
    if None in [ssx, ssz]:
        return [0.0, 0.0]

    _pssx = ssx * cos(_xz_angle) + ssz * sin(_xz_angle)
    _pssz = -ssx * sin(_xz_angle) + ssz * cos(_xz_angle)
    return [_pssx, _pssz]


def _pssxz_fwd(pssx=None, pssz=None):
    if None in [pssx, pssz]:
        return [0.0, 0.0]

    _ssx = pssx * cos(_xz_angle) - pssz * sin(_xz_angle)
    _ssz = pssx * sin(_xz_angle) + pssz * cos(_xz_angle)
    return [_ssx, _ssz]


# _pssxz = PseudoPositioner('_pssxz', [ssx, ssz], forward=_pssxz_fwd, reverse=_pssxz_rev,
#                           pseudo=['pssx', 'pssz'])
#
# pssx = _pssxz['pssx']
# pssz = _pssxz['pssz']


def _psxz_rev(sx=None, sz=None):
    if None in [sx, sz]:
        return [0.0, 0.0]
    _psx = sx * cos(_xz_angle) + sz * sin(_xz_angle)
    _psz = -sx * sin(_xz_angle) + sz * cos(_xz_angle)
    return [_psx, _psz]


def _psxz_fwd(psx=None, psz=None):
    if None in [psx, psz]:
        return [0.0, 0.0]
    _sx = psx * cos(_xz_angle) - psz * sin(_xz_angle)
    _sz = psx * sin(_xz_angle) + psz * cos(_xz_angle)
    return [_sx, _sz]


# _psxz = PseudoPositioner('_psxz', [sx, sz], forward=_psxz_fwd, reverse=_psxz_rev,
#                          pseudo=['psx', 'psz'])
# # psx, psz = _psxz
# psx = _psxz['psx']
# psz = _psxz['psz']


def movr_hth(angle):
    radian = angle*pi/180.0
    correction = -1.*tan(radian)*34376.6
    movr(hth, angle)
    movr(hx,correction)


def movr_ssx(d):
    dx_n = d * cos(15.*pi/180.)
    dz_n = d * sin(15.*pi/180.)
    movr(ssx, dx_n)
    movr(ssz, dz_n)

def movr_sx(d):
    dx_n = d * cos(15.*pi/180.)
    dz_n = d * sin(15.*pi/180.)
    movr(sx, dx_n)
    movr(sz, dz_n)


def movr_sz(d):
    dx_n = -d * sin(15.*pi/180.)
    dz_n = d * cos(15.*pi/180.)
    movr(sx, dx_n)
    movr(sz, dz_n)


def movr_ssz(d):
    dx_n = -d * sin(15.*pi/180.)
    dz_n = d * cos(15.*pi/180.)
    movr(ssx, dx_n)
    movr(ssz, dz_n)
