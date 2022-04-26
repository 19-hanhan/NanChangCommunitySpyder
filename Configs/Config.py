# 爬取根目录
BASE_URL = "https://passport.meituan.com/account/unitivelogin"

# 请求头
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
}

# 登录后的cookie信息
COOKIE = 'QN1=00008a8034fc3d3eb2d0ee00; QN205=organic; QN277=organic; _i=VInJOk6RdGpqMP_qmHZfzm642zxq; QN269=279C0B707EAE11ECAC39FA163E217C9C; qunar-assist={%22version%22:%2220211215173359.925%22%2C%22show%22:false%2C%22audio%22:false%2C%22speed%22:%22middle%22%2C%22zomm%22:1%2C%22cursor%22:false%2C%22pointer%22:false%2C%22bigtext%22:false%2C%22overead%22:false%2C%22readscreen%22:false%2C%22theme%22:%22default%22}; csrfToken=3yQUkKY8FowVUNALGDoE6ZMJu45jKEX8; _vi=vqJPvWR98aaExdRCExZJVgV4Gao3mOqZi4jY5lI5myG5IUQKrU-Px6SYQG7UhUiCtyZjajtuu2prFJl8jO9XoLsn9NzfWu4vWJAcReYmAMpfjTHd23d7RrZ62i0lD5w2_8yMkhNLFceVNzr78CRZmDphhm-jR6ZYrHskbw8dcQph; Hm_lvt_c56a2b5278263aa647778d304009eafc=1643204699,1643351887; JSESSIONID=77772300078531673B60FBFFC66F5BD3; viewdist=300021-6; uld=1-300021-6-1643352108; QN267=020513754589811a675; ariaDefaultTheme=null; Hm_lpvt_c56a2b5278263aa647778d304009eafc=1643352109; fid=f0f66099-409a-43e6-aad2-18e732eeda1a; QN271=c3cee14e-8445-4a01-b7d9-60bc5a19899a; SECKEY_ABVK=PQWN9tRXomymbdqRTW1Vr1D/1dInGtWOX/qLjfA604w%3D; BMAP_SECKEY=-2gNubr2JgZEMK9BshjBw4MV6-QVsNI_lHlFet1dEQn3AdMEj5cxUJYHjV-br_gmHWEeltQkQ3yh3b6hjHP5C8GE_V3ie19PTYs6ppQI6XcDLGHzGwMY5_cyk-0jcHymwMeyHFDlSH9XNhvgyv1RrIeSttrA2CIxmwHDXwibSFFayjWvd3CnjJTzrVi55kP2'

# TIME OUT
TIMEOUT = 5

# MAX PAGES
MAX_PAGES = 64

# 网页保存地址
HTML_SAVE_URL = 'Html/Qunar/Travel/'

# MYSQL SETTINGS
HOST = 'localhost'
USER = 'root'
PASS = 'password'
PORT = 3306
DB = 'qunar'
TABLE = 'travel'

if __name__ == '__main__':
    pass
