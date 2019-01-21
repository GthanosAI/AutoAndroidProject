package com.ifog.demo;

import android.app.Application;

import com.alibaba.android.arouter.launcher.ARouter;

import cn.com.earth.tools.EAppEnv;

/**
 * 介绍:
 * 作者: jacky
 * 时间: 2019/1/17 2:46 PM
 */
public class MainApplication extends Application {
    @Override
    public void onCreate() {
        super.onCreate();
        init();
    }

    private void init(){
        EAppEnv.init(this, true);
        ARouter.init(this);
    }
}
