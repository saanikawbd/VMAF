from abc import ABC
from vmaf.core.ciede_feature_extractor import CiedeFeatureExtractor
from vmaf.core.quality_runner import QualityRunnerFromFeatureExtractor
from vmaf.tools.decorator import override

class CiedeQualityRunner(QualityRunnerFromFeatureExtractor, ABC):

    TYPE = 'Ciede'
    VERSION = 'F' + CiedeFeatureExtractor.VERSION

    @override(QualityRunnerFromFeatureExtractor)
    def _get_feature_extractor_class(self):
        return CiedeFeatureExtractor

    @override(QualityRunnerFromFeatureExtractor)
    def _get_feature_key_for_score(self):
        return 'ciede'
