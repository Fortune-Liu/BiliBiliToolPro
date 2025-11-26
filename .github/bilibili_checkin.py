import os
import requests

# 从环境变量中获取Cookie，这些环境变量由GitHub Actions工作流注入
DEDEUSERID = os.getenv('DEDEUSERID')
SESSDATA = os.getenv('SESSDATA')
BILI_JCT = os.getenv('BILI_JCT')

def bilibili_checkin():
    # 构建请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Cookie': f"DedeUserID={DEDEUSERID}; SESSDATA={SESSDATA}; bili_jct={BILI_JCT}"
    }
    
    # 签到接口URL
    checkin_url = "https://api.bilibili.com/x/member/web/clock/add"
    # 请求签到
    response = requests.post(checkin_url, headers=headers)
    result = response.json()
    
    # 检查签到结果
    if result.get('code') == 0:
        print("🎉 B站签到成功！")
    else:
        print(f"❌ 签到失败: {result.get('message')}")
        
    # 可选：获取今日经验信息
    exp_url = "https://api.bilibili.com/x/member/web/exp/reward"
    exp_response = requests.get(exp_url, headers=headers)
    exp_result = exp_response.json()
    if exp_result.get('code') == 0:
        data = exp_result.get('data', {})
        print(f"📊 今日登录获得经验: {data.get('login', 0)}")
        print(f"📹 今日观看视频获得经验: {data.get('watch', 0)}")
    else:
        print("未能获取经验信息")

if __name__ == '__main__':
    bilibili_checkin()
