from vmaf.core.feature_extractor import VmafexecFeatureExtractorMixin, FeatureExtractor
from vmaf import ExternalProgramCaller
from vmaf.core.result import Result
import pandas as pd
import json


class CiedeFeatureExtractor(VmafexecFeatureExtractorMixin, FeatureExtractor):

    TYPE = "Ciede_feature"
    VERSION = "0.1"

    ATOM_FEATURES = ['ciede']

    ATOM_FEATURES_TO_VMAFEXEC_KEY_DICT = {
        'ciede': 'ciede'
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

        result_list = []
        for frame_result in log_dict['frames']:
            result_list.append({
                'dataset': asset.dataset,
                'content_id': asset.content_id,
                'asset_id': asset.asset_id,
                'ref_path': asset.ref_path,
                'dis_path': asset.dis_path,
                'feature_name': 'ciede',
                'frame_num': frame_result['frameNum'],
                'score': frame_result['metrics']['ciede']
            })

        df = pd.DataFrame(result_list)
        result = Result(asset, self.executor_id)
        result.result_df = df
        return result
