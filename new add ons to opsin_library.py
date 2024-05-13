def jaws(): neuron?
    """Returns a 4-state vf-Chrimson model.

    Params given in Bansal et al., 2020.
    Action spectrum from `Mager et al., 2018, Supp. Fig. 1a
    <https://static-content.springer.com/esm/art%3A10.1038%2Fs41467-018-04146-3/MediaObjects/41467_2018_4146_MOESM1_ESM.docx>`_,   (fix this)
    extracted using `Plot Digitizer <https://plotdigitizer.com/>`_.

    Parameters can be changed after initialization but *before injection*.
    """
    return BansalThreeStatePump(
        Gd=0.167 / ms,
        Gr=0.05 / ms,
        ka=1 / ms,
        p=0.8,
        q=1,
        phim=0.95e18 / mm2 / second,
        E=-400 * mV,
        g0=12.6 * nsiemens,
        a=0.02e-2 * mM / pcoulomb,
        b=6.5,
        name="Jaws",
        spectrum=[
            (593, 1),  # Assuming single value for the action spectrum peak
        ],
    )

def np_hr(): opsin
    """Returns a 4-state vf-Chrimson model.

    Params given in Bansal et al., 2020.
    Action spectrum from `Mager et al., 2018, Supp. Fig. 1a
    <https://static-content.springer.com/esm/art%3A10.1038%2Fs41467-018-04146-3/MediaObjects/41467_2018_4146_MOESM1_ESM.docx>`_,    (fix this)
    extracted using `Plot Digitizer <https://plotdigitizer.com/>`_.

    Parameters can be changed after initialization but *before injection*.
    """
    return BansalThreeStatePump(
        Gd=0.1099 / ms,
        Gr=0.05 / ms,
        ka=0.005 / ms,
        p=0.5,
        q=0.2,
        phim=1.5e18 / mm2 / second,
        E=-400 * mV,
        g0=17.7 * nsiemens,
        a=0.02e-2 * mM / pcoulomb,
        b=5,
        name="NpHR",
        spectrum=[
            (593, 1),  # Assuming single value for the action spectrum peak
        ],
    )

def chr2():
    """Returns a model of ChR2, an opsin for optical neural excitation.

    Params given in Bansal et al., 2021.
    Action spectrum from `Nagel et al., 2003, Fig. 4a
    <https://iopscience.iop.org/article/10.1088/1741-2552/ac1175`_,                  (fix this)
    extracted using `Plot Digitizer <https://plotdigitizer.com/>`_.
    """
    
    return BansalThreeStatePump(
        Gd1=0.09 / ms,
        Gd2=0.01 / ms,
        Gr=0.5e-3 / ms,
        g0=5.9 * nsiemens,
        phim=4e16 / mm2 / second,
        ka1=3 / ms,
        ka2=0.18 / ms,
        Gf0=0.015 / ms,
        Gb0=0.005 / ms,
        kf=0.03 / ms,
        kb=0.003 / ms,
        gamma=0.05,
        p=1,
        q=1,
        E=0 * mV,
        name="ChR2",
        spectrum=[],
    )

def reachr():
    """Returns a model of ChR2, an opsin for optical neural excitation.

    Params given in Bansal et al., 2021.
    Action spectrum from `Nagel et al., 2003, Fig. 4a
    <https://iopscience.iop.org/article/10.1088/1741-2552/ac1175`_,                 (fix this)
    extracted using `Plot Digitizer <https://plotdigitizer.com/>`_.
    """
    return BansalThreeStatePump(
        Gd1=7.7e-3 / ms,
        Gd2=1.25e-3 / ms,
        Gr=3.33e-5 / ms,
        g0=14.28 * nsiemens,
        phim=5e17 / mm2 / second,
        ka1=1.2 / ms,
        ka2=0.01 / ms,
        Gf0=0.0005 / ms,
        Gb0=0.0005 / ms,
        kf=0.012 / ms,
        kb=0.001 / ms,
        gamma=0.05,
        p=1,
        q=1,
        E=7 * mV,
        name="ReaChR",
        spectrum=[],
    )

