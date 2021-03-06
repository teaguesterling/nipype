# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.mipav.developer import JistLaminarProfileGeometry

def test_JistLaminarProfileGeometry_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    inProfile=dict(argstr='--inProfile %s',
    ),
    incomputed=dict(argstr='--incomputed %s',
    ),
    inoutside=dict(argstr='--inoutside %f',
    ),
    inregularization=dict(argstr='--inregularization %s',
    ),
    insmoothing=dict(argstr='--insmoothing %f',
    ),
    null=dict(argstr='--null %s',
    ),
    outResult=dict(argstr='--outResult %s',
    hash_files=False,
    ),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    xDefaultMem=dict(argstr='-xDefaultMem %d',
    ),
    xMaxProcess=dict(argstr='-xMaxProcess %d',
    usedefault=True,
    ),
    xPrefExt=dict(argstr='--xPrefExt %s',
    ),
    )
    inputs = JistLaminarProfileGeometry.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_JistLaminarProfileGeometry_outputs():
    output_map = dict(outResult=dict(),
    )
    outputs = JistLaminarProfileGeometry.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

