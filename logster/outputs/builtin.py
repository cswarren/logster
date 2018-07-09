from logster.outputs.stdout import StdoutOutput
from logster.outputs.graphite import GraphiteOutput
from logster.outputs.ganglia import GangliaOutput
from logster.outputs.statsd import StatsdOutput
from logster.outputs.cloudwatch import CloudwatchOutput
from logster.outputs.nsca import NSCAOutput
from logster.outputs.sfx import SignalfxOutput

builtin_output_classes = (
        StdoutOutput,
        GraphiteOutput,
        GangliaOutput,
        StatsdOutput,
        CloudwatchOutput,
        NSCAOutput,
        SignalfxOutput,
)

builtin_outputs = dict([(a.shortname, a) for a in builtin_output_classes])
