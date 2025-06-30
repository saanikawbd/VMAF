dataset_name = 'netflix'

yuv_fmt = 'yuv420p'
width = 1920
height = 1080

from vmaf.config import VmafConfig

ref_videos = [
    {'content_id': 0, 'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/netflix/ref/BigBuckBunny_25fps.yuv')},
    {'content_id': 1, 'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/netflix/ref/BirdsInCage_30fps.yuv')},
    {'content_id': 2, 'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/netflix/ref/CrowdRun_25fps.yuv')},
    {'content_id': 3, 'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/netflix/ref/ElFuente1_30fps.yuv')},
    {'content_id': 4, 'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/netflix/ref/ElFuente2_30fps.yuv')},
    {'content_id': 5, 'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/netflix/ref/FoxBird_25fps.yuv')},
    {'content_id': 6, 'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/netflix/ref/OldTownCross_25fps.yuv')},
    {'content_id': 7, 'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/netflix/ref/Seeking_25fps.yuv')},
    {'content_id': 8, 'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/netflix/ref/Tennis_24fps.yuv')},
]

dis_videos = [
    {'content_id': 0, 'asset_id': 0, 'dmos': 100, 'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/netflix/ref/BigBuckBunny_25fps.yuv')}, # ref
    {'content_id': 0, 'asset_id': 1, 'dmos': 85,  'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/netflix/dis/BigBuckBunny_85_1080_3800.yuv')},
    {'content_id': 0, 'asset_id': 2, 'dmos': 90,  'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/netflix/dis/BigBuckBunny_90_1080_4300.yuv')},
    {'content_id': 0, 'asset_id': 3, 'dmos': 95,  'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/netflix/dis/BigBuckBunny_95_1080_5800.yuv')},

    {'content_id': 1, 'asset_id': 4, 'dmos': 100,  'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/netflix/ref/BirdsInCage_30fps.yuv')}, # ref
    {'content_id': 1, 'asset_id': 5, 'dmos': 90,  'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/netflix/dis/BirdsInCage_90_1080_1800.yuv')},
    {'content_id': 1, 'asset_id': 6, 'dmos': 95,  'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/netflix/dis/BirdsInCage_95_1080_3000.yuv')},

    {'content_id': 2, 'asset_id': 7, 'dmos': 100, 'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/netflix/ref/CrowdRun_25fps.yuv')}, # ref
    {'content_id': 2, 'asset_id': 8, 'dmos': 50,  'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/netflix/dis/CrowdRun_50_1080_4300.yuv')},
    {'content_id': 2, 'asset_id': 9, 'dmos': 65,  'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/netflix/dis/CrowdRun_65_1080_5800.yuv')},
    {'content_id': 2, 'asset_id': 10, 'dmos': 75,  'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/netflix/dis/CrowdRun_75_1080_7500.yuv')},
    {'content_id': 2, 'asset_id': 11, 'dmos': 80,  'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/netflix/dis/CrowdRun_80_1080_10000.yuv')},
    {'content_id': 2, 'asset_id': 12, 'dmos': 90,  'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/netflix/dis/CrowdRun_90_1080_15000.yuv')},

    {'content_id': 3, 'asset_id': 13, 'dmos': 100, 'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/netflix/ref/ElFuente1_30fps.yuv')}, # ref
    {'content_id': 3, 'asset_id': 14, 'dmos': 70,  'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/netflix/dis/ElFuente1_70_1080_4300.yuv')},
    {'content_id': 3, 'asset_id': 15, 'dmos': 85,  'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/netflix/dis/ElFuente1_85_1080_5800.yuv')},
    {'content_id': 3, 'asset_id': 16, 'dmos': 90,  'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/netflix/dis/ElFuente1_90_1080_7500.yuv')},

    {'content_id': 4, 'asset_id': 17, 'dmos': 100, 'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/netflix/ref/ElFuente2_30fps.yuv')}, # ref
    {'content_id': 4, 'asset_id': 18, 'dmos': 60,  'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/netflix/dis/ElFuente2_60_1080_4300.yuv')},
    {'content_id': 4, 'asset_id': 19, 'dmos': 70,  'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/netflix/dis/ElFuente2_70_1080_5800.yuv')},
    {'content_id': 4, 'asset_id': 20, 'dmos': 80,  'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/netflix/dis/ElFuente2_80_1080_10000.yuv')},
    {'content_id': 4, 'asset_id': 21, 'dmos': 85,  'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/netflix/dis/ElFuente2_85_1080_15000.yuv')},
    {'content_id': 4, 'asset_id': 22, 'dmos': 90,  'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/netflix/dis/ElFuente2_90_1080_20000.yuv')},

    {'content_id': 5, 'asset_id': 23, 'dmos': 100, 'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/netflix/ref/FoxBird_25fps.yuv')}, # ref
    {'content_id': 5, 'asset_id': 24, 'dmos': 80,  'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/netflix/dis/FoxBird_80_1080_2300.yuv')},
    {'content_id': 5, 'asset_id': 25, 'dmos': 95,  'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/netflix/dis/FoxBird_95_1080_5800.yuv')},

    {'content_id': 6, 'asset_id': 26, 'dmos': 100, 'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/netflix/ref/OldTownCross_25fps.yuv')}, # ref
    {'content_id': 6, 'asset_id': 27, 'dmos': 90,  'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/netflix/dis/OldTownCross_90_1080_4300.yuv')},

    {'content_id': 7, 'asset_id': 28, 'dmos': 100, 'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/netflix/ref/Seeking_25fps.yuv')}, # ref
    {'content_id': 7, 'asset_id': 29, 'dmos': 65,  'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/netflix/dis/Seeking_65_1080_4300.yuv')},
    {'content_id': 7, 'asset_id': 30, 'dmos': 75,  'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/netflix/dis/Seeking_75_1080_5800.yuv')},
    {'content_id': 7, 'asset_id': 31, 'dmos': 85,  'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/netflix/dis/Seeking_85_1080_7500.yuv')},
    {'content_id': 7, 'asset_id': 32, 'dmos': 90,  'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/netflix/dis/Seeking_90_1080_15000.yuv')},
    {'content_id': 7, 'asset_id': 33, 'dmos': 95,  'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/netflix/dis/Seeking_95_1080_20000.yuv')},

    {'content_id': 8, 'asset_id': 34, 'dmos': 100, 'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/netflix/ref/Tennis_24fps.yuv')}, # ref
    {'content_id': 8, 'asset_id': 35, 'dmos': 90,  'path': VmafConfig.test_resource_path('yuv', '/Users/sapatel/vmaf/resource/netflix/dis/Tennis_90_1080_4300.yuv')},

]
