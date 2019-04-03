package com.ifog.demo.common;

import android.support.v4.app.Fragment;

import com.alibaba.android.arouter.launcher.ARouter;

/**
 * 介绍:
 * 作者: jacky
 * 时间: 2019/1/17 3:18 PM
 */
public class Router {
    public static void toHomeFragment() {
        Fragment fragment = (Fragment) ARouter.getInstance()
                .build("/mine/homefragment")
                .navigation();
    }
}