def chrimsonr():
    """Returns a model of ChR2, an opsin for optical neural excitation.

    Params given in Bansal et al., 2021.
    Action spectrum from `Nagel et al., 2003, Fig. 4a
    <https://iopscience.iop.org/article/10.1088/1741-2552/ac1175`_,              (fix this)
    extracted using `Plot Digitizer <https://plotdigitizer.com/>`_.
    """
    return BansalThreeStatePump(
        Gd1=0.067 / ms,
        Gd2=0.01 / ms,
        Gr=0.5e-3 / ms,
        g0=12.25 * nsiemens,
        phim=20e17 / mm2 / second,
        ka1=6 / ms,
        ka2=0.1 / ms,
        Gf0=0.02 / ms,
        Gb0=0.05 / ms,
        kf=0.1 / ms,
        kb=0.001 / ms,
        gamma=0.05,
        p=0.6,
        q=1,
        E=0 * mV,
        name="ChrimsonR",
        spectrum=[],
    )

def CsChrimson_params():
    """Returns a model of ChR2, an opsin for optical neural excitation.

    Params given in Bansal et al., 2021.
    Action spectrum from `Nagel et al., 2003, Fig. 4a
    <https://iopscience.iop.org/article/10.1088/1741-2552/ac1175`_,              (fix this)
    extracted using `Plot Digitizer <https://plotdigitizer.com/>`_.
    """
    return {
        "Gd1": 0.033,
        "Gd2": 0.017,
        "Gr": 5e-6,
        "g0_photocurrent": 18.48,
        "g0_hippocampal_neurons": 1.2,
        "g0_RGNs": 0.37,
        "phim": 6e16,
        "k1": 3,
        "k2": 0.04,
        "Gf0": 0.005,
        "Gb0": 0.01,
        "kf": 0.01,
        "kb": 0.6,
        "gamma": 0.05,
        "p": 1,
        "q": 1,
        "E": -10,
    }


def bReaChES_params():
    """Returns a model of ChR2, an opsin for optical neural excitation.

    Params given in Bansal et al., 2021.
    Action spectrum from `Nagel et al., 2003, Fig. 4a
    <https://iopscience.iop.org/article/10.1088/1741-2552/ac1175`_,              (fix this)
    extracted using `Plot Digitizer <https://plotdigitizer.com/>`_.
    """
    return {
        "Gd1": 0.025,
        "Gd2": 0.01,
        "Gr": 3.3e-5,
        "g0_photocurrent": 36.5,
        "g0_hippocampal_neurons": 0.7,
        "g0_RGNs": 0.73,
        "phim": 6e15,
        "k1": 0.4,
        "k2": 0.01,
        "Gf0": 0.002,
        "Gb0": 0.002,
        "kf": 0.01,
        "kb": 0.04,
        "gamma": 0.05,
        "p": 1,
        "q": 1,
        "E": 10,
    }


def ChRmine_params():
    """Returns a model of ChR2, an opsin for optical neural excitation.

    Params given in Bansal et al., 2021.
    Action spectrum from `Nagel et al., 2003, Fig. 4a
    <https://iopscience.iop.org/article/10.1088/1741-2552/ac1175`_,              (fix this)
    extracted using `Plot Digitizer <https://plotdigitizer.com/>`_.
    """
    return {
        "Gd1": 0.02,
        "Gd2": 0.013,
        "Gr": 5.9e-4,
        "g0_photocurrent": 110,
        "g0_hippocampal_neurons": 1.9,
        "g0_RGNs": 2.2,
        "phim": 2.1e15,
        "k1": 0.2,
        "k2": 0.01,
        "Gf0": 0.0027,
        "Gb0": 0.0005,
        "kf": 0.001,
        "kb": 0,
        "gamma": 0.05,
        "p": 0.8,
        "q": 1,
        "E": 5.6,
    }


