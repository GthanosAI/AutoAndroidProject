package ${package_name}.${sub_path};

import ${package_name}.R;
import ${package_name}.base.BaseMvpDsFragment;
import ${package_name}.databinding.Fragment${page_name}Binding;

import android.animation.ObjectAnimator;
import android.content.Intent;
import android.os.Build;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.view.View;

public class ${page_name}Fragment extends BaseMvpDsFragment<${page_name}Presenter, Fragment${page_name}Binding> implements I${page_name}View {
    @Override
    public void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
    }

    @Override
    protected ${page_name}Presenter createPresenter() {
        return new ${page_name}Presenter();
    }

    @Override
    protected int getLayoutId() {
        return R.layout.${page_view_name};
    }

    @Override
    protected void bindDataAndListener() {
        super.bindDataAndListener();
    }
}
