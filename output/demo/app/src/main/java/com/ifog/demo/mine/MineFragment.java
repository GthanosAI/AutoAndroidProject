package com.ifog.demo.mine;

import com.ifog.demo.R;
import com.ifog.demo.base.BaseMvpDsFragment;
import com.ifog.demo.databinding.FragmentMineBinding;

import android.animation.ObjectAnimator;
import android.content.Intent;
import android.os.Build;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.view.View;

public class MineFragment extends BaseMvpDsFragment<MinePresenter, FragmentMineBinding> implements IMineView {
    @Override
    public void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
    }

    @Override
    protected MinePresenter createPresenter() {
        return new MinePresenter();
    }

    @Override
    protected int getLayoutId() {
        return R.layout.fragment_mine;
    }

    @Override
    protected void bindDataAndListener() {
        super.bindDataAndListener();
    }
}
