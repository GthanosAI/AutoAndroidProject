package ${package_name}.base;

import java.util.HashMap;
import java.util.Map;

import cn.com.earth.net.Interceptor.IDomainProvider;
import okhttp3.HttpUrl;

/**
 * 介绍:
 * 作者: jacky
 * 邮箱: heweiflying@yeah.net
 * 时间:  2018/3/1 上午11:27
 */

public class DomainProvider implements IMultiDomain, IDomainProvider {

    private static Map<String, HttpUrl> domains = new HashMap<>();

    // 每次新增加新的domain的话只需要更新这个地方即可
    public static void setDebug(boolean isDebug) {
        if (isDebug) {
            domains.put(I_API, checkUrl(API_DOMAIN_DEBUG));

        } else {
            domains.put(I_API, checkUrl(API_DOMAIN_ONLINE));
        }
    }

    private static HttpUrl checkUrl(String url) {
        HttpUrl httpUrl = HttpUrl.parse(url);
        if (httpUrl == null) {
            throw new IllegalArgumentException("url 参数错误");
        } else {
            return httpUrl;
        }
    }

    @Override
    public HttpUrl getDomain(String identification) {
        return domains.get(identification);
    }

    @Override
    public String getMainUrl() {
        return GLOBAL_URL;
    }
}
