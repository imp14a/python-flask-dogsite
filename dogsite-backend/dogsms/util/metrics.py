from opencensus.ext.stackdriver import stats_exporter
from opencensus.stats import aggregation
from opencensus.stats import measure
from opencensus.stats import stats
from opencensus.stats import view
from opencensus.tags.tag_map import TagMap
from opencensus.tags import tag_key as tag_key_module
from opencensus.tags.tag_value import TagValue


error_count = measure.MeasureInt('error_count', 'Count of errors', 'entities')

count_view = view.View(
    f'error_count',
    'Count of errors',
    [],
    error_count,
    aggregation.CountAggregation()
)

error_type = tag_key_module.TagKey('error_type')

def exportAndRecordError(error_value):
    stats.stats.view_manager.register_view(count_view)
    exporter = stats_exporter.new_stats_exporter()
    stats.stats.view_manager.register_exporter(exporter)
    
    tag_map = TagMap()
    tag_map.insert(error_type, TagValue(error_value))
    recorder = stats.stats.stats_recorder
    mmap = recorder.new_measurement_map()
    mmap.measure_int_put(error_count, 1)

    try:
        mmap.record(tag_map)
    except Exception as e:
        print('error recording metric: %s', e)

