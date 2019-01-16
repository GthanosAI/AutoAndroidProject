package com.ifog.demo.base;

import cn.com.earth.net.Interceptor.ISupportMultiDomain;

/**
 * 介绍:
 * 作者: jacky
 * 邮箱: heweiflying@yeah.net
 * 时间:  2018/3/1 上午11:18
 */

public interface IMultiDomain extends ISupportMultiDomain {

    String GLOBAL_URL = "http://me.localhost.com";
    String I_API = "api_muse";

    String API_DOMAIN_DEBUG = "https://t.amuse.moreton.cn";
    String API_DOMAIN_ONLINE = "https://amuse.fogintelli.com";
}