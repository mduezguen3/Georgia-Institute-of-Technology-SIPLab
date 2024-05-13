def jaws(): neuron?
    """Returns a model of Jaws, an opsin for optical neural inhibition.

    Params given in Table 1.
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
    """Returns a model of NpHR, an opsin for optical neural inhibition.

    Params given in Table 1.
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
