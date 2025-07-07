from vmaf.core.feature_extractor import VmafexecFeatureExtractorMixin, FeatureExtractor
from vmaf import ExternalProgramCaller
from vmaf.core.result import Result
import pandas as pd
import xml.etree.ElementTree as ET
import json


class CiedeFeatureExtractor(VmafexecFeatureExtractorMixin, FeatureExtractor):

    TYPE = "Ciede_feature"
    VERSION = "0.1"

    ATOM_FEATURES = ['ciede']

    ATOM_FEATURES_TO_VMAFEXEC_KEY_DICT = {
        'ciede': 'ciede2000'  # match the XML attribute name exactly
    }

    def _generate_result(self, asset):
        quality_width, quality_height = asset.quality_width_height

        log_file_path = self._get_log_file_path(asset)
        yuv_type = self._get_workfile_yuv_type(asset)
        ref_path = asset.ref_procfile_path
        dis_path = asset.dis_procfile_path
        logger = self.logger

        optional_dict = self.optional_dict if self.optional_dict is not None else dict()
        optional_dict2 = self.optional_dict2 if self.optional_dict2 is not None else dict()

        # Call vmafexec for ciede feature
        ExternalProgramCaller.call_vmafexec_single_feature(
            'ciede', yuv_type, ref_path, dis_path, quality_width, quality_height,
            log_file_path, logger, options={**optional_dict, **optional_dict2}
        )

        result = self._read_result(asset, log_file_path)
        return result

    def _read_result(self, asset, log_file_path):
        with open(log_file_path, 'r') as f:
            log_dict = json.load(f)

        # Build a result_dict mapping score keys to score lists
        scores_key = self.get_scores_key('ciede')  # from FeatureExtractor
        scores = [frame_result['metrics']['ciede'] for frame_result in log_dict['frames']]

        result_dict = {scores_key: scores}

        # Create Result object with result_dict
        result = Result(asset, self.executor_id, result_dict=result_dict)
        return result

