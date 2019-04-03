package com.ifog.demo.common.router;

import android.support.v4.app.Fragment;

import com.alibaba.android.arouter.facade.template.IProvider;

/**
 * 介绍:
 * 作者: jacky
 * 时间: 2019/1/18 11:03 AM
 */


public interface DemotionFragmentService extends IProvider {
    Fragment demotion(String lossFragment);
}
