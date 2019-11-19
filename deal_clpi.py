# coding:utf-8
# 知识点：
# 正则表达式中()缺省表示捕获分组
# 加?:用来标识非捕获分组

import os
import re
from BLURAY import parse_clpi_file

fname = 'bluray:F:\_Hashed\_UHD\Toy.Story.4.2019.ULTRAHD.Blu-ray.2160p.HEVC.TrueHD.Atmos.7.1-xxx'
fname = 'bluray:F:\_Hashed\_UHD\Toy.Story.4.2019.ULTRAHD.Blu-ray.2160p.HEVC.TrueHD.Atmos.7.1-sGnb@CHDBits'
playlist = 104
if fname.startswith("bluray:"):
    # Attempt to load the MPLS file for this playlist ...
    nfo = parse_clpi_file(
        br=fname[len("bluray:"):],
        ip=playlist
    )

pass
