package com.ifog.demo.base;

import android.app.Activity;
import android.databinding.ViewDataBinding;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.view.View;

import cn.com.earth.base.BaseDataBindingFragment;
import cn.com.earth.mvp.MvpBasePresenter;

public abstract class BaseMvpDsFragment<P extends MvpBasePresenter, T extends ViewDataBinding>
        extends BaseDataBindingFragment<T> {

    protected P p;

    protected abstract P createPresenter();

    @Override
    public void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
    }

    @Override
    protected void bindDataAndListener() {
        p = createPresenter();
        if (p != null) {
            p.attachView(this);
        }
    }

    @Override
    public void onAttach(Activity activity) {
        super.onAttach(activity);

    }

    @Override
    public void onDetach() {
        if (p != null) {
            p.detachView(this);
        }
        super.onDetach();
    }

    @Override
    protected void initToolBarView(View view) {
        super.initToolBarView(view);
    }
}
