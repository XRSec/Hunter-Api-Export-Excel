#!/usr/bin/env python3
# -*- coding: UTF-8 -*

import requests
import xlwt
import datetime
import base64


def banner():
    print('''                            
    \033[1;31m _____      _      _   _      _      ___ \033[0m
    \033[1;32m|  ___|    / \    | | | |    / \    |_ _|\033[0m
    \033[1;33m| |_      / _ \   | |_| |   / _ \    | | \033[0m
    \033[1;34m|  _|    / ___ \  |  _  |  / ___ \   | | \033[0m
    \033[1;35m|_|     /_/   \_\ |_| |_| /_/   \_\ |___|\033[0m
    \033[1;36mhttps://www.fahai.org \033[0m
   \033[1;32m「 法海之路 - 生命不息，折腾不止 」\033[0m
    ''')


def write_excel(res):
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('Hunter数据平台导出')
    worksheet.write(0, 0, '网址')
    worksheet.write(0, 1, 'IP地址')
    worksheet.write(0, 2, '端口')
    worksheet.write(0, 3, '网站标题')
    worksheet.write(0, 4, '域名')
    worksheet.write(0, 5, '状态码')
    worksheet.write(0, 6, '系统名称')
    worksheet.write(0, 7, '公司名称')
    worksheet.write(0, 8, '备案号')
    worksheet.write(0, 9, '协议名称')
    worksheet.write(0, 10, '基础协议')
    worksheet.write(0, 11, '国家')
    worksheet.write(0, 12, '省份')
    worksheet.write(0, 13, '城市')
    worksheet.write(0, 14, '运营商')
    worksheet.write(0, 15, 'AS组织')
    worksheet.write(0, 16, '更新日期')
    worksheet.write(0, 17, '应用名称')
    worksheet.write(0, 18, '应用版本')
    row = 1
    for i in range(len(res["data"]["arr"])):
        url = res["data"]["arr"][i]["url"]  # 网址
        ip = res["data"]["arr"][i]["ip"]  # IP地址
        port = res["data"]["arr"][i]["port"]  # 端口
        web_title = res["data"]["arr"][i]["web_title"]  # 网站标题
        domain = res["data"]["arr"][i]["domain"]  # 域名
        status_code = res["data"]["arr"][i]["status_code"]  # 状态码
        os = res["data"]["arr"][i]["os"]  # 系统名称
        company = res["data"]["arr"][i]["company"]  # 公司名称
        number = res["data"]["arr"][i]["number"]  # 备案号
        protocol = res["data"]["arr"][i]["protocol"]  # 协议名称
        base_protocol = res["data"]["arr"][i]["base_protocol"]  # 基础协议
        country = res["data"]["arr"][i]["country"]  # 国家
        province = res["data"]["arr"][i]["province"]  # 省份
        city = res["data"]["arr"][i]["city"]  # 城市
        isp = res["data"]["arr"][i]["isp"]  # 运营商
        as_org = res["data"]["arr"][i]["as_org"]  # AS组织
        updated_at = res["data"]["arr"][i]["updated_at"]  # 更新日期
        if res["data"]["arr"][i]["component"] != None:
            for j in range(len(res["data"]["arr"][i]["component"])):
                component_name = res["data"]["arr"][i]["component"][j]["name"]  # 应用名称
                component_version = res["data"]["arr"][i]["component"][j]["version"]  # 应用版本
        else:
            pass
        worksheet.write(row, 0, url)
        worksheet.write(row, 1, ip)
        worksheet.write(row, 2, port)
        worksheet.write(row, 3, web_title)
        worksheet.write(row, 4, domain)
        worksheet.write(row, 5, status_code)
        worksheet.write(row, 6, os)
        worksheet.write(row, 7, company)
        worksheet.write(row, 8, number)
        worksheet.write(row, 9, protocol)
        worksheet.write(row, 10, base_protocol)
        worksheet.write(row, 11, country)
        worksheet.write(row, 12, province)
        worksheet.write(row, 13, city)
        worksheet.write(row, 14, isp)
        worksheet.write(row, 15, as_org)
        worksheet.write(row, 16, updated_at)
        worksheet.write(row, 17, component_name)
        worksheet.write(row, 18, component_version)
        row += 1
        workbook.save(save_time + '.xls')
    print("数据导出完毕！")


def Hunter_API():
    url = 'https://hunter.qianxin.com/openApi/search'
    params = {
        'api-key': api_key,
        'search': str(search),
        'page': 1,
        'page_size': 100,
        'start_time': start_time,
        'end_time': end_time,
    }
    res = requests.get(url, params=params).json()
    write_excel(res)


if __name__ == '__main__':
    banner()
    api_key = 'apiKey'
    search = input('请输入Hunter查询语法：')  # domain="fahai.org"
    search = base64.urlsafe_b64encode(search.encode("utf-8")).decode('ascii')
    now_time = datetime.datetime.now()
    start_time = (now_time - datetime.timedelta(days=365)).strftime("%Y-%m-%d %H:%M:%S")  # 默认查询时间为一年时间
    end_time = now_time.strftime("%Y-%m-%d %H:%M:%S")
    save_time = now_time.strftime("%Y%m%d%H%M%S")
    print(start_time, end_time, save_time)
    Hunter_API()