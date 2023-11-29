import tushare as ts


def get_tushare_pro():
    pro = ts.pro_api('20231124213221-d996ebbc-c52d-4c6c-bff2-bf4daf5fd33f')
    pro._DataApi__http_url = 'http://tsapi.majors.ltd:7000'
    return pro
