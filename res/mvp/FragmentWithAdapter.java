package ${package_name}.${sub_path};

import ${package_name}.R;
import ${package_name}.base.BaseMvpDsFragment;
import ${package_name}.databinding.Fragment${page_name}Binding;
import android.support.v7.widget.${layout_type}LayoutManager;

import android.animation.ObjectAnimator;
import android.content.Intent;
import android.os.Build;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.view.View;

public class ${page_name}Fragment extends BaseMvpDsFragment<${page_name}Presenter, Fragment${page_name}Binding> implements IHomeView {
    private List<${model_name}> list;
    private ${adapter_name}Adapter adapter;
    private ${layout_type}LayoutManager manager;
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
        return R.layout.fragment_${page_name_lowcase};
    }

    @Override
    protected void bindDataAndListener() {
        super.bindDataAndListener();
        list = new ArrayList<>();
        adapter = new ${adapter_name}(list, p);
        manager = new ${layout_type}LayoutManager(mActivity${layout_prama});
        mDataBinding.recyclerView.setLayoutManager(manager);
        mDataBinding.recyclerView.setAdapter(adapter);
    }
}
