package com.ifog.demo.common;

import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v4.app.Fragment;
import android.text.TextUtils;

import com.alibaba.android.arouter.facade.annotation.Autowired;
import com.alibaba.android.arouter.facade.annotation.Route;
import com.alibaba.android.arouter.launcher.ARouter;
import com.ifog.demo.common.router.DemotionFragmentService;

import cn.com.earth.base.BaseActivity;

/**
 * 介绍:
 * 作者: jacky
 * 时间: 2019/1/18 10:41 AM
 */
@Route(path = IPage.COM_ACTIVITY)
public class CommActivity extends BaseActivity {
    @Autowired(name = IPage.COMM_FRAGMENT_KEY)
    String target;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        ARouter.getInstance().inject(this);
        super.onCreate(savedInstanceState);
    }

    @Override
    protected Fragment getFirstFragment() {
        Fragment ret;
        if (!TextUtils.isEmpty(target)) {
            ret = (Fragment) ARouter.getInstance().build(target).navigation();
            if (ret != null) {
                return ret;
            }
        }

        ret = ((DemotionFragmentService) ARouter
                .getInstance()
                .build(IPage.DEMOTION_PAGE_SERVER)
                .navigation())
                .demotion(target);


        return ret;
    }
}
