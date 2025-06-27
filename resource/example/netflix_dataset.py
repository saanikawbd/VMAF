dataset_name = 'netflix'

yuv_fmt = 'yuv420p'
width = 1920
height = 1080

from vmaf.config import VmafConfig

ref_videos = [
    {'content_id': 0, 'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/videos/yuv/mkv/original_videos_Gaming_1080P_Gaming_1080P-0ce6.yuv')},
    {'content_id': 1, 'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/videos/yuv/mkv/original_videos_Gaming_1080P_Gaming_1080P-0ef8.yuv')},
    {'content_id': 2, 'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/videos/yuv/mkv/original_videos_Gaming_1080P_Gaming_1080P-2e97.yuv')},
    {'content_id': 3, 'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/videos/yuv/mkv/original_videos_Gaming_1080P_Gaming_1080P-12d4.yuv')},
    {'content_id': 4, 'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/videos/yuv/mkv/original_videos_Gaming_1080P_Gaming_1080P-13e3.yuv')},
    {'content_id': 5, 'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/videos/yuv/mkv/original_videos_Gaming_1080P_Gaming_1080P-26dc.yuv')},
    {'content_id': 6, 'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/videos/yuv/mkv/original_videos_Gaming_1080P_Gaming_1080P-35fa.yuv')},
    {'content_id': 7, 'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/videos/yuv/mkv/original_videos_Gaming_1080P_Gaming_1080P-173a.yuv')},
    {'content_id': 8, 'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/videos/yuv/mkv/original_videos_Gaming_1080P_Gaming_1080P-1704.yuv')},
    {'content_id': 9, 'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/videos/yuv/mkv/original_videos_Gaming_1080P_Gaming_1080P-2221.yuv')}
]

dis_videos = [
    {'content_id': 0, 'asset_id': 0, 'dmos': 100, 'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/videos/yuv/mkv/original_videos_Gaming_1080P_Gaming_1080P-0ce6.yuv')}, # ref
    {'content_id': 0, 'asset_id': 1, 'dmos': 0,  'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/videos/yuv/mp4/vp9_compressed_videos_Gaming_1080P-0ce6_orig.yuv')},

    {'content_id': 1, 'asset_id': 2, 'dmos': 100,  'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/videos/yuv/mkv/original_videos_Gaming_1080P_Gaming_1080P-0ef8.yuv')}, # ref
    {'content_id': 1, 'asset_id': 3, 'dmos': 0,  'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/videos/yuv/mp4/vp9_compressed_videos_Gaming_1080P-0ef8_orig.yuv')},

    {'content_id': 2, 'asset_id': 4, 'dmos': 100, 'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/videos/yuv/mkv/original_videos_Gaming_1080P_Gaming_1080P-2e97.yuv')}, # ref
    {'content_id': 2, 'asset_id': 5, 'dmos': 7.4,  'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/videos/yuv/mp4/vp9_compressed_videos_Gaming_1080P-2e97_orig.yuv')},

    {'content_id': 3, 'asset_id': 6, 'dmos': 100, 'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/videos/yuv/mkv/original_videos_Gaming_1080P_Gaming_1080P-12d4.yuv')}, # ref
    {'content_id': 3, 'asset_id': 7, 'dmos': 0,  'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/videos/yuv/mp4/vp9_compressed_videos_Gaming_1080P-12d4_orig.yuv')},

    {'content_id': 4, 'asset_id': 8, 'dmos': 100, 'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/videos/yuv/mkv/original_videos_Gaming_1080P_Gaming_1080P-13e3.yuv')}, # ref
    {'content_id': 4, 'asset_id': 9, 'dmos': 14.7,  'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/videos/yuv/mp4/vp9_compressed_videos_Gaming_1080P-13e3_orig.yuv')},

    {'content_id': 5, 'asset_id': 10, 'dmos': 100, 'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/videos/yuv/mkv/original_videos_Gaming_1080P_Gaming_1080P-26dc.yuv')}, # ref
    {'content_id': 5, 'asset_id': 11, 'dmos': 14.2,  'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/videos/yuv/mp4/vp9_compressed_videos_Gaming_1080P-26dc_orig.yuv')},

    {'content_id': 6, 'asset_id': 12, 'dmos': 100, 'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/videos/yuv/mkv/original_videos_Gaming_1080P_Gaming_1080P-35fa.yuv')}, # ref
    {'content_id': 6, 'asset_id': 13, 'dmos': 16.2,  'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/videos/yuv/mp4/vp9_compressed_videos_Gaming_1080P-35fa_orig.yuv')},

    {'content_id': 7, 'asset_id': 14, 'dmos': 100, 'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/videos/yuv/mkv/original_videos_Gaming_1080P_Gaming_1080P-173a.yuv')}, # ref
    {'content_id': 7, 'asset_id': 15, 'dmos': 6.7,  'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/videos/yuv/mp4/vp9_compressed_videos_Gaming_1080P-173a_orig.yuv')},

    {'content_id': 8, 'asset_id': 16, 'dmos': 100, 'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/videos/yuv/mkv/original_videos_Gaming_1080P_Gaming_1080P-1704.yuv')}, # ref
    {'content_id': 8, 'asset_id': 17, 'dmos': 20.8,  'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/videos/yuv/mp4/vp9_compressed_videos_Gaming_1080P-1704_orig.yuv')},

    {'content_id': 9, 'asset_id': 18, 'dmos': 100, 'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/videos/yuv/mkv/original_videos_Gaming_1080P_Gaming_1080P-2221.yuv')}, # ref
    {'content_id': 9, 'asset_id': 19, 'dmos': 31.3,  'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/videos/yuv/mp4/vp9_compressed_videos_Gaming_1080P-2221_orig.yuv')},

]
