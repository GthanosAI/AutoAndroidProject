package com.ifog.demo.common.router;

import android.content.Context;

import com.alibaba.android.arouter.facade.Postcard;
import com.alibaba.android.arouter.facade.annotation.Interceptor;
import com.alibaba.android.arouter.facade.callback.InterceptorCallback;
import com.alibaba.android.arouter.facade.template.IInterceptor;
import com.ifog.demo.common.IPage;

/**
 * 介绍:
 * 作者: jacky
 * 时间: 2019/1/17 5:58 PM
 */
@Interceptor(priority = 7)
public class ComInterceptor implements IInterceptor {
    private Context context;

    @Override
    public void process(Postcard postcard, InterceptorCallback callback) {
        if (IPage.HOME.equals(postcard.getPath())) {
            callback.onContinue(postcard);
        } else {
            callback.onContinue(postcard);
        }
    }

    @Override
    public void init(Context context) {
        this.context = context;
    }
}
