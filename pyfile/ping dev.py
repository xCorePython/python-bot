# -*- coding: utf-8 -*-
import pings

# 監視対象ドメイン
target_domain = "algorithm.joho.info"

p = pings.Ping()

# pingで疎通テスト
res = p.ping(target_domain) 

# 疎通できた場合
if res.is_reached():
  print("successful：", target_domain)

# 疎通できなかった場合
else:
  # 監視対象への接続ができなかった
  print("unsuccessful：", target_domain)
