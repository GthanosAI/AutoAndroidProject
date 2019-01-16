package ${package_name}.base;

import java.util.ArrayList;
import java.util.List;
import ${package_name}.tools.EncryptUtil;

import cn.com.earth.net.Interceptor.CommonParamInterceptor;
import cn.com.earth.net.Interceptor.IDomainProvider;
import cn.com.earth.net.Interceptor.MultiDomainInterceptor;
import cn.com.earth.net.Interceptor.TTInterceptor;
import cn.com.earth.net.RetrofitClient;

/**
 * 介绍:
 * 作者: jacky
 * 邮箱: heweiflying@yeah.net
 * 时间:  2017/8/23 下午2:52
 */

public class ApiClient {
    private final static String PARAM_KEY = "8OZkiIyhZI@ipR3t";

    private static class ClientHolder {
        static ApiClient instance = new ApiClient();
    }

    CommonParamInterceptor paramInterceptor;
    TTInterceptor ttInterceptor;

    private MultiDomainInterceptor multiDomainInterceptor;
    private IDomainProvider provider;

    private ApiClient() {
        provider = new DomainProvider();
        paramInterceptor = new CommonParamInterceptor()
                .addParam("appplt", "android")
                .addParam("appver", "1.0")
                .addParam("clientId", "focus");


        multiDomainInterceptor = new MultiDomainInterceptor(provider, true);
        ttInterceptor = new TTInterceptor();
    }

    public static ApiClient getInstance() {
        return ClientHolder.instance;
    }

    public static void setDebug(boolean isDebug) {
        DomainProvider.setDebug(isDebug);
    }

    private Api bussApi;

    public Api getApi() {
        if (bussApi == null) {
            bussApi = RetrofitClient
                    .getInstance()
                    .getRetrofit(provider.getMainUrl(),
                            multiDomainInterceptor,
                            paramInterceptor,
                            ttInterceptor)
                    .create(Api.class);
        }
        return bussApi;
    }


    public List<String> getParams() {
        String timeStamp = System.currentTimeMillis() + "";
        String dest = EncryptUtil.shaEncrypt(timeStamp + PARAM_KEY);
//        StringBuilder builder = new StringBuilder(dest);
//        builder.append();
        List<String> ret = new ArrayList<>();
        ret.add(timeStamp);
        ret.add(dest);
        return ret;
    }
}
