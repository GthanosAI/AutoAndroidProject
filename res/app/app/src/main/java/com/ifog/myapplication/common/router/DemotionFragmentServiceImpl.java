package com.ifog.demo.common.router;

import android.content.Context;
import android.support.v4.app.Fragment;

import com.alibaba.android.arouter.facade.annotation.Route;
import com.alibaba.android.arouter.launcher.ARouter;
import com.ifog.demo.common.IPage;

/**
 * 介绍:
 * 作者: jacky
 * 时间: 2019/1/18 11:06 AM
 */
@Route(path = IPage.DEMOTION_PAGE_SERVER)
public class DemotionFragmentServiceImpl implements DemotionFragmentService {
    private Context context;

    @Override
    public Fragment demotion(String lossFragment) {
        return (Fragment) ARouter.getInstance().build(IPage.LOGIN_FRAGMENT).navigation();
    }

    @Override
    public void init(Context context) {
        this.context = context;
    }
}
